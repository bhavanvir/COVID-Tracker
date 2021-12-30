from pip._vendor import requests
from datetime import datetime
import json

def fetch_info(website, statistic, location, date):
    params = {
        'stat': statistic.upper(),
        'loc': location.upper(),
        'date': date
    }
    
    response = requests.get(website, params)

    if response.status_code != 200:
        print("An error has occured.", response)
    else:
        data = response.json()

        if len(data['cases']) == 0:
            print("If 'today' was selected, no cases have been reported yet; please try again later.")
            exit(0)
    
    print("Province: ", location)
    print("Date: ", date)
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

    codes = ['ab', 'bc', 'mb', 'nb', 'nl', 'nt', 'ns', 'nu', 'on', 'pe', 'qc', 'sk', 'yt']            

    valid_stat = ['cases', 'mortality', 'recovered', 'testing', 'active']

    while True:
        print("Below are valid province codes:", end="")
        letter_codes = """
        • Alberta: AB
        • British Columbia: BC
        • Manitoba: MB
        • New Brunswick: NB
        • Newfoundland and Labrador: NL
        • Northwest Territories: NT
        • Nova Scotia: NS
        • Nunavut: NU
        • Ontario: ON
        • Prince Edward Island: PE
        • Quebec: QC
        • Saskatchewan: SK
        • Yukon: YT
        """
        print(letter_codes)

        raw_loc = input("Enter a two-letter province code or press 'q' to exit: ")

        if raw_loc in ['q', 'Q']:
            exit(0)
        else:
            if raw_loc.lower() in codes:
                print("Valid two-letter province code. \n")
                break
            else:
                print("Not a valid two-letter province code, please try again. \n")

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

    while True:
        raw_date = input("Please enter a valid date in YYYY-MM-DD format or enter 'today' for the current date: ")

        if raw_date in ['q', 'Q']:
            exit(0)
        else:
            try:
                if raw_date.lower() == 'today':
                    raw_date = datetime.today().strftime('%Y-%m-%d')
                else:
                    datetime.strptime(raw_date, '%Y-%m-%d')
                print("Valid date format. \n")
                break
            except ValueError:
                print("Specified date is not in YYYY-MM-DD format. \n")

    fetch_info(url, raw_stat, raw_loc, raw_date)            

if __name__ == "__main__":
    main()