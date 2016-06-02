from common import skew


def test_skew():
    skew_list = skew('CATGGGCATCGGCCATACGCC')
    assert ' '.join(map(str, skew_list)) == '0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2'
