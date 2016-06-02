from time import time

from common import min_skew


def min_skew_challenge():
    with open('../data/challenges/dataset_7_6.txt', 'r') as f:
        lines = f.read().splitlines()
    min_skew_pos = min_skew(lines[0])
    print ' '.join(map(str, min_skew_pos))


def run_all():
    print 'Running all challenges with timing'
    time1 = time()
    min_skew_challenge()
    time2 = time()
    print 'Comlete in %f seconds' % (time2 - time1)


if __name__ == '__main__':
    run_all()
