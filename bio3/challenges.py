from common import motif_enumeration


def motif_enumeration_challenge():
    with open('../data/challenges/dataset_156_7.txt', 'r') as f:
        lines = f.read().splitlines()
    motifs = motif_enumeration(lines[1:],
                               int(lines[0].split()[0]),
                               int(lines[0].split()[1]))
    print ' '.join(motifs)


if __name__ == '__main__':
    motif_enumeration_challenge()
