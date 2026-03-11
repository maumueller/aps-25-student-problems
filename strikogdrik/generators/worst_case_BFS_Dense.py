from collections import deque
import random
def input_generator(n):
    patterns = ["Rib", "Stockinette", "Lace"]
    tp = random.choice(["Rib", "Stockinette", "Lace"])
    patterns.remove(tp)
    edges = []

    #Check valid m
    max_edges = n * (n - 1) // 2
    """ if m > max_edges:
        print(f"Maximum possible edges for {n} nodes is {max_edges}")
        return """
    
     # Create deep path
    for i in range(1, n):
        for j in range(i+1,n+1):
            pattern = patterns[0] if i % 2 == 0 else patterns[1]
            edges.append((i, j, pattern))
            
    # Solution at end
    edges.append((n-1,n,tp))
    
    # Formatting
    print(tp)
    print(n, len(edges))
    for a,b, pattern in edges:
        print(a,b, pattern)
input_generator(10)
#input_generator(1_100)
#input_generator(25_000)
#input_generator(50_000)
#input_generator(80_000)
#input_generator(100_000)

