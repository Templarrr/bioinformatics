import constants


def get_complementary_string(nucleotides_string, rna_mode=False):
    complements = constants.rna_complementary \
        if rna_mode \
        else constants.dna_complementary
    result = ''
    for nucleotide in nucleotides_string:
        result += complements[nucleotide]
    return result


def count_kmers(nucleotides_string, kmer):
    kmer_len = len(kmer)
    nucleotides_string_len = len(nucleotides_string)
    count = 0
    for i in range(0, nucleotides_string_len - kmer_len + 1):
        if nucleotides_string[i:i + kmer_len] == kmer:
            count += 1
    return count
