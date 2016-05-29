from common import count_kmers, frequent_words, \
    get_complementary_string, find_all_occurencies, find_clumps


def kmer_challenge():
    with open('dataset_2_6.txt', 'r') as f:
        lines = f.read().splitlines()
    print count_kmers(lines[0], lines[1])


def frequent_words_challenge():
    with open('dataset_2_9.txt', 'r') as f:
        lines = f.read().splitlines()
    words = frequent_words(lines[0], int(lines[1]))
    print ' '.join(words)


def complementary_challenge():
    with open('dataset_3_2.txt', 'r') as f:
        lines = f.read().splitlines()
    print get_complementary_string(lines[0], rna_mode=False, reversed=True)


def occurencies_challenge():
    with open('dataset_3_5.txt', 'r') as f:
        lines = f.read().splitlines()
    occurences = find_all_occurencies(lines[0], lines[1])
    print ' '.join(map(str, occurences))


def vibrio_occurencies_challenge():
    with open('Vibrio_cholerae.txt', 'r') as f:
        lines = f.read().splitlines()
    occurences = find_all_occurencies('CTTGATCAT', lines[0])
    print ' '.join(map(str, occurences))


def find_clumps_challenge():
    with open('dataset_4_5.txt', 'r') as f:
        lines = f.read().splitlines()
    k, L, t = map(int, lines[1].split())
    clumps = find_clumps(lines[0], k, L, t)
    print ' '.join(clumps)


def e_coli_clumps_challenge():
    with open('E-coli.txt', 'r') as f:
        lines = f.read().splitlines()
    clumps = find_clumps(lines[0], 9, 500, 3)
    print len(clumps)
