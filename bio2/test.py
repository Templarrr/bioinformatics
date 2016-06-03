from common import skew, min_skew, hemming_distance, \
    approximate_pattern_matching, approximate_pattern_count


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


def test_approximate_pattern_matching():
    matches = approximate_pattern_matching(
        'ATTCTGGA',
        'CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT',
        3)
    assert ' '.join(map(str, matches)) == '6 7 26 27'


def test_approximate_pattern_matching_big_example():
    with open('../data/tests/approximate_match_data.txt', 'r') as f:
        lines = f.read().splitlines()
    matches = approximate_pattern_matching(
        lines[1],
        lines[2],
        int(lines[3]))
    assert ' '.join(map(str, matches)) == lines[5]


def test_approximate_pattern_count():
    assert approximate_pattern_count('AAAAA', 'AACAAGCTGATAAACATTTAAAGAG', 1) == 4
    assert approximate_pattern_count('GAGG', 'TTTAGAGCCTTCAGAGG', 2) == 4


def test_approximate_pattern_count_big_example():
    with open('../data/tests/ApproximatePatternCount.txt', 'r') as f:
        lines = f.read().splitlines()
    count = approximate_pattern_count(lines[1], lines[2], int(lines[3]))
    assert count == int(lines[5])
