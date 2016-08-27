import datetime


SHINGLE_SIZE = 2


def jaccard(set1, set2):
    """ use jaccard algorithm to estimate string similarity
        set1 and set2 are the set of shingles of the strings to compare
    """
    x = len(set1.intersection(set2))
    y = len(set1.union(set2))
    res = x / float(y)
    return res


def get_shingles(word):
    """ get list of bigrams of a string
    """
    result = set()
    lword = word.lower().strip()
    for i in range(0, len(lword) - SHINGLE_SIZE + 1):
        result.add(lword[i:i+SHINGLE_SIZE])
    return result
