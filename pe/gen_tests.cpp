#include <bits/stdc++.h>
using namespace std;

vector<int> shuffled(const int &n, const bool &firstRun) {
    vector<int> ans(n); // create array of size n
    iota(ans.begin(), ans.end(), 1); // populate it with 1 2 3 ... n

    mt19937 m; // Mersenne Twister
    if (firstRun) // if this is the first run
        m.seed(time(nullptr)); // then set the seed to current time
    else { // if this is the second run
        random_device rd; // then use a pseudo-random number engine
        m.seed(rd()); // and set the seed to this
    }

    shuffle(ans.begin(), ans.end(), m); // shuffle the array to get a random permutation
    return ans;
}

int main() {
    int t;
    cout << "Number of test cases to generate: ";
    cin >> t;

    int i, n;
    for (i = 0; i < t - 1; ++i) {
        cout << "Choose n for test case #" << i << ": ";
        cin >> n;

        ofstream fout(to_string(i) + ".in"); // create the .in file
        fout << n << '\n'; // put n on the first line

        auto A = shuffled(n, true); // get a random permutation of 1 2 3 ... n
        for (const auto &it: A) // and print it on the next line
            fout << it << ' ';

        fout << '\n';

        auto B = shuffled(n, false); // get another random permutation of 1 2 3 ... n
        for (const auto &it: B) // and print it on the next line
            fout << it << ' ';

        fout << '\n';
        fout.close(); // close the file
    }

    cout << "Last test case will generate a worst-case scenario.\n";
    // in this scenario the first permutation will be:
    // 1 2 3 ... n
    // and the second permutation will be:
    // n n-1 n-2 ... 1
    // which requires the most number of swaps.

    cout << "Choose n: ";
    cin >> n;

    ofstream fout(to_string(i) + ".in"); // create the .in file
    fout << n << '\n'; // put n on the first line

    vector<int> A(n); // permutation A
    iota(A.begin(), A.end(), 1); // set it to 1 2 3 ... n
    for (const auto &it: A) // and print it on the next line
        fout << it << ' ';

    fout << '\n';
    vector<int> B(n); // permutation B
    iota(B.rbegin(), B.rend(), 1); // set it to n n-1 n-2 ... 1
    for (const auto &it: B) // and print it on the next line
        fout << it << ' ';

    fout << '\n';
    fout.close();
    return 0;
}
