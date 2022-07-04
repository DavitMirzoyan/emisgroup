#!/usr/bin/env python3

from json2html import *
import json

def read_json_file(filename):
    try:
        with open(filename, "r") as f:
            data = json.loads(f.read())
    except:
        raise Exception(f"Reading {filename} file encountered an error")

    return data

def main():
    argument = sys.argv[1]
    #argument = "Aaron697_Dickens475_8c95253e-8ee8-9ae8-6d40-021d702dc78e"

    data = read_json_file(filename="data/"+argument+".json")

    v = json2html.convert(json = data)
    htmlfile = "html_files/"+argument+".html"

    with open(htmlfile, 'w') as ht:
        ht.write(str(v))
main()
'''
import os, sys
from copy import deepcopy
import pandas
import json

def read_json_file(filename):
    try:
        with open(filename, "r") as f:
            data = json.loads(f.read())
    except:
        raise Exception(f"Reading {filename} file encountered an error")

    return data

def cross_join(left, right):
    new_rows = []
    for left_row in left:
        for right_row in right:
            temp_row = deepcopy(left_row)
            for key, value in right_row.items():
                temp_row[key] = value
            new_rows.append(deepcopy(temp_row))
    return new_rows


def flatten_list(data):
    for elem in data:
        if isinstance(elem, list):
            yield from flatten_list(elem)
        else:
            yield elem

def json_to_dataframe(data_in):
    def flatten_json(data, prev_heading=''):
        if isinstance(data, dict):
            rows = [{}]
            for key, value in data.items():
                rows = cross_join(rows, flatten_json(value, prev_heading + '.' + key))
        elif isinstance(data, list):
            rows = []
            for i in range(len(data)):
                [rows.append(elem) for elem in flatten_list(flatten_json(data[i], prev_heading))]
        else:
            rows = [{prev_heading[1:]: data}]
        return rows

    return pandas.DataFrame(flatten_json(data_in))

def main():
    argument = sys.argv[1]

    data = read_json_file(filename="data/"+argument)
    df = json_to_dataframe(data)
    df.to_csv("csv_files/{}.csv".format(argument))

main()
'''