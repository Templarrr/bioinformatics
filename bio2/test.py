from common import skew, min_skew, hemming_distance


def test_skew():
    skew_list = skew('CATGGGCATCGGCCATACGCC')
    assert ' '.join(map(str, skew_list)) == '0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2'


def test_min_skew():
    min_skew_pos = min_skew('TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT')
    assert ' '.join(map(str, min_skew_pos)) == '11 24'


def test_min_skew_big_example():
    with open('../data/tests/minimum_skew_data.txt', 'r') as f:
        lines = f.read().splitlines()
    min_skew_pos = min_skew(lines[1])
    assert ' '.join(map(str, min_skew_pos)) == lines[3]


def test_hemming_distance():
    assert hemming_distance('GGGCCGTTGGT', 'GGACCGTTGAC') == 3


def test_hemming_distance_big_example():
    with open('../data/tests/HammingDistance.txt', 'r') as f:
        lines = f.read().splitlines()
    assert hemming_distance(lines[1], lines[2]) == int(lines[4])
