def karatsuba_multiply(x, y):
    """
    Implementação do algoritmo de Karatsuba para multiplicação de números inteiros.

    Args:
        x (int): Primeiro número inteiro
        y (int): Segundo número inteiro

    Returns:
        int: Produto de x e y usando o algoritmo de Karatsuba
    """
    # Caso base: se os números são pequenos, usar multiplicação direta
    if x < 10 or y < 10:
        return x * y

    # Determinar o número de dígitos do maior número
    n = max(len(str(abs(x))), len(str(abs(y))))

    # Se n for ímpar, adicionar 1 para facilitar a divisão
    if n % 2 != 0:
        n += 1

    # Calcular o divisor para separar os números
    divisor = 10 ** (n // 2)

    # Dividir os números em partes alta e baixa
    a = x // divisor
    b = x % divisor
    c = y // divisor
    d = y % divisor

    # Recursivamente calcular os três produtos necessários
    ac = karatsuba_multiply(a, c)  # Produto das partes altas
    bd = karatsuba_multiply(b, d)  # Produto das partes baixas
    ad_bc = (
        karatsuba_multiply(a + b, c + d) - ac - bd
    )  # Produto das somas menos ac e bd

    # Aplicar a fórmula de Karatsuba: (10^n * ac) + (10^(n/2) * ad_bc) + bd
    result = (10**n) * ac + (10 ** (n // 2)) * ad_bc + bd

    return result


def traditional_multiply(x, y):
    """
    Implementação da multiplicação tradicional para comparação.

    Args:
        x (int): Primeiro número inteiro
        y (int): Segundo número inteiro

    Returns:
        int: Produto de x e y usando multiplicação tradicional
    """
    return x * y


def compare_algorithms(x, y):
    """
    Compara os resultados dos dois algoritmos de multiplicação.

    Args:
        x (int): Primeiro número inteiro
        y (int): Segundo número inteiro

    Returns:
        dict: Dicionário com os resultados e tempo de execução
    """
    import time

    # Teste do algoritmo de Karatsuba
    start_time = time.time()
    karatsuba_result = karatsuba_multiply(x, y)
    karatsuba_time = time.time() - start_time

    # Teste da multiplicação tradicional
    start_time = time.time()
    traditional_result = traditional_multiply(x, y)
    traditional_time = time.time() - start_time

    return {
        "x": x,
        "y": y,
        "karatsuba_result": karatsuba_result,
        "traditional_result": traditional_result,
        "karatsuba_time": karatsuba_time,
        "traditional_time": traditional_time,
        "results_match": karatsuba_result == traditional_result,
    }


def main():
    """
    Função principal que demonstra o uso do algoritmo de Karatsuba.
    """
    print("=== Algoritmo de Karatsuba para Multiplicação de Números Inteiros ===\n")

    # Exemplos de teste
    test_cases = [
        (123, 456),
        (1234, 5678),
        (12345, 67890),
        (123456, 789012),
        (1234567, 8901234),
    ]

    for x, y in test_cases:
        print(f"Testando: {x} × {y}")

        result = compare_algorithms(x, y)

        print(f"  Resultado Karatsuba: {result['karatsuba_result']}")
        print(f"  Resultado Tradicional: {result['traditional_result']}")
        print(f"  Tempo Karatsuba: {result['karatsuba_time']:.6f} segundos")
        print(f"  Tempo Tradicional: {result['traditional_time']:.6f} segundos")
        print(f"  Resultados coincidem: {'Sim' if result['results_match'] else 'Não'}")

        if result["karatsuba_time"] < result["traditional_time"]:
            if result["karatsuba_time"] > 0:
                speedup = result["traditional_time"] / result["karatsuba_time"]
                print(f"  Karatsuba foi {speedup:.2f}x mais rápido!")
            else:
                print("  Karatsuba foi extremamente rápido!")
        else:
            if result["traditional_time"] > 0:
                slowdown = result["karatsuba_time"] / result["traditional_time"]
                print(f"  Karatsuba foi {slowdown:.2f}x mais lento")
            else:
                print("  Ambos os algoritmos foram extremamente rápidos!")

        print()


if __name__ == "__main__":
    main()
