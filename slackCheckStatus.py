import requests
url = 'https://slack-status.com/api/v2.0.0/'
latest = 'history'


from colorama import init, Fore, Style

init() #

from ast import increment_lineno
res = requests.get(url + latest)

if res.status_code == 200:
  content = res.json()
  for i in content:
    incident_id = i['id']
    incident_title = i['title']
    incident_status = i['status']
    if incident_status == 'resolved':
      print(Fore.GREEN + f'[{incident_id}] - {incident_title} - {incident_status}'+ Style.RESET_ALL )
    else:
      print(Fore.RED + f'[{incident_id}] - {incident_title} - {incident_status}'+ Style.RESET_ALL )
