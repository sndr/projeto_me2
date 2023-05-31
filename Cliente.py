class Cliente:
    def __init__(self, nome, cpf, dataDeNascimento, endereco, email, senha):
        self.__nome = nome
        self.__cpf = cpf
        self.__dataDeNascimento = dataDeNascimento
        self.__endereco = endereco
        self.__email = email
        self.__senha = senha

    @property
    def email(self):
        return self.__email

    @property
    def senha(self):
        return self.__email
    
    