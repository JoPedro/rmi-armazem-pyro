from Pyro5.api import expose, behavior, serve

@expose
@behavior(instance_mode="single") # Instância single-ton do objeto servidor
class Armazem(object):
    def __init__(self):
        self.conteudo = ["Notebook", "TV", "iPhone", "Caixa de som JBL", "Impressora"]

    def listar_conteudo(self):
        return self.conteudo

    def tirar(self, nome, item):
        self.conteudo.remove(item)
        print("{0} retirou {1}.".format(nome, item))

    def guardar(self, nome, item):
        self.conteudo.append(item)
        print("{0} guardou {1}.".format(nome, item))


serve(
    {
        Armazem: "example.armazem"
    },
    host = "localhost", use_ns=True)