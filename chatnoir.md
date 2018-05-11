# Guide (succinct) pour l'utilisation de ChatNoir

## Introduction

ChatNoir est un moteur de recherche sur des collections archivées du Web :

- Les collections [ClueWeb09](https://lemurproject.org/clueweb09/) (1 milliard de pages collectées entre janvier et février 2009) ou [ClueWeb12](https://lemurproject.org/clueweb12/) (750 million de pages web en anglais collectées entre février et mai 2012).
- La collection [Common Crawl](http://commoncrawl.org/) datant de novembre 2015. Common Crawl archive les pages Web depuis 2011.


**Attention: la limite est de 10000 requêtes par jour, merci d'en tenir compte !**

## Obtenir une clef pour l'API

Obtenir une clef API en allant sur le site  [chatnoir](https://www.chatnoir.eu/apikey). Le *passcode* à utiliser sera donné lors du hackathon. Vous recevrez un email avec un lien d'activation; en cliquant sur ce lien, vous arriverez sur une page où un 


## API

La documentation est accessible sur [le site chatnoir.eu](https://www.chatnoir.eu/doc/); en particulier, ce qui vous servira est [l'API de recherche](https://www.chatnoir.eu/doc/api/).

Il est possible de faire les opérations suivantes :

- [recherche de mots-clé](https://www.chatnoir.eu/doc/api/#api-basics)
- [recherche de phrases](https://www.chatnoir.eu/doc/api/#phrase-search)
- [obtenir le contenu d'un document](https://www.chatnoir.eu/doc/api/#retrieving-full-documents)

## Exemple en Python

Avec la librairie Python `requests`, il est facile d'interroger le moteur de recherche ChatNoir :

```python
import requests

data = {
    # La clef d'API que vous avez reçue
    "apikey": "<apikey>",

    # La question
    "query": "vaccine",
    
    # Index à utiliser: 
    # - cc1511 pour la collection Common Crawl, 
    # - cw09 pour ClueWeb 09, 
    # - cw12 pour ClueWeb 12
    "index": ["cc1511"],

    # Page de résultat 
    "from": 0,

    # Nombre de résultats par page
    "size": 10,

    # Donner des explications sur le résultat
    "explain": False,

    # Formattage de la réponse 
    "pretty": True
}

r = requests.post('https://www.chatnoir.eu/api/v1/_search', data)
print(r.text)
```

La réponse donnée sera 

```json
{
  "meta": {
    "query_time": 209,
    "total_results": 2800000,
    "indices": [
      "cc1511"
    ]
  },
  "results": [
    {
      "score": 782.72534,
      "uuid": "27af7f21-a4b9-565e-b467-e4740927f217",
      "index": "cc1511",
      "trec_id": null,
      "target_hostname": "www.vaccines.com",
      "target_uri": "http://www.vaccines.com/polio-ipv-vaccine-information.cfm",
      "page_rank": null,
      "spam_rank": null,
      "title": "Polio <em>Vaccine</em> | IPV <em>Vaccine</em>",
      "snippet": "infected have no symptoms, they can still spread the disease to others.29 Before the polio <em>vaccine</em>, 13,000 to 20,000 cases of polio were reported each year in the United States.30 The US is now polio-free because of vaccination. However, that doesn&#x27;t mean people don&#x27;t need the polio <em>vaccine</em>. Polio is",
      "explanation": null
    },
    ...
]
}
    ```