import pygame,sys
from pygame.locals import *
import time
from tkinter import *
from tkinter import messagebox
board_index={1:(0,0),3:(200,0),5:(400,0),7:(600,0),10:(100,100),12:(300,100),14:(500,100),16:(700,100),
            17:(0,200),19:(200,200),21:(400,200),23:(600,200),26:(100,300),28:(300,300),30:(500,300),32:(700,300),
            33:(0,400),35:(200,400),37:(400,400),39:(600,400),42:(100,500),44:(300,500),46:(500,500),48:(700,500),
            49:(0,600),51:(200,600),53:(400,600),55:(600,600),58:(100,700),60:(300,700),62:(500,700),64:(700,700)}

red_pawn={}
blue_pawn={}

Score_board=[0,0]
def drawBackground():
    RectangleObjects=[]
    for i in range(0,800,100):
        if(i%200==0):
            for j in range(0,800,200):
                pygame.draw.rect(Window,(0,0,0),Rect(i,j,100,100))
    for i in range(100,800,100):
        if(i%200!=0):
            for j in range(100,800,200):
                pygame.draw.rect(Window,(0,0,0),Rect(i,j,100,100))

def find_block(point):
    for i in board_index:
        if(point[0]>=board_index[i][0] and point[0]<board_index[i][0]+100 and point[1]>=board_index[i][1] and point[1]<board_index[i][1]+100):
            return i
    return -1

def empty_block(x):
    if(red_pawn.get(x)!=None):
        return False
    elif(blue_pawn.get(x)!=None):
        return False
    else:
        return True

def draw_score(Window):
    font = pygame.font.Font('freesansbold.ttf', 20)  
    text = font.render('Scores Are:', True, (0,0,0))
    textRect = text.get_rect()  
    textRect.center = (800+((200) // 2), 800 // 2 - 100)  
    Window.blit(text, textRect)
    text = font.render('Red : '+str(Score_board[0]), True, (0,0,0))
    textRect = text.get_rect()  
    textRect.center = (800+((200) // 2), 800 // 2)  
    Window.blit(text, textRect)  
    text = font.render('Blue : '+str(Score_board[1]), True, (0,0,0))
    textRect = text.get_rect()  
    textRect.center = (800+((200) // 2), 800 // 2+100)  
    Window.blit(text, textRect)  

def drawpawn(x,y,color):
    pygame.draw.circle(Window, color, (x+50,y+50), 30)

def draw_restart():
    red_pawn.clear()
    blue_pawn.clear()
    for i in board_index:
        t=board_index.get(i)
        if(i<=23):
            drawpawn(t[0],t[1],(255,0,0))
            red_pawn[i]="pawn"
        elif(i>=42):
            drawpawn(t[0],t[1],(0,255,255))
            blue_pawn[i]="pawn"
def possible(x,y):
    if(x>=0 and x<=700 and y>=0 and y<=700):
        return True
    return False
def move_pawn(firstChoice,secondChoice,Player,Window):
    x=find_block(firstChoice)
    y=find_block(secondChoice)
   # print(x,y)
    if(x==-1 or y==-1):
        return -1
    else:
        a=board_index[x][0]
        b=board_index[x][1]
        c=board_index[y][0]
        d=board_index[y][1]
       # print(abs(a-c),abs(b-d))
        if(Player==(255,0,0)):
            if(abs(a-c)!=100 or abs(b-d)!=100 or (red_pawn.get(x)!=None and red_pawn[x]=="pawn" and d<=b)):
                return -1
            elif(empty_block(y)):
                if(y==58 or y==60 or y==62 or y==64):
                    red_pawn[y]="king"
                else:
                    red_pawn[y]=red_pawn[x]
                del red_pawn[x]
                drawpawn(c,d,Player)
                drawpawn(a,b,(0,0,0))
                if(red_pawn[y]=="king"):
                    font = pygame.font.Font('freesansbold.ttf', 20)  
                    text = font.render('K', True, (0,0,0))
                    textRect = text.get_rect()  
                    textRect.center = (c+50,d+50)  
                    Window.blit(text, textRect)
                return 1
            elif(blue_pawn.get(y)!=None):
                diff_x=c-a
                diff_y=d-b
                if(possible(c+diff_x,d+diff_y) and empty_block(find_block((c+diff_x,d+diff_y)))):
                    drawpawn(c,d,(0,0,0))
                    drawpawn(a,b,(0,0,0))
                    drawpawn(c+diff_x,d+diff_y,Player)
                    l=find_block((c+diff_x,d+diff_y))
                    if(l==58 or l==60 or l==62 or l==64):
                        red_pawn[l]="king"
                    else:
                        red_pawn[l]=red_pawn[x]
                    del red_pawn[x]
                    del blue_pawn[y]
                    if(red_pawn[l]=="king"):
                        font = pygame.font.Font('freesansbold.ttf', 20)  
                        text = font.render('K', True, (0,0,0))
                        textRect = text.get_rect()  
                        textRect.center = (c+diff_x+50,d+diff_y+50)  
                        Window.blit(text, textRect)
                    return 1
                else:
                    return -1
            else:
                return -1
        elif(Player==(0,255,255)):
            if(abs(a-c)!=100 or abs(b-d)!=100 or (blue_pawn.get(x)!=None and blue_pawn[x]=="pawn" and d>=b)):
                return -1
            elif(empty_block(y)):
                drawpawn(c,d,Player)
                drawpawn(a,b,(0,0,0))
                if(y==1 or y==3 or y==5 or y==7):
                    blue_pawn[y]="king"
                else:
                    blue_pawn[y]=blue_pawn[x]
                del blue_pawn[x]
                if(blue_pawn[y]=="king"):
                    font = pygame.font.Font('freesansbold.ttf', 20)  
                    text = font.render('K', True, (0,0,0))
                    textRect = text.get_rect()  
                    textRect.center = (c+50,d+50)  
                    Window.blit(text, textRect)
                return 1
            elif(red_pawn.get(y)!=None):
                diff_x=c-a
                diff_y=d-b
                if(possible(c+diff_x,d+diff_y) and empty_block(find_block((c+diff_x,d+diff_y)))):
                    drawpawn(c,d,(0,0,0))
                    drawpawn(a,b,(0,0,0))
                    drawpawn(c+diff_x,d+diff_y,Player)
                    l=find_block((c+diff_x,d+diff_y))
                    if(l==1 or l==3 or l==5 or l==7):
                        blue_pawn[l]="king"
                    else:
                        blue_pawn[l]=blue_pawn[x]
                    del blue_pawn[x]
                    del red_pawn[y]
                    if(blue_pawn[l]=="king"):
                        font = pygame.font.Font('freesansbold.ttf', 20)  
                        text = font.render('K', True, (0,0,0))
                        textRect = text.get_rect()  
                        textRect.center = (c+diff_x+50,d+diff_y+50)  
                        Window.blit(text, textRect)
                    return 1
                else:
                    return -1
            else:
                return -1
        else:
            return -1
def bot(turn):
    turn=True
    return turn
def main():
    pygame.init()
    global Window
    Window = pygame.display.set_mode((1000,800))
    Window.fill((255,255,255))
    pygame.display.set_caption('First Game')
    drawBackground()
    draw_restart()
    print(Score_board)
    draw_score(Window)
    pygame.display.update()
    flag=0
    turn=True
    while True:
        if(not bool(red_pawn) and not bool(blue_pawn)):
            Tk().wm_withdraw() #to hide the main window
            messagebox.showinfo('Message','NO-ONE WON')
            main()
        elif(not bool(red_pawn)):
            Tk().wm_withdraw() #to hide the main window
            messagebox.showinfo('Message','BLUE WON')
            Score_board[1]+=1
            main()
        elif(not bool(blue_pawn)):
            Tk().wm_withdraw() #to hide the main window
            messagebox.showinfo('Message','RED WON')
            Score_board[0]+=1
            main()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.MOUSEBUTTONUP:
                mouse_position=pygame.mouse.get_pos()
                    #print(mouse_position)
                pygame.display.update()
                if (flag==0):
                    firstChoice=mouse_position
                    flag=1
                else:
                    secondChoice=mouse_position
                    flag=0
                    x=find_block(firstChoice)
                    if(x==-1):
                        print("INVALID MOVE")
                    else:
                        if(turn==False and red_pawn.get(x)!=None):
                            Player=(255,0,0)
                            v=move_pawn(firstChoice,secondChoice,Player,Window)
                            if(v==1):
                                pygame.display.update()
                                turn=True
                               # turn=bot(turn)
                            else:
                                print("INVALID MOVE")
                        elif(turn ==True and blue_pawn.get(x)!=None):
                            Player=(0,255,255)
                            v=move_pawn(firstChoice,secondChoice,Player,Window)
                            if(v==1):
                                pygame.display.update()
                                turn=False
                               # turn=bot(turn)
                            else:
                                print("INVALID MOVE")
                        else:
                            print("INVALID MOVE")
                



if __name__=="__main__":
    main()