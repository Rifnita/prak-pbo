import pygame
import sys

class TicTacToeGUI:
  def _init_(self):
    pygame.init()
    self.screen = pygame.display.set_mode((300, 350))
    pygame.display.set_caption("Tic Tac Toe")
    self.clock = pygame.time.Clock()
    self.font = pygame.font.Font(None, 48)
    self.game = Game()
    self.square_size = 100
    self.margin = 10
    self.offset = 50

  def draw_board(self):
    self.screen.fill((255, 255, 255))
    pygame.draw.line(self.screen, (0, 0, 0), (self.offset + self.square_size, self.offset), (self.offset + self.square_size, self.offset + 3*self.square_size), 5)
    pygame.draw.line(self.screen, (0, 0, 0), (self.offset + 2*self.square_size, self.offset), (self.offset + 2*self.square_size, self.offset + 3*self.square_size), 5)
    pygame.draw.line(self.screen, (0, 0, 0), (self.offset, self.offset + self.square_size), (self.offset + 3*self.square_size, self.offset + self.square_size), 5)
    pygame.draw.line(self.screen, (0, 0, 0), (self.offset, self.offset + 2*self.square_size), (self.offset + 3*self.square_size, self.offset + 2*self.square_size), 5)

  def draw_XO(self):
    for row in range(3):
      for col in range(3):
        square = row * 3 + col
        if self.game.board[square] == 'X':
          x_pos = col * self.square_size + self.offset + self.margin
          y_pos = row * self.square_size + self.offset + self.margin
          pygame.draw.line(self.screen, (255, 0, 0), (x_pos, y_pos), (x_pos + self.square_size - 2*self.margin, y_pos + self.square_size - 2*self.margin), 5)
          pygame.draw.line(self.screen, (255, 0, 0), (x_pos, y_pos + self.square_size - 2*self.margin), (x_pos + self.square_size - 2*self.margin, y_pos), 5)
        elif self.game.board[square] == 'O':
          x_pos = col * self.square_size + self.offset + self.square_size//2
          y_pos = row * self.square_size + self.offset + self.square_size//2
          radius = self.square_size // 2 - self.margin
          pygame.draw.circle(self.screen, (0, 0, 255), (x_pos, y_pos), radius, 5)

  def run(self):
    running = True
    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not self.game.game_over:
          x, y = pygame.mouse.get_pos()
          row = (y - self.offset) // self.square_size
          col = (x - self.offset) // self.square_size
          square = row * 3 + col
          if self.game.make_move(square):
            self.game.check_winner()
      self.draw_board()
      self.draw_XO()
      if self.game.game_over:
        self.show_winner()
      pygame.display.flip()
      self.clock.tick(60)
    pygame.quit()

  def show_winner(self):
    winner = self.game.current
