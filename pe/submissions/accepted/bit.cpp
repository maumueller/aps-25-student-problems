#include <bits/stdc++.h>
constexpr int N(1e6);
using namespace std;

int n, bit[N + 1];
void update(int i) {
    for (; i <= n; i += i & -i)
        ++bit[i];
}

int query(int i) {
    int ans = 0;
    for (; i; i -= i & -i)
        ans += bit[i];

    return ans;
}

int v[N + 1];
int main() {
    cin >> n;

    int i, x;
    for (i = 1; i <= n; ++i) {
        cin >> x;
        v[x] = i;
    }

    auto ans = (long long)n * (n - 1) / 2;
    for (i = 1; i <= n; ++i) {
        cin >> x;
        ans -= query(v[x]);
        update(v[x]);
    }

    cout << ans << '\n';
    return 0;
}
