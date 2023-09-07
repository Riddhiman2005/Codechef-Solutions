#include <bits/stdc++.h>

using namespace std;

#define endl '\n'

typedef long long LL;
const LL inf = LLONG_MAX;
const LL D = (LL)2e12;
const int NX = 10010;
const int QQ = 200100;
const int C = 100100;

struct Point {
	int x, y;
	Point(int x = 0, int y = 0) : x(x), y(y) {}
	void in() { cin >> x >> y; }
	Point operator + (const Point &a) const {
		return Point(x + a.x, y + a.y);
	}
	Point operator - (const Point &a) const {
		return Point(x - a.x, y - a.y);
	}
	LL operator * (const Point &a) const {
		return 1LL * x * a.y - 1LL * y * a.x;
	}
	LL operator % (const Point &a) const {
		return 1LL * x * a.x + 1LL * y * a.y;
	}
	bool operator < (const Point &a) const {
		LL z = *this * a;
		return ((z) ? z < 0 : x < a.x);
	}
} p[NX];

pair<Point, int> ord[NX];
int id[NX];
int B, L, R;

struct Query {
	int l, r, x, id;
	void in(int _id) {
		cin >> l >> r >> x;
		r ++;
		id = _id;
	}
	bool operator < (const Query &a) const {
		int id1 = l / B, id2 = a.l / B;
		if (id1 != id2) return id1 < id2;
		return (id1 & 1) ^ (r < a.r);
	}
} Q[QQ];

set<int> S;
set<LL> vals[2 * C];
set<int> activeY;
LL maxVal[2 * C];
int bad = 0;

inline void addSide(int p, int q) {
	if(p == -1 || q == -1) return;
	int k = ord[q].first.y - ord[p].first.y;
	LL v = (D + ord[q].first * ord[p].first) * NX + p;
	activeY.insert(k);
	vals[C + k].insert(-v);
	maxVal[C + k] = -(*vals[C + k].begin());
}

inline void removeSide(int p, int q) {
	if(p == -1 || q == -1) return;
	int k = ord[q].first.y - ord[p].first.y;
	LL v = (D + ord[q].first * ord[p].first) * NX + p;
	vals[C + k].erase(-v);
	if (vals[C + k].empty()) activeY.erase(k);
	else maxVal[C + k] = -(*vals[C + k].begin());
}

inline bool getBad(int x, int y, int z) {
	if (x == -1 || y == -1 || z == -1) return 0;
	return (ord[y].first - ord[x].first) * (ord[z].first - ord[y].first) > 0;
}

void add(int p) {
	auto it = S.upper_bound(p);
	int q1 = -1, q2 = -1, p1 = -1, p2 = -1;
	if (it != S.end()) {
		q1 = *it;
		it ++;
		if (it != S.end()) q2 = *it;
		it --;
	}
	it --;
	p1 = *it;
	if (it != S.begin()) p2 = *prev(it);
	bad -= getBad(p2, p1, q1);
	bad -= getBad(p1, q1, q2);
	bad += getBad(p2, p1, p);
	bad += getBad(p1, p, q1);
	bad += getBad(p, q1, q2);
	removeSide(p1, q1);
	addSide(p1, p);
	addSide(p, q1);
	S.insert(p);
}

void remove(int p) {
	auto it = S.lower_bound(p);
	int q1 = -1, q2 = -1, p1 = -1, p2 = -1;
	it ++;
	if (it != S.end()) {
		q1 = *it;
		it ++;
		if (it != S.end()) q2 = *it;
		it --;
	}
	it --;
	it --;
	p1 = *it;
	if (it != S.begin()) p2 = *prev(it);
	bad -= getBad(p2, p1, p);
	bad -= getBad(p1, p, q1);
	bad -= getBad(p, q1, q2);
	bad += getBad(p2, p1, q1);
	bad += getBad(p1, q1, q2);
	removeSide(p1, p);
	removeSide(p, q1);
	addSide(p1, q1);
	S.erase(p);
}

LL solve(int x) {
	if (bad > 0) return -1;
	Point P, Q, R = Point(x, 0);
	auto it = S.end();
	it --;
	Q = ord[*it].first;
	it --;
	P = ord[*it].first;
	if ((Q - P) * (R - Q) > 0) return -1;
	LL ans = 0;
	for (auto k : activeY) {
		LL w = maxVal[C + k] / NX - D;
		ans = max(ans, 1LL * k * x + w);
	}
	return ans;
}

LL ans[QQ];

int main(){
#ifndef ONLINE_JUDGE
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif

	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);
	
	int N, NQ;
	
	cin >> N;
	for (int i = 1 ; i <= N ; i ++) {
		p[i].in();
		ord[i] = {p[i], i};
	}
	sort(ord + 1, ord + N + 1);
	for (int i = 1 ; i <= N ; i ++) id[ord[i].second] = i;
	
	cin >> NQ;
	for (int i = 0 ; i < NQ ; i ++) {
		Q[i].in(i);
	}
	B = max(1, (int)(N / sqrt(NQ) + 0.5)); 
	sort(Q, Q + NQ);
	
	S.insert(0);
	
	L = R = 1;
	for (int i = 0 ; i < NQ ; i ++) {
		while (R < Q[i].r) add(id[R ++]);
		while (L > Q[i].l) add(id[-- L]);
		while (R > Q[i].r) remove(id[-- R]);
		while (L < Q[i].l) remove(id[L ++]);
		ans[Q[i].id] = solve(Q[i].x);
	}
	
	for (int i = 0 ; i < NQ ; i ++) cout << ans[i] << endl;
}
