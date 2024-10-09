from typing import Optional


class DatasetException(BaseException):
    pass


def gini(nb_total: int, nb: int) -> float:
    """computes the gini score for the binary case.
    calcule le score de gini pour un échantillon contenant nb_total
    éléments dont nb sont de classe 1 et le reste de classe 0.
    """
    if nb_total ==  0:
        return 0
    a = nb/nb_total
    return 2*a*(1-a)


class Dataset:
    """ a matrix of binary values represented as 0 and 1 
      columns is the list of column names
      attributes is the set of column indexes
    """
    def load(self, filename: str) -> None:
        """loads a file, containing a comma separated list of values. 
        The first line contains the column names. All other values are binary : 0 or 1. 
        Raises an DatasetException if the format in incorrect """
        with open(filename) as f:
            self.columns = [v.strip() for v in f.readline().strip().split(',')]
            self.attributes = set(range(len(self.columns)-1))
            n = len(self.columns)
            self.data = []
            for line in f:
                vec = []
                for v in line.strip().split(","):
                    v = int(v)
                    if v==0 or v==1:
                        vec.append(v)
                if len(vec) != n:
                    raise DatasetException("Incorrect line", line, self.columns, vec)
                self.data.append(vec)

    def sort(self, start: int, end: int, attribute: int) -> int:
        """puts all samples such that attributes is 0 before all samples such that attribute is 1, 
        between start and end. Returns the index where we find the latest 0"""
        i, j = start, end - 1
        while i <= j:
            while i < end and self.data[i][attribute] == 0:
                i += 1
            while j >= start and self.data[j][attribute] == 1:
                j -= 1
            if i < j:
                self.data[i], self.data[j] = self.data[j], self.data[i]
        return i

    def get_nb_pos(self, a: int, start: int, end: int) -> tuple[int, int, int]:
        """ returns the number of samples between start and end 
            - with target 1 and attribute a=1 and 
            - with target 1 and attribute a=0 and 
            - with attribute a = 1 """
        n1, n2, n3 = 0, 0, 0
        for line in self.data[start : end]:
            if line[-1] == 1 and line[a] == 1:
                n1 += 1
            elif line[-1] == 1 and line[a] == 0:
                n2 += 1
            if line[a] == 1:
                n3 += 1
        return [n1, n2, n3]
            
    def majority(self, start: int, end: int) -> int:
        """ returns the majority class of samples between start and end  """
        out = self.data[start]
        for line in self.data[start+1 : end]:
            if out.count(1) < line.count(1):
                out = line
        return out

    def same_class(self, start: int, end: int) -> bool:
        """returns True iff all the samples are of the same class between start and end"""
        pass


class Node:

    def __init__(self, dataset: Dataset,
                 start: Optional[int] = 0,
                 end: Optional[int] = None,
                 attributes: Optional[set[int]] = None,
                 level: Optional[int] = None) -> None:
        """attributes est un ensemble d'indices, ce constructeur en fait une copie.
        En effet attributes est un set, donc un mutable. L'instance pourra modifier cet ensemble. 
        Et donc l'ensemble doit être spécifique à ce noeud et non partagé avec les autres noeuds 
        (ce qui pourrait être le cas si aucune copie n'est effectuée)
        """
        self.dataset = dataset
        if start is None:
            self.start = 0
        else:
            self.start = start
        if end is None:
            self.end = len(dataset.data)
        else:
            self.end = end
        if attributes:
            self.attributes = attributes.copy()
        else:
            self.attributes = dataset.attributes.copy()
        if level is None:
            self.level = 1
        else:
            self.level = level
        
    def score_gini(self, attribute: int) -> float:
        """ computes the gini score for the dataset and attribute as 
        P[x_a=1]Gini(P[y=1|x_a=1]) + P[x_a=0]Gini(P[y=1|x_a=0])
        """
        # Calculate the gini score for the dataset and attribute
        pos_count = self.dataset.get_nb_pos(attribute, self.start, self.end)
        total_count = self.end - self.start
        p1 = pos_count[0] / total_count
        p2 = pos_count[1] / total_count
        return p1 * gini(total_count, pos_count[0]) + p2 * gini(total_count, pos_count[1])

    def set_best_attribute(self) -> None:
        """ computes the best attribute """
        best_score = 0
        best_attribute = None
        for attribute in self.attributes:
            score = self.score_gini(attribute)
            if score > best_score:
                best_score = score
                best_attribute = attribute
        self.best_attribute = best_attribute

    def build_tree(self, max_level: Optional[int] = None) -> None:
        if self.dataset.same_class(self.start, self.end):
            self.label = self.dataset.data[self.start][-1]

    def __str__(self) -> str:
        try:
            return "x_{}=0? (classe {}):\n{}{}\n{}{}".format(self.best_attribute,
                                                             self.label,
                                                             "  " * self.level,
                                                             self.tree0,
                                                             "  " * self.level,
                                                             self.tree1)
        except AttributeError:
            return "{}: classe {}".format(" " * self.level,
                                   self.label)


def dtree(filename: str) -> Node:
    dataset = Dataset()
    dataset.load(filename)
    n = Node(dataset)
    n.build_tree()
    return n    


    
if __name__ == "__main__":
    d = Dataset()
    d.load("test_large.data")
    print(d.data)
    print(d.attributes)
    # print(d)
