from Produto import Produto

class Loja:
    def __init__(self, nome, cnpj, produtos, clientes):
        self.__nome = nome
        self.__cnpj = cnpj
        self.__produtos = produtos
        self.__clientes = clientes

    @property
    def produtos(self):
        return self.__produtos
    
    def registrarProduto(self, produto):
        self.produtos.append(produto)

    def removerProduto(self, id):
        for produto in self.produtos:
            if produto.id == id:
                del self.produtos[id]

    