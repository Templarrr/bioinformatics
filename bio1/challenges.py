from common import count_kmers, frequent_words


def kmer_challenge():
    with open('dataset_2_6.txt', 'r') as f:
        lines = f.read().splitlines()
    print count_kmers(lines[0], lines[1])


def frequent_words_challenge():
    with open('dataset_2_9.txt', 'r') as f:
        lines = f.read().splitlines()
    words = frequent_words(lines[0], int(lines[1]))
    print ' '.join(words)
