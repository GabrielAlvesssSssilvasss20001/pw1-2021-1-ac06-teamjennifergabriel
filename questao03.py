class Televisão:
    def __init__(self, min, max):
        self.ligada = False
        self.canal = min
        self.cal_min = min
        self.cal_max = max

    def muda_canal_para_baixo(self):
        if self.canal-1 >= self.cal_min:
            self.canal -= 1
        else:
            self.canal = self.cal_max

    def muda_canal_para_cima(self):
        if self.canal+1 <= self.cal_max:
            self.canal += 1
        else:
            self.canal = self.cal_min


tv = Televisão(2, 10)
tv.muda_canal_para_baixo()
print(tv.canal)
tv.muda_canal_para_cima()
print(tv.canal)
