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

    
     # Create backbone path
    for i in range(1, n):
        pattern = patterns[0] if i % 2 == 0 else patterns[1]
        edges.add((i, i + 1, pattern))

    remaining_edges = m - (n - 1)

    # Add remaining edges with random connections
    while 1 < remaining_edges:
        a = random.randint(1, n - 1)
        b = random.randint(a + 1, n)
        
        # Skip if edge already exists or would modify backbone
        if (a, b) in [(x, y) for x, y, _ in edges]:
            continue
        
        # Add either regular pattern or drunk knitting
        if random.random() < 0.3:  # 30% chance for drunk edge
            edges.add((a, b, "DrunkKnitting"))
        else:
            pattern = patterns[0] if (a + b) % 2 == 0 else patterns[1]
            edges.add((a, b, pattern))
        remaining_edges-=1
            
    # Solution at end
    edges.add((n-1,n,tp))
    
    # Formatting
    print(tp)
    print(n, len(edges))
    for a,b, pattern in edges:
        print(a,b, pattern)
input_generator(100_000,50_000_000)
#input_generator(10,20)
