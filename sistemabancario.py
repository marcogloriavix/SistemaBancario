#Criando um sistema bancário: sacar, depositar,extrato 

# o sistema deve permitir 3 saques diários
# limite máximo 500 reais por saque

# Versão 1 - apenas 1 usuário / sem identificação de conta e banco

menu="""
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""
print (menu)

saldo =0
limite=500
extrato=""
numero_saques=0
LIMITE_SAQUES=2

while True:
    opcao=input(menu)

    if opcao=='d':
        print ("Depósito")
        deposito=float(input("Qual o valor a depositar ? Digite aqui : "))

        if deposito >= 0:
            saldo = deposito + saldo
            extrato += f"Depósito : R$ {deposito:.2f}\n"
            print ("fez o ciclo")

        else:
            print ("Operação falhou: O valor informado é inválido")

                

    elif opcao == 's':
        saque = float(input("Informe o valor do saque: "))

        excedeu_saldo = saque
        excedeu_limite = saque 
        excedeu_saques = numero_saques

        if excedeu_saldo > saldo:
            print("Operação cancelada! Saldo Insuficiente.")
        
        elif excedeu_limite > limite:
            print("Operação Cancelada ! Limite diário excedido")

        elif excedeu_saques > LIMITE_SAQUES:
            print ("Operação cancelada! Numero de Saques excedido")

        elif saque > 0:
            saldo = saldo - saque
            extrato += f"Saque: R$ {saque:.2f} \n"
            numero_saques = numero_saques + 1

        else:
            print ("Operação falhou: O valor informado é inválido")
    
    

    elif opcao == 'e':
        print ("\n************** Extrato ***************")
        print ("Não foram realizados movimentações." if not extrato else extrato)
        print (f"\n Saldo: R$ {saldo:.2f}")
        print ("============================")

        
    elif opcao == 'q':
        break

    else:
        print ("Operação inválida, Selecione uma das 4 opções")
        print ("============================")
        