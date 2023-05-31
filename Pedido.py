from Produto import Produto
class Pedido:
    def __init__(self, id, cliente, produtos):
        self.__id = id
        self.__cliente = cliente
        self.__produtos = produtos