import javax.swing.*;
import java.util.Arrays;

public class RouterNode {
  private int myID;
  private GuiTextArea myGUI;
  private RouterSimulator sim;

  private boolean PoisonedReverse = true;

  private int[] costs = new int[RouterSimulator.NUM_NODES];
  private int[] route = new int[RouterSimulator.NUM_NODES];
  // distanceTable[costFrom][costTo]
  private int[][] distanceTable = new int[RouterSimulator.NUM_NODES][RouterSimulator.NUM_NODES];

  //--------------------------------------------------
  public RouterNode(int ID, RouterSimulator sim, int[] costs) {
    myID = ID;
    this.sim = sim;
    myGUI =new GuiTextArea("  Output window for Router #"+ ID + "  ");

    System.arraycopy(costs, 0, this.costs, 0, RouterSimulator.NUM_NODES);


    // Init distanceTable
    for (int i = 0; i < RouterSimulator.NUM_NODES; i++){
      for (int j = 0; j < RouterSimulator.NUM_NODES; j++){
        if (i == j){  // distance to ourself is 0
          distanceTable[i][j] = 0;
        }
        else if (i == myID){  // we only know distances from us to others at initialization
          distanceTable[myID][j] = costs[j];
        }
        else {  // initialize all other rows as INFINITY
          distanceTable[i][j] = RouterSimulator.INFINITY;
        }
      }
    }

    // Init route, -1 if no direct path
    for (int i = 0; i < RouterSimulator.NUM_NODES; i++){
      if (costs[i] != RouterSimulator.INFINITY){
        route[i] = i;
      }
      else{
        route[i] = -1;
      }
    }
    for (int i = 0; i < RouterSimulator.NUM_NODES; i++){
      if (i != myID && costs[i] != RouterSimulator.INFINITY){
        sendUpdate(new RouterPacket(myID, i, distanceTable[myID]));
      }
    }
    printDistanceTable();
  }

  //--------------------------------------------------
  public void recvUpdate(RouterPacket pkt) {
    int[][] oldCosts = distanceTable.clone();
    distanceTable[pkt.sourceid] = pkt.mincost.clone();
    bellmanFord();
    if (!Arrays.deepEquals(oldCosts, distanceTable)){
      for (int i = 0; i < RouterSimulator.NUM_NODES; i++){
        if (i == myID) {continue;}
        if (costs[i] != RouterSimulator.INFINITY){
          sendUpdate(new RouterPacket(myID, i, distanceTable[myID]));
        }
      }
    }
  }


  //--------------------------------------------------
  private void sendUpdate(RouterPacket pkt) {
    sim.toLayer2(pkt);

  }


  //--------------------------------------------------
  public void printDistanceTable() {
    myGUI.println("\n\n\nCurrent table for " + myID + " at time " + sim.getClocktime());
    myGUI.println("Distancetable: ");
  	myGUI.print("    dst  |");
  	for(int i = 0; i < RouterSimulator.NUM_NODES; i++)
  	    myGUI.print("\t" + i);

    myGUI.print("\n-------------");
    for(int i = 0; i < RouterSimulator.NUM_NODES; i++)
        myGUI.print("------------------");

    for(int i = 0; i < RouterSimulator.NUM_NODES; i++){
      myGUI.print("\n" + " nbr " + i + " | " + "\t");
      for(int j = 0; j < RouterSimulator.NUM_NODES; j++)
        myGUI.print(distanceTable[i][j] + "\t");
      }
      myGUI.print("\n\n");

    	myGUI.println("Our distance vector and routes: ");
    	myGUI.print("     dst  |");
    	for(int i = 0; i < RouterSimulator.NUM_NODES; i++)
    	    myGUI.print("\t" + i);

    	myGUI.print("\n-------------");
    	for(int i = 0; i < RouterSimulator.NUM_NODES; i++)
    	    myGUI.print("-------------------");

    	myGUI.print("\n   cost  |\t");
    	for(int i = 0; i < RouterSimulator.NUM_NODES; i++)
          myGUI.print(String.valueOf(distanceTable[myID][i]) + "\t");

    	myGUI.print("\n  route |\t");
    	for(int i = 0; i < RouterSimulator.NUM_NODES; i++)
          if(route[i] == -1)
              myGUI.print("-\t");
          else
              myGUI.print(String.valueOf(route[i]) + "\t");

  }

  private void broadcast(){
    for (int i = 0; i < RouterSimulator.NUM_NODES; i++){
      if (i != myID && costs[i] != RouterSimulator.INFINITY && route[i] != -1){
        sendUpdate(new RouterPacket(myID, i, distanceTable[myID]));
      }
    }
  }
  //--------------------------------------------------
  public void updateLinkCost(int dest, int newcost) {
    int oldcost = costs[dest];
    costs[dest] = newcost;
    distanceTable[myID][dest] = newcost;

    bellmanFord();
    if (PoisonedReverse){
      for (int i = 0; i < RouterSimulator.NUM_NODES; i++){
        if (costs[i] != RouterSimulator.INFINITY && i != myID && i != dest){
          int[] poisonedDV = distanceTable[myID].clone();
          poisonedDV[dest] = RouterSimulator.INFINITY;
          sendUpdate(new RouterPacket(myID, i, poisonedDV));
        }
      }
    } else{
      for (int i = 0; i < RouterSimulator.NUM_NODES; i++){
        if (costs[i] != RouterSimulator.INFINITY && i != myID){
          sendUpdate(new RouterPacket(myID, i, distanceTable[myID]));
        }
      }
    }
  }


  // implements the Bellman-Ford algorithm
  public void bellmanFord() {
    for (int i = 0; i < RouterSimulator.NUM_NODES; i++){
      if (i == myID) {
        continue;
      }
      int shortest = RouterSimulator.INFINITY;
      int nextNode = -1;
      for(int j = 0; j < RouterSimulator.NUM_NODES; j++){
        if (costs[j] != RouterSimulator.INFINITY && j != myID){
          int estimatedCost = costs[j] + distanceTable[j][i];
          if (estimatedCost < shortest){
            shortest = estimatedCost;
            nextNode = j;
          }
        }
      }
      if (costs[i] < shortest){
        shortest = costs[i];
        nextNode = i;
      }
      distanceTable[myID][i] = shortest;
      //distanceTable[i][myID] = shortest;
      route[i] = nextNode;
    }
  }
}

// x == myID
// v == j
// y == i
// c(x,v) == costs[i]
// Dv(y) == distanceTable[i][destid]
// Dx(y) = min(costs[i] + distanceTable[i][destid]) for i in NUM_NODES
// maths we want: Dx(y) = minv(c(x,v) + Dv(y))
/*
loop
 wait (until I see a link cost change to some neighbor w or
           until I receive a distance vector from some neighbor w)
 for each y in N:
   Dx(y) = minv{c(x, v) + Dv(y)}

if Dx(y) changed for any destination y
    send distance vector Dx = [Dx(y): y in N] to all neighbors
forever*/
