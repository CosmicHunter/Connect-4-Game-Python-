import numpy as np
import pygame
import sys
import math
row_cnt = 6
col_cnt = 7
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)  # Yellow is the combination of both red and green


def drop_piece(board,row,col,piece):
    board[row][col]=piece


def is_valid_location(board,col):
    return board[row_cnt-1][col]==0


def get_next_open_row(board,col):
     for i in range(row_cnt):
         if board[i][col]==0:
             return i


def create_board():
    board = np.zeros((row_cnt,col_cnt))
    return board


def winning_move(board,piece):
    # Check horizontal locations for win
    for c in range(col_cnt-3):
        for r in range(row_cnt):
            if (board[r][c]==piece and board[r][c+1]==piece and board[r][c+2]==piece and board[r][c+3]==piece):
                 return True

    # Check for vertical locations for win
    for r in range(row_cnt-3):
        for c in range(col_cnt):
            if (board[r][c]==piece and board[r+1][c]==piece and board[r+2][c]==piece and board[r+3][c]==piece):
                return True

    # Check for the diagonal locations for win (positively sloped )

    for r in range(row_cnt-3):
        for c in range(col_cnt-3):
            if(board[r][c]==piece and board[r+1][c+1]==piece and board[r+2][c+2]==piece and board[r+3][c+3]==piece):
                return True

    # Check for the Negatively sloped Diagonals

    for r in range(row_cnt - 3):
        for c in range(col_cnt - 3):
            if (board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece):
                return True


def draw_board(board):
    for c in range(col_cnt):
        for r in range(row_cnt):
            pygame.draw.rect(game_screen,BLUE,(c*goti_size,r*goti_size+goti_size,goti_size,goti_size))
            centre_pos_hole = (int(c*goti_size + goti_size/2),int(r*goti_size+goti_size+goti_size/2))
            pygame.draw.circle(game_screen, BLACK, centre_pos_hole, RADIUS)

    for c in range(col_cnt):
        for r in range(row_cnt):
            if board[r][c]==1:
               pygame.draw.circle(game_screen, RED, (int(c*goti_size + goti_size/2),height-int(r*goti_size+goti_size/2)), RADIUS)
            elif board[r][c]==2:
                pygame.draw.circle(game_screen,YELLOW, (int(c*goti_size + goti_size/2),height-int(r*goti_size+goti_size/2)), RADIUS)
    pygame.display.update()  # to re render the screen

def print_board(board):
     print(np.flip(board,0))


board = create_board()
print_board(board)
game_over = False
turn = 0
pygame.init()

goti_size = 100   # Size of a goti is 100 pixels
# Defining width and Height of game board
width = col_cnt * goti_size
height = (row_cnt+1) * goti_size  # for having one extra row

gameboard_size = (width,height)   # Making a tuple defining size of the game board
RADIUS = int(goti_size/2 - 5)
game_screen = pygame.display.set_mode(gameboard_size)
draw_board(board)
pygame.display.update()
myfont = pygame.font.SysFont("monospace",75)

while not game_over:
      for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()

           if event.type == pygame.MOUSEMOTION:
               pygame.draw.rect(game_screen,BLACK,(0,0,width,goti_size))
               posx = event.pos[0]
               if turn == 0:
                   pygame.draw.circle(game_screen,RED,(posx,int(goti_size/2)),RADIUS)
               else:
                   pygame.draw.circle(game_screen,YELLOW,(posx,int(goti_size/2)),RADIUS)
               pygame.display.update()

           if event.type == pygame.MOUSEBUTTONDOWN:
                  pygame.draw.rect(game_screen, BLACK, (0, 0, width, goti_size))
                  #Ask for player 1 input
                  # print(event.pos)
                  if turn == 0:
                      posx = event.pos[0]
                      col  = int(math.floor(posx/goti_size))
                      if is_valid_location(board,col):
                          row = get_next_open_row(board,col)
                          drop_piece(board,row,col,1)
                          if winning_move(board,1):
                              print("Player 1 : Wins ")
                              label = myfont.render("Player 1:Wins !",1,RED)
                              game_screen.blit(label,(40,10))  # 40,10 is the position inside the window where we want the top left of the surface to be
                              game_over = True
                              # Blit(overlap) the surface on the canvas at the rect position

                  # BAsically we are tracing the position clicked by the user and we know game board width is
                  # 700 so if a user clicks in the range of x cordinate between 200-300 the col value will
                  # come out to be 2 based on the above formula which is correct
                  # col = int(input("Player 1 make your Selection (0-6):"))

                  # Ask for player 2 input
                  else:
                      # col = int(input("Player 2 make your Selection(0-6):"))
                      posx = event.pos[0]
                      col = int(math.floor(posx / goti_size))
                      if is_valid_location(board,col):
                          row = get_next_open_row(board,col)
                          drop_piece(board,row,col,2)
                          if winning_move(board,2):
                              print("Player 2 : Wins ")
                              label = myfont.render("Player 2:Wins !", 1, YELLOW)
                              game_screen.blit(label, (40, 10))
                              game_over = True

                  print_board(board)
                  draw_board(board)
                  turn +=1
                  turn = turn%2

                  # for the game screen to not get close immediately as a player wins

                  if game_over:
                      pygame.time.wait(3000)



