#include<bits/stdc++.h>

using namespace std;

int const maxn = 1e6 + 5, maxm = 2005;
int a[maxn], used[maxn], cur, numb[maxn];
vector < pair < int, int > > g[maxn];
vector < int > G[maxn];
vector < int > now;
vector < pair < int, int > > go[maxn];
int b[maxn], dist[maxn], inf = 1e9 + 7;
pair < int, int > imin[(1 << 13)];
int psh[(1 << 14)];
int good[(1 << 13)];
int free_good[(1 << 13)];

void dfs(int v) {
    used[v] = cur;
    now.push_back(v);
    for (auto u : G[v]) {
        if (used[u] == 0) dfs(u);
    }
}

void build(int i, int l, int r) {
    good[i] = r - l;
    free_good[i] = l;
    psh[i] = inf;
    imin[i] = {inf, l};
    if (r - l == 1) return;
    int m = (r + l) / 2;
    build(2 * i + 1, l, m);
    build(2 * i + 2, m, r);
}

inline void push(int i, int l, int r) {
    if (psh[i] == inf) return;
    if (good[i]) {
        if (psh[i] < imin[i].first) {
            imin[i] = {psh[i], free_good[i]};
        }
    }
    psh[2 * i + 1] = min(psh[2 * i + 1], psh[i]);
    psh[2 * i + 2] = min(psh[2 * i + 2], psh[i]);
    psh[i] = inf;
}

void update(int i, int l, int r, int lq, int rq, int x) {
    push(i, l, r);
    if (lq >= r || l >= rq) return;
    if (lq <= l && r <= rq) {
        psh[i] = x;
        push(i, l, r);
        return;
    }
    int m = (r + l) / 2;
    update(2 * i + 1, l, m, lq, rq, x);
    update(2 * i + 2, m, r, lq, rq, x);
    imin[i] = min(imin[2 * i + 1], imin[2 * i + 2]);
}

void del(int i, int l, int r, int lq) {
    push(i, l, r);
    if (!(l <= lq && lq < r)) return;
    if (r - l == 1) {
        good[i]--;
        imin[i] = {inf, l};
        return;
    }
    int m = (r + l) / 2;
    del(2 * i + 1, l, m, lq);
    del(2 * i + 2, m, r, lq);
    good[i]--;
    if (good[2 * i + 1]) free_good[i] = free_good[2 * i + 1];
    else free_good[i] = free_good[2 * i + 2];
    if (good[i]) imin[i] = min(imin[2 * i + 1], imin[2 * i + 2]);
    else imin[i] = {inf, l};
}

void solve(int v, int n) {
    build(0, 1, n + 1);
    update(0, 1, n + 1, v, v + 1, 0);
    for (int i = 1; i <= n; ++i) {
        pair < int, int > best = imin[0];
        dist[best.second] = best.first;
        del(0, 1, n + 1, best.second);
        int was = 0;
        for (auto key : go[best.second]) {
            update(0, 1, n + 1, key.first, key.first + 1, key.second + best.first);
            if (was + 1 != key.first) {
                update(0, 1, n + 1, was + 1, key.first, best.first + b[best.second]);
            }
            was = key.first;
        }
        if (was != n) update(0, 1, n + 1, was + 1, n + 1, best.first + b[best.second]);
     }
}

main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t, n, m, u, v, c;
    cin >> t;
    while (t--) {
        cin >> n;
        cur = 0;
        long long ans = 0;
        vector < pair < int, int > > all_elem;
        for (int i = 1; i <= n; ++i) {
            cin >> a[i];
            all_elem.push_back({a[i], i});
            g[i] = {};
            G[i] = {};
            used[i] = 0;
        }
        sort(all_elem.begin(), all_elem.end());
        cin >> m;
        for (int i = 1; i <= m; ++i) {
            cin >> u >> v >> c;
            G[u].push_back(v);
            G[v].push_back(u);
            g[u].push_back({v, c});
        }
        for (int i = 1; i <= n; ++i) {
            sort(g[i].begin(), g[i].end());
        }
        for (int i = 1; i <= n; ++i) {
            if (used[i] == 0) {
                cur++, now = {};
                dfs(i);
                if ((int)now.size() == 1) {
                    ans += (long long)a[i] * (n - 1);
                    continue;
                }
                int bad = -1;
                for (auto key : all_elem) {
                    if (used[key.second] != cur) {
                        bad = key.second;
                        now.push_back(bad);
                        break;
                    }
                }
                sort(now.begin(), now.end());
                for (int j = 0; j < (int)now.size(); ++j) numb[now[j]] = j + 1;
                for (int j = 1; j <= (int)now.size(); ++j) {
                    go[j] = {};
                    b[j] = a[now[j - 1]];
                    for (auto elem : g[now[j - 1]]) {
                        go[j].push_back({numb[elem.first], elem.second});
                    }
                }
                for (int j = 1; j <= (int)now.size(); ++j) {
                    if (now[j - 1] == bad) continue;
                    solve(j, (int)now.size());
                    int out = a[now[j - 1]];
                    for (int pos = 1; pos <= (int)now.size(); ++pos) {
                        ans += (long long)dist[pos];
                        out = min(out, dist[pos] + a[now[pos - 1]]);
                    }
                    ans += (long long)(n - (int)now.size()) * (long long)out;
                }
            }
        }
        cout << ans << '\n';
    }
    return 0;
}
