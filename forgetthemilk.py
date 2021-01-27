#!/usr/bin/env python
import json
import argparse
from json.decoder import JSONDecodeError
import csv
import datetime


def get_json_or_die(args):

    try:
        rtm_json_file = open(args.rtm_json)
        return json.load(rtm_json_file)
    except JSONDecodeError as jse:
        print(f"Invalid JSON specified! {jse}")
        exit()


def get_open_tasks(rtm_json_blob):
    tasks = rtm_json_blob['tasks']
    return [t for t in tasks if 'date_completed' not in t]


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "rtm_json", help="The JSON file you exported from Remember The Milk"
    )
    parser.add_argument("csv_result", help="CSV file you want your converted RTM tasks written to")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

rtm_json = get_json_or_die(args)

open_tasks = get_open_tasks(rtm_json)

with open(args.csv_result, 'w', newline='') as csv_result:
    rtm_writer = csv.writer(csv_result)

    rtm_writer.writerow(
        ['TYPE', 'CONTENT', 'PRIORITY', 'INDENT', 'AUTHOR', 'RESPONSIBLE', 'DATE', 'DATE_LANG', 'TIMEZONE'])
    for row_task in open_tasks:
        rtm_writer.writerow(['task',
                             row_task['name'],
                             1,  # priority
                             1,  # indent
                             '',  # author
                             '',  # responsible
                             '',  # Wow trying to convert an Excel numeric date to Python is a nightmare!
                             '',  # date_lang
                             ''  # timezone
                             ])
