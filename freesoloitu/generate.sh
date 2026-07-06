#!/bin/bash
DATA_DIR="./data/secret"

for file in "$DATA_DIR"/*.in; do
    python3 submissions/accepted/tabular_solution.py < "$file" > "${file%.in}.ans"
done
