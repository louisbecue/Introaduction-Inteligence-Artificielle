import numpy as np


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

    def mini(self, player: int) -> int:
        # retourne la valeur minimale pour ce joueur
        # on utilise undo pour éviter de copier le board
        if self.final():
            return self.utility(player)
        best_value = float('inf')
        for action in self.actions():
            self.trans(action, player)
            value = self.maxi(-player)
            self.undo(action)
            if value < best_value:
                best_value = value
        return best_value
        

    def maxi(self, player):
        # retourne la valeur ùaximale pour ce joueur
        # on utilise undo pour éviter de copier le board
        if self.final():
            return self.utility(player)
        best_value = float('-inf')
        for action in self.actions():
            self.trans(action, player)
            value = self.mini(-player)
            self.undo(action)
            if value > best_value:
                best_value = value
        return best_value
    

    def minimax(self, player):
        # Argmax des mini de l'opposant
        if self.final():
            return None, self.utility(player)        
        if player == 1 :
            best_value = float('-inf') 
        else :
            best_value = float('inf')
        best_action = None
        for action in self.actions():
            self.trans(action, player)
            _, value = self.minimax(-player)
            self.undo(action)
            if player == 1:
                if value > best_value:
                    best_value = value
                    best_action = action
            else:
                if value < best_value:
                    best_value = value
                    best_action = action
        return best_action, best_value
        

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
            if len(actions) == 9:
                pos = 0
            else :
                pos, val = b.minimax(player)
            print(f"Machine plays: {pos}")

        b.trans(pos, player)

        if b.final():
            if b.winner():
                print(f"Player {player} wins!")
            else:
                print("Tie!")
            break
        
        player = - player
    

