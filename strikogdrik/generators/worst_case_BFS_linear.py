from collections import deque
import random
def input_generator(n,m):
    patterns = ["Rib", "Stockinette", "Lace"]
    tp = random.choice(["Rib", "Stockinette", "Lace"])
    patterns.remove(tp)
    edges = set()

    #Check valid m
    max_edges = n * (n - 1) // 2
    if m > max_edges:
        print(f"Maximum possible edges for {n} nodes is {max_edges}")
        return
    
     # Create deep path
    for i in range(1, m):
        pattern = patterns[0] if i % 2 == 0 else patterns[1]
        edges.add((i, i + 1, pattern))
            
    # Solution at end
    edges.add((n-1,n,tp))
    
    # Formatting
    print(tp)
    print(n, len(edges))
    for a,b, pattern in edges:
        print(a,b, pattern)
input_generator(10**6,((10**6)-1))
#input_generator(10,20)
