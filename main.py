from pip._vendor import requests
from datetime import datetime
import json

"""
'date': datetime.today().strftime('%Y-%m-%d')
"""

def fetch_info(website, statistic, location):
    params = {
        'stat': statistic,
        'loc': location,
        'date': '2021-12-29'
    }
    
    response = requests.get(website, params)

    if response.status_code != 200:
        print("An error has occured.", response)
    else:
        data = response.json()
    
    print("Province: ", location)
    if statistic == 'cases':
        for item in data['cases']:
            print("Cases: ", item['cases'])
    elif statistic == 'mortality':
        for item in data['mortality']:
            print("Deaths: ", item['deaths'])
    elif statistic == 'recovered':
        for item in data['recovered']:
            print("Recovered: ", item['recovered'])
    elif statistic == 'testing':
        for item in data['testing']:
            print("Recovered: ", item['testing'])
    elif statistic == 'active':
        for item in data['active']:
            print("Active: ", item['active_cases'])

def main():
    url = 'https://api.opencovid.ca/timeseries'

    provinces = [
                    'alberta', 'british columbia', 'manitoba', 'new brunswick', 'newfoundland and labrador', 'northwest territories', 
                    'nova scotia', 'nunavut', 'ontario', 'prince edward island', 'quebec', 'saskatchewan', 'yukon'
                ]

    codes = ['ab', 'bc', 'mb', 'nb', 'nl', 'nt', 'ns', 'nu', 'on', 'pe', 'qc', 'sk', 'yt']            

    valid_stat = ['cases', 'mortality', 'recovered', 'testing', 'active']

    while True:
        raw_loc = input("Enter a province or press 'q' to exit: ")

        if raw_loc in ['q', 'Q']:
            exit(0)
        else:
            if raw_loc.lower() in provinces or raw_loc.lower() in codes:
                print("Valid province. \n")
                break
            else:
                print("Not a valid province, please try again. \n")

    while True:
        print("Below are valid statistics:", end="")
        stats = """
        • cases
        • mortality 
        • recovered 
        • testing 
        • active
                """
        print(stats)

        raw_stat = input("Enter a inquired statistic: ")

        if raw_stat in ['q', 'Q']:
            exit(0)
        else:
            if raw_stat.lower() in valid_stat:
                print("Valid statistic. \n")
                break
            else:
                print("Not a valid statistic, please try again \n")

    fetch_info(url, raw_stat, raw_loc)            

if __name__ == "__main__":
    main()