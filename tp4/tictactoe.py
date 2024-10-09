import numpy as np
import pygame


class Board:
    def __init__(self):
        self.board = np.zeros(9, dtype=int)
        self.render = self.board.reshape((3,3))

    def actions(self):
        return np.flatnonzero(self.board == 0)

    def trans(self, act, player):
        self.board[act] = player
    
    def undo(self, act):
        self.board[act] = 0
        
    def final(self):
        return len(self.actions()) == 0 or self.winner() 

    def winner(self):
        return ( np.any(np.abs(self.render.sum(axis=0)) == 3) or
                 np.any(np.abs(self.render.sum(axis=1)) == 3) or
                 np.abs(self.board[::4].sum()) == 3 or
                 np.abs(self.board[2::2].sum()) == 3)
    
    def utility(self, player):
        if self.winner():
            return -player   
        else:
            return 0

    def display(self):
        print(self.render)


    def mini_alphabeta(self, alpha, beta, player):
        # comme minimax mais en regardant alpha ou beta
        # pour couper
        pass

    def maxi_alphabeta(self, alpha, beta, player):
        # comme minimax mais en regardant alpha ou beta
        # pour couper
        pass

    def alphabeta(self, player):
        # calcul de l'argmax
        if self.final():
            return None, self.utility(player)
        if player == 1 :
            best_value = float('-inf')
            for action in self.actions():
                v = self.maxi_alphabeta(self, alpha, beta, -1)
                if v >= beta:
                    break
                alpha = max(alpha, v)
            return v


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

    while True:
        b.display()
        actions = b.actions()
        print(f"Player {player}; actions : {actions}")
        if player == -1:
            pos = int(input("pos ? "))
            if pos not in actions:
                print("impossible move")
                break
        else:
            pos, val = b.alphabeta(player)
            print(f"Machine plays: {pos}")

        b.trans(pos, player)
        if b.final():
            if b.winner():
                print(f"Player {player} wins!")
            else:
                print("Tie!")
            break

        player = - player
    

