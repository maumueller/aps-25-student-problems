def validate_input():
    import sys
    import re

    def is_valid_int(token):
        return re.fullmatch(r"(0|[1-9]\d*)", token) is not None

    def read_line_expect_exact_ints(expected_count, context):
        line = sys.stdin.readline()
        if line == '':
            raise ValueError(f"{context}: Unexpected end of input.")

        if line[-1] == '\n':
            line = line[:-1]

        # New check: exact format (e.g., "1 2 3", not " 1  2 3 ")
        pattern = r"\d+(?: \d+)*"
        if not re.fullmatch(pattern, line):
            raise ValueError(f"{context, line}: Line is not properly formatted (exact spacing required).")

        tokens = line.split(" ")
        if len(tokens) != expected_count:
            raise ValueError(f"{context}: Expected {expected_count} integers, got {len(tokens)}.")

        if not all(is_valid_int(tok) for tok in tokens):
            raise ValueError(f"{context}: Contains improperly formatted integers (e.g., leading zeros).")

        return list(map(int, tokens))


    try:
        n, mini, maxi = read_line_expect_exact_ints(3, "Header")

        if n <= 0:
            raise ValueError("Number of dice must be positive.")
        if mini > maxi:
            raise ValueError("Minimum sum must be less than or equal to maximum sum.")

        for i in range(n):
            context = f"Die {i + 1}"
            line = sys.stdin.readline()
            if line == '':
                raise ValueError(f"{context}: Missing line.")

            if line[-1] == '\n':
                line = line[:-1]

            if not re.fullmatch(r"[ \d]+", line):
                raise ValueError(f"{context}: Contains invalid characters.")

            tokens = line.strip().split()
            if len(tokens) < 2:
                raise ValueError(f"{context}: Too few integers.")

            if not all(is_valid_int(tok) for tok in tokens):
                raise ValueError(f"{context}: Contains improperly formatted integers.")

            amount, *sides = map(int, tokens)
            if amount <= 0:
                raise ValueError(f"{context}: Number of sides must be positive.")
            if amount != len(sides):
                raise ValueError(f"{context}: Expected {amount} side values, got {len(sides)}.")

        # Check for trailing data
        if sys.stdin.read().strip():
            raise ValueError("Extra input after expected data.")

        sys.exit(42)  # ✅ Explicit success

    except ValueError as e:
        print("Invalid input:", e)
        sys.exit(43)  # ✅ Explicit failure

validate_input()
