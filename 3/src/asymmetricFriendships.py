import MapReduce
import sys

mr = MapReduce.MapReduce()


def mapper(record):
    key = record[0]
    friend = record[1]
    mr.emit_intermediate(key, record);
    mr.emit_intermediate(friend, record);


def reducer(key, list_of_values):
    for v in list_of_values:
        nonRel = [v[1], v[0]]
        if nonRel not in list_of_values:
            if v[0] == key:
                mr.emit((v[0], v[1]))
            else:
                mr.emit((v[1], v[0]))


if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
