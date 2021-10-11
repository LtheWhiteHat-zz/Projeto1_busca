import skfuzzy as fuzz
import numpy as np
from skfuzzy import control as ctrl
from time import sleep
# Do this (new version)
from numpy.random import default_rng

qualidade = ctrl.Antecedent(np.arange(0,11, 1),'qualidade')
servico = ctrl.Antecedent(np.arange(0,11, 1),'servico')
gorgeta = ctrl.Consequent(np.arange(0,21,1), 'gorgeta')

print(qualidade, '\n', servico, '\n', gorgeta)
gorgeta.universe

qualidade.automf(number=3, names=["ruim","medio", "bom"])
servico.automf(number=3, names=["ruim","medio","bom"])

gorgeta['baixa'] = fuzz.trimf(gorgeta.universe, [0,0,8])
gorgeta['media'] = fuzz.trimf(gorgeta.universe, [2,10,10])
gorgeta['alta'] = fuzz.trimf(gorgeta.universe, [12,20,20])

regra1 = ctrl.Rule(qualidade['ruim'] | servico["ruim"], gorgeta['baixa'])
regra2 = ctrl.Rule( servico["medio"], gorgeta['media'])
regra3 = ctrl.Rule(qualidade['bom'] | servico["bom"], gorgeta['baixa'])
rng = np.random.default_rng(12345)

rints = rng.integers(low=0, high=10, size=10)
rints2 = rng.integers(low=0, high=10, size=10)


for i in range(10):
    sistema_controle = ctrl.ControlSystem([regra1, regra2, regra3])
    sistema = ctrl.ControlSystemSimulation(sistema_controle)
    print(rints[i], rints2[i])
    sistema.input['qualidade'] = rints[i]
    sistema.input['servico'] = rints2[i]
    sistema.compute()
    #sistema.input['qualidade'] = np.random.rand(0,10)
    print(sistema.output['gorgeta'])
