"""
JSON Data Reading
Chris Denq
"""
import csv
import json
csv_filepath = "netflix_titles.csv"
output_filepath = "netflix_json.json"


def convert_to_json(filepath):
    data = []
    with open(filepath, "r", encoding="utf-8") as csv_mem:
        reader = csv.DictReader(csv_mem)
        for line in reader:
            if line["type"] == "TV Show":
                temp_dict = {"show_id": line['show_id'],
                             "director": line['director'],
                             "country": line['country'],
                             "date_added": line['date_added'],
                             "duration": line['duration']}
                data.append(temp_dict)

        with open(output_filepath, 'w', encoding='utf-8') as csv_mem2:
            csv_mem2.write(json.dumps(data, indent=4))


def main():
    convert_to_json(csv_filepath)
    return


if __name__ == "__main__":
    main()

r"""
--- sample run of unit_test() ---

"""