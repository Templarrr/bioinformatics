from bio1.constants import dna_nucleotides
from bio2.common import neighbors


def kmers_in_string(string_len, kmer_len):
    return string_len - kmer_len + 1


def probability_of_kmer(kmer_len):
    return 1.0 / len(dna_nucleotides) ** kmer_len


def expected_number_of_kmer(number_of_strings, string_len, kmer_len):
    kmer_count = number_of_strings * kmers_in_string(string_len, kmer_len)
    return kmer_count * probability_of_kmer(kmer_len)


def get_all_kmers_in_string(string, kmer_len):
    string_kmers = set()
    string_len = len(string)
    for i in range(0, string_len - kmer_len + 1):
        kmer = string[i:i + kmer_len]
        string_kmers.add(kmer)
    return string_kmers


def motif_enumeration(dna, kmer_len, max_hemming_distance):
    dna_kmers = [get_all_kmers_in_string(string, kmer_len) for string in dna]

    all_kmers = set()
    for kmer_list in dna_kmers:
        all_kmers.update(kmer_list)

    all_kmers_with_heighbors = set()
    for kmer in all_kmers:
        all_kmers_with_heighbors.update(neighbors(kmer, max_hemming_distance))

    patterns = set()
    for kmer in all_kmers_with_heighbors:
        kmer_neighbors = neighbors(kmer, max_hemming_distance)
        matches = [kmer_neighbors.intersection(kmer_list) for kmer_list in dna_kmers]
        if all(matches):
            patterns.add(kmer)

    return patterns
