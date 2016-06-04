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


def run_all():
    print 'Running all challenges with timing'
    time1 = time()
    min_skew_challenge()
    hemming_distance_challenge()
    approximate_pattern_matching_challenge()
    approximate_pattern_count_challenge()
    neighbors_challenge()
    time2 = time()
    print 'Comlete in %f seconds' % (time2 - time1)


if __name__ == '__main__':
    frequent_words_with_mismatches_challenge()
