import csv
import sys
import os


SHINGLE_SIZE = 2
THRESHOLD = 0.6
PANAMA_FILE = "data/Officers.csv"


def get_shingles(word):
    """ get list of bigrams of a string
    """
    result = set()
    lword = word.lower().strip()
    for i in range(0, len(lword) - SHINGLE_SIZE + 1):
        result.add(lword[i:i+SHINGLE_SIZE])
    return result


def jaccard(set1, set2):
    """ use jaccard algorithm to estimate string similarity
        set1 and set2 are the set of shingles of the strings to compare
    """
    x = len(set1.intersection(set2))
    y = len(set1.union(set2))
    return x / float(y)


def find_doc(name, docs):
    """ find the string name in the list of string docs
        you need to precalculate the shingles for docs
    """
    shingles1 = get_shingles(name)
    for doc in docs:
        shingles2 = doc['shingles']
        score = jaccard(shingles1, shingles2)
        if score > THRESHOLD:
            yield {'score': score, 'original': doc}


def parse_csv(csv_file):
    """ read a csv file
    """
    reader = csv.reader(csv_file, delimiter=',', quotechar='"')
    for row in reader:
        yield row


def read_panama_file():
    """ read panama file and precalculate shingles
    """
    with open(PANAMA_FILE, 'r') as csvfile:
        for row in parse_csv(csvfile):
            name = row[0]
            if name and name.lower() != "the bearer":
                yield {
                    'name': row[0],
                    'node_id': row[5],
                    'shingles': get_shingles(name)
                }


def panama_link(node_id):
    """ build link to view the entity in offshoreleaks
    """
    return "https://offshoreleaks.icij.org/nodes/" + node_id


def match_file(input_file, output_file):
    """ search names in input_file
        write matches in output_file
    """
    docs = list(read_panama_file())
    with open(output_file, 'w') as fp:
        a = csv.writer(fp, delimiter=',')

        with open(input_file, 'r') as csvfile:
            for index, row in enumerate(parse_csv(csvfile)):
                if index == 0:
                    titles = ["score", "link", "name"]
                    titles.extend(row)
                    a.writerow(titles)
                if index % 10 == 0:
                    print (index)
                name = ("%s %s" % (row[0], row[1])).strip()
                if name:
                    for match in find_doc(name, docs):
                        data = [match['score'],
                                panama_link(match['original']['node_id']),
                                '"%s"' % match['original']['name'].upper()
                                ]
                        data.extend(row)
                        a.writerow(data)


if __name__ == '__main__':
    input_file = sys.argv[1]
    match_file(input_file, "output/" + os.path.basename(input_file))
