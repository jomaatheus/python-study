cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()  
# Os carros agora estão em ordem alfabética e não podemos mais retornar à ordem original
print(cars)
cars.sort(reverse=True) 
#Também podemos ordenar essa lista em ordem alfabética inversa,
#passando o argumento reverse=True ao método sort().
print(cars)
print("\nHere is the original list:") 
print(cars)
print("\nHere is the sorted list:") 
print(sorted(cars))
#Para preservar a ordem original de uma lista, mas apresentá-la de forma
# ordenada, podemos usar a função sorted().
print(sorted(cars, reverse=True))
#Essa função também pode aceitar um argumento 
# reverse=True se você quiser exibir uma lista em ordem alfabética inversa.
print("\nHere is the original list again:") 
print(cars,'\n')
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
#Para inverter a ordem original de uma lista, podemos usar o método reverse().
#reverse() não reorganiza em ordem alfabética inversa; elesimplesmente inverte a ordem da lista.
print(cars)
#O método reverse() muda a ordem de uma lista de forma permanente, mas podemos restaurar a ordem original a
#qualquer momento aplicando reverse() à mesma lista uma segunda vez.