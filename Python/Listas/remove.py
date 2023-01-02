motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# Após definir a lista
print(motorcycles)
too_expensive = 'ducati'
# armazenamos o valor 'ducati' em uma variável chamada too_expensive
motorcycles.remove(too_expensive) 
# Então utilizamos essa variável para dizer a Python qual valor deve ser removido da lista 
print(motorcycles)  
print("\nA " + too_expensive.title() + " is too expensive for me.")
# o valor 'ducati' foi removido da lista, mas 
# continua armazenado na variável too_expensive, permitindo exibir uma frase 
# sobre o motivo pelo qual removemos

#O método remove() apaga apenas a primeira ocorrência do valor que você especificar.