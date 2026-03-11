#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector <int> v(n);
    for (auto &it: v)
        cin >> it;

    vector <int> w(n);
    for (auto &it: w)
        cin >> it;

    auto ans = 0ll;
    int i, j;
    for (i = 0; i < n; ++i) { // for each i, place w[i] in position i of v
        j = i; // find v[i] in w at index j
        while (w[j] != v[i])
            ++j;

        while (j > i) { // swap it repeatedly to its right place
            swap(w[j], w[j - 1]);
            --j;
            ++ans;
        }
    }

    cout << ans;
    return 0;
}
