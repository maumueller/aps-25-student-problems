
# TODO
# Check for duplicates


import sys, re

def checkLeadingZero(line):
        if len(line[0]) > 1:
            if line[0][0] == "0":
                print(1)
                sys.exit(43)

def checkForNewLine(line):
    if line[-1] != '\n':
        print(2)
        sys.exit(43)

def checkLine(line):
    if re.match(r"(?:(?:[^a-zA-Z0-9])+ (?:[^a-zA-Z0-9]*)|(?:[^a-zA-Z0-9] ))", line):
        print(line)
        print(3)
        sys.exit(43)
        
def checkSentenceLength(sen):
    if len(sen) > 50:
        print(4)
        sys.exit(43)



line = sys.stdin.readline()
checkLine(line)
sentences = set()

try:
    checkForNewLine(line)

    n, m = line.split()

    checkLeadingZero(n)
    checkLeadingZero(m)
    n = int(n)
    m = int(m)
    if n > (5 * 10**5) or m > (5 * 10**5) or n < 1 or m < 1:
        sys.exit(43)

    if n == 0 or m == 0:
        print(5)
        sys.exit(43)
    map = {}
    for i in range(n):
        line = sys.stdin.readline()
        checkLine(line)
        checkForNewLine(line)
        line = line.split()
        checkLeadingZero(line)   
        number = int(line[0])
        sentence = " ".join(line[1:]).strip()
        checkSentenceLength(sentence) 
        if sentence in sentences:
            sys.exit(43)
        sentences.add(sentence)
        map[sentence] = i
    
    for _ in range(m):
        line = sys.stdin.readline()
        checkLine(line)
        checkForNewLine(line)
        if line == "calculate\n":
            line = sys.stdin.readline()
            checkLine(line)
            checkForNewLine(line)
            sentence1 = line.strip()
            checkSentenceLength(sentence1)
            line = sys.stdin.readline()
            checkLine(line)
            checkForNewLine(line)
            sentence2 = line.strip()
            checkSentenceLength(sentence2)
            if sentence1 not in sentences or sentence2 not in sentences:
                print(sentence1)
                print(sentence2)
                print(sentences)
                print(6)
                sys.exit(43)
            if map[sentence1] > map[sentence2]:
                sys.exit(43)
        elif line == "add\n":
            line = sys.stdin.readline()
            checkLine(line)
            checkForNewLine(line)
            line = line.split()
            checkLeadingZero(line[0])
            number = int(line[0])
            if number > 2147483647 or number < -2147483648:
                sys.exit(43)
            sentence = " ".join(line[1:]).strip()
            if sentence not in sentences:
                sys.exit(43)
        else:
            sys.exit(43)



            

    line = sys.stdin.readline()
    if line != "\n":
        print(75)
        print(line)
    endoffile = False
    try:
        input()
    except EOFError:
        endoffile = True

    if not endoffile:
        sys.exit(43)
    

except ValueError:
    print(7)
    sys.exit(43)

sys.exit(42)

# if not re.match(r"(?:0|(?:[1-9][0-9]*))\n", line):
#     sys.exit(43)

# try:
#     n = int(line)
#     if not 0 <= n < 1_000_000:
#         sys.exit(43)
#
#     for _ in range(n):
#         line = sys.stdin.readline()
#         if not re.match(r"[a-zA-Z\W_]+\n", line):
#             sys.exit(43)
#     
# except ValueError:
#     sys.exit(43)
#
# if sys.stdin.readline() != "":
#     sys.exit(43)
#
# sys.exit(42)
#
