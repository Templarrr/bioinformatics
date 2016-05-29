from common import count_kmers, frequent_words, \
    get_complementary_string, find_all_occurencies


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
