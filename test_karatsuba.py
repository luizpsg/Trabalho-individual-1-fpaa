#!/usr/bin/env python3
"""
Arquivo de teste adicional para demonstrar a eficiência do algoritmo de Karatsuba.
Este arquivo testa o algoritmo com números maiores para mostrar melhor a diferença
de performance entre os métodos tradicional e Karatsuba.
"""

from main import karatsuba_multiply, traditional_multiply, compare_algorithms
import time
import random


def generate_large_number(digits):
    """
    Gera um número aleatório com o número especificado de dígitos.

    Args:
        digits (int): Número de dígitos desejados

    Returns:
        int: Número aleatório com o número especificado de dígitos
    """
    start = 10 ** (digits - 1)
    end = 10**digits - 1
    return random.randint(start, end)


def benchmark_algorithms():
    """
    Executa um benchmark comparativo entre os algoritmos.
    """
    print("=== BENCHMARK: Algoritmo de Karatsuba vs Multiplicação Tradicional ===\n")

    # Casos de teste com números de diferentes tamanhos
    test_cases = [
        (123, 456, "Pequenos (3 dígitos)"),
        (1234, 5678, "Médios (4 dígitos)"),
        (12345, 67890, "Médios (5 dígitos)"),
        (123456, 789012, "Grandes (6 dígitos)"),
        (1234567, 8901234, "Grandes (7 dígitos)"),
        (12345678, 90123456, "Muito grandes (8 dígitos)"),
        (123456789, 987654321, "Muito grandes (9 dígitos)"),
    ]

    # Adicionar alguns números gerados aleatoriamente para teste
    for digits in [10, 15, 20]:
        x = generate_large_number(digits)
        y = generate_large_number(digits)
        test_cases.append((x, y, f"Aleatórios ({digits} dígitos)"))

    total_karatsuba_time = 0
    total_traditional_time = 0

    for x, y, description in test_cases:
        print(f"Testando: {description}")
        print(f"  Números: {x} × {y}")

        # Executar comparação
        result = compare_algorithms(x, y)

        # Verificar se os resultados coincidem
        if result["results_match"]:
            print(f"  ✓ Resultados coincidem: {result['karatsuba_result']}")
        else:
            print(f"  ✗ ERRO: Resultados diferentes!")
            print(f"    Karatsuba: {result['karatsuba_result']}")
            print(f"    Tradicional: {result['traditional_result']}")
            return

        # Mostrar tempos
        karatsuba_time = result["karatsuba_time"]
        traditional_time = result["traditional_time"]

        print(f"  Tempo Karatsuba: {karatsuba_time:.6f} segundos")
        print(f"  Tempo Tradicional: {traditional_time:.6f} segundos")

        # Calcular speedup
        if karatsuba_time > 0 and traditional_time > 0:
            if karatsuba_time < traditional_time:
                speedup = traditional_time / karatsuba_time
                print(f"  🚀 Karatsuba foi {speedup:.2f}x mais rápido!")
            else:
                slowdown = karatsuba_time / traditional_time
                print(f"  🐌 Karatsuba foi {slowdown:.2f}x mais lento")
        else:
            print("  ⚡ Ambos os algoritmos foram extremamente rápidos!")

        # Acumular tempos totais
        total_karatsuba_time += karatsuba_time
        total_traditional_time += traditional_time

        print()

    # Resumo final
    print("=== RESUMO DO BENCHMARK ===")
    print(f"Tempo total Karatsuba: {total_karatsuba_time:.6f} segundos")
    print(f"Tempo total Tradicional: {total_traditional_time:.6f} segundos")

    if total_karatsuba_time > 0 and total_traditional_time > 0:
        if total_karatsuba_time < total_traditional_time:
            overall_speedup = total_traditional_time / total_karatsuba_time
            print(f"🚀 Karatsuba foi {overall_speedup:.2f}x mais rápido no geral!")
        else:
            overall_slowdown = total_karatsuba_time / total_traditional_time
            print(f"🐌 Karatsuba foi {overall_slowdown:.2f}x mais lento no geral")
    else:
        print("⚡ Ambos os algoritmos foram extremamente rápidos!")


def test_edge_cases():
    """
    Testa casos extremos e especiais do algoritmo.
    """
    print("=== TESTE DE CASOS EXTREMOS ===\n")

    edge_cases = [
        (0, 0, "Zero × Zero"),
        (0, 12345, "Zero × Número"),
        (12345, 0, "Número × Zero"),
        (1, 999999, "Um × Número grande"),
        (999999, 1, "Número grande × Um"),
        (-123, 456, "Negativo × Positivo"),
        (123, -456, "Positivo × Negativo"),
        (-123, -456, "Negativo × Negativo"),
    ]

    for x, y, description in edge_cases:
        print(f"Testando: {description}")
        print(f"  Números: {x} × {y}")

        try:
            karatsuba_result = karatsuba_multiply(x, y)
            traditional_result = traditional_multiply(x, y)

            if karatsuba_result == traditional_result:
                print(f"  ✓ Resultado correto: {karatsuba_result}")
            else:
                print(f"  ✗ ERRO: Resultados diferentes!")
                print(f"    Karatsuba: {karatsuba_result}")
                print(f"    Tradicional: {traditional_result}")
        except Exception as e:
            print(f"  ✗ ERRO: {e}")

        print()


if __name__ == "__main__":
    print("Iniciando testes do algoritmo de Karatsuba...\n")

    # Testar casos extremos primeiro
    test_edge_cases()

    # Executar benchmark principal
    benchmark_algorithms()

    print("Testes concluídos!")
