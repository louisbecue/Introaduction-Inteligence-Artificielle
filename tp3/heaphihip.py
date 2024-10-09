from numpy import infty
import heap_exception as ex

Content = int | float

class Heap:
    def __init__(self) -> None:
        """ initialiser le tas et fixer les attributs"""
        self.heap: list[Content] = [0]
        self.size: int = 1

    def head(self) -> Content:
        """Retourner la valeur à la racine de l'arbre (indice 1 du tableau)"""
        if self.size > 0:
            return self.heap[1]
        else :
            raise ex.HeadException("Empty")

    def parent(self, i: int) -> int:
        """retourner l'indice du père du noeud d'indice i"""
        return i//2

    def left(self, i: int) -> int:
        """retourner l'indice du fils gauche du noeud d'indice i"""
        if self.size >= i*2:
            return i*2
        # else :
        #     raise ex.LeftException("Element : " + str(self.heap[i]) + ", in position : " + str(i) + ", has no left son.\n" + str(self.heap))

    def right(self, i: int) -> int:
        """retourner l'indice du fils droit du noeud d'indice i"""
        if self.size >= i*2+1:
            return i*2+1
        # else :
        #     raise ex.RightException("Element : " + str(self.heap[i]) + ", in position : " + str(i) + " has no right son.\n" + str(self.heap))
        
    def max_heapify(self, i: int) -> None:
        """appliquer l'algorithme qui assure la propriété
        max_heap sur le tableau de cette instance"""
        l = self.left(i)
        r = self.right(i)
        if l <= self.size and self.heap[l] > self.heap[i]:
            largest = l
        else:
            largest = i
        if r <= self.size and self.heap[r] > self.heap[largest]:
            largest = r
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.max_heapify(largest)

    def build_max_heap(self, tab: list) -> None:
        """construire une maxheap à partir d'un tableau"""
        self.size = len(tab)
        self.heap = tab
        for i in reversed(range(1, len(tab)//2)):
            self.max_heapify(i)

    def heapsort(self, tab: list) -> None:
        """Trier le tableau tab en place en O(nlogn) avec l'API
        et mettre à jour cette instance"""
        self.build_max_heap(tab)
        for i in range(len(tab), 2):
            self.heap[i], self.heap[1] = self.heap[1], self.heap[i]
            self.size -= 1
            self.max_heapify(1)

    def display(self) -> None:
        """Affiche dans la terminal la heaplist"""
        print(self.heap)

    def display_element(self, i:int) -> None:
        """Affiche dans la terminal l'element i de la heaplist"""
        if self.size >= i:
            print(self.heap[i])
        else :
            raise ex.notInHeapException("Element not in list")


class PriorityQueue:
    def __init__(self) -> None:
        """Initialiser la queue de priorité. Elle utilise un tas"""
        self.queue = Heap()

    def insert(self, key: Content) -> None:
        """Insérer un élément dans la queue et maintenir 
        la propriété d'avoir la propriété max heap du tas"""
        self.queue.size += 1
        self.queue.heap.append(-infty)
        self.increase_key(self.queue.size ,key)

    def maximum(self) -> Content:
        """Retourner l'élément maximal de la queue"""
        return self.queue.heap[1]

    def extract_max(self) -> Content:
        """Enlever l'élément maximal de la queue"""
        if self.queue.size < 1:
            raise ex.HeadUnderflowException("head underflow")
        max = self.queue.heap[1]
        self.queue.heap[1] = self.queue.heap[self.queue.size]
        self.queue.size -= 1
        self.queue.max_heapify(1)
        return max

    def increase_key(self, i: int, key: Content) -> None:
        """Modifier la valeur d'un élément à l'indice i 
        en la remplaçant par key"""
        if key < self.queue.heap[i]:
            raise ex.KeySamllerException("new key is smaller than current key")
        self.queue.heap[i] = key
        while x > 1 and self.queue[self.queue.parent()] < self.queue.heap[i]:
            self.queue.heap[i], self.queue.heap[self.queue.parent()] = self.queue.heap[self.queue.parent()], self.queue.heap[i]
            i = self.queue.heap[self.queue.parent()]


if __name__ == "__main__":
    from random import randint

    h = Heap()
    h.build_max_heap([1, 5, 3, 6, 20, 50, 3, 2])
    # afficher h
    h.display()

    h.build_max_heap(list(range(10, 1, -1)))
    # afficher h
    h.display()

    h.heapsort([1, 5, 3, 6, 20, 50, 3, 2])
    # afficher h
    h.display()

    q = PriorityQueue()
    for _ in range(10):
        x = randint(1, 10)
        q.insert(x)
        # afficher x et le contenu de q
        print(x)
        q.queue.display()
    print("dequeue")

    for _ in range(10):
        top = q.extract_max()
        # afficher top et le contenu de q
        q.queue.display()
        print(top)
    try:
        q.extract_max()
    except ex.PriorityQueueError as e:
        print(e)

    print("enqueue")
    for _ in range(10):
        x = randint(1, 10)
        q.insert(x)
        # afficher x et le contenu de q
        print(x)
        q.queue.display()
        
