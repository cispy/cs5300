# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    stack = util.Stack()
    discoveredList = []
    startState = problem.getStartState()
    markedList = [startState]
    pathMap = {}
    stack.push(startState)
    currentState = startState
    while not problem.isGoalState(currentState) and not stack.isEmpty():
        currentState = stack.pop()
        if problem.isGoalState(currentState):
            break
        if currentState in discoveredList:
            continue        
        discoveredList.append(currentState)
        childList = problem.getSuccessors(currentState)
        for child in childList:
            if child[0] not in markedList:
                stack.push(child[0])
                pathMap[child[0]] = currentState, child[1]
                markedList.append(child[0])
    path = []
    while currentState != startState:
        tempState = pathMap[currentState]
        currentState = tempState[0]
        path.append(tempState[1])
    path.reverse()
    from game import Directions
    n = Directions.NORTH
    e = Directions.EAST
    s = Directions.SOUTH
    w = Directions.WEST
    output = list()
    for element in path:
        if element == 'South':
            output.append(s)
        elif element == 'West':
            output.append(w)
        elif element == 'North':
            output.append(n)
        elif element == 'East':
            output.append(e)
    return output
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    
    loc = problem.getStartState()
    currentpath = util.Stack()
    count = 0
    levelnodes = util.Queue()
    setofpath = set([loc])
    "while loop to run as long as it hasn't reach goal"
    while not problem.isGoalState(loc):
        "getting possible successors from current location"
        posspath = problem.getSuccessors(loc)
        numofsuc = len(posspath)
        parent = loc
        "expand all nodes in loc"
        for leafnode in xrange(numofsuc):
            if not posspath[leafnode][0] in setofpath:
                levelnodes.push(posspath[leafnode])
                status = posspath[leafnode] , parent
                currentpath.push(status)
                count = count + 1
                setofpath.add(posspath[leafnode][0])

        "assign the next expaned node as current loc"
        nextnode = levelnodes.pop()
        loc = nextnode[0]
        
    "find the goal location path, first section is to find the goal node"
    path = currentpath.pop()
    sub = 1
    while not path[0][0] == loc:
        path = currentpath.pop()
        sub = sub + 1
    rightpath = util.Stack()
    rightpath.push(path)
    pathcount = 1
    for track in xrange(count-sub):
        pathback = currentpath.pop()
        if path[1] == pathback[0][0]:
            rightpath.push(pathback)
            path = pathback
            pathcount = pathcount + 1
            
    from game import Directions
    n = Directions.NORTH
    e = Directions.EAST
    s = Directions.SOUTH
    w = Directions.WEST
    output = list()
    for numb in xrange(pathcount):
        finalpath = rightpath.pop()
        if finalpath[0][1] == 'South':
            output.append(s)
        if finalpath[0][1] == 'West':
            output.append(w)
        if finalpath[0][1] == 'North':
            output.append(n)
        if finalpath[0][1] == 'East':
            output.append(e)
    return output
    
    util.raiseNotDefined()

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
