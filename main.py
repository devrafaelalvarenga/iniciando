# Calculo de bonus com entrada do usuario

ano_vigente: int = 2024
valor_base_calculo_bonus: int = 1000
nome_usuario: str = input("Digite seu nome: ").title()
salario_usuario: float = float(input("Digite o valor do seu salario: "))
bonus_usuario: float = float(input("Informe o valor do bonus recebido: "))

calculo_valor_bonus_usuario = valor_base_calculo_bonus + \
    salario_usuario * bonus_usuario

print(f"{nome_usuario} o valor do bonus a receber referente ao ano de {
      ano_vigente} é de R${calculo_valor_bonus_usuario:.2f}")
