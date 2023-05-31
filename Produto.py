class Produto:
    def __init__(self, nome, descricao, preco, categoria, estoque):
        self.__nome = nome
        self.__descricao = descricao
        self.__preco = preco
        self.__categoria = categoria
        self.__quantidadeCarrinho = 0
        self.__estoque = estoque

    @property
    def preco(self):
        return self.__preco

    @property
    def quantidadeCarrinho(self):
        return self.__quantidadeCarrinho
    
    def subTotal(self):
        return self.preco * self.quantidadeCarrinho	

    def atualizarCarrinho(self,quantidade):
        self.quantidadeCarrinho = quantidade
        