'''
TODO Exercicio 3: Faça uma versão básica de uma relção bancario. Onde deve ser possível o depósito de um valor positivo na sua conta bancária. Todos os depósitos
devem ser armazenados em uma variável e exibidos na operação do extrato.
     A segunda parte do exercício é, deve-se permitir realizar 3 saques diários com limite máximo de 500 reais por saque. Caso o usuário não tenha saldo em conta, 
o sistema deve exibir uma mensagem informando que não era possível sacar o dinheiro por falta de saque.Todos os saques devem ser armazenados e exibidos na opera-
ção dos extratos.
    Por fim temos que a operação do extrato deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta
'''
menu = """

<-----------------MENU--------------------->

[0] = Depositar
[1] = Sacar
[2] = Extrato
[3] = Sair

<------------------------------------------>

"""

Saldo = 0
LIMITE = 500
Extrato =""
Numero_saques = 0
LIMITE_SAQUES = 3


print(menu)
while True:
    opcao = int(input("DIGITE SUA OPÇÃO:  "))


    if opcao == 0:
        print("Deposito")
        Entrada = float(input("Digite o valor a ser depositado:  "))
        if Entrada < 0:
            print("Operação inválida!! Valor de entrada negativo")

        else:
            print(f"Operação aceita!! O valor R${Entrada:0.2f} irá ser depositado")
            print()
            Saldo += Entrada
            Extrato += f"\nEntrada:   R${Entrada:0.2f}"
            print(f"Seu saldo é : {Saldo:0.2f}")
            print()

    elif opcao == 1:
         print("Sacar")
         Saida = float(input("Digite o valor a ser sacado:  "))

         if Saida > Saldo:
            print("Operação inválida!! Valor sacado ultrapassa seu Saldo")
            

         elif Saida > LIMITE:
            print("Operação inválida!! Valor sacado ultrapassa seu limite")
            

         elif Saida < 0:
            print("Operação inválida!! Valor a sacar é negativo")
            

         else:
            Numero_saques+=1
            if Numero_saques > 3:
                print("Operação inválida!! Valor sacado ultrapassa seu limite de saques")
                
            else:
                print(f"Operação aceita!! O valor R${Saida:0.2f} irá ser sacado")
                print()
                Saldo-= Saida
                print(Saldo)
                print()
                Extrato += f"\nSaida:   R${Saida:0.2f}"

    elif opcao == 2:
         print("=====================Extrato====================")
         print(Extrato)
         print(f'\n Saldo: R${Saldo:0.2f}')
         print("================================================")

    elif opcao == 3:
         print("Sair")
         break
    else:
         print("Operação inválida !! Selecione novamente uma opção ")
         print()