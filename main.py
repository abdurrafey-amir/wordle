import pygame
import requests
import random


# words
words = None
api = requests.get('https://api.frontendexpert.io/api/fe/wordle-words').json()
words = api
word = list(random.choice(words))
print(word)


# general setup
pygame.init()

WIDTH = 500
HEIGHT = 670

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Wordle')
clock = pygame.time.Clock()

# board
board = [
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-'],
]

font = pygame.font.Font("freesansbold.ttf", 50)

# colors
grey = pygame.Color('grey12')
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)



rects = [[], [], [], [], []]
def draw_board():
    global rects
    
    
    for col in range(5):
        for row in range(6):
            rect = pygame.FRect((col * 100 + 12, row * 100 + 12, 75, 75))
            pygame.draw.rect(screen, (255, 255, 255), rect, 2)
            text = font.render(board[row][col], True, (255, 255, 255))
            screen.blit(text, (col * 100 + 35, row * 100 + 25))
            rects[col].append(rect)
    return rects

turn = 0

def letter(event):
    global turn 

    if event == pygame.K_a:
        input_letter('a')
    elif event == pygame.K_b:
        input_letter('b')
    elif event == pygame.K_c:
        input_letter('c')
    elif event == pygame.K_d:
        input_letter('d')
    elif event == pygame.K_e:
        input_letter('e')
    elif event == pygame.K_f:
        input_letter('f')
    elif event == pygame.K_g:
        input_letter('g')
    elif event == pygame.K_h:
        input_letter('h')
    elif event == pygame.K_i:
        input_letter('i')
    elif event == pygame.K_j:
        input_letter('j')
    elif event == pygame.K_k:
        input_letter('k')
    elif event == pygame.K_l:
        input_letter('l')
    elif event == pygame.K_m:
        input_letter('m')
    elif event == pygame.K_n:
        input_letter('n')
    elif event == pygame.K_o:
        input_letter('o')
    elif event == pygame.K_p:
        input_letter('p')
    elif event == pygame.K_q:
        input_letter('q')
    elif event == pygame.K_r:
        input_letter('r')
    elif event == pygame.K_s:
        input_letter('s')
    elif event == pygame.K_t:
        input_letter('t')
    elif event == pygame.K_u:
        input_letter('u')
    elif event == pygame.K_v:
        input_letter('v')
    elif event == pygame.K_w:
        input_letter('w')
    elif event == pygame.K_x:
        input_letter('x')
    elif event == pygame.K_y:
        input_letter('y')
    elif event == pygame.K_z:
        input_letter('z')
    

row = 0

def input_letter(letter):
    global turn, row, running
    letter = letter.upper()
    
    # turns
    if turn == 5:
            turn = 0
            row +=1
    
    # game end
    if row == 6:
        running = False
        print('Game Over')
    # print(turn)
    
    # print(turn)
    if running:
        board[row][turn] = letter
        turn += 1
    
    
    
    # print(turn)
    

r_green = False
r_yellow = False
r_red = False
recs = []


def checkword(rects):
    global turn, row, running, r_green, r_yellow, r_red, recs
    # print(word[turn])
    # print(board[row][turn])
    # correct
    if running:
        for i in range(5):
            rect = rects[i][row]
            if word[i] == board[row][i]:
                recs.append((green, rect))
            elif board[row][i] in word:
                recs.append((yellow, rect))
            elif board[row][i] not in word:
                recs.append((red, rect))
    


# other rects
info = pygame.Rect(0, HEIGHT - 80, WIDTH, 80)
info_text = font.render('Wordle', True, (255, 255, 255))



# main loop
clicked = False
running = True
while running:
    # fps
    clock.tick(60)

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            clicked = True
            letter(event.key)

            # if event.key == pygame.K_a:
            #     input_letter('a')
            # elif event.key == pygame.K_b:
            #     input_letter('b')
            # elif event.key == pygame.K_c:
            #     input_letter('c')
            # elif event.key == pygame.K_d:
            #     input_letter('d')
            # elif event.key == pygame.K_e:
            #     input_letter('e')
            # elif event.key == pygame.K_f:
            #     input_letter('f')
            # elif event.key == pygame.K_g:
            #     input_letter('g')
            # elif event.key == pygame.K_h:
            #     input_letter('h')
            # elif event.key == pygame.K_i:
            #     input_letter('i')
            # elif event.key == pygame.K_j:
            #     input_letter('j')
            # elif event.key == pygame.K_k:
            #     input_letter('k')
            # elif event.key == pygame.K_l:
            #     input_letter('l')
            # elif event.key == pygame.K_m:
            #     input_letter('m')
            # elif event.key == pygame.K_n:
            #     input_letter('n')
            # elif event.key == pygame.K_o:
            #     input_letter('o')
            # elif event.key == pygame.K_p:
            #     input_letter('p')
            # elif event.key == pygame.K_q:
            #     input_letter('q')
            # elif event.key == pygame.K_r:
            #     input_letter('r')
            # elif event.key == pygame.K_s:
            #     input_letter('s')
            # elif event.key == pygame.K_t:
            #     input_letter('t')
            # elif event.key == pygame.K_u:
            #     input_letter('u')
            # elif event.key == pygame.K_v:
            #     input_letter('v')
            # elif event.key == pygame.K_w:
            #     input_letter('w')
            # elif event.key == pygame.K_x:
            #     input_letter('x')
            # elif event.key == pygame.K_y:
            #     input_letter('y')
            # elif event.key == pygame.K_z:
            #     input_letter('z')



    screen.fill(grey)
    rects = draw_board()
    pygame.draw.rect(screen, (255, 255, 255), info, 2)
    # input_letter()
    checkword(rects)
    
    # if r_green:
    #     pygame.draw.rect(screen, green, rec, 2)
    # elif r_yellow:
    #     pygame.draw.rect(screen, yellow, rec, 2)
    # elif r_red:
    #     pygame.draw.rect(screen, red, rec, 2)
    # for rec in recs:
    #    rec
    inf = screen.blit(info_text, (WIDTH / 2 - 70, HEIGHT - 60))
    
    if clicked:
        for color, rect in recs:
            pygame.draw.rect(screen, color, rect, 2)

    # update display
    pygame.display.flip()

pygame.quit()
# print(rects)
# print(recs)