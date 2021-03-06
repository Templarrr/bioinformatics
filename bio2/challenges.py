from time import time

from common import min_skew, hemming_distance, approximate_pattern_matching, \
    approximate_pattern_count, neighbors, frequent_words_with_mismatches


def min_skew_challenge():
    with open('../data/challenges/dataset_7_6.txt', 'r') as f:
        lines = f.read().splitlines()
    min_skew_pos = min_skew(lines[0])
    print ' '.join(map(str, min_skew_pos))


def hemming_distance_challenge():
    with open('../data/challenges/dataset_9_3.txt', 'r') as f:
        lines = f.read().splitlines()
    print hemming_distance(lines[0], lines[1])


def approximate_pattern_matching_challenge():
    with open('../data/challenges/dataset_9_4.txt', 'r') as f:
        lines = f.read().splitlines()
    matches = approximate_pattern_matching(lines[0], lines[1], int(lines[2]))
    print ' '.join(map(str, matches))


def approximate_pattern_count_challenge():
    with open('../data/challenges/dataset_9_6.txt', 'r') as f:
        lines = f.read().splitlines()
    count = approximate_pattern_count(lines[0], lines[1], int(lines[2]))
    print count


def neighbors_challenge():
    with open('../data/challenges/dataset_3014_3.txt', 'r') as f:
        lines = f.read().splitlines()
    neighbors_list = neighbors(lines[0], int(lines[1]))
    for neighbor in neighbors_list:
        print neighbor


def frequent_words_with_mismatches_challenge():
    with open('../data/challenges/dataset_9_7.txt', 'r') as f:
        lines = f.read().splitlines()
    words = frequent_words_with_mismatches(
        lines[0],
        int(lines[1].split()[0]),
        int(lines[1].split()[1]))
    print ' '.join(words)


def frequent_words_with_mismatches_challenge2():
    with open('../data/challenges/dataset_9_8.txt', 'r') as f:
        lines = f.read().splitlines()
    words = frequent_words_with_mismatches(
        lines[0],
        int(lines[1].split()[0]),
        int(lines[1].split()[1]), True)
    print ' '.join(words)


def salmonella_challenge():
    with open('../data/examples/Salmonella_enterica.txt', 'r') as f:
        lines = f.read().splitlines()
    # combine dna
    dna = ''.join(lines[1:])
    # find min skewness
    min_skew_pos = min_skew(dna)[0]
    print 'Minimum skew position: %d' % min_skew_pos
    # get window
    window_half_size = 500
    sample = dna[min_skew_pos - window_half_size:min_skew_pos + window_half_size]
    # find max occurencies
    words = frequent_words_with_mismatches(sample, 9, 1)
    print ' '.join(words)


def run_all():
    print 'Running all challenges with timing'
    time1 = time()
    min_skew_challenge()
    hemming_distance_challenge()
    approximate_pattern_matching_challenge()
    approximate_pattern_count_challenge()
    neighbors_challenge()
    frequent_words_with_mismatches_challenge()
    frequent_words_with_mismatches_challenge2()
    salmonella_challenge()
    time2 = time()
    print 'Comlete in %f seconds' % (time2 - time1)


if __name__ == '__main__':
    salmonella_challenge()
