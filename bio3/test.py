from common import kmers_in_string, probability_of_kmer, \
    expected_number_of_kmer, motif_enumeration, motif_set_score, \
    motif_consensus


def assert_almost_equal(val1, val2, precision=0.0001):
    assert abs(val1 - val2) < precision


def test_kmers_in_string():
    # AB, BC in ABC
    assert kmers_in_string(3, 2) == 2
    # ABC in ABC
    assert kmers_in_string(3, 3) == 1
    # A, B, C in ABC
    assert kmers_in_string(3, 1) == 3


def test_probability_of_kmer():
    assert_almost_equal(probability_of_kmer(1), 0.25)
    assert_almost_equal(probability_of_kmer(2), 0.0625)
    assert_almost_equal(probability_of_kmer(3), 0.015625)


def test_expected_number_of_kmer():
    assert_almost_equal(expected_number_of_kmer(500, 1000, 9), 1.892089)


def test_motif_enumeration():
    assert motif_enumeration(['ATTTGGC', 'TGCCTTA', 'CGGTATC', 'GAAAATT'], 3, 1) == {'ATT', 'TTT', 'GTT', 'ATA'}


def test_motif_enumeration_big_example():
    with open('../data/tests/motif_enumeration_data.txt', 'r') as f:
        lines = f.read().splitlines()
    assert motif_enumeration(lines[2:8],
                             int(lines[1].split()[0]),
                             int(lines[1].split()[1])) == set(lines[9].split())


motifs_example = [
    'TCGGGGGTTTTT',
    'CCGGTGACTTAC',
    'ACGGGGATTTTC',
    'TTGGGGACTTTT',
    'AAGGGGACTTCC',
    'TTGGGGACTTCC',
    'TCGGGGATTCAT',
    'TCGGGGATTCCT',
    'TAGGGGAACTAC',
    'TCGGGTATAACC'
]


def test_motif_set_score():
    assert motif_set_score(motifs_example) == 30


def test_motif_consensus():
    assert motif_consensus(motifs_example) == 'TCGGGGATTTCC'
