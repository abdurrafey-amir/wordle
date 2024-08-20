import pygame


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

def draw_board():
    for col in range(5):
        for row in range(6):
            pygame.draw.rect(screen, (255, 255, 255), (col * 100 + 12, row * 100 + 12, 75, 75), 2)
            text = font.render(board[row][col], True, (255, 255, 255))
            screen.blit(text, (col * 100 + 35, row * 100 + 25))

# other rects
info = pygame.Rect(0, HEIGHT - 80, WIDTH, 80)
info_text = font.render('Wordle', True, (255, 255, 255))


# colors
grey = pygame.Color('grey12')

# main loop
running = True
while running:
    # fps
    clock.tick(60)

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    screen.fill(grey)
    draw_board()
    pygame.draw.rect(screen, (255, 255, 255), info, 2)
    inf = screen.blit(info_text, (WIDTH / 2 - 70, HEIGHT - 60))


    # update display
    pygame.display.flip()

pygame.quit()