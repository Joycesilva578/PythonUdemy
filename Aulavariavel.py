nome = 'joyce'
idade = 22
altura = 1.63
maior_de_idade = idade > 18
peso = 52
imc = peso/altura ** 2


print('nome:',nome)
print('idade:',idade)
print('altura:',altura)
print('maior_de_idade:', maior_de_idade)
print('peso:',peso)

print(nome,'tem',idade, 'anos', altura,'metros',peso,'kilos','e',{imc:.2f},'de massa muscular')
