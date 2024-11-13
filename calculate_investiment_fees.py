print("\n--------------Bem vindo ao calculador de investimento--------------\n")

investimento_mensal = float(input("Quanto deseja investir por mês? R$ ").strip())
taxa_juros_mensal = float(input("Informe a taxa de juros mensal (em %): ").strip()) / 100
ano = 1

saldo_total = 0

while True:
    for mes in range(12):
        saldo_total += investimento_mensal
        saldo_total += saldo_total * taxa_juros_mensal
    
    print(f"\n**Saldo do investimento após {ano} ano(s): R$ {saldo_total:.2f}**\n")
    
    resp = input("Deseja processar mais um ano? (S/N): ").strip().lower()
    if resp != 's':
        break
    
    ano += 1