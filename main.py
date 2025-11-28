board =["-","-","-",
        "-","-","-",
        "-","-","-"]                  
rungame=True
import random
x=y=z=a=False
curplayer="X"
print("1.TwoPlayers")
print("2.OnePlayer")
tp=int(input("enter value "))

class two_player():
    
    def printboard(self,board):
            print(board[0] +" | "+board[1]+" | "+board[2])
            print("----------")
            print(board[3] +" | "+board[4]+" | "+board[5])
            print("----------")
            print(board[6] +" | "+board[7]+" | "+board[8])
    def inputplay(self,curplayer):
        while(True):
            print("enter value 1-9 of player ",curplayer," : ",end='')
            inp=int(input())            
            if board[inp-1] =="-"and inp<=9 and inp>=1:
                board[inp-1]=curplayer
                break
            else:
                print("the space is occcupied !")
    def checkhor(self):
        if board[0]==board[1]==board[2] and board[0]!="-":
            return True
        elif board[3]==board[4]==board[5] and board[3]!="-": 
            return True
        elif board[6]==board[7]==board[8] and board[6]!="-":
            return True
    def checkver(self):
        if board[0]==board[3]==board[6] and board[0]!="-":
            return True
        elif board[1]==board[4]==board[7] and board[1]!="-":
            return True
        elif board[2]==board[5]==board[8] and board[2]!="-":                                                                                
            return True
    def checkdig(self):
        if board[0]==board[4]==board[8] and board[0]!="-": 
            return True
        elif board[2]==board[4]==board[6] and board[3]!="-":
            return True
    def checkboard(self):
        if "-"not in board:
            return True
obj=two_player() 
if tp==1:                                                                                    
    while(rungame):
        obj.printboard(board)
        obj.inputplay(curplayer)
        x=obj.checkhor()
        y=obj.checkver()
        z=obj.checkdig()
        a=obj.checkboard()
        if x or y or z  :
           print("winner is ",curplayer)
           break
        if a:
            print("game is tie ")
            break   
        if curplayer=="X":
            curplayer="O"
        else:
           curplayer="X" 
           
class ai(two_player):
       def computer_move(self,board):
            while(True):  
                a=random.randrange(0,8)
                if board[a]=="-":
                    board[a]=curplayer
                    break
            #ai.printboard(two_player,board)       
obj2=ai()
if tp==2:
     obj.printboard(board)
     while(True):
        #obj.printboard(board)
        obj.inputplay(curplayer)
        obj.printboard(board)
        x=obj.checkhor()
        y=obj.checkver()
        z=obj.checkdig()
        a=obj.checkboard()
        if x or y or z  :
           print("winner is ",curplayer)
           break
        if a:
            print("game is tie ")
            break   
        if curplayer=="X":
            curplayer="O"
        else:
           curplayer="X"
        print()
        print()  
        obj2.computer_move(board)
        obj.printboard(board)
        x=obj.checkhor()
        y=obj.checkver()
        z=obj.checkdig()
        a=obj.checkboard()
        if x or y or z  :
           print("winner is ",curplayer)
           obj.printboard(board)
           break
        if a:
            print("game is tie ")
            obj.printboard(board)
            break   
        if curplayer=="X":
            curplayer="O"
        else:
           curplayer="X"  
         
         
      