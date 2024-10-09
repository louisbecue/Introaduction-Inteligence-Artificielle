import pfc
import random

def decode_key(key: int) -> list[tuple[int, int]] :
    r = []
    # cas de l'intial
    if key == 1:
        return r
    while key > 1:
        tmp = key % 9
        key = key // 9
        r.append((tmp % 3, tmp // 3))
    return r

def decode_histo(histo):
    r = []
    for k, v  in histo.items():
        key = k // 3
        p = k % 3
        r.append(((decode_key(key), p), v))
    return r

def test_histo_base():
    h = pfc.HistoriqueBase()
    h.add(1, 2)
    h.add(1, 2)
    assert(h.nb_rounds == 2)


def test_histo_un():
    h = pfc.Historique(1)
    h.add(1, 2)
    print(h.histo)
    print(decode_histo(h.histo))
    assert(h.length == 1)
    assert(h.key == 16)
    assert(4 in h.histo)
    assert(decode_key(h.key) == [(1, 2)])
    assert(decode_histo(h.histo) == [(([], 1), 1)])

    h.add(1, 2)
    print(decode_histo(h.histo))
    assert(len(h.histo) == 2)
    assert(h.key == 16)
    assert(49 in h.histo and 4 in h.histo)
    assert(decode_key(h.key) == [(1, 2)])
    assert(decode_histo(h.histo) == [(([], 1), 1), (([(1, 2)], 1), 1)])

    h.add(0, 0)
    print(h.histo)
    print(decode_histo(h.histo))
    assert(len(h.histo) == 3)
    assert(h.length == 1)
    assert(h.key == 9)
    assert(decode_key(h.key) == [(0,0)])
    assert(decode_histo(h.histo) == [(([], 1), 1), (([(1, 2)], 1), 1), (([(1, 2)], 0), 1)])

def test_histo_trois():
    res = [(([], 1), 1), 
           (([(1, 1)], 0), 1), 
           (([(0, 1), (1, 1)], 2), 1), 
           (([(2, 1), (0, 1), (1, 1)], 1), 1), 
           (([(1, 1), (2, 1), (0, 1)], 1), 1), 
           (([(1, 1), (1, 1), (2, 1)], 2), 1), 
           (([(2, 0), (1, 1), (1, 1)], 2), 1), 
           (([(2, 0), (2, 0), (1, 1)], 1), 1), 
           (([(1, 0), (2, 0), (2, 0)], 0), 1), 
           (([(0, 2), (1, 0), (2, 0)], 1), 1)]
    random.seed(0)
    h = pfc.Historique(3)
    for _ in range(10):
        h.add(random.randint(0, 2), random.randint(0, 2))
        print(h.histo)
        print(decode_histo(h.histo))
    assert(decode_histo(h.histo) == res)