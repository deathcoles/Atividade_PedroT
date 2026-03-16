contato = {
    'nome': 'Pedro',
    'telefone': 3298144390,
    'email': 'pedrotdefreitas2@gmail.com',
    'cidade':'Tocantins-MG'
}
'''
#a)
l = list(contato.items())
print(l)
'''
'''
#b)
contato['instagram'] = '@pedro_teixf'
print(contato)
'''
'''
#c)
del contato['telefone']
print(contato)
'''
'''
#d)
if 'email' in contato:
    print('Chave existe!')
else:
    print('Chave não existe!')
'''