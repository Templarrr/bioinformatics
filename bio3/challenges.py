from common import motif_enumeration, median_string


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


if __name__ == '__main__':
    median_string_big_challenge()
