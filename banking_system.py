class ContaBancaria:

    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial
        self.extrato = []

    def deposito(self, valor):

        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")

        else:
           print('Por favor, digite um valor válido.')

    def saque(self, valor):

        if self.saldo >= valor:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
        else:
            print("Operação falhou! Você não tem saldo suficiente.")

    def exibir_extrato(self):

        print("Extrato:")

        for operacao in self.extrato:
            print(operacao)
        print(f'\nSaldo atual R$ {self.saldo:.2f}')

def menu():

    print(
    """

    Opções:
    1. Depositar
    2. Sacar
    3. Exibir Extrato
    0. Sair      
    """
    )


# Função para ler a opção digitada pelo usuário
def ler_opcao():

    while True:

        try:

            opcao = int(input("Digite a opção desejada: "))
            if (opcao >= 0) and (opcao <= 3):
                return opcao
            else:
                print("Opção inválida. Digite novamente.")
        except:
            print("Entrada inválida. Digite novamente.")

# Função principal para executar o menu
def main():

    conta = ContaBancaria(saldo_inicial = 0)

    limite = 500 # Valor máximo para operação de saque
    numero_saques = 0 # Contador do número de saques
    LIMITE_SAQUES = 3 # Número máximo de saques
    
    while True:

        menu()
        opcao = ler_opcao()

        if opcao == 1:
            valor = float(input("Digite o valor: "))
            conta.deposito(valor)

        elif opcao == 2:

            valor = float(input("Digite o valor a sacar: "))
            
            if valor > 0:

                if valor <= limite:
                    if numero_saques <= LIMITE_SAQUES:
                        conta.saque(valor)
                        numero_saques += 1
                    else:
                        print("Limite de saques diários atingido.")
                else:
                    print("Por favor, digite um valor abaixo do limite R$ 500,00.")

            
            else:
                print("Operação falhou! O valor informado é inválido.")
        
        elif opcao == 3:
            conta.exibir_extrato()
        
        elif opcao == 0:
            print("Saindo do programa.")
            break

if __name__ == "__main__":
    main()