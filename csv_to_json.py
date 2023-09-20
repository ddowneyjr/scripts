import csv
import json

input_csv = ""
output_json = ":"

data = []

with open(input_csv, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        data.append(row)

with open(output_json, 'w') as json_file:
    json.dump(data, json_file, indent=4)

print(f"CSV file '{input_csv}' converted to JSON file '{output_json}'")
