#include <cstdio>
#include <cstdlib>
#include <cstring>
 
#include <map>
#include <algorithm>
 
using namespace std;
 
typedef long long ll;
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define ALL(A) A.begin(), A.end()
 
int N, rc;
int a[1<<16];
ll su, b[1<<16], cie[1<<16], r[1<<16];
map<ll,int> ir;
 
int bis[1<<16];
void inc(int idx) {
    idx++;
    while(idx <= rc) {
        bis[idx]++;
        idx += (idx&-idx);
    }
}
int val(int idx) {
    idx++;
    int res = 0;
    while(idx) {
        res += bis[idx];
        idx -= (idx&-idx);
    }
    return res;
}
 
ll residue(ll v) {
    return (v%su) ? su-(v%su) : 0;
}
 
ll t[1<<16];
ll do_sort(int si, int ei) {
    if(1 >= ei-si) return 0;
    int mi = (si + ei) / 2;
    ll res = do_sort(si, mi);
    res += do_sort(mi, ei);
    int ai = si, bi = mi, ci = si;
    while(ai < mi && bi < ei) {
        if(b[ai] <= b[bi]) t[ci++] = b[ai++];
        else {
            res += mi-ai;
            t[ci++] = b[bi++];
        }
    }
    while(ai < mi) t[ci++] = b[ai++];
    while(bi < ei) t[ci++] = b[bi++];
    memcpy(b+si,t+si,sizeof(ll)*(ei-si));
    return res;
}
 
int main() {
    int T;
    scanf("%d",&T);
    while(T--) {
        scanf("%d",&N);
        FOR(i,0,N) scanf("%d",&a[i]);
        /* pivot sums array such that each sum is positive */
        su = a[0];
        ll ls = a[0]; int lsi = 0;
        FOR(i,1,N) {
            su += a[i];
            if(ls > su) {
                ls = su;
                lsi = i;
            }
        }
        b[0] = 0;
        FOR(i,1,N) {
            b[i] = b[i-1] + a[(lsi+i)%N];
        }
        /* sort the sums, calculating the number of inversions */
        ll res = do_sort(0,N);
        /* build lookup of unique residues modulo su */
        FOR(i,0,N) r[i] = residue(b[i]);
        sort(r,r+N);
        ir.clear();
        rc = 0;
        FOR(i,0,N) {
            if(ir.find(r[i]) == ir.end()) ir[r[i]] = rc++;
        }
        /* calculate inversions in infinite array */
        memset(bis,0,sizeof(bis));
        FOR(i,0,N) cie[i] = (b[i] + su - 1) / su;
        ll ks = 0;
        int k = 0;
        FOR(i,1,N) {
            while(b[k]+su < b[i]) {
                inc(ir[residue(b[k])]);
                ks += cie[k];
                k++;
            }
            res += k*cie[i] - ks - val(ir[residue(b[i])]);
        }
        printf("%lld\n",res);
    }
    return 0;
}
