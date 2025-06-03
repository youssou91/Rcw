import requests
 
url = 'http://localhost:8000/'  # URL correcte de FastAPI
 
response = requests.get(url)
data = response.json()  # Corrigé ici
print(data['message'])  # Affiche le message retourné par FastAPI
 