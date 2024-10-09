import pygame
import numpy as np
from tictac import Board


class PygameDisplay:
    def __init__(self, board):
        self.board = board
        self.cell_size = 100
        self.width = self.cell_size * 3
        self.height = self.cell_size * 3
        self.colors = {
            -1: (255, 0, 0),  # Red for Human
            1: (0, 0, 255),  # Blue for Machine
            0: (255, 255, 255)  # White for empty cell
        }

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Tic Tac Toe")

    def draw_board(self):
        self.screen.fill((0, 0, 0))  # Black background

        for row in range(3):
            for col in range(3):
                cell_value = self.board.render[row, col]
                color = self.colors[cell_value]
                pygame.draw.rect(self.screen, color, (col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size))

        pygame.display.flip()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.draw_board()

        pygame.quit()


if __name__ == "__main__":
    b = Board()

    # choose the player who starts
    chance = np.random.randint(0, 2)
    if chance == 1:
        print("Human (-1) plays first")
        player = -1
    else:
        print("Machine (1) plays first")
        player = 1

    display = PygameDisplay(b)

    while True:
        display.draw_board()
        actions = b.actions()
        print(f"Player {player}; actions : {actions}")
        if player == -1:
            pos = int(input("pos ? "))
            if pos not in actions:
                print("impossible move")
                break
        else:
            if len(actions) == 9:
                pos = 0
            else:
                pos, val = b.minimax(player)
            print(f"Machine plays: {pos}")

        b.trans(pos, player)

        if b.final():
            if b.winner():
                print(f"Player {player} wins!")
            else:
                print("Tie!")
            break

        player = -player