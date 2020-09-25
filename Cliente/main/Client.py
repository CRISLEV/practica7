import threading
import requests
import time

from flask import Flask, request

app  = Flask(__name__)

def testClient():
    return ("Hola, soy el ciente.")

def startClient():
    print("Start client");
    t1 = threading.Thread(target=menu)
    t1.start()

def menu():
    choice = ''
    while choice != '0':
        print("     Menu para Cliente: seleccione acción")
        print("         1. Solicitar pedido")
        print("         2. Verificar estado de pedido a Restaurante")
        print("         3. Verificar estado de pedido a Repartidor")
        print("         0. Salir.")

        choice = input("    Selecciona una opción: ")
        if choice == "1":
            print("Solicitando pedido...")
            solicitaPedido()
        elif choice == "2":
            coped = input("--> Ingresa código de pedido: ")
            print("Verificando estado de pedido a Restaurante...")
            solicitaEstadoRestaurante(coped)
        elif choice == "3":
            coped = input("--> Ingresa código de pedido: ")
            print("Verificando estado de pedido a Repartidor...")
            solicitaEstadoRepartidor(coped)
        else:
            print("No existe la opcion seleccionada.")

def solicitaPedido():
    r = requests.get("http://127.0.0.1:4400/service1EBS");
    print(r.text)

def solicitaEstadoRestaurante(coped):
    payload={'codigo':coped}
    r = requests.post("http://127.0.0.1:4400/service2EBS", json=payload);
    print(r.text)

def solicitaEstadoRepartidor(coped):
    payload = {'codigo': coped}
    r = requests.post("http://127.0.0.1:4400/service3EBS", json=payload);
    print(r.text)


#Services
@app.route('/responseEBS', methods=['POST'])
def service1():
    req_data = request.get_json();
    print(req_data["response"])
    return "ok!"

if __name__ == "__main__":
    app.run(startClient(),debug=True, port=4100)
