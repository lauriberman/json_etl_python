# JSON ETL [Python]
# Ejercicio de profundización 

# Autor: Laura Berman

import json
import requests
import matplotlib.pyplot as plt




url = 'https://api.mercadolibre.com/sites/MLA/search?category=MLA1459&q=Departamentos%20Alquilers%20Mendoza%20&limit=50'

    

def fetch():

    response = requests.get(url)
    json_response = response.json()
    dataset = json_response["results"]

    lista_filtrada = [{"price": x["price"], "condition": x["condition"]} for x in dataset if x["currency_id"] == "ARS"]
    print(json.dumps(lista_filtrada, indent=4))
    return lista_filtrada
    


def transform(dataset, min, max):
    
    lista_min = [x["price"] for x in dataset if x["price"] < min]
    lista_intermedia = [x["price"] for x in dataset if min < x["price"] < max]
    lista_max = [x["price"] for x in dataset if x["price"] > max]

    print(json.dumps(lista_min, indent=4))
    print(json.dumps(lista_intermedia, indent=4))
    print(json.dumps(lista_max, indent=4))

    lista_count = [len(lista_min), len(lista_intermedia), len(lista_max)]
    print(lista_count)
    return lista_count

def report(data):

    labels = ["Precios abajo del min", "Precios intermedios", "Precios arriba del max"]
    plt.pie(data, labels=labels, autopct="%0.1f %%")
    plt.axis("equal")
    plt.title("Repartición de precios en alquiler")
    plt.show


if __name__ == '__main__':

    min = int(input('Seleccione un precio mínimo:'))
    max = int(input('Seleccione un precio máximo:'))

    dataset = fetch()
    data = transform(dataset, min, max)
    report(data)


        
