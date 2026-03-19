def list_shift(lista, valor):
    """
    Modifica la lista original sumando 'valor' a cada elemento.
    Al ser una lista un objeto mutable, los cambios persisten fuera de la función.
    """
    for i in range(len(lista)):
        lista[i] += valor
    # No hay return, la modificación es "in-place"

def calc_avg(lista):
    """
    Calcula y retorna el promedio aritmético.
    """
    promedio = sum(lista) / len(lista)
    return float(promedio)

def print_normalized(lista):
    """
    Simplemente imprime la lista en consola.
    """
    print(lista)