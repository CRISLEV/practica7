import threading
import requests
import time

from flask import Flask, jsonify, request

app  = Flask(__name__)

pedidos = []

def testRepartidor():
    return ("Hola, soy el repartidor.")

def start():
    print("Start Restaurant")
    threading.Thread(target=menu).start()

def menu():
    time.sleep(2)
    choice = ''
    while choice != '0':
        print("     Menu de Repartidor: selecciona acción:")
        print("         1. Marcar pedido como entregado.")
        print("         0. Salir.")

        choice = input("    Selecciona una opción: ")

        if choice == "1":
            coped = input("--> Ingresa código de pedido: ")
            print("Marcando pedido como entregado...")
            marcarPedidoComoEntregado(coped)
        else:
            print("No existe la opcion seleccionada.")

def marcarPedidoComoEntregado(coped):
    global pedidos
    payload = {'codigo': coped}
    r = requests.post("http://127.0.0.1:4400/service5EBS", json=payload)
    for p in pedidos:
        if p['idPedido'] == coped:
            p['estado'] = 'ENTREGADO'
    print("***> Se ha entregado el pedido " + coped)
    print(pedidos)

#Services
@app.route('/recibirPedidoRestaurante', methods=['POST'])
def service1():
    global pedidos
    req_data = request.get_json();
    coped = req_data['codigo']
    print("Recibiendo pedido de restaurante...:" + coped)
    pedido = {"idPedido":coped, "estado":"EN CAMINO"}
    pedidos.append(pedido)
    print(pedidos)
    print("******************************\n Recibiendo pedido "+coped+" \n******************************\n")
    return "******************************\n Pedido de tacos recibido: "+coped+"!\n******************************\n"


@app.route('/informarEstadoCli', methods=['POST'])
def service2():
    global pedidos
    req_data = request.get_json();
    coped = req_data['codigo']
    print("Revisando estado de pedido...:"+coped)
    for p in pedidos:
        if p['idPedido'] == coped:
            print("Pedido en estado:"+p['estado'])
            return "******************************\nPedido "+coped+" en estado:"+p['estado']+"\n******************************\n"
    return "No existe pedido"


if __name__ == "__main__":
    app.run(start(),debug=True, port=4200)
