import requests
from colorama import init, Fore, Style

# Inicializa o colorama para funcionar no Windows/Linux
init() 

url = 'https://slack-status.com/api/v2.0.0/'
endpoint = 'history'

print(f"Consultando status do Slack em: {url + endpoint}...\n")

try:
    res = requests.get(url + endpoint)

    if res.status_code == 200:
        content = res.json()
        for i in content:
            incident_id = i.get('id', 'N/A')
            incident_title = i.get('title', 'Sem Título')
            incident_status = i.get('status', 'Unknown')
            
            # Formatação da saída
            if incident_status == 'resolved':
                print(Fore.GREEN + f'[{incident_id}] - {incident_title} - {incident_status}' + Style.RESET_ALL)
            else:
                print(Fore.RED + f'[{incident_id}] - {incident_title} - {incident_status}' + Style.RESET_ALL)
    else:
        print(Fore.RED + f"Erro na requisição: {res.status_code}" + Style.RESET_ALL)

except Exception as e:
    print(Fore.RED + f"Ocorreu um erro: {e}" + Style.RESET_ALL)