#include <bits/stdc++.h>
using namespace std;

vector<int> v, w;
long long ans;

// merges the sorted arrays w[lo .. mid) and w[mid .. hi)
void merge(int lo, int mid, int hi) {
    vector<int> aux;

    int i = lo, j = mid;
    while (i < mid && j < hi)
        if (v[w[i]] < v[w[j]])
            aux.push_back(w[i++]);
        else {
            aux.push_back(w[j++]);
            ans += mid - i;
        }

    while (i < mid)
        aux.push_back(w[i++]);

    while (j < hi)
        aux.push_back(w[j++]);

    copy(aux.begin(), aux.end(), w.begin() + lo); // w[lo .. hi) = aux[0 .. k)
}

void mergesort(int lo, int hi) {
    int mid = (lo + hi) / 2;
    if (lo + 1 < mid)
        mergesort(lo, mid);

    if (mid + 1 < hi)
        mergesort(mid, hi);

    // w[lo .. mid) and w[mid .. hi) are now sorted
    merge(lo, mid, hi);
}

int main() {
    int n;
    cin >> n;

    v.resize(n);
    w.resize(n);

    int i, x;
    for (i = 0; i < n; i++) {
        cin >> x;
        v[x - 1] = i;
    }

    for (auto &it: w) {
        cin >> it;
        --it;
    }

    mergesort(0, n);
    cout << ans;
    return 0;
}
