#include<bits/stdc++.h>
using namespace std;
const int MAXN = 1005;
const int Len = 1e7;
typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
template <typename T> void chkmax(T &x, T y) {x = max(x, y); }
template <typename T> void chkmin(T &x, T y) {x = min(x, y); } 
template <typename T> void read(T &x) {
	x = 0; int f = 1;
	char c = getchar();
	for (; !isdigit(c); c = getchar()) if (c == '-') f = -f;
	for (; isdigit(c); c = getchar()) x = x * 10 + c - '0';
	x *= f;
}
template <typename T> void write(T x) {
	if (x < 0) x = -x, putchar('-');
	if (x > 9) write(x / 10);
	putchar(x % 10 + '0');
}
template <typename T> void writeln(T x) {
	write(x);
	puts("");
}
int n, m, p[MAXN], rk[MAXN], cnt[MAXN], ans[MAXN];
bool flg, vis[MAXN], mp[MAXN][MAXN]; int col[MAXN];
vector <int> a[MAXN];
bool cmp(int x, int y) {
	if (col[x] == col[y]) {
		if (col[x]) return a[x].size() < a[y].size();
		else return a[x].size() > a[y].size();
	} else return col[x] < col[y];
}
void work(int pos) {
	for (auto x : a[pos])
		if (vis[x]) flg |= col[pos] == col[x];
		else {
			vis[x] = true;
			col[x] = 2 - col[pos];
			work(x);
		}
}
int main() {
	int T; read(T);
	while (T--) {
		read(n), read(m);
		memset(mp, 0, sizeof(mp));
		for (int i = 1; i <= n; i++)
			a[i].clear();
		for (int i = 1; i <= m; i++) {
			int x, y;
			read(x), read(y);
			mp[x][y] = mp[y][x] = true;
			a[x].push_back(y);
			a[y].push_back(x);
		}
		flg = false;
		memset(col, 0, sizeof(col));
		memset(vis, false, sizeof(vis));
		int mid = 0;
		for (int i = 1; i <= n; i++)
			if (a[i].size() == 2) {
				int x = a[i][0], y = a[i][1];
				if (mp[x][y]) {
					mid = i;
					break;
				}
			}
		col[mid] = 1;
		vis[mid] = true;
		for (int i = 1; i <= n; i++)
			if (!vis[i]) {
				col[i] = 0;
				vis[i] = true;
				work(i);
			}
		if (flg) {
			puts("No");
			continue;
		}
		for (int i = 1; i <= n; i++)
			p[i] = i;
		sort(p + 1, p + n + 1, cmp);
		int fn = 0, fm = mid != 0, tn = 0;
		for (int i = 1; i <= n; i++) {
			rk[p[i]] = i;
			fn += col[i] == 0;
			tn += col[i] == 2;
		}
		for (int i = fn + fm + 1; i <= n; i++) {
			int Max = 0;
			for (auto x : a[p[i]])
				chkmax(Max, rk[x]);
			cnt[i] = Max;
			flg |= Max != a[p[i]].size();
		}
		if (flg) {
			puts("No");
			continue;
		}
		puts("Yes");
		int fp = 1, tp = 1, pos = 1;
		if (fm) {
			while (fp <= fn || tp <= tn - 1) {
				if (fp > fn) ans[p[fn + fm + tp++]] = Len + pos++;
				else if (tp > tn - 1) ans[p[fp++]] = pos++;
				else if (cnt[fn + fm + tp] >= fp) ans[p[fp++]] = pos++;
				else ans[p[fn + fm + tp++]] = Len + pos++;
			}
			ans[mid] = Len + 1;
			ans[p[n]] = 2 * Len + 1;
		} else {
			while (fp <= fn || tp <= tn) {
				if (fp > fn) ans[p[fn + fm + tp++]] = Len + pos++;
				else if (tp > tn) ans[p[fp++]] = pos++;
				else if (cnt[fn + fm + tp] >= fp) ans[p[fp++]] = pos++;
				else ans[p[fn + fm + tp++]] = Len + pos++;
			}
		}
		printf("%d", 2 * Len);
		for (int i = 1; i <= n; i++)
			printf(" %d", ans[i]);
		printf("\n");
	}
	return 0;
}
