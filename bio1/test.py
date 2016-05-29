from common import get_complementary_string, \
    count_kmers, frequent_words_counts, frequent_words, find_all_occurencies


def test_complementary_string():
    input_string = 'ACGCGA'
    assert get_complementary_string(input_string, rna_mode=False) == 'TGCGCT'
    assert get_complementary_string(input_string, rna_mode=True) == 'UGCGCU'
    assert get_complementary_string(input_string, rna_mode=True, reversed=True) == 'UCGCGU'
    assert get_complementary_string(input_string, rna_mode=False, reversed=True) == 'TCGCGT'
    assert get_complementary_string('AAAACCCGGT', rna_mode=False, reversed=True) == 'ACCGGGTTTT'


def test_complementary_string_big_example():
    with open('reverse_complement_data.txt', 'r') as f:
        lines = f.read().splitlines()
    assert get_complementary_string(lines[1], rna_mode=False, reversed=True) == lines[3]


def test_count_kmers():
    assert count_kmers('CGATATATCCATAG', 'ATA') == 3
    assert count_kmers('CGATATATCCATAGATA', 'ATA') == 4
    assert count_kmers('GCGCG', 'GCG') == 2


def test_count_kmers_big_example():
    with open('PatternCount.txt', 'r') as f:
        lines = f.read().splitlines()
    assert count_kmers(lines[1], lines[2]) == int(lines[4])


def test_frequent_words_counts():
    assert frequent_words_counts('ACTGACTCCCACCCC', 3) == [2, 1, 1, 1, 2, 1, 1, 3, 1, 1, 1, 3, 3]


def test_frequent_words():
    assert frequent_words('ACTGACTCCCACCCC', 3) == {'CCC'}
    assert frequent_words('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4) == {'CATG', 'GCAT'}


def test_frequent_words_big_example():
    with open('frequent_words_data.txt', 'r') as f:
        lines = f.read().splitlines()
    assert frequent_words(lines[1], int(lines[2])) == set(lines[4].split())


def test_all_occurencies():
    assert find_all_occurencies('ATAT', 'GATATATGCATATACTT') == [1, 3, 9]


def test_all_occurencies_big_example():
    with open('pattern_matching_data.txt', 'r') as f:
        lines = f.read().splitlines()
    occurences = find_all_occurencies(lines[1], lines[2])
    assert ' '.join(map(str, occurences)) == lines[4]
