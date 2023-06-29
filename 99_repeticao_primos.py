# Lista de exercícios - Exercícios com números primos
# Para formas melhores de resolver esse problema leia o artigo:
# https://wiki.python.org.br/DeterminandoPrimos


def é_primo(n):
    """Verifique se o valor informado é primo.
    Um número primo é aquele que é divisível apenas por ele mesmo e por 1.

    Argumento:
        valor (int): um número inteiro.

    Retorna:
        bool: True ou False, se o valor é ou não primo.
    """

    if n <= 1: return False
    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True

def quantidade_de_primos(inicio, fim):
    """Retorne a quantidade de primos entre os valores informados, incluindo
    os limites.

    Argumentos:
        inicio (int): limite inferior;
        fim (int): limite superior;

    Retorna:
        int: a quantidade de números primos dentro do intervalo especificado.
    """

    # compreensão de lista
    return len([i for i in range(inicio, fim+1) if é_primo(i)])

def lista_de_primos(inicio, fim):
    """Retorne uma lista de primos entre os valores informados, incluindo
    os limites.

    Argumentos:
        inicio (int): limite inferior;
        fim (int): limite superior;

    Retorna:
        lista de inteiros, os primos dentro do intervalo especificado.
    """

    # compreensão de lista
    return [i for i in range(inicio, fim+1) if é_primo(i)]

# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0


def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = "\033[31m%s" % ("Falhou")
    else:
        prefixo = "\033[32m%s" % ("Passou")
        acertos += 1
    print(
        "%s Esperado: %s \tObtido: %s\033[1;m" % (prefixo, repr(esperado), repr(obtido))
    )


def main():

    print("Verifica se um número é primo:")
    test(é_primo(0), False)
    test(é_primo(1), False)
    test(é_primo(2), True)
    test(é_primo(3), True)
    test(é_primo(4), False)
    test(é_primo(5), True)
    test(é_primo(7), True)
    test(é_primo(11), True)
    test(é_primo(17), True)
    test(é_primo(121), False)
    test(é_primo(169), False)

    print("Quantidade de primos no intervalo:")
    test(quantidade_de_primos(5, 10), 2)
    test(quantidade_de_primos(5, 11), 3)
    test(quantidade_de_primos(10, 20), 4)
    test(quantidade_de_primos(0, 21), 8)
    test(quantidade_de_primos(43, 102), 13)

    print("Lista de primos no intervalo:")
    test(lista_de_primos(0, 1), [])
    test(lista_de_primos(5, 10), [5, 7])
    test(lista_de_primos(10, 20), [11, 13, 17, 19])
    test(lista_de_primos(0, 21), [2, 3, 5, 7, 11, 13, 17, 19])
    test(
        lista_de_primos(43, 102), [43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    )


if __name__ == "__main__":
    main()
    print(
        "\n%d Testes, %d Ok, %d Falhas: Nota %.1f"
        % (total, acertos, total - acertos, float(acertos * 10) / total)
    )
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")
