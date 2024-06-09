import requests
import PIL
import json
from newsapi import NewsApiClient
from PIL import Image
import os
import sys
import shutil
import random
import requests
from newsapi import NewsApiClient
from PIL import Image
from io import BytesIO
import os
#token:
# Setze deinen API-Schlüssel hier
import requests
from newsapi import NewsApiClient
from PIL import Image
from io import BytesIO

# Setze deinen API-Schlüssel hier
newsapi = NewsApiClient(api_key='d486a6c7692e47c7b1679de2483c2129')
hugging_face_api_key = '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'

# Hole die neuesten Schlagzeilen von BBC News
headlines = newsapi.get_everything(sources='bbc-news', language='en', sort_by='publishedAt')

# Prüfe, ob Schlagzeilen gefunden wurden
if not headlines.get('articles'):
    print("Keine Artikel gefunden.")
    exit()

# Nehme die erste Schlagzeile
article = headlines.get('articles')[0]
prompt = article.get('description')

# Hugging Face API-Endpunkt für die Bildgenerierung (Stable Diffusion oder anderes Modell)
hf_api_url = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"

# Anfrage an Hugging Face API
headers = {"Authorization": f"Bearer {hugging_face_api_key}"}
response = requests.post(hf_api_url, headers=headers, json={"inputs": prompt})

# Prüfe, ob die Anfrage erfolgreich war
if response.status_code != 200:
    print("Fehler bei der Anfrage an Hugging Face API:", response.status_code)
    print(response.text)
    exit()

# Hole das Bild aus der Antwort
image_data = response.content
image = Image.open(BytesIO(image_data))

# Bestimme den Dateinamen basierend auf der Schlagzeilenbeschreibung
file_name = "{}.jpg".format(prompt.replace(" ", "_")[:50])

# Speichere das Bild
image.save(file_name)

# Öffne und zeige das Bild
image.show()
