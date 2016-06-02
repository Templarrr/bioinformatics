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
