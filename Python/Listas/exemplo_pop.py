motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop(0) 
#sempre que usar pop(), o item com o qual você trabalhar não estará mais armazenado na lista.
print("The last motorcycle I owned was a "+ last_owned.title() + ".") 
#quando quiser apagar um item de uma lista e esse item não vai ser usado de modo algum, utilize a instrução del;
#se quiser usar um item à medida que removê-lo, utilize o método pop().