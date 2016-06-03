from collections import Counter
from bio1.common import number_to_pattern


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


def approximate_pattern_count(pattern, nucleotides_string, max_hemming_distance):
    counter = Counter()
    nucleotides_string_len = len(nucleotides_string)
    kmer_len = len(pattern)
    for i in range(0, nucleotides_string_len - kmer_len + 1):
        kmer = nucleotides_string[i:i + kmer_len]
        counter[kmer] += 1
    result = 0
    for kmer in counter:
        if hemming_distance(pattern, kmer) <= max_hemming_distance:
            result += counter[kmer]
    return result


def frequent_words_with_mismatches(nucleotides_string, kmer_len, max_hemming_distance):
    counter = Counter()
    nucleotides_string_len = len(nucleotides_string)
    for i in range(0, nucleotides_string_len - kmer_len + 1):
        kmer = nucleotides_string[i:i + kmer_len]
        counter[kmer] += 1
    patterns = {}
    for i in range(4 ** kmer_len):
        pattern = number_to_pattern(i, kmer_len)
        pattern_appearences_with_mismatches = 0
        for kmer in counter:
            if hemming_distance(kmer, pattern) <= max_hemming_distance:
                pattern_appearences_with_mismatches += counter[kmer]
        if pattern_appearences_with_mismatches:
            patterns[pattern] = pattern_appearences_with_mismatches
    max_appearences = max(patterns.values())
    return [pattern for pattern in patterns if patterns[pattern] == max_appearences]
