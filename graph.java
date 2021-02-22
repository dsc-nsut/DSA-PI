import java.io.*;
import java.util.*;

class Graph
{
    private int V;
    private LinkedList<Integer> adj[];

    Graph(int v)
    {
        V = v;
        adj = new LinkedList[v];
        for (int i=0; i<v; ++i)
            adj[i] = new LinkedList();
    }

    void addEdge(int v,int w)
    {
        adj[v].add(w);
    }

    public static void main(String args[])
    {
    /*
     10---30---50
     |\   |   /
     | \  |  /
     |  \ |/
    20---40
    */
        Graph g = new Graph(5);

        g.addEdge(10, 20);
        g.addEdge(10, 40);
        g.addEdge(10, 30);
        g.addEdge(20, 40);
        g.addEdge(30, 40);
        g.addEdge(30, 50);
        g.addEdge(40, 50);

    }
}