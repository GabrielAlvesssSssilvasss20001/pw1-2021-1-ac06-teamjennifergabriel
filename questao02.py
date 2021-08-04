class Televisao:
     def __init__(self, canal):
           self.ligada = False
           self.canal = canal
     def muda_canal_para_baixo(self):
           self.canal -= 1
     def muda_canal_para_cima(self):
           self.canal += 1

tv = Televisao()
tv.muda_canal_para_cima()
tv.muda_canal_para_cima()
print(tv.canal)
tv.muda_canal_para_baixo()
print(tv.canal)