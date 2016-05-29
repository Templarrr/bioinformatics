from common import count_kmers


def kmer_challenge():
    with open('dataset_2_6.txt', 'r') as f:
        lines = f.read().splitlines()
    print count_kmers(lines[0], lines[1])
