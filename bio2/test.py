from common import skew, min_skew, hemming_distance, \
    approximate_pattern_matching, approximate_pattern_count, \
    frequent_words_with_mismatches, neighbors


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


def test_frequent_words_with_mismatches():
    words = frequent_words_with_mismatches('AACAAGCTGATAAACATTTAAAGAG', 5, 1)
    assert ' '.join(words) == 'AAAAA'
    words = frequent_words_with_mismatches('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4, 1)
    assert ' '.join(words) == 'GATG ATGC ATGT'
    words = frequent_words_with_mismatches('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4, 1, True)
    assert set(words) == {'ATGT', 'ACAT'}


# slow
# def test_frequent_words_with_mismatches_big_example():
#     with open('../data/tests/frequent_words_mismatch_data_1.txt', 'r') as f:
#         lines = f.read().splitlines()
#     words = frequent_words_with_mismatches(
#         lines[1],
#         int(lines[2].split()[0]),
#         int(lines[2].split()[1]))
#     assert ' '.join(words) == lines[4]


# slow
# def test_frequent_words_with_mismatches_big_example2():
#     with open('../data/tests/frequent_words_mismatch_complement.txt', 'r') as f:
#         lines = f.read().splitlines()
#     words = frequent_words_with_mismatches(
#         lines[1],
#         int(lines[2].split()[0]),
#         int(lines[2].split()[1]),
#         True)
#     assert set(words) == set(lines[4].split())


def test_neighbors():
    neighbors_list = neighbors('ACG', 1)
    assert neighbors_list == {
        'CCG',
        'TCG',
        'GCG',
        'AAG',
        'ATG',
        'AGG',
        'ACA',
        'ACC',
        'ACT',
        'ACG'
    }


def test_neighbors_big_example():
    with open('../data/tests/Neighbors.txt', 'r') as f:
        lines = f.read().splitlines()
    supposed_result = set(lines[4:])
    neighbors_list = neighbors(lines[1], int(lines[2]))
    assert neighbors_list == supposed_result
