import json
import csv
import requests
from collections import defaultdict

def main():
    data = requests.get('http://data.cityofnewyork.us/api/views/25th-nujf/rows.json').json()
    rows = defaultdict( int )
    data_test = {}
    for index, row in enumerate(data['data']):
        year = int( row[ -6 ] )
        count = row[ -2 ]
        eth = row[ -4 ]
        name = row[ -3 ]
        data_test.update({index:[year, count, eth, name]})
        if 2011 < year < 2015:
                rows[ (name, eth) ] += int( count )

    with open('data.json', 'w') as f:
        json.dump(data_test, f)

    with open('grouped_data.csv', 'w') as csvfile:
        for key, value in rows.items():
            fieldnames = ['First Name', 'Ethnicity', 'Count']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'First Name':key[0], 'Ethnicity':key[1], 'Count':value})

    json_data = {}
    with open('grouped_data.json', 'w') as f:
        for key, value in enumerate(rows.items()):
            json_data.update({key:[value[0][0], value[0][1],value[1]]})
        json.dump(json_data, f)

if __name__ == '__main__':
    main()
