import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class BinaryNetworkFlow {
    static class Edge {
        Node to;
        long capacity;
        long flow;
        long tempCap;

        Edge(Node to, long capacity) {
            this.to = to;
            this.capacity = capacity;
            this.flow = 0;
            this.tempCap = capacity;
        }
    }

    static class Node {
        int id;
        List<Edge> edges;

        Node(int id) {
            this.id = id;
            this.edges = new ArrayList<>();
        }

        void addEdge(Node to, long capacity) {
            edges.add(new Edge(to, capacity));
        }
    }

    static long[] maxFlow(int source, int sink, Node[] network, long flowLimit) {
        // Reset flows and tempCaps
        for (Node node : network) {
            if (node == null) continue;
            for (Edge e : node.edges) {
                e.flow = 0;
                e.tempCap = (e.to.id != sink)
                    ? Math.min(e.capacity, flowLimit)
                    : e.capacity;
            }
        }

        long maxFlow = 0;
        int n = network.length;
        int[] parent = new int[n];

        while (true) {
            // BFS
            Arrays.fill(parent, -1);
            Queue<Integer> queue = new LinkedList<>();
            queue.add(source);
            parent[source] = source;
            boolean found = false;

            while (!queue.isEmpty() && !found) {
                int u = queue.poll();
                for (Edge e : network[u].edges) {
                    int v = e.to.id;
                    if (parent[v] == -1 && e.tempCap - e.flow > 0) {
                        parent[v] = u;
                        if (v == sink) { found = true; break; }
                        queue.add(v);
                    }
                }
            }
            if (parent[sink] == -1) break;

            long push = Long.MAX_VALUE;
            int v = sink;
            while (v != source) {
                int u = parent[v];
                for (Edge e : network[u].edges) {
                    if (e.to.id == v) {
                        push = Math.min(push, e.tempCap - e.flow);
                        break;
                    }
                }
                v = parent[v];
            }

            maxFlow += push;
            v = sink;
            while (v != source) {
                int u = parent[v];

                for (Edge e : network[u].edges) {
                    if (e.to.id == v) {
                        e.flow += push;
                        break;
                    }
                }

                for (Edge e : network[v].edges) {
                    if (e.to.id == u) {
                        e.flow -= push;
                        break;
                    }
                }
                v = u;
            }
        }
        return new long[]{maxFlow};
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] line = br.readLine().split(" ");
        int C = Integer.parseInt(line[0]);
        int P = Integer.parseInt(line[1]);
        line = br.readLine().split(" ");
        int T = Integer.parseInt(line[0]);
        int N = Integer.parseInt(line[1]);
        int R = Integer.parseInt(line[2]);

        int endPoint = N + T + 1;
        Node[] network = new Node[endPoint + 1];

        network[0] = new Node(0);
        network[endPoint] = new Node(endPoint);

        for (int i = 0; i < T; i++) {
            network[i + 1] = new Node(i + 1);
        }
        for (int i = 0; i < N; i++) {
            long cap = Long.parseLong(br.readLine());
            Node city = new Node(T + i + 1);
            city.addEdge(network[endPoint], cap);
            network[T + i + 1] = city;
        }
        for (int i = 0; i < R; i++) {
            line = br.readLine().split(" ");
            int u = Integer.parseInt(line[0]);
            int v = Integer.parseInt(line[1]);
            long cap = Long.parseLong(line[2]);
            network[u].addEdge(network[v], cap);
        }

        long originalMaxFlow = maxFlow(0, endPoint, network, Long.MAX_VALUE)[0];

        long low = 0, high = originalMaxFlow;
        long resultFlow = 0, resultLimit = 0;

        while (low <= high) {
            long mid = (low + high) / 2;
            long flow = maxFlow(0, endPoint, network, mid)[0];
            if (flow == originalMaxFlow) {
                resultFlow = flow;
                resultLimit = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }

        long profit = resultFlow * (P - C) - resultLimit * P;
        if (profit > 0) {
            System.out.println((resultFlow - resultLimit) + " " + profit);
        } else {
            System.out.println("Not worth");
        }

        br.close();
    }
}