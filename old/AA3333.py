#!/usr/bin/env python3

#https://quirkycort.github.io/tutorials/20-Pygame-Zero-Basics/37-Dodge/60-enemies1.html
#https://buildmedia.readthedocs.org/media/pdf/pygame-zero/latest/pygame-zero.pdf
import pgzrun 

HEIGHT = 600
WIDTH = 800


face = Actor('face')
face.pos = (25,25+50*8)
exitGate = Actor('gate22')
exitGate.pos =(25,25+50*1)

tops = []
blocks = []

bars = []
rect = Rect(0,0,0,0)

bombs = []
bomb_list = []

rock = []
rock_list = []

score=0
timer = 0
diff = 3
diff_text={0:'Loud',1.5:'Gentle',3:'Quiet'}
lvl = 0
last_level = 5

start_button = Rect(0,0,0,0)
quit_button = Rect(0,0,0,0)
mm_button = Rect(0,0,0,0)
button = Rect(0,0,0,0)
b1 = Rect(0,0,0,0)
b2 = Rect(0,0,0,0)
b3 = Rect(0,0,0,0)

main_menu = False
game_over = False
finish = False
start_screen = True
round_screen = True
win_screen = False

mm = True

def clear():
    global tops,blocks,bombs,count,rect,bomb_list,timer,bars,score,start_button,quit_button,button,b1,b2,b3,mm_button
    face.pos = (9999,25)
    exitGate.pos = (25+50,9999)
    blocks = []
    bars = []
    bombs = []
    tops = []
    bomb_list = []
    count=0
    score=0
    rect = Rect(0,0,0,0)
    start_button = Rect(0,0,0,0)
    quit_button = Rect(0,0,0,0)
    mm_button = Rect(0,0,0,0)
    button = Rect(0,0,0,0)
    b1 = Rect(0,0,0,0)
    b2 = Rect(0,0,0,0)
    b3 = Rect(0,0,0,0)

def next_level(lvl):
    global tops,blocks,bombs,count,rect,bomb_list,face,rock,rock_list,exitGate,x,finish,timer,win_screen, start_screen
    win_screen = False
    finish = False
    start_screen = False
    clear()

    if lvl==1:
        timer = 4.20+diff
        bomb_list =[37,63,57,93,134,99]
        face.pos = (25+50*14,25+50*2)
        exitGate.pos =(25+50*1,25+50*10)
        create_blocks(mainList = blocks,secondList = bomb_list,returnList2 = bombs,picName='block',picName2 = 'bomb',startnum1 =1,num1=12,num2=16)


    if lvl ==2 :
        timer = 5.05+diff
        bomb_list =[5,23,39,58,31,15,105,116,122,127,135,141,158,161,97]
                    #space space     long    long
                    #  x     y         x       y
        rect = Rect((50*2),(50*6),(25+50*14),(50))
        face.pos = (25,25+50*1)
        exitGate.pos =(25+50*15,25+50*10)
        create_blocks(mainList = blocks,secondList = bomb_list,returnList2 = bombs,picName='block',picName2 = 'bomb',startnum1 =1,num1=12,num2=16)
        create_blocks(mainList = bars, picName = 'bar1',startnum1 = 6,num1 = 7,startnum2=2,num2 = 16)

    elif lvl==3:
        timer = 5.17+diff
        bomb_list =[5,23,39,58,31,15,95,105,116,122,127,135,141,158,161, 97]
        rect = Rect(0,250,700,50)
        face.pos = (25,25+50*1) 
        exitGate.pos =(25+50*15,25+50*10)
        create_blocks(mainList = blocks,secondList = bomb_list,returnList2 = bombs,picName='block',picName2 = 'bomb',startnum1 =1,num1=12,num2=16)
        create_blocks(mainList = bars, picName = 'bar1',startnum1 = 5,num1 = 6,num2 = 14)

    elif lvl==4:
        bomb_list =[5,13,17,22,25,40,47,52,95,105,116,122,127,135,141,158]
        rect = Rect(0,250,700,50)
        timer = 7.8+diff
        face.pos = (25,25+50*8)
        exitGate.pos =(25,25+50*1)
        create_blocks(mainList = blocks,secondList = bomb_list,returnList2 = bombs,picName='block',picName2 = 'bomb',startnum1 =1,num1=12,num2=16)
        create_blocks(mainList = bars, picName = 'bar1',startnum1 = 5,num1 = 6,num2 = 14)

    elif lvl==5:
        bomb_list = [7, 21, 38, 55, 17, 50, 35, 52, 56, 25, 11, 43, 58, 76, 29, 47,  114, 81, 83, 148, 133, 165, 146, 100, 118, 134, 151, 120, 106,
                     153, 152, 138, 139, 124, 141, 158, 171, 110, 144]
        rect = Rect((50*3),(50*6),(25+50*14),(50))
        timer = 13.5+diff*2
        face.pos = (25+50*7,25+50*1)
        exitGate.pos =(25+50*4,25+50*10)
        create_blocks(mainList = blocks,secondList = bomb_list,returnList2 = bombs,picName='block',picName2 = 'bomb',startnum1 =1,num1=12,num2=16)
        create_blocks(mainList = bars, picName = 'bar1',startnum1 = 6,num1 = 7,startnum2 = 3, num2 = 16)

def create_blocks(mainList,secondList=[],returnList2 =[],thirdList=[],returnList3=[]
                  ,picName='nun',picName2='nun',picName3='nun'
                  , startnum1=0, num1=1,startnum2=0, num2=1):
    count = 0
    for i in range(startnum1,num1):
        for j in range(startnum2,num2):
            count+=1
            block = Actor(picName)
            block.x = 25+50*j
            block.y= 25+50*i
            if count in secondList:
                block2 = Actor(picName2)
                block2.pos = block.pos
                returnList2.append(block2)
            elif count in thirdList:
                block3 = Actor(picName3)
                block3.pos = block.pos
                returnList3.append(block3)    
            mainList.append(block)
             
def draw():
    screen.clear()
    if not game_over:
        for block in blocks:
            block.draw()
            
        face.draw()
        exitGate.draw()
        
        for bar in bars:
            bar.draw()
            
        for dia in bombs:
            dia.draw()
        screen.draw.text('Time: ' + str(round(timer, 2)), (330,10), color=(255,255,255), fontsize=30)
        screen.draw.rect(rect,(0,0,0))
    if start_screen:
        start_display()
    elif round_screen:
        screen.fill((70,130,180))
        display_message('GOOD JOB',('Time left was '+str(abs(round(timer,2)))+' seconds'),'NEXT ROUND',color =(144,238,144),mm=True)
    elif game_over:
        screen.fill('black')
        display_message('YOU LOST' , "nan",'RETRY',color='brown',mm=True)
    elif win_screen:
        screen.fill((34,139,34))
        display_message('VICTORY' ,('Time left was '+str(round(timer,2))+' seconds'),button_text='MAIN MENU',color =(255,192,110))

def update():
    global score, bomb_list,timer,game_over,exitGate,lvl,finish,round_screen,last_level,win_screen,start_screen,timer,mm


    if face.colliderect(exitGate):
        if lvl == last_level:
            clear()
            win_screen = True
        elif not game_over:
            round_screen = True


    if round_screen:
        game_over = False

    if finish:
        if round_screen or win_screen or mm:
            mm = False
            lvl +=1
        round_screen = False
        next_level(lvl)

    elif (timer < 0 or score == 1) and not win_screen and not win_screen :
        game_over = True
    else:
        if not round_screen and not game_over and not win_screen:
            timer -= 1 / 60
        
    if keyboard.left and face.left>=0 and not(face.colliderect(rect) and abs(face.left-rect.right) < 5) and not game_over :
        face.x = face.x-4
    elif keyboard.right and WIDTH>=face.right and not(face.colliderect(rect) and abs(face.right-rect.left) < 5) and not game_over:
        face.x = face.x+4
    elif keyboard.up and face.top>=50 and not(face.colliderect(rect) and abs(face.top-rect.bottom) < 5 ) and not game_over:
        face.y = face.y-4        
    elif keyboard.down and HEIGHT>=face.bottom and not(face.colliderect(rect) and abs(face.bottom - rect.top) < 5) and not game_over:
        face.y = face.y+4  

    if keyboard.SPACE and round_screen:
        finish = True
    if keyboard.SPACE and (game_over or win_screen):
        if game_over:
            score = 0
            game_over = False
            finish = True 
            timer = 1
        else:
            lvl = 0
            start_screen = True
            score = 0
            game_over = False
            finish = False
    

    for block in blocks:
        if face.colliderect(block) or exitGate.colliderect(block):
            blocks.remove(block)
        # for bomb in bombs:
        #     if bomb.colliderect(block):
        #         blocks.remove(block)
    for bomb in bombs:
        if face.colliderect(bomb):
            score+=1
            bombs.remove(bomb)

def display_message(heading_text , sub_heading_text = 'nan',button_text = 'nan' ,color = (255,255,255),mm = False):
    global button,mm_button
    if sub_heading_text != 'nan':
        button = Rect(WIDTH/2-150,HEIGHT/2+15,300,40)
        screen.draw.text(heading_text,    fontsize= 90, center = (WIDTH/2,HEIGHT/2-50),     color = color)
        screen.draw.text(sub_heading_text,fontsize = 30,center = (WIDTH/2, HEIGHT/2-7 ),color = color)
    else:
        button = Rect(WIDTH/2-150,HEIGHT/2+15,300,40)
        screen.draw.text(heading_text,    fontsize= 140, center = (WIDTH/2,HEIGHT/2-50),     color = color)

        
    if button_text!='nan':
        screen.draw.rect(button,(color))
        screen.draw.text(button_text,fontsize = 40,center = (WIDTH/2,HEIGHT/2+38),color = (color))
    if mm == True:
        mm_button = Rect(WIDTH/2-150,HEIGHT/2+60,300,40)
        screen.draw.rect(mm_button,(color))
        screen.draw.text('MAIN MENU',fontsize = 40,center = (WIDTH/2,HEIGHT/2+82),color = (color))

def start_display():
    global b1,b2,b3,start_button,quit_button
    screen.fill('brown')
    color = ((238,213,174))
    # screen.fill((106,74,60))   fav best
    # color = ((238,213,174))
    # screen.fill('#676767')
    # color = ((231,120,0))
    # screen.fill('#676767')
    # color = ((200,184,138))
    
    start_button = Rect(WIDTH/2-100,HEIGHT/2-70,200,45)
    quit_button = Rect(WIDTH/2-100,HEIGHT/2-20,200,45)
    b1 = Rect(WIDTH/2+100,HEIGHT/2+100,90,40)
    b2 = Rect(WIDTH/2-45,HEIGHT/2+100,90,40)
    b3 = Rect(WIDTH/2-190,HEIGHT/2+100,90,40)
    screen.draw.text('START',fontsize = 50,center = (WIDTH/2,HEIGHT/2-45),color = (color))
    screen.draw.text('QUIT',fontsize = 50,center = (WIDTH/2,HEIGHT/2+5),color = (color))
    screen.draw.text('QUIET',fontsize = 25,center = (WIDTH/2-145,HEIGHT/2+120),color = (color))
    screen.draw.text('GENTLE',fontsize = 25,center = (WIDTH/2,HEIGHT/2+120),color = (color))
    screen.draw.text('LOUD',fontsize = 25,center = (WIDTH/2+145,HEIGHT/2+120),color = (color))
    screen.draw.rect(start_button,color)
    screen.draw.rect(quit_button,color)
    screen.draw.rect(b1,color)
    screen.draw.rect(b2,color)
    screen.draw.rect(b3,color)
    screen.draw.text("AA3333",    fontsize= 90, center = (WIDTH/2,HEIGHT/2-120),     color = color)
    screen.draw.text("Difficulty Set To "+diff_text[diff],fontsize = 30,center = (WIDTH/2, HEIGHT/2+70 ),color = color)
 
def on_mouse_down(pos):
    global game_over, lvl,finish,score,diff,start_screen,blocks,timer,mm

    if button.collidepoint(pos) and round_screen:
        finish = True
    if button.collidepoint(pos) and (game_over or win_screen):
        if game_over:
            score = 0
            game_over = False
            finish = True 
            timer = 1
        else:
            lvl = 0
            start_screen = True
            score = 0
            game_over = False
            finish = False
            
    if mm_button.collidepoint(pos):
        mm = True
        lvl = 0
        start_screen = True
        score = 0
        game_over = False
        finish = False


    if start_button.collidepoint(pos):
        finish = True
        mm = True
    elif quit_button.collidepoint(pos):
        quit()    
    if b1.collidepoint(pos):
        diff = 0
    elif b2.collidepoint(pos):
        diff = 1.5
    elif b3.collidepoint(pos):
        diff =3

    
    


pgzrun.go()


    #   BOMB LIST  MAKER:::

    # chosen = []

    #global = chosen

    # if lvl==1:
    #     clear()
    #     timer = 999
    #     bomb_list =[]
    #     create_blocks(mainList = blocks,secondList = bomb_list,returnList2 = bombs,picName='block',startnum1 =1,num1=12,num2=16)

    # c = 0
    # if face.collidepoint(pos):
    #     print(chosen)
    # for block in blocks:
    #     c+=1
    #     if block.collidepoint(pos):
    #         chosen.append(c)
    #         block.pos(0,2000)