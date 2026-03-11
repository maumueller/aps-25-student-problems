#!/usr/bin/env python3
import sys

try:
    with open(sys.argv[2], 'r') as f:
        judge_answer = int(f.read().strip())
    
    team_input = sys.stdin.read().strip()
    
    if not team_input:
        sys.exit(43)
    
    team_output = int(team_input)
    
    # Compare
    if team_output == judge_answer:
        sys.exit(42)
    else:
        sys.exit(43)
        
except (ValueError, IndexError, FileNotFoundError):
    sys.exit(43)
except Exception:
    sys.exit(43)