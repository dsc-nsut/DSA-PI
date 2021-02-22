#include<bits/stdc++.h>
using namespace std;


void addEdge(vector<int> adj[], int u, int v)
{
    adj[u].push_back(v);
    adj[v].push_back(u);
}


int main()
{
    /*
    10---30---50
     |\   |   /
     | \  |  /
     |  \ |/
    20---40
    */
    int V = 5;
    vector<int> adj[V];
    addEdge(adj, 10, 20);
    addEdge(adj, 10, 40);
    addEdge(adj, 10, 30);
    addEdge(adj, 20, 40);
    addEdge(adj, 30, 40);
    addEdge(adj, 30, 50);
    addEdge(adj, 40, 50);

    return 0;
}