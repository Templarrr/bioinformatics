from bio3.common import motif_set_score, motif_consensus, motif_set_entropy_score

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

print motif_set_score(motifs_example)
print motif_consensus(motifs_example)
print motif_set_entropy_score(motifs_example)