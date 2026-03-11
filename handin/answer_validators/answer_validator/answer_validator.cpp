#include "validation.h"

// This program will be called as
// answer_validator input < ans
//
// You should verify the grammar of the answer file.
// See input_validator.cpp for information on how to use the Validator class.
// Furthermore you should check simple properties of the answer.

// TODO: Remove these comments, and summarize your answer validator.

int main(int argc, char *argv[]) {
    // Set up the input and answer streams.
    std::ifstream in(argv[1]);
    AnswerValidator v(argc, argv);

    int input;
    in >> input;
    // possible inputs are either two numbers or "Not worth"
    bool N = v.peek('N', "start of Not worth");
    if (N) {
        v.test_string("Not");
        v.space();
        v.test_string("worth");
        v.newline();
    } else {
        int64_t flow = (pow(2, 31)-1)*100;
        int64_t limit = flow/500;
        int a = v.read_integer("a", 1, flow-limit);
        v.space();
        int b = v.read_integer("b", 1, flow*(1000-1)-limit*1000);
        v.newline();
    }
}
