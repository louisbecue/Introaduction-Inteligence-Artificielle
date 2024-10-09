# L2S4 - Introduction à l'Inteligence Artificielle

## Projet Chifoumi

### 1. Avancement 

Le jeu est fini est fonctionne comme souhaiter, et tous les tests sont réussis.

### 2. Commandes

#### Lancement du jeu :

``` bash
./ python3 pfc.py
```

#### Lancement des tests :

``` bash
./ python3 pfc.py
```

### 3. Fonctionnement du code

* **Historique** :

    * **add()** :
        Ajoute le couple de proposition dans l'historique de base et dans le dictionnaire avec de la clé qui est recalculer a chaque fois.

        Ajoute aussi dans une liste le couple sous le forme `list[tuple[int, int]]` (voir Remarque).

    * **_add_history()** :
        Met simplement à jour le dictionnaire `histo` en ajoutant le couple codé à l'aide de la clé et incrémente la taille.

    * **_add_to_key()** :
        Calcule la clé a l'aide de l'historique.

    * **prop_ordi()** :
        Calcule la valeur que l'ordi va jouer, en regardant le coup joué par le joueur le plus fréquent dans l'historique.
        * D'abord on crée un dictionnaire de la fréquence des coups, par exemple :

            `{0:3, 1:3, 2:0}`.
        * Ensuite on calule le(s) nombre(s) les plus fréquent(s) qu'on place dans une liste, ici dans l'exemple :

            `[0, 1]`.
        * On tire une propsition au hasard et on retroune le coups gagant de celui garce a la formule :
            
            $x-1\mod{3}$

            ici dans l'exemple :

            `2` ou `0`.

    * **decode_key()** :
        Fonction déja présente dans les tests.

    * **decode_histo()** :
        Fonction qui renvoye les n derniers propositions de l'historique.

### 3. Remarque 

J'ai eu du mal à comprendre pourquoi le dictionnaire était codé à l'aide de la clé, et j'ai donc utilisé une liste pour stocker l'historique car cela était plus simple.

De plus, j'ai remarqué que l'historique est décalé d'une proposition en retard quand il est sous la forme d'un dictionnaire.

Liste : 

``[(0, 1), (0, 2), (2, 2), (2, 2), (1, 2), (0, 1), (1, 2), (2, 2), (1, 2), (0, 2)]``

Dictionnaire: 

``[(0, 1), (0, 2), (2, 2), (2, 2), (1, 2), (0, 1), (1, 2), (2, 2), (1, 2)]``

L'implémentation sans la liste est possible, il suffit de remplacer les `self.histo_liste` par `self.decode_histo()`.
Mais le problème de décalage pose problème dans le calcul de la clé.

J'utilise donc la liste pour le calcul de la clé dans **_add_to_key()**  et aussi dans **prop_ordi()** pour avoir des meilleurs résultat lors des premiers coups (sinon nous avoins un coups de retard).

