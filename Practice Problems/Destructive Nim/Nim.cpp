#include <bits/stdc++.h>
using namespace std;
int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int tt;
  cin >> tt;
  while (tt--) {
    int n;
    cin >> n;
    vector<int> a(n);
    int cnt = 0;
    for (int i = 0; i < n; i++) {
      cin >> a[i];
      cnt += (a[i] == 1);
    }
    if (*max_element(a.begin(), a.end()) == 1) {
      cnt += 1;
    }
    cout << (cnt % 2 == 0 ? "Utkarsh" : "Ashish") << '\n';
  }
  return 0;
}
