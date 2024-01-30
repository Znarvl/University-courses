// This is the CPP file you will edit and turn in.
// Also remove these comments here and add your own, along with
// comments on every function and on complex code sections.

#include "costs.h"
#include "trailblazer.h"

#include <queue>
#include <algorithm>
#include "pqueue.h"

using namespace std;

/*
 * help function to DFS  
 * using recursion,
 * starts at root and explores as far on each branch before
 * backtracking 
 * 
 */
vector<Vertex*> DFSRecursion(BasicGraph& graph, vector<Vertex*> path, Vertex* start, Vertex* end)
{
    start->visited = true;
    start->setColor(GREEN);
    if (start == end)
    {
        path.push_back(start);
    }
    else
    {
        for (Node* node: graph.getNeighbors(start))
        {
            if (!node->visited){

                vector<Vertex*> newNode = DFSRecursion(graph, path, node, end);
                if (newNode.empty())
                {
                    node->setColor(GRAY);
                }
                else
                {
                    path.push_back(start);
                    path.insert(path.end() ,newNode.begin(), newNode.end());
                    break;
                }
            }
        }
    }
    return path;
}

/*
 * Start node and resets data
 */

vector<Node *> depthFirstSearch(BasicGraph& graph, Vertex* start, Vertex* end) {
    vector<Vertex*> path;
    graph.resetData();
    return DFSRecursion(graph, path, start, end);
}


/*
 * Help function to BFS
 * collects the right nodes to build
 * a path from start to finish
 */
vector<Vertex*> buildPath(Vertex* end)
{
    vector<Vertex*> path;
    Vertex* curVertex = end;

    while(true)
    {
        if(curVertex->previous == NULL)
        {
            path.push_back(curVertex);
            break;
        }

        path.push_back(curVertex);
        curVertex = curVertex->previous;
    }
    // start node is last and end is first before reversing
    reverse(path.begin(), path.end());
    return path;
}


/* 
 * BFS algorithm
 * Starts at tree root, explores all neighbour nodes
 * at the present depth untill moving to next depth
 */
vector<Node *> breadthFirstSearch(BasicGraph& graph, Vertex* start, Vertex* end) {
   graph.resetData();
   queue<Vertex*> vertexQueue;
   vertexQueue.push(start);

   Vertex* curVertex;
   while(!vertexQueue.empty())
   {
       curVertex = vertexQueue.front();
       curVertex->setColor(GREEN);
       curVertex->visited = true;
       vertexQueue.pop();

       // Found the end
       if(curVertex == end)
       {
           break;
       }

       for(Vertex* neighbour : graph.getNeighbors(curVertex))
       {
           if(!neighbour->visited)
           {
               neighbour->visited = true;
               neighbour->previous = curVertex;
               neighbour->setColor(YELLOW);
               vertexQueue.push(neighbour);
           }
       }
   }
   return buildPath(end);
}

/*
 * Checks all nodes arou
 */
vector<Node *> dijkstrasAlgorithm(BasicGraph& graph, Vertex* start, Vertex* end) {
    graph.resetData();
    PriorityQueue<Node*> pathQueue;
    vector<Node*> path;

    for (Node* node: graph.getNodeSet()){
        node->cost = INFINITY;
        //adds all nodes to the rear
        pathQueue.enqueue(node, node->cost);
    }

    //first node
    start->cost = 0;
    pathQueue.changePriority(start, start->cost);
    while(!pathQueue.isEmpty()){
        Node* curr = pathQueue.dequeue();
        curr->visited = true;
        curr->setColor(GREEN);

        if (curr == end)
        {
            return buildPath(end);
        }
        
        for (Node* node: graph.getNeighbors(curr)){
            double dist = graph.getArc(curr,node)->cost + curr->cost;
            if(!node->visited)
            {
                if(node->cost > dist)
                {
                    node->cost = dist;
                    pathQueue.changePriority(node, node->cost);
                    node->previous = curr;
                    node->setColor(YELLOW);
                }
            }
        }
     }
}

/*
 * A* algorithm uses weighted graphs 
 * (one for start node and one for designated node)
 * to find the path least distance travelled, shortest time etc.
 */
vector<Node *> aStar(BasicGraph& graph, Vertex* start, Vertex* end) {
    graph.resetData();
    PriorityQueue<Node*> pathQueue;
    vector<Node*> path;

    for (Node* node: graph.getNodeSet()){
        node->cost = INFINITY;
        //adds all nodes to the rear
        pathQueue.enqueue(node, node->cost);
    }

    //first node
    start->cost = 0;
    pathQueue.changePriority(start, start->cost);
    while(!pathQueue.isEmpty()){
        Node* curr = pathQueue.dequeue();
        curr->visited = true;
        curr->setColor(GREEN);

        if (curr == end)
        {
            return buildPath(end);
        }

        for (Node* node: graph.getNeighbors(curr)){
            double dist = graph.getArc(curr,node)->cost + curr->cost;
            if(!node->visited)
            {
                if(node->cost > dist)
                {
                    node->cost = dist;
                    pathQueue.changePriority(node, node->cost + node->heuristic(end));
                    node->previous = curr;
                    node->setColor(YELLOW);
                }
            }
        }
     }
}
