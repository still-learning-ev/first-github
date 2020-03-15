#this is my first game to try 
#author zeeshan lone
#I will try first object orieted approach in python
class Eight_Puzzle:
    def __init__(self):
        #we have depth from the top state
        self.depth=0
        self.heuristic=0 #we have heuristic distance from the current state to goal state
        self.board=[]
        self.board=[[0 for i in range(3)] for j in range(3)]
        self.goal_state=[[1,2,3],[4,5,6],[7,8,0]]
        self.free=[]
    def take_input(self):
        print("Enter the start state of the board")
        for i in range(3):
            for j in range(3):
                try:
                    temp_in=int(input())
                    if 0<=temp_in<=9:
                        self.board[i][j]=temp_in
                    else:
                        temp_in=int(input("Enter a value between 0,9 only"))
                        if 0<=temp_in<=9:
                            self.board[i][j]=temp_in#correct this this is not good
                except ValueError:
                    pass
             
    def solve(self):
        r,c=self.get_moves(self.board)#this will get the moves 
        self.swap_and_check(self.free,self.board,self.depth,r,c,self.goal)# this will check for the best state
        
    def get_moves(self,board):
        col=0
        row=0
        for i in range(3):
            for j in range(3):
                if(board[i][j]==0):
                    col=j
                    row=i
        if row>0:
            self.free.append((row-1,col))
        if col>0:
            self.free.append((row,col-1))
        if row<2:
            self.free.append((row+1,col))
        if col<2:
            self.free.append((row,col+1))
        return row,col
        
    def find_heuristic(self,new_board,goalboard):
        

    def check_open_closed(self):
        pass

    def is_goal(self):
        pass  

    def swap_and_check(self,free,new_board,depth,r,c,goal):#this will get all the moves to be swapped
        count=0
        print(self.free)
        for rc in self.free:
            row,col=rc
            print(rc)
            self.swap(new_board,depth,row,col,r,c,goal)#swap function is called
            print(rc)
            count+=1
            print("count is this {}".format(count))
        self.free=[]
        
    def swap(self,new_board,depth,row,col,r,c,goal):#swaps the cloned list
        temp=new_board[row][col]
        new_board[row][col]=new_board[r][c]
        new_board[r][c]=temp
        self.find_heuristic(new_board,goal)#this will find the heuristic

print("hello world")
p=Eight_Puzzle()
p.take_input()
print(p.board)
p.solve()