from common import get_complementary_string, \
    count_kmers, frequent_words_counts, frequent_words, \
    find_all_occurencies, find_clumps, faster_frequent_words, \
    pattern_to_number, number_to_pattern, computing_frequencies


def test_complementary_string():
    input_string = 'ACGCGA'
    assert get_complementary_string(input_string, rna_mode=False) == 'TGCGCT'
    assert get_complementary_string(input_string, rna_mode=True) == 'UGCGCU'
    assert get_complementary_string(input_string, rna_mode=True, reversed=True) == 'UCGCGU'
    assert get_complementary_string(input_string, rna_mode=False, reversed=True) == 'TCGCGT'
    assert get_complementary_string('AAAACCCGGT', rna_mode=False, reversed=True) == 'ACCGGGTTTT'


def test_complementary_string_big_example():
    with open('../data/tests/reverse_complement_data.txt', 'r') as f:
        lines = f.read().splitlines()
    assert get_complementary_string(lines[1], rna_mode=False, reversed=True) == lines[3]


def test_count_kmers():
    assert count_kmers('CGATATATCCATAG', 'ATA') == 3
    assert count_kmers('CGATATATCCATAGATA', 'ATA') == 4
    assert count_kmers('GCGCG', 'GCG') == 2


def test_count_kmers_big_example():
    with open('../data/tests/PatternCount.txt', 'r') as f:
        lines = f.read().splitlines()
    assert count_kmers(lines[1], lines[2]) == int(lines[4])


def test_frequent_words_counts():
    assert frequent_words_counts('ACTGACTCCCACCCC', 3) == [2, 1, 1, 1, 2, 1, 1, 3, 1, 1, 1, 3, 3]


def test_frequent_words():
    assert frequent_words('ACTGACTCCCACCCC', 3) == {'CCC'}
    assert frequent_words('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4) == {'CATG', 'GCAT'}


def test_frequent_words_big_example():
    with open('../data/tests/frequent_words_data.txt', 'r') as f:
        lines = f.read().splitlines()
    assert frequent_words(lines[1], int(lines[2])) == set(lines[4].split())


def test_faster_frequent_words():
    assert faster_frequent_words('ACTGACTCCCACCCC', 3) == {'CCC'}
    assert faster_frequent_words('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4) == {'CATG', 'GCAT'}
    with open('../data/tests/frequent_words_data.txt', 'r') as f:
        lines = f.read().splitlines()
    assert faster_frequent_words(lines[1], int(lines[2])) == set(lines[4].split())


def test_all_occurencies():
    assert find_all_occurencies('ATAT', 'GATATATGCATATACTT') == [1, 3, 9]


def test_all_occurencies_big_example():
    with open('../data/tests/pattern_matching_data.txt', 'r') as f:
        lines = f.read().splitlines()
    occurences = find_all_occurencies(lines[1], lines[2])
    assert ' '.join(map(str, occurences)) == lines[4]


def test_find_clumps():
    clumps = find_clumps('CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA', 5, 50, 4)
    assert clumps == {'CGACA', 'GAAGA'}
    clumps = find_clumps('ACGACCGATT', 2, 5, 2)
    assert clumps == {'AC'}


def test_find_clumps_big_example():
    with open('../data/tests/clump_finding_data.txt', 'r') as f:
        lines = f.read().splitlines()
    k, L, t = map(int, lines[2].split())
    clumps = find_clumps(lines[1], k, L, t)
    expected_clumps = set(lines[4].split())
    assert clumps == expected_clumps


def test_pattern_to_number():
    assert pattern_to_number('AGT') == 11
    assert pattern_to_number('CTTCTCACGTACAACAAAATC') == 2161555804173


def test_number_to_pattern():
    assert number_to_pattern(45, 4) == 'AGTC'
    assert number_to_pattern(5353, 7) == 'CCATGGC'


def test_computing_frequencies():
    frequencies = computing_frequencies('ACGCGGCTCTGAAA', 2)
    assert ' '.join(map(str, frequencies)) == '2 1 0 0 0 0 2 2 1 2 1 0 0 1 1 0'


def test_computing_frequencies_big_example():
    with open('../data/tests/FrequencyArray.txt', 'r') as f:
        lines = f.read().splitlines()
    frequencies = computing_frequencies(lines[1], int(lines[2]))
    assert ' '.join(map(str, frequencies)) == lines[4]
