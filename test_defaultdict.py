import random

from defaultlist import defaultlist


def test_int_key():
    l = defaultlist(int)

    l[2] = 5
    l[4] = 10
    l[6] = 15

    assert l == [0, 0, 5, 0, 10, 0, 15]


def test_slice_key():
    l = defaultlist(int)

    l[2:4] = [5, 10]
    l[4:6] = [15, 20]

    assert l == [0, 0, 5, 10, 15, 20]


def test_slice_key_start_only():
    l = defaultlist(int)

    l[2:]

    assert l == [0, 0, 0]


def test_slice_key_stop_only():
    l = defaultlist(int)

    l[:2]

    assert l == [0, 0]


def test_str_factory():
    l = defaultlist(lambda: f"Empty{random.randint(0, 100)}")

    l[2] = "Hello"
    l[4] = "World"

    assert len(set(l)) == 5

    assert len([i for i in l if i.startswith("Empty")]) == 3

    assert [i for i in l if not i.startswith("Empty")] == ["Hello", "World"]


def test_get_key():
    l = defaultlist(int)

    l[2]

    assert l == [0, 0, 0]


def test_get_negative_key():
    l = defaultlist(int)

    l[-3]

    assert l == [0, 0, 0]


def test_set_slice_negative():
    l = defaultlist(int)

    l[-3:-1] = [5, 10]

    assert l == [5, 10, 0]


def test_set_slice_negative_start():
    l = defaultlist(int)

    l[-3:] = [5, 10]

    assert l == [5, 10]


def test_set_slice_negative_stop():
    l = defaultlist(int)

    l[:-1] = [5, 10]

    assert l == [5, 10, 0]
