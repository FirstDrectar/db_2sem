import MapReduce
import sys

mr = MapReduce.MapReduce()


def mapper(record):
    string = record[1]
    string = string[:-10]
    mr.emit_intermediate(string, 1);


def reducer(key, list_of_values):
    mr.emit(key)


if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
