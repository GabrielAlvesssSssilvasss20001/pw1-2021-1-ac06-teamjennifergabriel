class State: 
    def __init__(self, name, initials):
        self.name = name
        self.initials = initials
        self.citys = []

    def add_citys(self, city):
        city.state = self
        self.citys.append(city)

    def population(self):
        return sum([c.population for c in self.citys])

class City:
    def __init__(self,name, population):
        self.name = name
        self.population = population
        self.state = None

    def __str__(self):
        return "Cidade (nome = {}, População={}, Estado = {})".format(self.name, self.population, self.state)

ce = State('Ceará', 'CE')
ce.add_citys(City('Mauriti',48168))
ce.add_citys(City('Juazeiro do Norte', 276264))
ce.add_citys(City('Fortaleza', 210711))

pe = State('Pernambuco', 'PE')
pe.add_citys(City('Petrolina', 354317))
pe.add_citys(City('Recife', 1555000))
pe.add_citys(City('Olinda', 393115))

pb = State('Paraíba', 'PB')
pb.add_citys(City('Cajazeiras', 62289))
pb.add_citys(City('João Pessoa', 817511))
pb.add_citys(City('Campina Grande', 402912))

for state in [ce, pe, pb]:
    print('Estado:{}- {}'.format(state.name,state.initials))
    for city in state.citys:
        print('Cidade: {} População: {}'.format(city.name, city.population))
    print('População total do estado: {}\n'.format(state.population()))