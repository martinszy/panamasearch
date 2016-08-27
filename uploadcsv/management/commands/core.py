import csv
import sys
import os
import datetime
from set_implementation import get_shingles, jaccard


THRESHOLD = 0.6
PANAMA_FILE = "data/Officers.csv"


def find_doc(name, docs):
    """ find the string name in the list of string docs
        you need to precalculate the shingles for docs
    """
    shingles1 = get_shingles(name)
    for doc in docs:
        shingles2 = doc['shingles']
        if shingles2:
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
    print (datetime.datetime.now())
    with open(PANAMA_FILE, 'r') as csvfile:
        for row in parse_csv(csvfile):
            name = row[0].strip().lower()
            if name and name != "the bearer":
                yield {
                    'name': row[0],
                    'node_id': row[5],
                    'shingles': get_shingles(name)
                }
    print (datetime.datetime.now())


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
                name = row[0].strip()
                if name:
                    for match in find_doc(name, docs):
                        data = [match['score'],
                                panama_link(match['original']['node_id']),
                                match['original']['name'].upper()
                                ]
                        data.extend(row)
                        a.writerow(data)


if __name__ == '__main__':
    input_file = sys.argv[1]
    match_file(input_file, "output/" + os.path.basename(input_file))
