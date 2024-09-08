# Gabriel Alejo Cota Ruiz 22760043
# Oredenamiento romano


orden = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

palabras = ["Pixel", "Civil", "Paco", "Hijo", "Toxico","Camion","Clave","Ximena"]

def descartar_palabras(palabras):
    palabras_validas = [] 
    for i in palabras: 
        if any(letra.upper() in orden for letra in i):
            palabras_validas.append(i)
    return palabras_validas

def extraer_letras_romanas(palabras_validas):
    letras_romanas_encontradas = {} 
    for i in palabras_validas:

        letras_palabras = [letra.upper() for letra in i if letra.upper() in orden]
        if letras_palabras:
            letras_romanas_encontradas[i] = letras_palabras
    
    return letras_romanas_encontradas



def convertir_romano_individual(secuencia):
    total = 0
    prev_value = float('inf')

    for i in secuencia:
        valor = orden[i]
        if valor > prev_value:
            break
        total += valor
        prev_value = valor

    return total


def procesar_letras_romanas(letras_romanas_ecnontradas):
    resultados = {}

    for palabra, secuencia in letras_romanas_ecnontradas.items():
        valor_decimal = convertir_romano_individual(secuencia)
        resultados[palabra] = valor_decimal

    return resultados


def ordenar_por_valor_decimal(resultados):
    resultados_ordenados = dict(sorted(resultados.items(),key = lambda item: item[1], reverse = True ))

    return resultados_ordenados


def main():
    
    palabras_validas = descartar_palabras(palabras)
    print("\nPalabras con letras romanas:", palabras_validas)

    #
    letras_romanas_encontradas = extraer_letras_romanas(palabras_validas)
    print("\nLetras Romanas Encontradas en cada palabra: ", letras_romanas_encontradas)

    
    resultado_final = procesar_letras_romanas(letras_romanas_encontradas)
    print("\nValores decimales de letras validas(desordenado): ", resultado_final)

    resultado_ordenado = ordenar_por_valor_decimal(resultado_final)
    print("\nPalabras de mayor a menor en sistema decimal(ordenado)", resultado_ordenado)
    

if __name__ == "__main__":
    main()