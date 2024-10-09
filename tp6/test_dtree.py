import dtree
import pytest

def test_load():
    d = dtree.Dataset()
    d.load('test.data')
    assert(d.columns == ['A', 'B', 'C', 'target'])
    assert(d.attributes == {0, 1, 2})
    assert(d.data==[[0, 1, 0, 0], [1, 0, 1, 1]])

def test_gini():
    d = dtree.Dataset()
    assert(dtree.gini(10,0)==0)
    assert(dtree.gini(10,5) == 0.5)
    assert(dtree.gini(10,4) > dtree.gini(10,2))

def test_load_bad():
    with pytest.raises(dtree.DatasetException):
        d = dtree.Dataset()
        d.load("test_bad.data")


def test_sort():
    d = dtree.Dataset()
    d.load("test_large.data")
    n = len(d.data)
    r = d.sort(0, n, 0)
    assert(r == 2)
    assert(d.data[0] == [0, 1, 1, 0, 0])
    assert(d.data[1] == [0, 1, 1, 0, 1])
    r = d.sort(0, n, 2)
    assert(r == 0)
    r = d.sort(0, n, 3)
    assert(r == n)
    d.load("test_large.data")
    r = d.sort(4, n, 0)
    assert(r == 5)
    assert(d.data[0] == [0, 1, 1, 0, 0])
    assert(d.data[4] == [0, 1, 1, 0, 1])

def test_get_nb_pos():
    d = dtree.Dataset()
    d.load("test_large.data")
    pa, pna, a = d.get_nb_pos(1, 0, 5)
    assert(pa==0)
    assert(pna==2)
    assert(a==3)
    pa, pna, a = d.get_nb_pos(1, 5, 10)
    assert(pa==2)
    assert(pna==2)
    assert(a==3)
