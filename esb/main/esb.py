import threading
import requests
import time

from flask import Flask, jsonify, request

app  = Flask(__name__)

contPedidos = 1
pedidos = []



def testEsb():
    return ("Hola, soy el esb.")


def start():
    print("Start ESB")


def solicitaPedido():
    r = requests.get("http://127.0.0.1:4300/recibirPedido")
    responseRest = r.text
    #print(responseRest)
    payload = {'response': responseRest}
    requests.post("http://127.0.0.1:4100/responseEBS", json=payload)

def solicitaEstadoRestaurante(coped):
    payload={'codigo':coped}
    r = requests.post("http://127.0.0.1:4300/informarEstadoCli", json=payload)
    responseRest = r.text
    payload = {'response': responseRest}
    requests.post("http://127.0.0.1:4100/responseEBS", json=payload)

def solicitaEstadoRepartidor(coped):
    payload = {'codigo': coped}
    r = requests.post("http://127.0.0.1:4200/informarEstadoCli", json=payload)
    responseRest = r.text
    payload = {'response': responseRest}
    requests.post("http://127.0.0.1:4100/responseEBS", json=payload)

def avisarRepartidorPedidoListo(coped):
    payload = {'codigo': coped}
    r = requests.post("http://127.0.0.1:4200/recibirPedidoRestaurante", json=payload)
    if r.ok:
        requests.post("http://127.0.0.1:4300/responseEBSservice4", json=payload)

def marcarPedidoComoEntregado(coped):
    payload = {'codigo': coped}
    requests.post("http://127.0.0.1:4300/marcarPedidoComoEntregado", json=payload)

#Services
@app.route('/service1EBS')
def service1():
    print("---------------->Solicitando pedido EBS")
    solicitaPedido()
    return "ok!"

@app.route('/service2EBS', methods=['POST'])
def service2():
    print("---------------->Solicitando estado restaurante EBS")
    req_data = request.get_json()
    responseCode = req_data["codigo"]
    solicitaEstadoRestaurante(responseCode)
    return "ok!"

@app.route('/service3EBS', methods=['POST'])
def service3():
    print("---------------->Solicitando estado repartidor EBS")
    req_data = request.get_json()
    responseCode = req_data["codigo"]
    solicitaEstadoRepartidor(responseCode)
    return "ok!"

@app.route('/service4EBS', methods=['POST'])
def service4():
    print("---------------->Avisando a repartidor pedido listo EBS")
    req_data = request.get_json()
    responseCode = req_data["codigo"]
    avisarRepartidorPedidoListo(responseCode)
    return "ok!"

@app.route('/service5EBS', methods=['POST'])
def service5():
    print("---------------->Marcando pedido como entregado EBS")
    req_data = request.get_json()
    responseCode = req_data["codigo"]
    marcarPedidoComoEntregado(responseCode)
    return "ok!"

if __name__ == "__main__":
    app.run(start(),debug=True, port=4400)
