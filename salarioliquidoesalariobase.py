'Programa para calcular salario liquido e salario base + cesta básica
ht=float(input("Digite as horas trabalhadas:"))
vh=float(input("Digite o valor hora:"))
pd=float(input("Digite o porcentual de descontos:"))
sb=ht*vh
td=(pd/100)*sb
sl=sb-td
#a cesta básica está demonstrada abaixo como 120
print("O salario base + cesta básica é de %5.2f" % (sb+120))
print("O salario liquido é de %3.2f" % sl)

