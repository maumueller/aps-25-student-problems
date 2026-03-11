#include <iostream>
#include <string>
#include <vector>
#include <map>


using namespace std;

vector<string> split(const string& str, char delimiter);

int main() {
    string line;
    getline(cin, line);

    map<string, long> m;
    vector<long> task_list;
    
    vector<string> inp = split(line, ' ');
    long N = stol(inp[0]);
    long M = stol(inp[1]);

    for (int i = 0; i < N; i++) {
        getline(cin, line);
        size_t end = line.find(' ');
        string str_value = line.substr(0, end);
        m[line.substr(end + 1)] = i;
        task_list.push_back(stol(str_value));
    }

    for (int i = 0; i < M; i++) {
        getline(cin, line);

        if (line == "calculate") {
            getline(cin, line);
            long fst = m[line];
            getline(cin, line);
            long snd = m[line];

            long answer = 0;
            for (int j = fst; j < snd+1; j++) {
                answer += task_list[j];
            }
            cout << answer << endl;
        } else {
            getline(cin, line);
            size_t end = line.find(' ');
            string str_value = line.substr(0, end);
            long n = stol(str_value);
            long idx = m[line.substr(end + 1)];
            task_list[idx] += stol(str_value);
        }
    }
    return 0;
}

vector<string> split(const string& str, char delimiter) {
    vector<string> tokens;
    size_t start = 0;
    size_t end = str.find(delimiter);
    
    while (end != string::npos) {
        tokens.push_back(str.substr(start, end - start));
        start = end + 1;
        end = str.find(delimiter, start);
    }

    tokens.push_back(str.substr(start));
    return tokens;
}