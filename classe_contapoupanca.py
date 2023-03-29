class ContaPoupanca:
    def depositar(valor, saldo):        
        saldo = saldo + valor
        return saldo

    def sacar(valor, saldo):
        if saldo >= valor: 
            saldo = saldo - valor
            print("Saldo poupança atualizado: "+str(saldo))
        else:
            print('Saldo poupança insuficiente') 
        return saldo

    def rendimentos(saldo):
        saldo_1hr = (((saldo * 0.005) / 30) / 2) / 12
        saldo_12hr = ((saldo * 0.005) / 30) / 2
        saldo_dia = (saldo * 0.005) / 30
        saldo_mes = saldo * 0.005
        saldo_ano = saldo_mes * 12
        saldo_24  = saldo_ano * 2

        print("Rendimentos: ")
        print("R$ "+str(saldo_1hr) + ' em 1 hora')
        print("R$ "+str(saldo_12hr) + ' em 12 horas')
        print("R$ "+str(saldo_dia) + ' por dia')
        print("R$ "+str(saldo_mes) + ' por mes')
        print("R$ "+str(saldo_ano) + ' por ano')
        print("R$ "+str(saldo_24) + ' em 2 anos')