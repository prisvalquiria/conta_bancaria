import classe_contacorrente
import classe_contapoupanca

class Conta:
    def __init__(self, titular, balance, poup):
        self.saldo = balance
        self.saldo_poupanca = poup
        self.nome = titular

nome = input("Digite seu nome: ")


# instanciando classe conta

conta_usuario = Conta(nome, 2400, 3000)

print("Seu nome é: "+ conta_usuario.nome)
print("Seu saldo é: "+ str(conta_usuario.saldo))
print("Seu saldo da poupanca é: "+ str(conta_usuario.saldo_poupanca))

def menu_poupanca():
    opcao = input("Digite a opção desejada: 1. Sacar | 2. Depositar | 3. Saldo e Rendimentos | 4. Sair: ")
    if opcao == "1":
        valor_sacar = input("Digite o valor que deseja sacar: ")
        conta_usuario.saldo = classe_contapoupanca.ContaPoupanca.sacar(int(valor_sacar), conta_usuario.saldo_poupanca)
        menu_poupanca()
    if opcao == "2":
        valor_depositar = input("Digite o valor que deseja depositar: ")
        conta_usuario.saldo = classe_contapoupanca.ContaPoupanca.depositar(int(valor_depositar), conta_usuario.saldo_poupanca)
        print("Saldo atualizado: "+str(conta_usuario.saldo_poupanca))
        menu_poupanca()
    if opcao == "3":
        print("Seu saldo é: "+str(conta_usuario.saldo_poupanca))
        classe_contapoupanca.ContaPoupanca.rendimentos(conta_usuario.saldo_poupanca)
        menu_poupanca()
    if opcao == '4':
        exit

def menu_corrente():
    opcao = input("Digite a opção desejada: 1. Sacar | 2. Depositar | 3. Saldo | 4. Sair: ")
    if opcao == "1":
        valor_sacar = input("Digite o valor que deseja sacar: ")
        conta_usuario.saldo = classe_contacorrente.ContaCorrente.sacar(int(valor_sacar), conta_usuario.saldo)
        menu_corrente()
    if opcao == "2":
        valor_depositar = input("Digite o valor que deseja depositar: ")
        conta_usuario.saldo = classe_contacorrente.ContaCorrente.depositar(int(valor_depositar), conta_usuario.saldo)
        print("Saldo atualizado: "+str(conta_usuario.saldo))
        menu_corrente()
    if opcao == "3":
        print("Saldo atualizado: "+str(conta_usuario.saldo))
        menu_corrente()
    if opcao == '4':
        exit

selecione = input("Digite a opção desejada: 1. Conta Corrente | 2. Conta Poupança : ")
if selecione == "1":
    menu_corrente()
elif selecione == "2":
    menu_poupanca()




