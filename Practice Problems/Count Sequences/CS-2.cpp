#include <cassert>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

using namespace std;

using Int = long long;

template <class T1, class T2> ostream &operator<<(ostream &os, const pair<T1, T2> &a) { return os << "(" << a.first << ", " << a.second << ")"; };
template <class T> ostream &operator<<(ostream &os, const vector<T> &as) { const int sz = as.size(); os << "["; for (int i = 0; i < sz; ++i) { if (i >= 256) { os << ", ..."; break; } if (i > 0) { os << ", "; } os << as[i]; } return os << "]"; }
template <class T> void pv(T a, T b) { for (T i = a; i != b; ++i) cerr << *i << " "; cerr << endl; }
template <class T> bool chmin(T &t, const T &f) { if (t > f) { t = f; return true; } return false; }
template <class T> bool chmax(T &t, const T &f) { if (t < f) { t = f; return true; } return false; }

template <unsigned M_> struct ModInt {
  static constexpr unsigned M = M_;
  unsigned x;
  constexpr ModInt() : x(0U) {}
  constexpr ModInt(unsigned x_) : x(x_ % M) {}
  constexpr ModInt(unsigned long long x_) : x(x_ % M) {}
  constexpr ModInt(int x_) : x(((x_ %= static_cast<int>(M)) < 0) ? (x_ + static_cast<int>(M)) : x_) {}
  constexpr ModInt(long long x_) : x(((x_ %= static_cast<long long>(M)) < 0) ? (x_ + static_cast<long long>(M)) : x_) {}
  ModInt &operator+=(const ModInt &a) { x = ((x += a.x) >= M) ? (x - M) : x; return *this; }
  ModInt &operator-=(const ModInt &a) { x = ((x -= a.x) >= M) ? (x + M) : x; return *this; }
  ModInt &operator*=(const ModInt &a) { x = (static_cast<unsigned long long>(x) * a.x) % M; return *this; }
  ModInt &operator/=(const ModInt &a) { return (*this *= a.inv()); }
  ModInt pow(long long e) const {
    if (e < 0) return inv().pow(-e);
    ModInt a = *this, b = 1U; for (; e; e >>= 1) { if (e & 1) b *= a; a *= a; } return b;
  }
  ModInt inv() const {
    unsigned a = M, b = x; int y = 0, z = 1;
    for (; b; ) { const unsigned q = a / b; const unsigned c = a - q * b; a = b; b = c; const int w = y - static_cast<int>(q) * z; y = z; z = w; }
    assert(a == 1U); return ModInt(y);
  }
  ModInt operator+() const { return *this; }
  ModInt operator-() const { ModInt a; a.x = x ? (M - x) : 0U; return a; }
  ModInt operator+(const ModInt &a) const { return (ModInt(*this) += a); }
  ModInt operator-(const ModInt &a) const { return (ModInt(*this) -= a); }
  ModInt operator*(const ModInt &a) const { return (ModInt(*this) *= a); }
  ModInt operator/(const ModInt &a) const { return (ModInt(*this) /= a); }
  template <class T> friend ModInt operator+(T a, const ModInt &b) { return (ModInt(a) += b); }
  template <class T> friend ModInt operator-(T a, const ModInt &b) { return (ModInt(a) -= b); }
  template <class T> friend ModInt operator*(T a, const ModInt &b) { return (ModInt(a) *= b); }
  template <class T> friend ModInt operator/(T a, const ModInt &b) { return (ModInt(a) /= b); }
  explicit operator bool() const { return x; }
  bool operator==(const ModInt &a) const { return (x == a.x); }
  bool operator!=(const ModInt &a) const { return (x != a.x); }
  // !
  bool operator<(const ModInt &a) const { return (x < a.x); }
  friend std::ostream &operator<<(std::ostream &os, const ModInt &a) { return os << a.x; }
};

constexpr unsigned MO = 1'000'000'007;
using Mint = ModInt<MO>;


unsigned xrand() {
  static unsigned x = 314159265, y = 358979323, z = 846264338, w = 327950288;
  unsigned t = x ^ x << 11; x = y; y = z; z = w; return w = w ^ w >> 19 ^ t ^ t >> 8;
}


vector<Mint> findLinearRecurrence(const vector<Mint> &as) {
  const int n = as.size();
  int d = 0, m = 0;
  vector<Mint> cs(n + 1, 0), bs(n + 1, 0);
  cs[0] = bs[0] = 1;
  Mint invBef = 1;
  for (int i = 0; i < n; ++i) {
    ++m;
    Mint dif = as[i];
    for (int j = 1; j < d + 1; ++j) dif += cs[j] * as[i - j];
    if (dif.x != 0) {
      auto csDup = cs;
      const Mint r = dif * invBef;
      for (int j = m; j < n; ++j) cs[j] -= r * bs[j - m];
      if (2 * d <= i) {
        d = i + 1 - d;
        m = 0;
        bs = csDup;
        invBef = dif.inv();
      }
    }
  }
  cs.resize(d + 1);
  return cs;
}

vector<Mint> powerRev(const vector<Mint> &cs, Int e) {
  assert(!cs.empty());
  assert(cs[0] == 1);
  const int d = (int)cs.size() - 1;
  if (d == 0) {
    return {};
  } else if (d == 1) {
    return {cs[0].pow(e)};
  }
  auto mul = [&](const vector<Mint> &fs, const vector<Mint> &gs) {
    vector<Mint> hs(d + d - 1, 0);
    for (int i = 0; i < d; ++i) for (int j = 0; j < d; ++j) {
      hs[i + j] += fs[i] * gs[j];
    }
    for (int i = d + d - 1; --i >= d; ) {
      for (int j = 1; j <= d; ++j) {
        hs[i - j] -= cs[j] * hs[i];
      }
    }
    hs.resize(d);
    return hs;
  };
  vector<Mint> xs(d, 0), ys(d, 0);
  xs[1] = 1;
  ys[0] = 1;
  for (; ; xs = mul(xs, xs)) {
    if (e & 1) ys = mul(ys, xs);
    if (!(e >>= 1)) break;
  }
  return ys;
}


constexpr int MAX_M = 40;
constexpr int MAX_N = 1 << 10;

Mint dp[MAX_N][MAX_M];
vector<Mint> asss[MAX_M + 1][MAX_M];
vector<Mint> css[MAX_M + 1];

int main() {
  for (int M = 1; M <= MAX_M; ++M) {
    for (int N = 16; ; N <<= 1) {
      assert(N <= MAX_N);
      for (int n = 0; n < N; ++n) {
        fill(dp[n], dp[n] + M, 0);
      }
      dp[0][1 % M] = 1;
      for (int i = 1; i <= M; ++i) {
        for (int n = 0; n + 1 < N; ++n) {
          for (int x = 0; x < M; ++x) {
            dp[n + 1][(x * i) % M] += dp[n][x];
          }
        }
      }
      auto findMinPoly = [&]() -> vector<Mint> {
        vector<Mint> coef(M);
        for (int x = 0; x < M; ++x) {
          coef[x] = xrand();
        }
        vector<Mint> bs(N, 0);
        for (int n = 0; n < N; ++n) {
          for (int x = 0; x < M; ++x) {
            bs[n] += coef[x] * dp[n][x];
          }
        }
        return findLinearRecurrence(bs);
      };
      const auto cs = findMinPoly();
      const auto cs1 = findMinPoly();
      if (cs == cs1 && 3 * ((int)cs.size() - 1) <= N) {
        for (int x = 0; x < M; ++x) {
          asss[M][x].resize(N);
          for (int n = 0; n < N; ++n) {
            asss[M][x][n] = dp[n][x];
          }
        }
        css[M] = cs;
cerr<<M<<": "<<N<<" "<<(int)cs.size()-1<<endl;
        break;
      }
    }
  }
  
  for (int numCases; ~scanf("%d", &numCases); ) { for (; numCases--; ) {
    Int N;
    int M;
    scanf("%lld%d", &N, &M);
    
    const auto fs = powerRev(css[M], N);
    vector<Mint> ans(M, 0);
    for (int x = 0; x < M; ++x) {
      for (int n = 0; n < (int)fs.size(); ++n) {
        ans[x] += fs[n] * asss[M][x][n];
      }
    }
    
    for (int x = 0; x < M; ++x) {
      if (x) printf(" ");
      printf("%u", ans[x].x);
    }
    puts("");
  }
#ifndef LOCAL
  break;
#endif
  }
  return 0;
}
