function rand(x, y) {
    return Math.floor(Math.random()*(y-x)+x);
}

function createLineGraph(nodes, cities) {

    /**@type {Array<number[]>} */
    let graph = Array.from({length: nodes}).map(_ => []);

    let tradingPosts = nodes-cities-cities-1;

    // determine the lengths of each line;
    let randoms = [0];
    let lengths = [];
    for (let i = 0; i < cities-1; i++) {
        randoms.push(rand(1, tradingPosts));
    }
    randoms.sort((a, b) => a - b);
    randoms.push(tradingPosts);
    for (let i = 1; i < cities+1; i++) {
        lengths.push(randoms[i]-randoms[i-1]);
    }
    console.log("lengths:", lengths);

    let edges = 0;
    for (let i = 0; i < cities; i++) {
        graph[0].push(++edges);
        for (let j = 0; j < lengths[i]; j++) {
            graph[edges].push(++edges);
        }
        graph[edges].push(tradingPosts+cities+1+i);
    }
    edges += cities;
    
    console.log("graph:", graph.map(e => "[" + e.join(", ") + "]"));
    console.log("edges:", edges);
    
}

// createLineGraph(30, 5)

function worstInput(nodes, cities) {

    /**@type {Array<number[]>} */
    let graph = Array.from({length: nodes}).map(_ => []);
    let graphW = Array.from({length: nodes}).map(_ => []);

    let first = nodes/4;
    let length = nodes/2;
    let last = nodes/4*3;
    /*
      0-124: first ramp
      125-349: wall
      350-499: last ramp
    */

    let edges = 0;
    
    for (let i = 0; i < length/2-1; i++) {
        graph[i].push(i+1);
        graph[last+i].push(last+i+1);
        edges++;
        edges++;
        graphW[i].push(2**31);
        graphW[last+i].push(2**31);
    }
    graph[first-1].push(last);
    graphW[first-1].push(2**31-length*first);
    edges++
    // graph[nodes-1].push(nodes);
    // graphW[nodes-1].push(2**31);
    // edges++
    
    for (let i = 0; i < length/2; i++) {
        for (let j = 0; j < length; j++) {
            graph[i].push(first+j);
            graph[first+j].push(last+i);
            edges++;
            edges++;
            graphW[i].push(1);
            graphW[first+j].push(1);
        }
    }

    
    // console.log("graph:", graph.map(e => "[" + e.join(", ") + "]"));
    return [graph, graphW, edges];
    
}

let size = 76
let [graph, graphW, edges] = worstInput(size, 0);
console.log(1, 2);
console.log(size-2, 1, edges);
console.log(2**31)
for (let i = 0; i < size; i++) {
    for (let j = 0; j < graph[i].length; j++) {
        console.log(i, graph[i][j], graphW[i][j]);
    }
}


