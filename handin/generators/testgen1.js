function generateGraph(numNodes) {
    if (numNodes < 2) {
        throw new Error("Graph must have at least 2 nodes (start and end).");
    }

    const graph = {};
    for (let i = 0; i < numNodes; i++) {
        graph[i] = new Set();
    }
    let edges = 0;
    
    // Create a base path from start (0) to end (numNodes-1)
    for (let i = 0; i < numNodes - 1; i++) {
        graph[i].add(i + 1);
        edges++
    }
    

    // Optionally add more edges to increase connectivity, while preserving DAG properties
    for (let i = 0; i < numNodes; i++) {
        for (let j = i + 2; j < numNodes; j++) {
            if (Math.random() < 0.3) { // 30% chance to add an extra forward edge
                graph[i].add(j);
                edges++;
            }
        }
    }

    // Convert sets to arrays for cleaner output
    for (let key in graph) {
        graph[key] = Array.from(graph[key]);
    }

    return [graph, edges];
}

// Example usage:
const numNodes = 600;
const maxCap = 1000000;
const minCap = 1000000;
const [graph, numEdges] = generateGraph(numNodes);
// console.log("Generated graph:", graph);

let postOutput = [];
console.log(1, 4); // aglet pricing
console.log(numNodes-2, 1, numEdges); // graph size
console.log(Math.floor(Math.random()*maxCap+1)); // citiy weight

let lines = 0;
for (let i = 0; i < numNodes; i++) {
    for (let node of graph[i]) {
        console.log(`${i} ${node} ${Math.floor(Math.random()*(maxCap-minCap)+minCap)}`); // caravans/edges
        lines++;
    }
}

// console.log(postOutput.join("\n")); // graph/caravans
