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
