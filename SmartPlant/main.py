import urequests

# Définir l'URL de l'API
api_url = "http://adresse-de-votre-api/humidity"

# Valeur d'humidité à envoyer
humidity = 42

# Envoyer une requête POST à l'API avec la valeur d'humidité
response = urequests.post(api_url, json={"humidity": humidity})

# Afficher la réponse de l'API
print(response.json())
