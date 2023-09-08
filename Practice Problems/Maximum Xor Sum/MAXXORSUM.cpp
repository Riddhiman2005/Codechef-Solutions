#include<bits/stdc++.h>

using namespace std;

#define int long long

#define fast() ios_base::sync_with_stdio(false);cin.tie(NULL); cout.tie(NULL)
#define endl '\n'

const int mod = 1e9 + 7;

void solve(){
	int n;
	cin >> n;
	vector<int> a(n), b(n);
	for(int &i: a) cin >> i;
	for(int &i: b) cin >> i;
	
	int ans = 0;
	for(int bit = 0; bit < 32; bit++){
		
		int andLast = n;
		for(int i = n - 1; i >= 0; i--){
			if((b[i] & (1 << bit)) == 0) break;
			andLast = i;
		}
		int orFirst = -1;
		for(int i = 0; i < n; i++){
			if(a[i] & (1 << bit)){
				orFirst = i;
				break;
			}
		}
		
	
		if(orFirst == -1) continue;
		
		
		else if(andLast == orFirst || orFirst + 2 == andLast){
			int cnt = n - andLast + (int) (orFirst + 2 == andLast);
			if(cnt % 2 == 1) ans += (1 << bit);
		}
		
		
		else ans += (1 << bit);
	}
	
	cout << ans << endl;
	
	
	  
}

signed main() {
    fast();
	int t = 1;
	cin >> t;
	while(t--){
        solve();
    }
	return 0;
}







