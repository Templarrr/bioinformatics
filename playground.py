from bio3.common import randomized_motif_search

dna = [
    'CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA',
    'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG',
    'TAGTACCGAGACCGAAAGAAGTATACAGGCGT',
    'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC',
    'AATCCACCAGCTCCACGTGCAATGTTGGCCTA',
]

print randomized_motif_search(dna, 8)