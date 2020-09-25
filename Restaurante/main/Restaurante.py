import threading
import requests
import time

from flask import Flask, jsonify, request

app  = Flask(__name__)

contPedidos = 1
pedidos = []

def testRestaurante():
    return ("Hola, soy el restaurante.")

def start():
    print("Start Restaurant")
    threading.Thread(target=menu).start()

def menu():
    time.sleep(2)
    choice = ''
    while choice != '0':
        print("     Menu de Restaurante: selecciona acción:")
        print("         1. Avisar a repartidor que el pedido esta listo.")
        print("         0. Salir.")

        choice = input("    Selecciona una opción: ")

        if choice == "1":
            coped = input("--> Ingresa código de pedido: ")
            print("Avisando a repartidor que el pedido esta listo...")
            avisarRepartidorPedidoListo(coped)
        else:
            print("No existe la opcion seleccionada.")


def avisarRepartidorPedidoListo(coped):
    global pedidos
    payload = {'codigo': coped}
    r = requests.post("http://127.0.0.1:4400/service4EBS", json=payload)
    if r.ok:
        for p in pedidos:
            if p['idPedido'] == coped:
                p['estado'] = 'ENVIADO'
    print("***> Se ha enviado el pedido "+coped)
    print(pedidos)

#Services
@app.route('/recibirPedido')
def service1():
    global contPedidos
    global pedidos
    idpedido= "P100" + str(contPedidos)
    pedido = {"idPedido":idpedido, "estado":"RECIBIDO"}
    pedidos.append(pedido)
    print("******************************\n Recibiendo pedido... \n******************************\n")
    contPedidos = contPedidos + 1
    return "******************************\n Pedido de tacos recibido: "+idpedido+"!\n******************************\n"


@app.route('/informarEstadoCli', methods=['POST'])
def service2():
    global pedidos
    req_data = request.get_json();
    coped = req_data['codigo']
    print("Revisando estado de pedido...:"+coped)
    print(pedidos)
    for p in pedidos:
        if p['idPedido'] == coped:
            print("Pedido en estado:"+p['estado'])
            return "******************************\nPedido "+coped+" en estado:"+p['estado']+"\n******************************\n"
    return "No existe pedido"

@app.route('/responseEBSservice4', methods=['POST'])
def responseEBSservice4():
    global pedidos
    req_data = request.get_json();
    coped = req_data['codigo']
    for p in pedidos:
        if p['idPedido'] == coped:
            p['estado'] = 'ENVIADO'
    print("***> Se ha enviado el pedido "+coped)
    print(pedidos)
    return ("ok!")

@app.route('/marcarPedidoComoEntregado', methods=['POST'])
def marcarPedidoComoEntregado():
    global pedidos
    req_data = request.get_json();
    coped = req_data['codigo']
    for p in pedidos:
        if p['idPedido'] == coped:
            p['estado'] = 'ENTREGADO'
    print("***> Se ha entregado el pedido "+coped)
    print(pedidos)
    return ("ok!")

if __name__ == "__main__":
    app.run(start(),debug=True, port=4300)
