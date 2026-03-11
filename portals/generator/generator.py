from random import randint , choice , shuffle
from collections import defaultdict


def makeEdges(n_nodes , n_edges, n_portals , max_weight=1):
    # verify input and find layers
    if max_weight < 1: 
        raise ValueError(f'max_weight must be greater than 0, not {max_weight}')
    
    n_middle_nodes = n_nodes - n_portals - 1
    if n_middle_nodes <= 0:
        raise ValueError('not enough nodes to accomodate sources, sinks and middle nodes')
    
    layers = findLayers(n_portals , n_nodes)

    minimum_possible_n_edges = sum(max(l1,l2) for l1,l2 in zip(layers[:-1] , layers[1:]))
    if n_edges < minimum_possible_n_edges:
        raise ValueError(f'Not enough edges for {n_nodes} nodes. For {n_nodes} nodes, {minimum_possible_n_edges} edges are required.')
    
    max_possible_n_edges = sum([a*b for a,b in zip(layers[:-1] , layers[1:])])
    if n_edges > max_possible_n_edges:
        raise ValueError(f'Too many edges for {n_nodes} nodes. {n_nodes} nodes can support at most {max_possible_n_edges} edges.')
    
    # build minimal correct graph

    unused_edge_table = []
    found_edges = []
    n_remaining_edges = n_edges
    n_nodes_before_l1 = 0
    for l1,l2 in zip(layers[:-1] , layers[1:]):
        req_edges , adj_dict = findRequiredEdges(l1 , l2 , n_nodes_before_l1 , max_weight)
        n_remaining_edges -= len(req_edges)
        found_edges.extend(req_edges)
        for v in range(n_nodes_before_l1 , n_nodes_before_l1+l1):
            unused_edge_table.append([w for w in range( n_nodes_before_l1 , n_nodes_before_l1+l1+l2 ) if w not in adj_dict[v] and w != v])
        n_nodes_before_l1 += l1
    
    # use remaining edges
    valid_start_nodes = []
    for i,lst in enumerate(unused_edge_table):
        if lst:
            shuffle(lst)
            valid_start_nodes.append(i)
    
    for _ in range(n_remaining_edges):
        v = choice(valid_start_nodes)
        w = unused_edge_table[v].pop()
        if len(unused_edge_table[v]) == 0:
            valid_start_nodes.remove(v)
        # find the layer of v to see if v and w are in the same layer
        n_nodes_in_previous_layers = 0
        for layer in layers:
            n_nodes_in_previous_layers += layer
            if n_nodes_in_previous_layers > v:
                n_nodes_in_previous_layers -= layer
                break
        # if w is in the same layer as v, make max_weight smaller
        if n_nodes_in_previous_layers <= w < n_nodes_in_previous_layers + layer:
            found_edges.append((v,w,randint(1,max(max_weight//2,1))))
        else: # if not, use standard max_weight
            found_edges.append((v,w,randint(1,max_weight)))


    portals = list(range(n_nodes-n_portals , n_nodes))
    
    return portals , found_edges
    


def findLayers(n_sinks , n_nodes):
    n_middle_nodes = n_nodes - 1 - n_sinks
    
    n_remaining_middle_nodes = n_middle_nodes
    n_layers = int(n_middle_nodes**.5)
    layers = [1]

    for n_layer in range(n_layers):
        nodes_in_this_layer = n_remaining_middle_nodes // (n_layers - n_layer)
        n_remaining_middle_nodes -= nodes_in_this_layer
        layers.append(nodes_in_this_layer)
    layers.append(n_sinks)
    return layers

         

def findRequiredEdges(l1 , l2 , n_nodes_before_l1 , max_weight):
    nbl1 = n_nodes_before_l1
    adj_dict = defaultdict(set)
    edges = []
    left_layer = list(range( nbl1 , nbl1+l1 ))
    right_layer = list(range( nbl1+l1 , nbl1+l1+l2 ))
    shuffle(right_layer)

    while left_layer or right_layer:
        if left_layer:
            v = left_layer.pop()
        else:
            v = randint( nbl1 , nbl1+l1-1 )
        if right_layer:
            w = right_layer.pop()
        else:
            w = randint(nbl1+l1 , nbl1+l1+l2-1 )

        adj_dict[v].add(w)
        edges.append((v,w,randint(1,max_weight)))
    
    return edges , adj_dict

def saveEdgesInFile(n_nodes , n_edges , n_portals , max_weight , file_name):
    portals , edges = makeEdges(n_nodes , n_edges , n_portals , max_weight)
    with open(f'./{file_name}.in','w') as doc:
        doc.write(f'{n_nodes} {len(edges)} {len(portals)}\n')
        doc.write(' '.join(map(str , portals)) + '\n')
        for v,w,weight in edges:
            doc.write(' '.join(map(str , (v,w,weight))) + '\n')


if __name__ == '__main__':
    name = input()
    runes, edges, portals, max_cap = map(int, input().split())
    saveEdgesInFile(runes , edges , portals , max_cap , name)
