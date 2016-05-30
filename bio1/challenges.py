from time import time

from common import count_kmers, frequent_words, \
    get_complementary_string, find_all_occurencies, \
    find_clumps, computing_frequencies


def kmer_challenge():
    with open('../data/challenges/dataset_2_6.txt', 'r') as f:
        lines = f.read().splitlines()
    print count_kmers(lines[0], lines[1])


def frequent_words_challenge():
    with open('../data/challenges/dataset_2_9.txt', 'r') as f:
        lines = f.read().splitlines()
    words = frequent_words(lines[0], int(lines[1]))
    print ' '.join(words)


def complementary_challenge():
    with open('../data/challenges/dataset_3_2.txt', 'r') as f:
        lines = f.read().splitlines()
    print get_complementary_string(lines[0], rna_mode=False, reversed=True)


def occurencies_challenge():
    with open('../data/challenges/dataset_3_5.txt', 'r') as f:
        lines = f.read().splitlines()
    occurences = find_all_occurencies(lines[0], lines[1])
    print ' '.join(map(str, occurences))


def vibrio_occurencies_challenge():
    with open('../data/examples/Vibrio_cholerae.txt', 'r') as f:
        lines = f.read().splitlines()
    occurences = find_all_occurencies('CTTGATCAT', lines[0])
    print ' '.join(map(str, occurences))


def find_clumps_challenge():
    with open('../data/challenges/dataset_4_5.txt', 'r') as f:
        lines = f.read().splitlines()
    k, L, t = map(int, lines[1].split())
    clumps = find_clumps(lines[0], k, L, t)
    print ' '.join(clumps)


def e_coli_clumps_challenge():
    with open('../data/examples/E-coli.txt', 'r') as f:
        lines = f.read().splitlines()
    clumps = find_clumps(lines[0], 9, 500, 3)
    print len(clumps)


def frequencies_challange():
    with open('../data/challenges/dataset_2994_5.txt', 'r') as f:
        lines = f.read().splitlines()
    frequencies = computing_frequencies(lines[0], int(lines[1]))
    print ' '.join(map(str, frequencies))


def run_all():
    print 'Running all challenges with timing'
    time1 = time()
    kmer_challenge()
    frequent_words_challenge()
    complementary_challenge()
    occurencies_challenge()
    vibrio_occurencies_challenge()
    find_clumps_challenge()
    e_coli_clumps_challenge()
    frequencies_challange()
    time2 = time()
    print 'Comlete in %f seconds' % (time2 - time1)


if __name__ == '__main__':
    run_all()
