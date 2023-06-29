# Lista de exercícios Code Wars


def nome_de_dominio(url):
    """Recebe uma URL, em diversos formatos e devolve o nome de domínio.

    Args:
        url (string): a URL

    Returns:
        string: o nome de domínio
    """


def posicao_no_alfabeto(s):
    """Dada uma string, substitua cada letra por sua posição no alfabeto.
    Se algo no texto não for uma letra, ignore e não devolva.
    "a" = 1, "b" = 2, etc.

    Args:
        s (string): um texto, contendo letras, números e pontuação.

    Returns:
        string: um texto, contendo a posição no alfabeto de cada letra do texto dado
    """


def ordem_descendente(num):
    """Sua tarefa é fazer uma função que pode tomar qualquer número inteiro \
    não negativo como um argumento e retorná-lo com seus dígitos em \
    ordem decrescente. Essencialmente, reorganize os dígitos para criar \
    o maior número possível.

    Args:
        num (int): um numero inteiro

    Returns:
        int: um número inteiro, conforme o enunciado
    """


def explode_string_plus(s):
    """Resolva, baseado nos testes.

    Args:
        s (string): uma string que inclui somente letras de a..z e A..Z.

    Returns:
        string: Uma string, conforme os testes.
    """


def crescimento_populacional_2(populacao_atual, percentual, aumento, populacao_final):
    """Em uma pequena cidade, a população é p0 = 1000 no início do ano. \
    A população aumenta regularmente em 2% ao ano e, além disso, 50 novos \
    habitantes por ano vêm morar na cidade. \
    Quantos anos a cidade precisa para ver sua população maior ou igual a p = 1200 habitantes?

    No final do primeiro ano, haverá:
    1000 + 1000 * 0,02 + 50 => 1070 habitantes

    No final do 2º ano, haverá:
    1070 + 1070 * 0,02 + 50 => 1141 habitantes (o número de habitantes é um inteiro)

    No final do 3º ano, haverá:
    1141 + 1141 * 0,02 + 50 => 1213

    Serão necessários 3 anos inteiros.

    Observação:
    Não se esqueça de converter o parâmetro de porcentagem em porcentagem \
    no corpo de sua função: se o parâmetro de porcentagem for 2, você deve \
    convertê-lo para 0,02.

    Args:
        populacao_atual (int): a população inicial, no ano zero.
        percentual (float): o percentual de aumento da população a cada ano.
        aumento (int): a quantidade de pessoas que chegam na cidade de fora.
        populacao_final (int): a população que se quer chegar.

    Returns:
        int: a quantidade de anos até se alcançar (ou passar) a população final.
    """


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

    print("Nome de domínio")
    test(nome_de_dominio("github.com"), "github")
    test(nome_de_dominio("http://www.zombie-bites.com"), "zombie-bites")
    test(nome_de_dominio("https://www.cnet.com"), "cnet")
    test(nome_de_dominio("http://google.com"), "google")
    test(nome_de_dominio("http://google.co.jp"), "google")
    test(nome_de_dominio("www.xakep.ru"), "xakep")
    test(nome_de_dominio("https://youtube.com"), "youtube")

    print("Posição no alfabeto:")
    test(
        posicao_no_alfabeto("The sunset sets at twelve o' clock."),
        "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11",
    )
    test(
        posicao_no_alfabeto("The narwhal bacons at midnight."),
        "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20",
    )

    print("Ordem Descendente:")
    test(ordem_descendente(0), 0)
    test(ordem_descendente(15), 51)
    test(ordem_descendente(42145), 54421)
    test(ordem_descendente(145263), 654321)
    test(ordem_descendente(123456789), 987654321)

    print("Explode String Plus:")
    test(
        explode_string_plus("ZpglnRxqenU"),
        "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu",
    )
    test(
        explode_string_plus("NyffsGeyylB"),
        "N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb",
    )
    test(
        explode_string_plus("MjtkuBovqrU"),
        "M-Jj-Ttt-Kkkk-Uuuuu-Bbbbbb-Ooooooo-Vvvvvvvv-Qqqqqqqqq-Rrrrrrrrrr-Uuuuuuuuuuu",
    )
    test(
        explode_string_plus("EvidjUnokmM"),
        "E-Vv-Iii-Dddd-Jjjjj-Uuuuuu-Nnnnnnn-Oooooooo-Kkkkkkkkk-Mmmmmmmmmm-Mmmmmmmmmmm",
    )
    test(
        explode_string_plus("HbideVbxncC"),
        "H-Bb-Iii-Dddd-Eeeee-Vvvvvv-Bbbbbbb-Xxxxxxxx-Nnnnnnnnn-Cccccccccc-Ccccccccccc",
    )

    print("Crescimento Populacional 2:")
    test(crescimento_populacional_2(1000, 2, 50, 1200), 3)
    test(crescimento_populacional_2(1500, 5, 100, 5000), 15)
    test(crescimento_populacional_2(1500000, 2.5, 10000, 2000000), 10)


if __name__ == "__main__":
    main()
    print(
        f"\n{total} Testes, {acertos} Ok, {total - acertos} Falhas: Nota {round(acertos * 100 / total)}"
    )
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")
