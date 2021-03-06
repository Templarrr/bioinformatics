from bio3.common import get_profile_from_text_presentation
from common import kmers_in_string, probability_of_kmer, \
    expected_number_of_kmer, motif_enumeration, motif_set_score, \
    motif_consensus, motif_column_entropy, motif_set_entropy_score, \
    motif_alternate_score, median_string, motif_profile, pr, \
    profile_most_probable_kmer, greedy_motif_search, randomized_motif_search, \
    gibbs_sampler


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


def test_motif_column_entropy():
    assert_almost_equal(motif_column_entropy({'A': 0.2, 'C': 0.0, 'G': 0.6, 'T': 0.2}), 1.371)
    assert_almost_equal(motif_column_entropy({'A': 0.0, 'C': 0.6, 'G': 0.0, 'T': 0.4}), 0.971)
    # typo in course, this is the right result
    assert_almost_equal(motif_column_entropy({'A': 0.0, 'C': 0.0, 'G': 0.9, 'T': 0.1}), 0.469)


def test_motif_set_entropy_score():
    assert_almost_equal(motif_set_entropy_score(motifs_example), 9.91629)


def test_motif_alternate_score():
    assert motif_alternate_score(motifs_example) == motif_set_score(motifs_example)


def test_median_string():
    dna = [
        'AAATTGACGCAT',
        'GACGACCACGTT',
        'CGTCAGCGCCTG',
        'GCTGAGCACCGG',
        'AGTTCGGGACAG'
    ]
    assert median_string(dna, 3) == 'GAC'


# def test_median_string_big_example():
#     with open('../data/tests/medium_string_data.txt', 'r') as f:
#         lines = f.read().splitlines()
#     assert median_string(lines[2:12], int(lines[1])) == lines[13]


def test_pr():
    profile = motif_profile(motifs_example)
    assert_almost_equal(pr('ACGGGGATTACC', profile), 0.0008)
    assert_almost_equal(pr('TCGGGGATTTCC', profile), 0.0205)


def test_profile_most_probable_kmer():
    profile = get_profile_from_text_presentation([
        '0.2 0.2 0.3 0.2 0.3',
        '0.4 0.3 0.1 0.5 0.1',
        '0.3 0.3 0.5 0.2 0.4',
        '0.1 0.2 0.1 0.1 0.2',
    ])
    assert profile_most_probable_kmer('ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT', 5, profile) == 'CCGAG'


def test_profile_most_probable_kmer_big_example():
    with open('../data/tests/profile_most_1.txt', 'r') as f:
        lines = f.read().splitlines()
    profile = get_profile_from_text_presentation(lines[3:7])
    assert profile_most_probable_kmer(lines[1], int(lines[2]), profile) == lines[8]


def test_greedy_motif_search():
    dna = [
        'GGCGTTCAGGCA',
        'AAGAATCAGTCA',
        'CAAGGAGTTCGC',
        'CACGTCAATCAC',
        'CAATAATATTCG'
    ]
    k = 3
    greedy_best_motif = greedy_motif_search(dna, k)
    assert greedy_best_motif == ['CAG', 'CAG', 'CAA', 'CAA', 'CAA']
    greedy_best_motif_laplace = greedy_motif_search(dna, k, laplace_rule=True)
    assert greedy_best_motif_laplace == ['TTC', 'ATC', 'TTC', 'ATC', 'TTC']


def test_greedy_motif_search_big_example():
    with open('../data/tests/greedy_data.txt', 'r') as f:
        lines = f.read().splitlines()
    k, t = int(lines[1].split()[0]), int(lines[1].split()[1])
    dna = lines[2:2 + t]
    expected_motif = lines[3 + t:]
    assert greedy_motif_search(dna, k) == expected_motif


def test_greedy_motif_search_laplace_big_example():
    with open('../data/tests/greedy_pseudo.txt', 'r') as f:
        lines = f.read().splitlines()
    k, t = int(lines[1].split()[0]), int(lines[1].split()[1])
    dna = lines[2:2 + t]
    expected_motif = lines[3 + t:]
    assert greedy_motif_search(dna, k, laplace_rule=True) == expected_motif


# randomized
# def test_randomized_motif_search():
#     dna = [
#         'CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA',
#         'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG',
#         'TAGTACCGAGACCGAAAGAAGTATACAGGCGT',
#         'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC',
#         'AATCCACCAGCTCCACGTGCAATGTTGGCCTA',
#     ]
#     motifs = randomized_motif_search(dna, 8)
#     assert motifs == [
#         'TCTCGGGG',
#         'CCAAGGTG',
#         'TACAGGCG',
#         'TTCAGGTG',
#         'TCCACGTG'
#     ]


# randomized
# def test_randomized_motif_search_big_example():
#     with open('../data/tests/randomized.txt', 'r') as f:
#         lines = f.read().splitlines()
#     k, t = int(lines[1].split()[0]), int(lines[1].split()[1])
#     dna = lines[2:2 + t]
#     expected_motif = lines[3 + t:]
#     assert randomized_motif_search(dna, k) == expected_motif


# randomized
# def test_gibbs_sampler():
#     dna = [
#         'CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA',
#         'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG',
#         'TAGTACCGAGACCGAAAGAAGTATACAGGCGT',
#         'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC',
#         'AATCCACCAGCTCCACGTGCAATGTTGGCCTA',
#     ]
#     motifs = gibbs_sampler(dna, 8, 100)
#     assert motifs == [
#         'TCTCGGGG',
#         'CCAAGGTG',
#         'TACAGGCG',
#         'TTCAGGTG',
#         'TCCACGTG'
#     ]
