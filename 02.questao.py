# Programa: Cadastro de Pessoa
import os
os.system('cls')

# Entrada de dados
nome = input("Digite o nome: ")
sexo = input("Digite o sexo (M/F): ").upper()
estado_civil = input("Digite o estado civil: ").upper()

tempo_casada = None  # inicializa vazio

# Condição: mulher e casada
if sexo == "F" and estado_civil == "CASADA":
    tempo_casada = int(input("Digite o tempo de casada (em anos): "))

# Saída de dados
print("\n==== Dados do Usuário ====")
print("Nome:", nome)
print("Sexo:", sexo)
print("Estado Civil:", estado_civil)

if tempo_casada is not None:
    print("Tempo de casada:", tempo_casada, "anos")
