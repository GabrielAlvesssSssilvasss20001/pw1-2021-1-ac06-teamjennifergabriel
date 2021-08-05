class Televisao:
    def __init__(self):
        self.tamanho = 30
        self.marca = "Sansung"


tv = Televisao()
tv.tamanho = 32
tv.marca = "Sansung"

print("A TV %s tem %d polegadas" % (tv.marca, tv.tamanho))
