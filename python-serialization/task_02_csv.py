#!/usr/bin/env python3

import json
import csv


def convert_csv_to_json(csv_file):
    """Convert CSV to JSON."""
    data = []
    try:
        with open(csv_file, encoding='utf-8') as csvf:
            csvReader = csv.DictReader(csvf)

            for rows in csvReader:
                data.append(rows)

        with open("data.json", 'w', encoding='utf-8') as jsonf:
            jsonf.write(json.dumps(data, indent=4))
            print(f"Data CSV [{csv_file}] converted to data.json")
            return True
    except FileNotFoundError:
        print(f"Error: file {csv_file} not found")
    except Exception as e:
        print(f"Error: {e}")
    return False


csv_file = 'Names.csv'

convert_csv_to_json(csv_file)
