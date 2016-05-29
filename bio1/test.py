from common import get_complementary_string, count_kmers


def test_complementary_string():
    input_string = 'ACGCGA'
    assert get_complementary_string(input_string, rna_mode=False) == 'TGCGCT'
    assert get_complementary_string(input_string, rna_mode=True) == 'UGCGCU'


def test_count_kmers():
    assert count_kmers('CGATATATCCATAG', 'ATA') == 3
    assert count_kmers('CGATATATCCATAGATA', 'ATA') == 4
    assert count_kmers('GCGCG', 'GCG') == 2


def test_count_kmers_big_example():
    with open('PatternCount.txt', 'r') as f:
        lines = f.read().splitlines()
    assert count_kmers(lines[1], lines[2]) == int(lines[4])
