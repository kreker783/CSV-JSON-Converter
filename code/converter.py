import csv
import json
from shutil import rmtree
from os import mkdir, path


def create_dir():
    mkdir('temp')


def remove_dir():
    rmtree('temp')


def csv_to_json(csv_file, json_file):
    arr = list()

    if path.exists(csv_file):
        with open(csv_file, encoding="utf8") as f:
            reader = csv.DictReader(f)

            for line in reader:
                arr.append(line)

        with open(json_file, 'w', encoding="utf8") as f:
            indent = len(arr[0])
            conv = json.dumps(arr, indent=indent, ensure_ascii=False)
            f.write(conv)
    else:
        return "CSV file doesn't exist!"


# def json_to_csv(csv_file, json_file):
#
    return
