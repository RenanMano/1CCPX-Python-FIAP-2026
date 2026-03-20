'''from xml.dom.minidom import ReadOnlySequentialNamedNodeMap

print(7 + 4)
print("7 + 4")
print("7" + "4") # CONCATENAÇÃO DE STRINGS'''

#Comentários de 1 linha
'''
    Comentários de 
    multiplas linhas
'''

''''# VARIÁVEIS
nome = "Renan" #str
idade = 26 # int
peso = 90.1 # float

print(nome,idade,peso)
print(f"oi, {nome}!!")

# INPUTS - SIMULAÇÃO DE FORMS NO CMD
nome = input("Digite o seu nome: ")
idade = int(input("Digte sua idade: "))

nova_idade = idade + 1
print(nome, idade)
print(nova_idade)'''

def exercicio_01():
    print("----Calcule a área de um círculo com raio 5. Use a fórmula: área=Pi*raio^2.\n(Dica: Você pode usar 3.14159 como valor de Pi.----")
    raio = 5
    pi = 3.14159
    area = pi * (raio ** 2)
    print(f"Se o círculo tem raio igual a {raio}, então sua área sera: {area:.2f}")
def exercicio_02():
    print("----Converta uma temperatura de Fahrenheit para Celsius. A fómula de conversão é: Celsius=(Fahrenheit-32)*5/9----")
    fahrenheit = float(input("Qual a temperatura atual em Fahreheit?"))
    celsius = (fahrenheit-32) * 5/9
    print(f"A temperatura informada {fahrenheit}fº convertida para Celsius é igual a: {celsius:.2f}cº")
def exercicio_03():
    print("----É a mesma coisa do exercicio 02----")
def exercicio_04():
    print("----Você comprou 3 livros por R$25,00 cada e 2 canetas por R$05,00 cada. Calcule o total gasto.----")
    livro = 25
    caneta = 5
    valor_gasto = (3*25) + (2*5)
    print(f"Já que você comprou 03un de livros por R${livro:.2f} e 02un de canetas por R${caneta:.2f}, você terá que pagar um total de: R${valor_gasto:.2f}.")
def exercicio_05():
    print("----Um caro percorreu 150km a uma velocidade média de 60km/h.Quanto tempo (em horas) o carro levou para percorrer essa distância?----")
    distancia = 150
    velocidade = 60
    tempo = distancia / velocidade
    horas = int(tempo)
    minutos = int((tempo - horas) * 60)

    print(f"O carro levou {horas} horas e {minutos} para percorrer a distância.")
def exercicio_06():
    print("---Leia 2 valores A e B, que correspondem a 2 notas de um aluno. A seguir calcule a média aritmética do aluno----")
    nt01 = float(input("Qual a primeira nota?\n"))
    nt02 = float(input("Qual a segunda nota?\n"))
    media = (nt01 + nt02) / 2
    print(f"A média aritmética do aluno é {media:.1f}")
def exercicio_07():
    print("----Leia 2 valores A e B, que correspondem a 2 noas de um aluno.A seguir calcule e informe a média")
exercicio_06()
