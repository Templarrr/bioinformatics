def skew(genome, max_i=None):
    if max_i is None:
        max_i = len(genome) - 1
    result = [0]
    for i in range(0, max_i + 1):
        if genome[i] == 'C':
            result.append(result[-1] - 1)
        elif genome[i] == 'G':
            result.append(result[-1] + 1)
        else:
            result.append(result[-1])
    return result


def min_skew(genome):
    skew_list = skew(genome)
    min_skew_value = min(skew_list)
    return [pos for pos, skew_value in enumerate(skew_list) if skew_value == min_skew_value]


def hemming_distance(text1, text2):
    return sum([text1[i] != text2[i] for i in xrange(len(text1))])


def approximate_pattern_matching(pattern, text, max_hemming_distance):
    result = []
    text_len = len(text)
    pattern_len = len(pattern)
    for i in range(0, text_len - pattern_len + 1):
        kmer = text[i:i + pattern_len]
        if hemming_distance(pattern, kmer) <= max_hemming_distance:
            result.append(i)
    return result
