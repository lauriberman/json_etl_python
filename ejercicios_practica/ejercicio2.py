# JSON ETL [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

import json
import requests

import matplotlib.pyplot as plt
from sqlalchemy import true



if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Ejercicio de consumo de datos por API
    url = "https://jsonplaceholder.typicode.com/todos"

    # El primer paso es que copien esa URL en su explorador web
    # y analicen los datos en general:
    # 1) Observando la URL se puede ver que en total hay 200 entradas,
    # del id=1 al id=200
    # 2) Observando la URL se puede ver que en total hay 10 usuarios,
    # del userId=1 al userId=10
    # 3) En cada entrada se especifica si el usuario completó ese título,
    # mediante el campo "completed".


    # Alumno, de cada usuario en el total de las 200 entradas
    # debe contar cuantos títulos completó cada usuario (de los 10 posibles)
    # y armar un gráfico de barras resumiendo la información.
    # gráfico en el eje "x" está cada uno de los 10 usuarios y en el eje
    # "y" la cantidad de títulos completados

    # Para poder ir haciendo esto debe ir almacenando la información
    # de cada usuario a medida que "itera" en un bucle los datos
    # del JSON recolectado. Al finalizar el bucle deberá tener la data
    # de los 10 usuarios con cuantos títulos completó cada uno.

    # Debe poder graficar dicha información en un gráfico de barras.
    # En caso de no poder hacer el gráfico comience por usar print
    # para imprimir cuantos títulos completó cada usuario
    # y verifique si los primeros usuarios (mirando la página a ojo)
    # los datos recolectados son correctos.

    response = requests.get(url)
    data = response.json()

    usuarios = []
    userId_1 = []
    userId_2 = []
    userId_3 = []
    userId_4 = []
    userId_5 = []
    userId_6 = []
    userId_7 = []
    userId_8 = []
    userId_9 = []
    userId_10 = []

    for d in data: 
        if d["completed"] == True:
           usuarios.append(d) 

    for i in usuarios:
        if i['userId'] == 1:
            userId_1.append(i)
        elif i['userId'] == 2:
            userId_2.append(i)
        elif i['userId'] == 3:
            userId_3.append(i)
        elif i['userId'] == 4:
            userId_4.append(i)
        elif i['userId'] == 5:
            userId_5.append(i)
        elif i['userId'] == 6:
            userId_6.append(i)
        elif i['userId'] == 7:
            userId_7.append(i)
        elif i['userId'] == 8:
            userId_8.append(i)
        elif i['userId'] == 9:
            userId_9.append(i)
        elif i['userId'] == 10:
            userId_10.append(i)
    
    print('userId_1:', len(userId_1))
    print('userId_2:', len(userId_2))
    print('userId_3:', len(userId_3))
    print('userId_4:', len(userId_4))
    print('userId_5:', len(userId_5))
    print('userId_6:', len(userId_6))
    print('userId_7:', len(userId_7))
    print('userId_8:', len(userId_8))
    print('userId_9:', len(userId_9))
    print('userId_10:', len(userId_10))

    id_usuarios = ['userId_1', 'userId_2', 'userId_3', 'userId_4', 'userId_5', 'userId_6','userId_7', 'userId_8', 'userId_9', 'userId_10']
    titulos_completados = [11, 8, 7, 6, 12, 6, 9, 11, 8, 12]

    fig = plt.figure()
    fig.suptitle('Titulos completados por usuario', fontsize=15, label='usuarios')
    ax = fig.add_subplot()

    ax.bar(id_usuarios, titulos_completados)
    ax.legend()
    ax.grid()
    plt.show()

        
    print("terminamos")