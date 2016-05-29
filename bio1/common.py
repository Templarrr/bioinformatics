from collections import Counter

import constants


def get_complementary_string(nucleotides_string, rna_mode=False, reversed=False):
    complements = constants.rna_complementary \
        if rna_mode \
        else constants.dna_complementary
    result = ''
    for nucleotide in nucleotides_string:
        result += complements[nucleotide]
    if reversed:
        result = result[::-1]
    return result


def count_kmers(nucleotides_string, kmer):
    kmer_len = len(kmer)
    nucleotides_string_len = len(nucleotides_string)
    count = 0
    for i in range(0, nucleotides_string_len - kmer_len + 1):
        if nucleotides_string[i:i + kmer_len] == kmer:
            count += 1
    return count


# Course name for method
PatternCount = count_kmers


def frequent_words_counts(nucleotides_string, kmer_len):
    nucleotides_string_len = len(nucleotides_string)
    result = []
    for i in range(0, nucleotides_string_len - kmer_len + 1):
        kmer = nucleotides_string[i:i + kmer_len]
        result.append(count_kmers(nucleotides_string, kmer))
    return result


def frequent_words(nucleotides_string, kmer_len):
    counts = frequent_words_counts(nucleotides_string, kmer_len)
    max_count = max(counts)
    frequent_patterns = set()
    for i in range(len(counts)):
        if counts[i] == max_count:
            frequent_patterns.add(nucleotides_string[i:i + kmer_len])
    return frequent_patterns


# Course name for method
FrequentWords = frequent_words


def find_all_occurencies(pattern, genome):
    result = []
    start_pos = 0
    while genome.find(pattern, start_pos) != -1:
        index = genome.find(pattern, start_pos)
        result.append(index)
        start_pos = index + 1
    return result


def get_t_clumps(counter, t):
    max_clump_size = max(counter.values())
    result = set()
    if max_clump_size < t:
        return result
    all_clump_size_to_check = range(t, max_clump_size + 1)
    clump_sizes_in_counter = set(counter.values())
    all_clump_size_to_check = [clump_size
                               for clump_size
                               in all_clump_size_to_check
                               if clump_size in clump_sizes_in_counter]
    for clump in counter:
        if counter[clump] in all_clump_size_to_check:
            result.add(clump)
    return result


def find_clumps(genome, k, L, t):
    window_size = L - k + 1
    counter = Counter()
    for i in range(window_size):
        counter[genome[i:i + k]] += 1

    result = get_t_clumps(counter, t)
    for i in range(window_size, len(genome) - k + 1):
        kmer_to_add = genome[i:i + k]
        kmer_to_remove = genome[i - window_size:i - window_size + k]
        counter[kmer_to_add] += 1
        counter[kmer_to_remove] -= 1
        if counter[kmer_to_add] >= t:
            result.add(kmer_to_add)

    return result
