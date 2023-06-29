import random

def embaralha(palavra):
    """ Embaralha uma palavra.

    Args:
        palavra (string): uma palavra

    Retorna:
        (string): a palavra embaralhada
    """

    palavra = palavra.lower()
    letras = list(palavra)
    random.shuffle(letras)

    palavra_embaralhada = ''.join(letras)

    return palavra_embaralhada
    
