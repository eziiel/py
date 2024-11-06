# var1, var2 = 'casa', 'cadeira'
# print(var1, var2)

# var3 = var4 = 'casa'
# print(var3, var4)

# desconpactar
# var5 = 'casa', 'jardim', "quintal"
# var6, var7, var8 = var5
# print(var6)
# print(var6, var7, var8)

#concatenação não funciona com números #literal
#teste = "casa"
#teste1 = 1
# print("voce mora na sua", teste ) 
# print("voce mora na sua" + teste) #success
# print("voce mora na sua" + teste1) #Error 

## ex1:
# idade = 25
# nome = "João"
# saldo = 100.50
# soma = (idade + saldo)
# print("a soma é de:", soma)

## ex1:
# nota1 = 7.5
# nota2 = 8.3
# nota3 = 6.9
# media = (nota1 + nota2 + nota3)/3
# # arredondar duas casas decimais
# print("a media é de:", round(media,2)) 
# print("a media2 é de:", format(media,".2f")) 

# nome = input('Qual teu nome?')
# nota = float(input('Qual tua primeira nota?'))
# nota2 = float(input('Qual tua segunda nota?'))
# print(nome, "tua nota é:", (nota + nota2)/2)

## ex3
# numero = int(input("Escreva um número inteiro para vermos a tabuada dele:"))

# for id in range(11):
#   print(f"{numero} * {id} = ", numero * id)

## ex4
# import datetime

# nascimento = int(input('qual ano você nasceu?'))
# anoAtual = int(datetime.datetime.now().year)
# idade = nascimento - anoAtual
# print("Sua idade aproximada é:", idade)

# random
# import random

# print(format(random.randrange(1,100),"5f"))
# print(random.randrange(1,100))
# print(random.random())
# print(random.randint(10, 20))
# print(random.choice(['sofá', 'geladeira', 'mesa', 'rodinho']))
# numeros = [1, 2, 3, 4, 5, 6]
# random.shuffle(numeros)
# print(numeros)

# posicaoLetra = 'o conceito de IA é muito mais amplo do que se imagina'
# print(posicaoLetra[5])
# print(posicaoLetra[1:4])
# print(posicaoLetra[-4])
# print(posicaoLetra[2:])
# print(posicaoLetra[:2])

## ex
## metodos
## str.stripe() # remove espaçamento no início e no final da string
## remove outras coisas
# value = 'UUUUUUUUcasaUUUUU'
# print(value.strip("U"))

## ex
# frase = 'o conceito de IA é muito mais amplo do que se imagina'
# if ('IA' in frase):
#   print('a frase tem a palavra "IA"')
# else:
#   print('a frase NÂO tem a palavra "IA"')

## ex
# inicio = int(input("escreva um numero para começar a soma: "))
# print("Irá parar quando digitar 0")
# total = inicio
# while True: 
#   inicio = int(input("escreva um numero para começar a soma: "))
#   total += inicio
#   if inicio == 0:
#       print(f"A soma total dos números digitados é: {total}")
#       break

## ex
# total = 0
# inicio = int(input("escreva um numero para começar a soma: "))
# while inicio != 0: 
#   total += inicio
#   inicio = int(input("escreva um numero para começar a soma: "))
# print(f"A soma total dos números digitados é: {total}")


## ex
# numero = -1
# numeroEntrada = int(input("Digite um numero inteiro, "))
# while True:
#   numeroEntrada = int(input("Digite um outro numero inteiro"))
#   if numeroEntrada > numero:
#     numero = numeroEntrada
#   if numeroEntrada <= 0:
#     break
# print(f"O maior numero digitado é: {numero}")

## ex
# numero1 = 3
# numero2 = 9
# numero3 = 8
# if numero3 > numero2 or numero1:
#   print(f"{numero3} é maior que {numero1} e {numero2}")

## ex
# nota = float(input("Digite a nota do aluno"))
# if nota > 89 and nota <= 100:
#   print(f'nota: {nota} excelente')
# elif nota > 69 and nota < 90:
#   print(f'nota: {nota} boa')
# elif nota > 49 and nota < 70:
#   print(f'nota: {nota} satisfatório')
# else:
#   print(f'nota: {nota} insuficiente')

## ex
# valorCompra = float(input("Digite o valor de entrada da compra: "))
# if(valorCompra >= 1000):
#   desconto = valorCompra * 0.2
#   print(f"A compra terá valor total de: R${str(valorCompra - desconto)} pois aplicar 20% de desconto")
# elif(valorCompra < 1000 and valorCompra >= 500):
#   desconto = valorCompra * 0.1
#   print(f"A compra terá valor total de: R${str(valorCompra - desconto)} pois aplicar 10% de desconto")
# else:
#   print(f"A compra terá valor total de: R${str(valorCompra)} sem desconto")
  
  ## ex
# print('responda apenas com "sim" ou "não"')
# vip = input("Você tem convite VIP? ")
# convidado = input("Você está na lista de convidados? ")
# membro = input("Você é membro do clube? ")
# if vip == 'sim' and convidado == "sim" and membro == "sim":
#   print("pode entrar!")
# else:
#   print("não pode entrar!")

## ex
# saldo = 0
# while True:
#   opcao = int(input("Caixa eletrônica: \n 1 - Verificar saldo \n 2 - Depositar dinheiro \n 3 - Sacar dinheiro \n 4 - Sair \n Escolha uma opção (1/4): "))
#   if opcao == 1:
#     print(f"\n seu saldo é de R${saldo:.2f}\n")
#   elif opcao == 2:
#     adicionar = float(input("\n Deposite um valor: "))
#     saldo+=adicionar
#   elif opcao == 3:
#     adicionar = float(input("\n Saque um valor: "))
#     total = saldo - adicionar
#     if total < 0:
#       print("\n Saldo insuficiente para o valor solicitado!")
#     else:
#       saldo = total
#   elif opcao == 4:
#     print("\n Até mais 🖐️")
#     break

## ex
# while True:
#   opcao = int(input("Calculadora: \n 1 - Somar \n 2 - Subtrair \n 3 - Multiplicar \n 4 - Dividir \n 5 - Sair \n Escolha uma opção (1/4): "))
#   num1 = float(input("digite o primeiro número: "))
#   num2 = float(input("digite o segundo número: "))
  
#   if(opcao == 1): 
#     print(f"\n {num1} + {num2} é {num1 + num2}")
#   elif(opcao == 2): 
#     print(f"\n {num1} - {num2} é {num1 - num2}")
#   elif(opcao == 3): 
#     print(f"\n {num1} * {num2} é {num1 * num2}")
#   elif(opcao == 4): 
#     if(num2 == 0):
#       print(f"Número não é divisível por 0")
#     else:
#       print(f"\n {num1} ÷ {num2} é {num1 / num2}")
#   elif(opcao == 5): 
#     print("Até mais")
#     break
#   else:
#     print("Opção inválida, tente novamente")


## ex
# print(2 < 4 or not 1 > 2)
# for numero in range(1,10):
#   print(numero)

## ex
# flag = 1
# for numero in range(1, 6):
#   flag*=numero
#   print(flag)

## ex
# rangeNum = int(input("digite um numero inteiro: "))
# print(f"será realizado uma soma de 1 até {rangeNum} apenas para os números pares")
# sumNumPair = 0
# for num in range(rangeNum+1):
#   if num % 2 == 0:
#     sumNumPair+=num
# print(f"o total da soma dos pares é {sumNumPair}")

## ex
# num = int(input("digite o número para validarmos a tabuada: "))
# for n in range(11):
#   print(f"{num} * {n} = {num * n}")

## ex
# n = int(input("digite um número para validar a raiz de todos os menores: "))
# print("os menores serão a partir do numero - 1")
# sum = 0
# for num in range(n+1):
#   sum+= num**2
#   print(f"{num} ** 2 = {num ** 2}")
# print(sum)

## ex
# list = ["a", "b", "c", "d", "e"]
# for letra in list:
#   print(letra)
#   if letra == 'c':
#     break
# # print(len(list))

## ex
# list = ['maça', 'leite', 'caju', 'picole de morango', 'fritadeira']

# for item in list:
#   print(f'preciso comprar {item}')

# # ex
# num = int(input("Digite um número inteiro: "))
# for n in range(num + 1):
#   print(n)

# # ex
# num = int(input("Digite um número inteiro: "))
# for n in range(num):
#   if n % 2 == 0:
#     print(f"{n} é par")
#   else:
#     print(f"{n} é ímpar")

# num = int(input("Digite um número inteiro: "))
# for n in range(num, 0, -1):
#   print(n * "*")

# # ex
# list = ['maça', 'leite', 'caju', 'picole de morango', 'fritadeira']
# for item in list:
#   if len(item) > 4:
#     print(' ', end=item)

# # ex
# for i in range(1, 6):
#   for j in range(1, 6):
#     print(i, '*', j, '=', i * j )

# # ex
# quadrados = [x**2 for x in range(11) if x % 2 != 0]
# print(quadrados)

# list = ["A", "B", "C", "D"]

# index = int(input('digite um número: ')) 

# for i in range(len(list)):
#   if(list[i] == "C"):
#     print(list[i], i)
#     break 

# try:
#   print(list[index])
# except:
#   print('numero não encontrado')

# count = int(input("insira um número: "))

# for i in range(count):
#   if i % 2 == 0:
#     print(f'numero {i} é par')
#   else:
#     print(f'{i} é impar')
