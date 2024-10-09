from enum import Enum
import random
import sys
from collections import Counter


get_val={'p': 0, 'pierre': 0, 
         'c': 1, 'ciseaux': 1,
         'f': 2, 'feuille': 2
         }
vals = ['Pierre', 'Ciseaux', 'Feuille']

class HistoriqueBase:
    """Une historique qui ne mémorise rien des coups passés et propose 
    un tirage aléatoire uniforme entre les 3 possibilités.
    Elle mémorise le nombre de parties jouées.
    """
    def __init__(self) -> None:
        self.nb_rounds = 0

    def prop_ordi(self) -> int:
        """Retourne une proposition"""
        return random.randint(0, 2)

    def add(self, prop_joueur: int, prop_ordi: int) -> None:
        """mémorise le nombre de parties jouées."""
        self.nb_rounds += 1


class Historique(HistoriqueBase):
    """On calcule simplement les probabilités de jeu du joueur"""
    def __init__(self, max_length: int=1) -> None:
        """Initialiser la clef, sa longueur 
        et la longueur maximale de l'historique"""
        super().__init__()
        self.length = 0
        self.max_length = max_length
        self.key = 1
        self.histo = {}
        self.histo_liste = []

    def add(self, prop_joueur: int, prop_ordi: int) -> None:
        """Ajouter un couple de propositions à l'historique et 
        met à jour la clef courante"""
        super().add(prop_joueur, prop_ordi)
        self._add_history(prop_joueur)
        # utilisation d'une liste
        if (len(self.histo_liste) + 1) > self.max_length : 
            self.histo_liste.pop(0)
        self.histo_liste.append((prop_joueur, prop_ordi))
        # fin
        self._add_to_key(prop_joueur, prop_ordi)

    def _add_history(self, prop: int) -> None:
        """Mettre à jour l'historique avec le couple de propositions"""
        # shift the key to add the prop: we store histo x prop -> int
        index = self.key*3 + prop
        if index in self.histo:
            self.histo[index] += 1
        else:
            self.histo[index] = 1
        if (self.length + 1) <= self.max_length :
            self.length += 1

    def _add_to_key(self, prop_joueur: int, prop_ordi: int) -> None:
        """Store couples of propositions encoded as ternary values 
        and mark the older couple with a trailing 1.
        For instance, a play of self.length 2: (2, 1) followed by (0, 1) is encoded
        (0 * 3^0 + 1 * 3^1) + (2 * 3^2 + 1* 3^3) + 1 * 3^4
        Older propositions have higher powers. 
        """
        new_key = (prop_joueur * 3 ** 0 + prop_ordi * 3 ** 1)
        exp = 2
        for prop_joueur, prop_ordi in (list(reversed(self.histo_liste))[1:]):
            new_key += ((prop_joueur) * 3** exp + (prop_ordi) * 3 **(exp+1))
            exp += 2
        self.key = (new_key + 1 * 3** exp)
        
    def prop_ordi(self) -> int:
        """Calculer la proposition de la machine considérant l'historique
        Il faut trouver ici la/les proposition/s du joueur qui est la plus fréquente
        selon l'historique puis jouer ce qui va battre cette proposition. 
        En cas d'égalité ou tire au sort."""
        if self.histo_liste:
            print(" ")
            print("liste               : " + str(self.histo_liste))
            print("dictionnaire décodé : " + str(self.decode_histo()))
            print(" ")
            dict_max = dict(Counter([t[0] for t in self.histo_liste]))
            valeur_max = max(dict_max.values())
            cles_max = [cle for cle, valeur in dict_max.items() if valeur == valeur_max]
            print(cles_max)
            return (cles_max[random.randint(0, (len(cles_max) - 1))] - 1) % 3
        else:
            return random.randint(0, 2)

    def decode_key(self, key: int) -> list[tuple[int, int]] :
        r = []
        if key == 1:
            return r
        while key > 1:
            tmp = key % 9
            key = key // 9
            r.append((tmp % 3, tmp // 3))
        return r

    def decode_histo(self) -> list[tuple[int, int]]:
        for k, _  in self.histo.items():
            key = k // 3
        return self.decode_key(key)


def winner(prop_joueur: int, prop_ordi: int) -> int:
    """ Retourne 0 en cas d'égalité, 1 si la prop_joueur gagne et 2 sinon."""
    if prop_joueur == prop_ordi:
        return 0
    if (prop_joueur + 1) % 3 == prop_ordi :
        return 1
    else:
        return 2

def jeu(histo: Historique, debug: bool=True):
    nb_points = [0, 0]
    while True:
        # Les deux joueurs se prononcent !
        s_prop_joueur = input("Pierre, feuille ou ciseaux ? ").lower()
        prop_joueur = get_val.get(s_prop_joueur, None)
        if prop_joueur is None:
            break
        prop_ordi = histo.prop_ordi()

        # on conserve les choix pour les tours suivants
        histo.add(prop_joueur, prop_ordi)

        # on affiche le match et le résultat
        print("{} contre {} : ".format(vals[prop_joueur], vals[prop_ordi]), end="")

        w = winner(prop_joueur, prop_ordi)
        if w == 0:
            print("Égalité")
        else:
            nb_points[w-1] =nb_points[w-1] + 1
            if w == 1:
                print("Vous gagnez")
            else: 
                print("Vous perdez")
        if debug:
            print(histo.histo)
    print("Score final\n\tVous : {}\n\tOrdi : {}".format(*nb_points))


if __name__ == "__main__":
    jeu(Historique(10), True)
        
        