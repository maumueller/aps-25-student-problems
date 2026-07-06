#include "validation.h"
#include "cmath"

int main(int argc, char *argv[]) {
    InputValidator v(argc, argv);
    int c = v.read_integer("C", 0, 100);
    v.space();
    int p = v.read_integer("P", c+1, 1000);
    v.newline();
    int t = v.read_integer("T", 0, 500);
    v.space();
    int n = v.read_integer("N", 1, 100);
    int total = n+t+1;
    v.space();
    int r = v.read_integer("R", 1, 1500);
    v.newline();
    for (int i = 0; i < n; i++) {
        int city = v.read_integer("city", 0, pow(2, 31)-1);
        v.newline();
    }
    for (int i = 0; i < r; i++) {
        int from = v.read_integer("from", 0, total);
        v.space();
        int to = v.read_integer("to", 0, total);
        v.space();
        int cap = v.read_integer("cap", 0, pow(2, 31)-1);
        v.newline();
    }
    return 0;

    // v.space();
    // int tn = v.read_integer("n", 0, 100000);
    // int tf = v.read_float("f", 0, 100000);
    // v.newline();
    // // Other useful commands:
    // // read_{float,integer}[s] takes an optional tag:
    // // Unique, Increasing, Decreasing, StrictlyIncreasing, StrictlyDecreasing
    // v.read_integers("v", /*count=*/10, 0, 1000000, Unique);
    // v.test_string("ACCEPTED"); // only succeeds when it reads the given string.
    // v.read_string("s", 4, 5);     // only succeeds when it reads a string with length in inclusive range.
    // bool b = v.peek('x'); // test the next character.
    // v.WA("The input is not valid."); // Print error and exit with code 43.
    // v.check(false, "WA on false");
}
