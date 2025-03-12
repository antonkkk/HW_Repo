# RE 2.
import re


def find_dates_in_file(filename):

    date_pattern = re.compile(r'\b(\d{2}\.\d{2}\.\d{4})\b')

    with open(filename, 'r', encoding='utf-8') as file:

        for line in file:
            dates = date_pattern.findall(line)
            if dates:
                for date in dates:
                    print(date)


filename = 'textfile.txt'
find_dates_in_file(filename)
