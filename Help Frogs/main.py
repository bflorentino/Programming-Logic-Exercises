from collections import deque

# Solving problem with BFS search algorithm
class Frogs_state():

    def __init__(self, config, parent = None, action="Initial", cost=0) -> None:
        
        self.cost = cost
        self.parent = parent
        self.action = action
        self.config = list(config)
        self.children = []
        self.blank_line = config.index('_')

    def moveWhiteFrogOne(self):

        if self.blank_line == 0 :
            return None
        
        if self.config[self.blank_line - 1] == 'W':

            target = self.blank_line - 1
            new_config = list(self.config)
            new_config[self.blank_line], new_config[target] = new_config[target],new_config[self.blank_line]
            return Frogs_state(new_config, parent=self, action='w', cost=self.cost + 1)
        
        else:
            return None


    def moveBlackFrogOne(self):

        if self.blank_line == len(self.config) - 1:
            return None
        
        if self.config[self.blank_line + 1 ] == 'B':

            target = self.blank_line + 1
            new_config = list(self.config)
            new_config[self.blank_line], new_config[target] = new_config[target],new_config[self.blank_line]
            return Frogs_state(new_config,  parent=self, action='b', cost=self.cost + 1)
        
        else:
            return None


    def makeWhiteFrogJump(self):

        if self.blank_line < 2:
            return None

        if self.config[self.blank_line - 2] == 'W' and self.config[self.blank_line - 1 ] == 'B':

            target = self.blank_line - 2
            new_config = list(self.config)
            new_config[self.blank_line], new_config[target] = new_config[target], new_config[self.blank_line]
            return Frogs_state(new_config, parent=self, action='j', cost=self.cost + 1)
        
        else:
            return None
        

    def makeBlackFrogJump(self):

        if self.blank_line > len(self.config) - 3:
            return None

        if self.config[self.blank_line + 2] == 'B' and self.config[self.blank_line + 1 ] == 'W':

            target = self.blank_line + 2
            new_config = list(self.config)
            new_config[self.blank_line], new_config[target] = new_config[target], new_config[self.blank_line]
            return Frogs_state(new_config, parent=self, action='j', cost=self.cost + 1)
        
        else:
            return None

    def expand(self):
        
        # Expand nodes
        # Movements in order w - b - w (jump) - b (jump)
        # Cost must be greater than 0 to indicate that the white frog made a movement
        if len(self.children) == 0:

            wchild = self.moveWhiteFrogOne()
            bchild = self.moveBlackFrogOne()
            wchildWithJump = self.makeWhiteFrogJump()
            bchildWithJump = self.makeBlackFrogJump()

            if wchild != None:
                self.children.append(wchild)

            if bchild != None and self.cost > 0:
                
                self.children.append(bchild)

            if wchildWithJump != None and self.cost > 0:
                self.children.append(wchildWithJump)
            
            if bchildWithJump != None and self.cost > 0:
                self.children.append(bchildWithJump)

        return self.children


def BFS(initialState):
# BFS Algorithm search

    frontier = deque();
    openList = []
    explored = []
    frontier.append(initialState)
    openList.append(initialState.config)

    print("Searching...")
    while len(frontier) > 0:
        newState = frontier.popleft()

        if testGoal(newState):          
            return ''.join(getSolutionMovements(initialState.action, newState))

        explored.append(newState.config)

        #Expanding children
        for child in newState.expand():
            if(child.config not in explored and child.config not in openList):
                    frontier.append(child)
                    openList.append(child.config)
    
    print("No solution was found")
    return None


def testGoal(state):
    
    stateList = tuple(state.config)
    leftSide = stateList[slice(state.blank_line)]
    rightSide = stateList[slice(state.blank_line + 1, len(state.config))]

    if('W' not in leftSide and 'B' not in rightSide):
        return True

    return False


def getSolutionMovements(initNode, state):

    reconst_path = []
    node = state

    while node.parent != None:
        reconst_path.append(node.action)
        node = node.parent

    return reconst_path[::-1]


def main():

    nValue = int(input("Introduce the N value "))    
    wPositions = ''.join(['W' for i in range(0, nValue)])
    bPositions = ''.join(['B' for i in range(0, nValue)])
    initialState = f"{wPositions}_{bPositions}"
    hardState = Frogs_state(initialState)
    print(BFS(hardState))

if __name__ == '__main__':
    main()  