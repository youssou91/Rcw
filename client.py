import requests
 
url = 'https://apiapp-a0gbffgfedepemby.canadacentral-01.azurewebsites.net'  # URL correcte de FastAPI
 
response = requests.get(url)
data = response.json()  # Corrigé ici
print(data['message'])  # Affiche le message retourné par FastAPI
 