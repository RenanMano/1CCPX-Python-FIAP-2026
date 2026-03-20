from xml.dom.minidom import ReadOnlySequentialNamedNodeMap

print(7 + 4)
print("7 + 4")
print("7" + "4") # CONCATENAÇÃO DE STRINGS

#Comentários de 1 linha
'''
    Comentários de 
    multiplas linhas
'''

# VARIÁVEIS
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
print(nova_idade)