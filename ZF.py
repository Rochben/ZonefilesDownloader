import requests, os, csv, getpass

# Input variables
token = getpass.getpass('Paste your token here: ')
token = token.strip()
list_type = input('Please select the list type (full, update, fulldata, updatedata): ') or 'full'
zone_id = input('Please type in a zone ID: ') or '1'

# File variables
desktop = os.path.normpath(os.path.expanduser("~/Desktop"))
filename = f'Zonefiles_Zone_{zone_id}_{list_type.capitalize()}.csv'
path = f"{desktop}/{filename}"
url = f"https://zonefiles.io/a/{token}/{list_type}/{zone_id}/"

# Writing .csv
response = requests.get(url)
with open(f'{path}', 'wb') as n:
    r = (response)
    n.write(r.content)
