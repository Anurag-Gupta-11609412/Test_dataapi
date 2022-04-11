import requests
import csv
import json
import os

base_url = 'https://dummyjson.com/products'
resp = requests.get(base_url)
data = resp.json()
print(data)
def output():
    return
    for i in range(0,10):
        data['products'][i]


def csv_file():
    details = output()
    csv_header = ['id', 'title', 'description', 'discountPercentage', 'rating', 'stock', 'brand']
    with open('E:\Internship\detailsfile.csv', 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter='\t')
        # check if the file is empty
        if os.stat("E:\Internship\detailsfile.csv").st_size == 0:
            csv_writer.writerow(csv_header)
            csv_writer.writerow(details)
        else:
            csv_writer.writerow(details)

    csv_file.close()


def main():
    output()
    csv_file()



