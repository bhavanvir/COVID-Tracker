from pip._vendor import requests
from datetime import datetime

def print_info(data, statistic):
    to_fetch = statistic

    if statistic == 'mortality':
        to_fetch = 'deaths'
    elif statistic == 'active':
        to_fetch = 'active_cases'

    for item in data[statistic]:
        print(statistic.title() + ": ", item[to_fetch])

def fetch_info(website, statistic, location, date):
    params = {
        'stat': statistic.upper(),
        'loc': location.upper(),
        'date': date
    }
    
    response = requests.get(website, params)

    if response.status_code != 200:
        print("An error has occured.", response) 
        print("Paramaters input: ", params)
    else:
        data = response.json()

        if len(data['cases']) != 0:
            print("Province: ", location.upper())
            print("Date: ", date)
            print_info(data, statistic)
        else: 
            if date == datetime.today().strftime('%Y-%m-%d'):
                print("No cases have been reported for " + date + " yet, please try again later.")
            else:
                print("Entered date has no data available.")

def get_loc(codes):
    while True:
        print("\n" + "Below are valid province codes:", end="")
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

        raw_loc = input("Enter a two-letter province code: ")

        if raw_loc in ['q', 'Q']:
            exit(0)
        else:
            if raw_loc.lower() in codes:
                print("Valid two-letter province code. \n")
                return raw_loc
            else:
                print("Not a valid two-letter province code, please try again. \n")

def get_stat(valid_stat):
    while True:
        print("Below are valid statistics:", end="")
        stats = """
        • Cases
        • Mortality 
        • Recovered 
        • Testing 
        • Active
        """
        print(stats)

        raw_stat = input("Enter a inquired statistic: ")

        if raw_stat in ['q', 'Q']:
            exit(0)
        else:
            if raw_stat.lower() in valid_stat:
                print("Valid statistic. \n")
                return raw_stat
            else:
                print("Not a valid statistic, please try again \n")

def get_date():
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
                print("Valid date format.")
                print("\n" + "------------------------------------------------------------------------------------------------" + "\n")
                return raw_date
            except ValueError:
                print("Specified date is not in YYYY-MM-DD format. \n")

def main():
    url = 'https://api.opencovid.ca/timeseries'

    codes = ['ab', 'bc', 'mb', 'nb', 'nl', 'nt', 'ns', 'nu', 'on', 'pe', 'qc', 'sk', 'yt']            

    valid_stat = ['cases', 'mortality', 'recovered', 'testing', 'active']

    while True:   
        print("Enter 'q' anytime to exit.")

        raw_loc = get_loc(codes)
        raw_stat = get_stat(valid_stat)
        raw_date = get_date()

        fetch_info(url, raw_stat, raw_loc, raw_date)

        valid_req = False

        while valid_req != True:
            continue_req = input("\n" + "Would you like to continue with a new query (Y/N): ") 

            if continue_req in ['y', 'Y']:
                valid_req = True
            elif continue_req in ['n', 'N', 'q', 'Q']:
                exit(0)
            else:
                print("Not a valid response, please try again.")
                valid_req = False

if __name__ == "__main__":
    main()