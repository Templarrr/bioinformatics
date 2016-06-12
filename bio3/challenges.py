from common import motif_enumeration, median_string, get_profile_from_text_presentation, profile_most_probable_kmer


def motif_enumeration_challenge():
    with open('../data/challenges/dataset_156_7.txt', 'r') as f:
        lines = f.read().splitlines()
    motifs = motif_enumeration(lines[1:],
                               int(lines[0].split()[0]),
                               int(lines[0].split()[1]))
    print ' '.join(motifs)


def subtle_motif_enumeration_challenge():
    with open('../data/challenges/15_4_implanted_motif_2.txt', 'r') as f:
        lines = f.read().splitlines()
    motifs = motif_enumeration(lines,
                               15,
                               4)
    print ' '.join(motifs)


def median_string_big_challenge():
    with open('../data/challenges/dataset_158_9.txt', 'r') as f:
        lines = f.read().splitlines()
    print median_string(lines[1:], int(lines[0]))


def profile_most_probable_kmer_challenge():
    with open('../data/challenges/dataset_159_3.txt', 'r') as f:
        lines = f.read().splitlines()
    profile = get_profile_from_text_presentation(lines[2:])
    print profile_most_probable_kmer(lines[0], int(lines[1]), profile)


if __name__ == '__main__':
    profile_most_probable_kmer_challenge()
