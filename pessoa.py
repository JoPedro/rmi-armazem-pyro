class Pessoa(object):
    def __init__(self, nome):
        self.nome = nome

    def visitar(self, armazem):
        print("Aqui é {0}.".format(self.nome))
        self.depositar(armazem)
        self.retirar(armazem)
        print("Obrigado, volte sempre!")

    def depositar(self, armazem):
        print("O armazém contém:", armazem.listar_conteudo())
        item = input("Insira o que você quer depositar (ou não insira nada): ").strip()
        if item:
            armazem.guardar(self.nome, item)

    def retirar(self, armazem):
        print("O armazém contém:", armazem.listar_conteudo())
        item = input("Insira o que você quer retirar (ou não insira nada): ").strip()
        if item:
            armazem.tirar(self.nome, item)