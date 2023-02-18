''' 
    Programa que calcula o mais realista possivel
    a folha de pagamento de um funcionario 

------------------------------------------------ '''


while (True):
    print('------------------------------------')
    salario = float(input('Entre com o salário Bruto: '))
    descINSS = 0
    
    # valor do Desconto do INSS

    if salario <= 1212.00:
        descINSS = 7.5
        valorDescINSS = salario * descINSS/100
        
    if salario >= 1212.01 and salario <= 2427.35:
        descINSS = 9.0
        valorDescINSS = salario * descINSS/100
        
    if salario >= 2427.36 and salario <= 3641.03:
        descINSS = 12.0
        valorDescINSS = salario * descINSS/100
        
    if salario >= 3641.04 and salario <= 7087.21:
        descINSS = 14.0
        valorDescINSS = salario * descINSS/100
        
    if salario > 7087.22:
        descINS = 'Teto'
        valorDescINSS = 0.0

    # Desconto do IRRF
    
    if salario <= 1903.98:
        descIR = 'Isento'
        valorDescIR = 0.00

    if salario >= 1903.99 and salario <= 2826.65:
        descIR = 7.5
        valorDescIR = salario * descIR/100

    if salario >= 2826.66 and salario <= 3751.05:
        descIR = 15
        valorDescIR = salario * descIR/100

    if salario >= 3751.06 and salario <= 4664.68:
        descIR = 22.5
        valorDescIR = salario * descIR/100

    if salario > 4664.68:
        descIR = 27.5
        valorDescIR = salario * descIR/100

    salarioLiq = salario - valorDescINSS - valorDescIR
    
    print(f'Salario Bruto: R${salario:.2f}')
    print(f'INSS: {descINSS:.1f}% - R${valorDescINSS:.2f}')
    print(f'IRRF: {descIR:.1f}% - R${valorDescIR:.2f}')
    print(f'Salario Liquido: R${salarioLiq:.2f}')

    sair = input('Digite S para sair ou qualquer tecla para continuar... ')
    if sair == 's' or sair == 'S':
        break
