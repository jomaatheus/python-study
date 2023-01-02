jantar=['deborah', 'anna', 'eduarda' ]
sair= 'Oi, '+ jantar[0].title() +"."+' Você gostaria de sair sabado a noite?'
sair1= 'Oi, '+ jantar[1].title() +"."+' Você gostaria de sair sabado a noite?'
sair2= 'Oi, '+ jantar[2].title() +"."+' Você gostaria de sair sabado a noite?'
print(jantar)
print('\n'+ "Lista de quem não poderá comparecer:"+ '\n'+jantar[0])
jantar[0]= 'luiza'
sair3= 'Oi, '+ jantar[0].title() +"."+' Você gostaria de sair sabado a noite?'
sair4= 'Oi, '+ jantar[1].title() +"."+' Você gostaria de sair sabado a noite?'
sair5= 'Oi, '+ jantar[2].title() +"."+' Você gostaria de sair sabado a noite?'
print('\n'+ sair3)
print(sair4)
print(sair5)
mensagem= 'Olá, pessoal. Há mais convites disponiveis.'
print('\n'+ mensagem+'\n')
jantar.insert(0, 'marina')
jantar.insert(2, 'mariana')
jantar.append('giovana')
print(jantar)
convidados_novos='Oi, '+ jantar[0].title() +"."+' Você gostaria de sair sabado a noite?'
convidados_novos2='Oi, '+ jantar[1].title() +"."+' Você gostaria de sair sabado a noite?'
convidados_novos3='Oi, '+ jantar[2].title() +"."+' Você gostaria de sair sabado a noite?'
convidados_novos4='Oi, '+ jantar[3].title() +"."+' Você gostaria de sair sabado a noite?'
convidados_novos5='Oi, '+ jantar[4].title() +"."+' Você gostaria de sair sabado a noite?'
convidados_novos6='Oi, '+ jantar[5].title() +"."+' Você gostaria de sair sabado a noite?'
print('\n'+convidados_novos)
print(convidados_novos2)
print(convidados_novos3)
print(convidados_novos4)
print(convidados_novos5)
print(convidados_novos6)
aviso="Olá, tudo bem? houve um imprevisto, terei que reduzir o numero de convidados a dois."
print('\n'+aviso+'\nAtenção, João Matheus')
desconvidando = jantar.pop()
print( '\nSinto muito, '+desconvidando+'.')
desconvidando = jantar.pop()
print( 'Sinto muito, '+desconvidando+'.')
desconvidando = jantar.pop()
print( 'Sinto muito, '+desconvidando+'.')
desconvidando = jantar.pop()
print( 'Sinto muito, '+desconvidando+'.'+'\n')
del jantar[0]
del jantar[0]
print(jantar)


