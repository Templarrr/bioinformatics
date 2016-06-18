from bio3.common import motif_set_score, motif_consensus, motif_set_entropy_score, \
    pr, motif_profile, median_string, get_profile_from_text_presentation

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

# profile = motif_profile(motifs_example)
# print pr('TCGTGGATTTCC', profile)

profile = get_profile_from_text_presentation(
    [
        '0.4 0.3 0.0 0.1 0.0 0.9',
        '0.2 0.3 0.0 0.4 0.0 0.1',
        '0.1 0.3 1.0 0.1 0.5 0.0',
        '0.3 0.1 0.0 0.4 0.5 0.0'
    ]
)

print pr('AAGTTC', profile)