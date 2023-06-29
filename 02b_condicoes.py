# Lista de exercícios - Condições (Adicional)


from numpy import indices


def situacao_aluno(nota1, nota2, nota3, faltas, aulas_ministradas):
    """
    A média do aluno é dada pela média aritmética simples entre as 3 notas.
    Se o aluno tiver mais de 25% de faltas, está automaticamente reprovado por faltas (RF).
    Se ele tiver média abaixo de 7.0, está em Exame Final (EF)
    Se tiver média acima de 7.0 e frequencia igual ou superior a 75% está aprovado (AP).

    Args:
        nota1 (float): 1a nota
        nota2 (float): 2a nota
        nota3 (float): 3a nota
        faltas (int): número de faltas
        aulas_ministradas (int): quantidade de aulas ministradas

    Returns:
        string: a situação do aluno
    """

    percentual_faltas = faltas / aulas_ministradas * 100
    media = (nota1 + nota2 + nota3) / 3

    if percentual_faltas > 25:
        return "RF"
    elif media < 7:
        return "EF"
    else:
        return "AP"


def aumento_preco(preco):
    """
    Calcula o aumento do preço, baseado no seguinte critério:
    - até 280 (inclusive): aumento de 20%
    - até 700 (inclusive): aumento de 15%
    - até 1500 (inclusive): aumento de 10%
    - acima de 1500: aumento de 5%

    Argumentos:
        preco (float): o preço atual do produto

    Retorna:
        tupla de floats: preco atual, percentual de aumento, valor do aumento e
                            novo preço, todos com duas casas decimais.
    """
    if preco <= 280:
        percentual = 20
    elif preco <= 700:
        percentual = 15
    elif preco <= 1500:
        percentual = 10
    else:
        percentual = 5

    valor_aumento = preco * (percentual / 100)
    novo_preco = preco + valor_aumento
    return preco, percentual, valor_aumento, novo_preco


def idade_canina(idade_humana, porte_do_cao):
    """
    É sabido que os caẽs amadurecem mais rapidamente do que os seres
        humanos (na verdade, alguns serem humanos parecem nunca amadurecer).
    Calcule sua idade canina, baseada nos seguintes fatores:
    - cães de porte pequeno: fator 5;
    - cães de porte médio: fator 6;
    - cães grandes: fator 7.

    Argumentos:
        idade_humana (int): a idade do ser humano
        porte_do_cao (string): um texto informando o porte do cão (veja os testes para detalhes)

    Retorna:
        int: a idade canina do ser humano
    """
    fator = {"pequeno": 5, "medio": 6, "grande": 7}
    return int(idade_humana / fator[porte_do_cao])

    # if porte_do_cao == "pequeno":
    #     fator = 5
    # elif porte_do_cao == "medio":
    #     fator = 6
    # else:
    #     fator = 7

    # return int(idade_humana / fator)


def aumento_salario(salario):
    """
    Calcule o aumento de salário de acordo com a seguinte tabela:
    - até 1 SM(inclusive): aumento de 20%
    - de 1 até 2 SM(inclusive): aumento de 15%
    - de 2 até 5 SM(inclusive): aumento de 10%
    - acima de 5 SM: aumento de 5%

    Salário mínimo para referência: R$ 724,00

    Argumentos:
        salario (float): o salario atual

    Retorna:
        float: novo salário, com duas casas decimais.
    """
    sm = 724
    if salario <= sm:
        percentual = 20
    elif salario <= sm * 2:
        percentual = 15
    elif salario <= sm * 5:
        percentual = 10
    else:
        percentual = 5

    aumento = salario * (percentual / 100)
    novo_salario = salario + aumento

    return round(novo_salario, 2)


def nota_para_conceito(nota):
    """
    Converta a nota para conceito, conforme a tabela abaixo:
    Nota                     Conceito
    Entre 10.0 e 9.0            A
    Entre 8.9 e 8.0             B
    Entre 7.9 e 7.0             C
    Entre 6.9 e 6.0             D
    Entre 5.9 e zero            E

    Argumento:
        nota(float): a nota, com 1 casa decimal

    Retorna:
        string: o conceito correspondente
    """
    if nota >= 9.0:
        conceito = "A"
    elif nota >= 8.0:
        conceito = "B"
    elif nota >= 7.0:
        conceito = "C"
    elif nota >= 6.0:
        conceito = "D"
    else:
        conceito = "E"

    return conceito


def imc(peso, altura):
    """
    Escreva uma função que calcula o índice de massa corporal (imc = peso / altura ** 2),
    de acordo com a seguinte tabela:

    imc <= 18.5: "Subpeso"
    imc <= 25.0: "Normal"
    imc <= 30.0: "Sobrepeso"
    imc > 30: "Obeso"


    Argumentos:
        peso (float): peso em Kg
        altura (float): altura em metros

    Retorna:
        string: índice de massa corporal
    """
    indice = peso / (altura ** 2)

    if indice <= 18.5:
        resultado = "Subpeso"
    elif indice <= 25.0:
        resultado = "Normal"
    elif indice <= 30.0:
        resultado = "Sobrepeso"
    else:
        resultado = "Obeso"

    return resultado


def converte_hora_24_para_12(horario):
    """
    Recebe um horário no formato 24 horas e retorna no formato 12 horas (am/pm).
    - am: antes do meio-dia
    - pm: depois do meio-dia

    Para detalhes. consulte: https://pt.wikihow.com/Converter-o-Hor%C3%A1rio-do-Formato-24h-Para-12h

    Argumento:
        horario (string): um horário no formato 24 horas

    Retorna:
        string: horario no formato 12 horas (am/pm)
    """
    hora, minuto = horario.split(":")
    hora = int(hora)

    if hora == 0:
        return f"12:{minuto} am"
    elif hora < 12:
        return f"{hora}:{minuto} am"
    elif hora == 12:
        return f"{hora}:{minuto} pm"
    else:
        return f"{hora - 12}:{minuto} pm"


def converte_hora_12_para_24(horario):
    """
    Recebe um horário no formato 12 horas (am/pm) e retorna no formato 24 horas.
    - am: antes do meio-dia
    - pm: depois do meio-dia

    Para detalhes. consulte: https://pt.wikihow.com/Converter-o-Hor%C3%A1rio-do-Formato-24h-Para-12h

    Argumento:
        horario (string): um horário no formato 12 horas (am/pm)

    Retorna:
        string: horario no formato 24 horas
    """
    horario, periodo = horario.split(" ")
    hora, minuto = horario.split(":")
    hora = int(hora)

    if periodo == "am":
        if hora == 12:
            return f"00:{minuto}"
        elif hora < 10:
            return f"0{hora}:{minuto}"
        else:
            return f"{hora}:{minuto}"
    else:  # periodo == "pm"
        if hora == 12:
            return f"{hora}:{minuto}"
        else:
            return f"{hora + 12}:{minuto}"


def conta_combustivel(qtde_litros, tipo_combustivel, tipo_pagamento):
    """
    O posto Tabajara está vendendo combustíveis com a seguinte tabela de preços:
        a. Tabela de preços
            Álcool: R$ 3,159
            Gasolina: R$ 3,739
            Diesel: 3,090
        b. Se o pagamento for feito à vista ou débito, o cliente recebe um desconto de 10% sobre o valor total
        c. Escreva um função que leia o número de litros vendidos, o tipo de combustível (gasolina, álcool, diesel),
            e o tipo de pagamento (à vista, débito, crédito), calcule e devolva o valor total da compra.


    Args:
        qtde_litros (float): quantidade de litros vendida
        tipo_combustivel (string): uma letra indicando o tipo de combustível
        tipo_pagamento (string): uma letra, indicando o tipo de pagamento

    Returns:
        float: o valor a ser pago, com duas casas decimais
    """

    if tipo_combustivel == "a":
        preco_litro = 3.159
    elif tipo_combustivel == "g":
        preco_litro = 3.739
    elif tipo_combustivel == "d":
        preco_litro = 3.090

    preco_total = qtde_litros * preco_litro

    if tipo_pagamento in ["v", "d"]:
        preco_total *= 0.9

    return round(preco_total, 2)


def comprar_frutas(qtde_morango=0, qtde_uva=0):
    """
    Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                          Até 5 Kg           Acima de 5 Kg
    Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
    Uva             R$ 1,80 por Kg          R$ 1,50 por Kg

    Se o cliente comprar mais de 8 Kg em frutas ou o valor total da
    compra ultrapassar R$ 25,00, receberá ainda um desconto de 10%
    sobre este total.
    Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a
    quantidade (em Kg) de uvas adquiridas e escreva o valor a ser
    pago pelo cliente.

    Argumentos:
        morango (float): a quantidade de morangos, em Kg
        uva (float): a quantidade de uvas, em Kg

    Retorna:
        float: o preço a pagar, com 2 casas decimais
    """
    peso_limite_para_desconto = 5
    preco_morango_ate_limite = 2.50
    preco_morango_acima_limite = 2.20
    preco_uva_ate_limite = 1.80
    preco_uva_acima_limite = 1.50
    preco_para_desconto = 25
    qtde_para_desconto = 8
    percentual_desconto = 0.9

    if qtde_morango > peso_limite_para_desconto:
        preco_morango = preco_morango_acima_limite
    else:
        preco_morango = preco_morango_ate_limite

    if qtde_uva > peso_limite_para_desconto:
        preco_uva = preco_uva_acima_limite
    else:
        preco_uva = preco_uva_ate_limite

    preco_total = preco_morango * qtde_morango + preco_uva * qtde_uva

    if (
        preco_total > preco_para_desconto
        or (qtde_morango + qtde_uva) > qtde_para_desconto
    ):
        preco_total *= percentual_desconto

    return round(preco_total, 2)


# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0


def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = f"\033[31m{'Falhou'}"
    else:
        prefixo = f"\033[32m{'Passou'}"
        acertos += 1
    print(f"{prefixo} Esperado: {esperado} \tObtido: {obtido}\033[1;m")


def main():
    print("Situacao aluno:")
    test(situacao_aluno(10, 10, 10, 18, 72), "AP")
    test(situacao_aluno(7, 7, 7, 18, 72), "AP")
    test(situacao_aluno(6, 7, 8, 18, 72), "AP")
    test(situacao_aluno(7, 7, 6, 18, 72), "EF")
    test(situacao_aluno(7, 7, 6.9, 18, 72), "EF")
    test(situacao_aluno(5, 7, 7, 18, 72), "EF")
    test(situacao_aluno(10, 10, 10, 19, 72), "RF")
    test(situacao_aluno(10, 10, 10, 20, 72), "RF")
    test(situacao_aluno(0, 0, 0, 30, 72), "RF")

    print("Aumento preço:")
    test(aumento_preco(100), (100, 20, 20.0, 120.0))
    test(aumento_preco(1500), (1500, 10, 150.0, 1650.0))
    test(aumento_preco(3000), (3000, 5, 150.0, 3150.0))

    print("Idade canina:")
    test(idade_canina(40, "pequeno"), 8)
    test(idade_canina(40, "medio"), 6)
    test(idade_canina(40, "grande"), 5)

    print("Aumento salarial:")
    # até 1 SM: 20%
    test(aumento_salario(500.00), 600.00)
    test(aumento_salario(724.00), 868.80)
    # 1-2 SM: 15%
    test(aumento_salario(725.00), 833.75)
    test(aumento_salario(1448.00), 1665.20)
    # 2-5 SM: 10%
    test(aumento_salario(1449.00), 1593.90)
    test(aumento_salario(3620.00), 3982.00)
    # >5 SM: 5%
    test(aumento_salario(3621.00), 3802.05)
    test(aumento_salario(4000.00), 4200.00)

    print("Nota para conceito:")
    test(nota_para_conceito(10.0), "A")
    test(nota_para_conceito(9.1), "A")
    test(nota_para_conceito(9.0), "A")
    test(nota_para_conceito(8.9), "B")
    test(nota_para_conceito(8.1), "B")
    test(nota_para_conceito(8.0), "B")
    test(nota_para_conceito(7.9), "C")
    test(nota_para_conceito(7.1), "C")
    test(nota_para_conceito(7.0), "C")
    test(nota_para_conceito(6.9), "D")
    test(nota_para_conceito(6.1), "D")
    test(nota_para_conceito(6.0), "D")
    test(nota_para_conceito(5.9), "E")
    test(nota_para_conceito(5.1), "E")
    test(nota_para_conceito(5.0), "E")
    test(nota_para_conceito(4.9), "E")
    test(nota_para_conceito(4.0), "E")

    print("IMC")
    test(imc(50, 1.80), "Subpeso")
    test(imc(80, 1.80), "Normal")
    test(imc(90, 1.80), "Sobrepeso")
    test(imc(110, 1.80), "Obeso")
    test(imc(50, 1.50), "Normal")

    print("Converte hora 24 para 12:")
    # 1- Adicione 12 à meia-noite e finalize com “am”.
    test(converte_hora_24_para_12("00:00"), "12:00 am")
    test(converte_hora_24_para_12("00:01"), "12:01 am")
    test(converte_hora_24_para_12("00:59"), "12:59 am")

    # 2- Coloque "am" nos horários entre “1:00” e “11:59”.
    # Retire o zero à esquerda.
    test(converte_hora_24_para_12("01:00"), "1:00 am")
    test(converte_hora_24_para_12("01:01"), "1:01 am")
    test(converte_hora_24_para_12("11:00"), "11:00 am")
    test(converte_hora_24_para_12("11:59"), "11:59 am")

    # Adicione “pm” ao intervalo entre “12:00” e “12:59”.
    test(converte_hora_24_para_12("12:00"), "12:00 pm")
    test(converte_hora_24_para_12("12:01"), "12:01 pm")
    test(converte_hora_24_para_12("12:59"), "12:59 pm")

    # Subtraia 12 dos horários entre “13:00” e “23:59” e finalize com “pm”.
    # Não acrescente zeros à esquerda.
    test(converte_hora_24_para_12("13:00"), "1:00 pm")
    test(converte_hora_24_para_12("13:01"), "1:01 pm")
    test(converte_hora_24_para_12("23:00"), "11:00 pm")
    test(converte_hora_24_para_12("23:59"), "11:59 pm")

    print("Converte hora 12 para 24:")
    # 1- Use “00:00” para representar a meia-noite.
    test(converte_hora_12_para_24("12:00 am"), "00:00")
    test(converte_hora_12_para_24("12:01 am"), "00:01")
    test(converte_hora_12_para_24("12:59 am"), "00:59")

    # 2- Apague o “am” das horas entre "1:00 am" e "11:59 am".
    # Acrescente um zero à esquerda se a hora for de um dígito apenas.
    test(converte_hora_12_para_24("1:00 am"), "01:00")
    test(converte_hora_12_para_24("1:01 am"), "01:01")
    test(converte_hora_12_para_24("9:01 am"), "09:01")
    test(converte_hora_12_para_24("11:00 am"), "11:00")
    test(converte_hora_12_para_24("11:59 am"), "11:59")

    # 3- Deixe o horário do meio-dia igual e simplesmente remova o “pm”.
    test(converte_hora_12_para_24("12:00 pm"), "12:00")
    test(converte_hora_12_para_24("12:01 pm"), "12:01")
    test(converte_hora_12_para_24("12:59 pm"), "12:59")

    # 4- Some 12 horas ao período entre "1:00 pm" e "11:59 pm" e apague o “pm”.
    test(converte_hora_12_para_24("1:00 pm"), "13:00")
    test(converte_hora_12_para_24("1:01 pm"), "13:01")
    test(converte_hora_12_para_24("11:00 pm"), "23:00")
    test(converte_hora_12_para_24("11:59 pm"), "23:59")

    print("Conta combustível:")
    test(conta_combustivel(1, "a", "c"), 3.16)
    test(conta_combustivel(10, "a", "c"), 31.59)
    test(conta_combustivel(1, "g", "c"), 3.74)
    test(conta_combustivel(10, "g", "c"), 37.39)
    test(conta_combustivel(1, "d", "c"), 3.09)
    test(conta_combustivel(10, "d", "c"), 30.90)
    test(conta_combustivel(1, "a", "d"), 2.84)
    test(conta_combustivel(10, "a", "d"), 28.43)
    test(conta_combustivel(1, "g", "d"), 3.37)
    test(conta_combustivel(10, "g", "d"), 33.65)
    test(conta_combustivel(1, "d", "d"), 2.78)
    test(conta_combustivel(10, "d", "d"), 27.81)
    test(conta_combustivel(10, "a", "v"), 28.43)
    test(conta_combustivel(10, "g", "v"), 33.65)
    test(conta_combustivel(10, "d", "v"), 27.81)

    print("Comprar frutas:")
    # Teste de zeros:
    test(comprar_frutas(), 0)
    test(comprar_frutas(qtde_morango=0), 0)
    test(comprar_frutas(qtde_uva=0), 0)
    test(comprar_frutas(qtde_morango=0, qtde_uva=0), 0)
    test(comprar_frutas(qtde_uva=0, qtde_morango=0), 0)
    test(comprar_frutas(qtde_morango=0), 0)

    # Testes só com morango:
    test(comprar_frutas(qtde_morango=1, qtde_uva=0), 2.50)
    test(comprar_frutas(qtde_morango=2, qtde_uva=0), 5.00)
    test(comprar_frutas(qtde_morango=4, qtde_uva=0), 10.00)
    test(comprar_frutas(qtde_morango=5, qtde_uva=0), 12.50)
    # Testes só com morangos, muda a faixa:
    test(comprar_frutas(qtde_morango=6, qtde_uva=0), 13.20)
    test(comprar_frutas(qtde_morango=5.1, qtde_uva=0), 11.22)
    test(comprar_frutas(qtde_morango=8, qtde_uva=0), 17.60)
    # Testes só com morangos, recebe desconto por peso:
    test(comprar_frutas(qtde_morango=9, qtde_uva=0), 17.82)
    test(comprar_frutas(qtde_morango=10, qtde_uva=0), 19.80)
    # Testes só com morangos, recebe desconto por preço:
    test(comprar_frutas(qtde_morango=20, qtde_uva=0), 39.60)

    # Testes só com uva:
    test(comprar_frutas(qtde_morango=0, qtde_uva=1), 1.80)
    test(comprar_frutas(qtde_morango=0, qtde_uva=2), 3.60)
    test(comprar_frutas(qtde_morango=0, qtde_uva=4), 7.20)
    test(comprar_frutas(qtde_morango=0, qtde_uva=5), 9.0)
    # Testes só com uvas, muda a faixa:
    test(comprar_frutas(qtde_morango=0, qtde_uva=6), 9.00)
    test(comprar_frutas(qtde_morango=0, qtde_uva=5.1), 7.65)
    test(comprar_frutas(qtde_morango=0, qtde_uva=8), 12.00)
    # Testes só com uvas, recebe desconto por peso:
    test(comprar_frutas(qtde_morango=0, qtde_uva=9), 12.15)
    test(comprar_frutas(qtde_morango=0, qtde_uva=10), 13.5)
    # Testes só com uvas, recebe desconto por preço:
    test(comprar_frutas(qtde_morango=0, qtde_uva=20), 27.00)

    # Testes com as duas frutas:
    test(comprar_frutas(qtde_morango=2, qtde_uva=2), 8.60)
    test(comprar_frutas(qtde_morango=4, qtde_uva=4), 17.20)
    test(comprar_frutas(qtde_morango=5, qtde_uva=5), 19.35)
    test(comprar_frutas(qtde_morango=10, qtde_uva=10), 33.30)


if __name__ == "__main__":
    main()
    print(
        f"\n{total} Testes, {acertos} Ok, {total - acertos} Falhas: Nota {round(acertos * 100 / total)}"
    )
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")
