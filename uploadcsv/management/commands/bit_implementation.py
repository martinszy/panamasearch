import datetime


SHINGLE_SIZE = 2
BIGRAMS = {}


def profile(log):
    if False:
        print (log)


def letter_idx(l):
    if ord('z') >= ord(l) >= ord('a'):
        return ord(l) - ord('a')
    else:
        return ord('a') - 1


def bits_bigram(bigram):
    if bigram not in BIGRAMS:
        x = letter_idx(bigram[1]) * 28 + letter_idx(bigram[0])
        BIGRAMS[bigram] = 1 << x
    return BIGRAMS[bigram]


def get_shingles(word):
    """ get list of bigrams of a string
    """
    result = 0
    lword = word.lower().strip()
    for i in range(0, len(lword) - SHINGLE_SIZE + 1):
        result = result + bits_bigram(lword[i:i+SHINGLE_SIZE])
    return result


def jaccard(X, Y):
    """ use jaccard algorithm to estimate string similarity
        X and Y are the bit representation of shingles
    """
    t = datetime.datetime.now()
    x = bin(X & Y).count("1")
    y = bin(X | Y).count("1")
    res = x / float(y)
    profile (datetime.datetime.now() - t)
    return res

if __name__ == '__main__':
    for i in range(1000000):
        jaccard(get_shingles("Macri Mauricio"), get_shingles("Mauricio Macri"))
