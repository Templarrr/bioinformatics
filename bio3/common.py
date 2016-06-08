from bio1.constants import dna_nucleotides


def kmers_in_string(string_len, kmer_len):
    return string_len - kmer_len + 1


def probability_of_kmer(kmer_len):
    return 1.0 / len(dna_nucleotides) ** kmer_len


def expected_number_of_kmer(number_of_strings, string_len, kmer_len):
    kmer_count = number_of_strings * kmers_in_string(string_len, kmer_len)
    return kmer_count * probability_of_kmer(kmer_len)
