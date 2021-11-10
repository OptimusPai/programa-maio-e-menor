familia=('Anderson', 'josiane', 'Vitória',
       'Livia', 'Sônia', 'Ney', 'Neno', 'Cristina',
         'Daiane', 'Tatiane', 'Fabiano',)
print('-='*20)
print(f'lista de familia:{familia} ')
print('-='*15)
print(f'Os 5 primeiros são {familia[0:5]}')
print('-='*20)
print(f'Os 4 ultimos familiares são {familia[-4:]}')
print('-='*20)
print(f'Familia em ordem alfabetica{sorted(familia)}')
print('-=*'*15)
print(f'O neno está na {familia.index("Neno")} posição')

