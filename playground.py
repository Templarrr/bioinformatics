from bio3.common import motif_set_score, motif_consensus, motif_set_entropy_score, pr, motif_profile

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

profile = motif_profile(motifs_example)
print pr('TCGTGGATTTCC', profile)
