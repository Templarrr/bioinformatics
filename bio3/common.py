from math import log

from bio1.common import number_to_pattern
from bio1.constants import dna_nucleotides
from bio2.common import neighbors, hemming_distance


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


def get_all_kmers_in_string_as_ordered_list(string, kmer_len):
    string_kmers = []
    string_len = len(string)
    for i in range(0, string_len - kmer_len + 1):
        kmer = string[i:i + kmer_len]
        string_kmers.append(kmer)
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


def motif_counts(motifs, laplace_rule=False):
    result = []
    for i in range(len(motifs[0])):
        if laplace_rule:
            result.append({'A': 1, 'C': 1, 'G': 1, 'T': 1})
        else:
            result.append({'A': 0, 'C': 0, 'G': 0, 'T': 0})
    for motif in motifs:
        for index, char in enumerate(motif):
            result[index][char] += 1
    return result


def motif_profile(motifs, laplace_rule=False):
    result = []
    for i in range(len(motifs[0])):
        if laplace_rule:
            result.append({
                'A': 1.0 / (4 + len(motifs)),
                'C': 1.0 / (4 + len(motifs)),
                'G': 1.0 / (4 + len(motifs)),
                'T': 1.0 / (4 + len(motifs))
            })
        else:
            result.append({'A': 0, 'C': 0, 'G': 0, 'T': 0})
    for motif in motifs:
        for index, char in enumerate(motif):
            if laplace_rule:
                result[index][char] += 1.0 / (4 + len(motifs))
            else:
                result[index][char] += 1.0 / len(motifs)
    return result


def motif_consensus(motifs):
    counts = motif_counts(motifs)
    result = ''
    for count_column in counts:
        max_value = max(count_column.values())
        for char in count_column:
            if count_column[char] == max_value:
                result += char
                break
    return result


def motif_set_score(motifs):
    counts = motif_counts(motifs)
    result = 0
    for count_column in counts:
        result += sum(count_column.values()) - max(count_column.values())
    return result


def motif_column_entropy(profile_column):
    result = 0
    for nucleotide in profile_column:
        if profile_column[nucleotide] == 0:
            continue
        result += profile_column[nucleotide] * log(profile_column[nucleotide], 2)
    return -1 * result


def motif_set_entropy_score(motifs):
    profile = motif_profile(motifs)
    result = 0
    for profile_column in profile:
        result += motif_column_entropy(profile_column)
    return result


def motif_alternate_score(motifs):
    consensus = motif_consensus(motifs)
    distances = [hemming_distance(consensus, motif) for motif in motifs]
    return sum(distances)


def d_text(pattern, text):
    # I reaaaally tired thinking about more suitable names now...
    kmers = get_all_kmers_in_string(text, len(pattern))
    return min([hemming_distance(pattern, kmer) for kmer in kmers])


def d_dna(pattern, dna):
    return sum(d_text(pattern, text) for text in dna)


def median_string(dna, k):
    max_distance = k * len(dna) + 1
    median = ''
    for i in range(4 ** k):
        pattern = number_to_pattern(i, k)
        distance = d_dna(pattern, dna)
        if distance < max_distance:
            max_distance = distance
            median = pattern
    return median


def pr(string, profile):
    result = 1
    for i in range(len(string)):
        result *= profile[i][string[i]]
    return result


def profile_most_probable_kmer(string, k, profile):
    kmers = get_all_kmers_in_string_as_ordered_list(string, k)
    max_prob = -1
    max_kmer = ''
    for kmer in kmers:
        prob = pr(kmer, profile)
        if prob > max_prob:
            max_prob = prob
            max_kmer = kmer
    return max_kmer


def get_profile_from_text_presentation(lines):
    result = []
    for i in range(len(lines[0].split())):
        result.append({'A': 0, 'C': 0, 'G': 0, 'T': 0})
    nucleotides = ['A', 'C', 'G', 'T']
    for i in range(4):
        prs = map(float, lines[i].split())
        for j in range(len(prs)):
            result[j][nucleotides[i]] = prs[j]
    return result


def greedy_motif_search(dna, k, laplace_rule=False):
    best_motif = None
    best_motif_score = len(dna) * len(dna[0])
    start_kmers = get_all_kmers_in_string(dna[0], k)
    for kmer0 in start_kmers:
        motifs = [kmer0]
        for i in range(1, len(dna)):
            profile = motif_profile(motifs, laplace_rule)
            motifs.append(profile_most_probable_kmer(dna[i], k, profile))
        motif_score = motif_set_score(motifs)
        if motif_score < best_motif_score:
            best_motif = motifs
            best_motif_score = motif_score
    return best_motif


import random


def pick_random_kmer(string, k):
    start_pos = random.randint(0, len(string) - k)
    return string[start_pos:start_pos + k]


def randomized_motif_search(dna, k, repeats=1000):
    best_motif = None
    best_motif_score = len(dna) * len(dna[0])
    for i in range(repeats):
        best_motif_i = [pick_random_kmer(string, k) for string in dna]
        best_motif_score_i = motif_set_score(best_motif_i)
        while True:
            profile = motif_profile(best_motif_i, laplace_rule=True)
            new_motif = [profile_most_probable_kmer(string, k, profile) for string in dna]
            new_motif_score = motif_set_score(new_motif)
            if new_motif_score < best_motif_score_i:
                best_motif_i = new_motif
                best_motif_score_i = new_motif_score
            else:
                break
        if best_motif_score_i < best_motif_score:
            best_motif = best_motif_i
            best_motif_score = best_motif_score_i
    return best_motif


def probability_of_capturing_at_least_one_kmer(dna_str_len, dna_len, k):
    probability_of_not_capturing_kmer_in_str = 1 - 1.0 / (dna_str_len - k + 1)
    probability_of_not_capturing_kmer_in_dna = probability_of_not_capturing_kmer_in_str ** dna_len
    return 1 - probability_of_not_capturing_kmer_in_dna


def probability_of_capturing_at_least_two_kmer(dna_str_len, dna_len, k):
    probability_of_capturing_kmer_in_str = 1.0 / (dna_str_len - k + 1)
    probability_of_not_capturing_kmer_in_str = 1 - probability_of_capturing_kmer_in_str
    probability_of_capturing_0_kmer_in_dna = probability_of_not_capturing_kmer_in_str ** dna_len
    probability_of_capturing_1_kmer_in_dna = dna_len * probability_of_not_capturing_kmer_in_str ** (
        dna_len - 1) * probability_of_capturing_kmer_in_str
    return 1 - probability_of_capturing_0_kmer_in_dna - probability_of_capturing_1_kmer_in_dna


import bisect


def cdf(weights):
    total = sum(weights)
    result = []
    cumsum = 0.0
    for w in weights:
        cumsum += w
        result.append(cumsum / total)
    return result


def choice(population, weights):
    assert len(population) == len(weights)
    cdf_vals = cdf(weights)
    x = random.random()
    idx = bisect.bisect(cdf_vals, x)
    return population[idx]


def profile_randomly_generated_kmer(string, k, profile):
    kmers = get_all_kmers_in_string_as_ordered_list(string, k)
    weights = [pr(kmer, profile) for kmer in kmers]
    return choice(kmers, weights)


def gibbs_sampler(dna, k, N, repeats=20):
    best_motif = None
    best_motif_score = len(dna) * len(dna[0])
    for __ in range(repeats):
        motifs = [pick_random_kmer(string, k) for string in dna]
        best_motifs = motifs[:]
        best_motifs_score = motif_set_score(best_motifs)
        for _ in range(N):
            i = random.randint(0, len(dna) - 1)
            modified_motifs = [motif for j, motif in enumerate(best_motifs) if j != i]
            profile = motif_profile(modified_motifs, laplace_rule=True)
            motifs[i] = profile_randomly_generated_kmer(dna[i], k, profile)
            motifs_score = motif_set_score(motifs)
            if motifs_score < best_motifs_score:
                best_motifs = motifs[:]
                best_motifs_score = motifs_score
        if best_motifs_score < best_motif_score:
            best_motif = best_motifs
            best_motif_score = best_motifs_score
    return best_motif
