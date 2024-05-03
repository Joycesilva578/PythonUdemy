"""
operacao ternaria (condicional de uma linha)
(valor) if  -condicao> else (outro valor)

if e else na mesma linha
"""

condicao = 10 == 19
variavel = 'Valor' if condicao else 'Outro valor'

digito = 8
##novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito > 9 else digito
print(novo_digito)