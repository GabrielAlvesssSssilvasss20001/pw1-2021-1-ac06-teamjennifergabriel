class Televisao:
     def __init__(self, canal, min = 2, max = 14):
           self.ligada = False
           self.canal = canal
           self.canal_min = min
           self.canal_max = max
     def muda_canal_para_baixo(self):
           self.canal -= 1
     def muda_canal_para_cima(self):
           self.canal += 1

tv = Televisao(3)
tv.muda_canal_para_cima()
tv.muda_canal_para_cima()
print(tv.canal)
tv.muda_canal_para_baixo()
print(tv.canal)