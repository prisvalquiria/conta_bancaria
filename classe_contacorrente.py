class ContaCorrente:
    def depositar(valor, saldo):        
        saldo = saldo + valor
        return saldo

    def sacar(valor, saldo):
        if saldo >= valor: 
            saldo = saldo - valor
            print("Saldo atualizado: "+str(saldo))
        else:
            print('Saldo insuficiente') 
        return saldo
