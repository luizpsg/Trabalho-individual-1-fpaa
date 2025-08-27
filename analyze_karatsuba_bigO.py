#!/usr/bin/env python3
"""
Script para analisar a complexidade Big-O do algoritmo de Karatsuba
usando o projeto BigOComplex.
"""

import sys
import os
import time
import random

# Adicionar o diretório BigOComplex ao path
sys.path.append(os.path.join(os.path.dirname(__file__), "BigOComplex"))

try:
    from BigOComplex.main import measure_complexity
    from BigOComplex.wrapper import *

    print("✅ Projeto BigOComplex carregado com sucesso!")
except ImportError as e:
    print(f"❌ Erro ao importar BigOComplex: {e}")
    print("Verifique se o projeto BigOComplex está configurado corretamente.")
    sys.exit(1)


def create_karatsuba_wrapper():
    """
    Cria um wrapper para o algoritmo de Karatsuba que seja compatível com o BigO Calculator.
    """
    from main import karatsuba_multiply

    def karatsuba_wrapper(arr):
        """
        Wrapper para o algoritmo de Karatsuba.
        Multiplica dois números aleatórios baseados no tamanho do array.
        """
        if len(arr) < 2:
            return [0]

        # Gerar dois números com base no tamanho do array
        # Para números maiores, o algoritmo será mais lento
        size = len(arr)
        # Limitar o número de dígitos para evitar erros de limite
        max_digits = min(max(1, size // 20), 100)  # Máximo de 100 dígitos

        # Gerar números com o número especificado de dígitos
        x = random.randint(10 ** (max_digits - 1), 10**max_digits - 1)
        y = random.randint(10 ** (max_digits - 1), 10**max_digits - 1)

        # Executar o algoritmo de Karatsuba
        result = karatsuba_multiply(x, y)
        return [result]

    return karatsuba_wrapper


def create_traditional_wrapper():
    """
    Cria um wrapper para a multiplicação tradicional.
    """
    from main import traditional_multiply

    def traditional_wrapper(arr):
        """
        Wrapper para a multiplicação tradicional.
        """
        if len(arr) < 2:
            return [0]

        size = len(arr)
        # Limitar o número de dígitos para evitar erros de limite
        max_digits = min(max(1, size // 20), 100)  # Máximo de 100 dígitos

        x = random.randint(10 ** (max_digits - 1), 10**max_digits - 1)
        y = random.randint(10 ** (max_digits - 1), 10**max_digits - 1)

        result = traditional_multiply(x, y)
        return [result]

    return traditional_wrapper


def analyze_karatsuba_bigO():
    """
    Analisa a complexidade Big-O do algoritmo de Karatsuba.
    """
    print("=== ANÁLISE DA COMPLEXIDADE BIG-O - ALGORITMO DE KARATSUBA ===\n")

    # Criar wrappers para nossos algoritmos
    karatsuba_wrapper = create_karatsuba_wrapper()
    traditional_wrapper = create_traditional_wrapper()

    # Funções para análise
    functions_to_analyze = [
        ("karatsuba_multiply", karatsuba_wrapper),
        ("traditional_multiply", traditional_wrapper),
        ("binary_search_wrapper", binary_search_wrapper),
        ("linear_search_wrapper", linear_search_wrapper),
        ("merge_sort", merge_sort),
        ("bubble_sort", bubble_sort),
    ]

    print("📊 ANÁLISE DA COMPLEXIDADE BIG-O\n")

    results = {}

    for func_name, func in functions_to_analyze:
        print(f"🔍 Analisando função: {func_name}")

        try:
            # Medir a complexidade usando o BigO Calculator
            complexity = measure_complexity(func)
            results[func_name] = complexity

            print(f"   📈 Complexidade Big-O: {complexity}")

            # Análise específica para nossos algoritmos
            if func_name in ["karatsuba_multiply", "traditional_multiply"]:
                if "log" in str(complexity) or "1.585" in str(complexity):
                    interpretation = (
                        "✅ Complexidade logarítmica - Excelente para números grandes!"
                    )
                elif "n^2" in str(complexity) or "n²" in str(complexity):
                    interpretation = "⚠️  Complexidade quadrática - Pode ser melhorada"
                elif "n" in str(complexity) and "log" not in str(complexity):
                    interpretation = (
                        "🔄 Complexidade linear - Boa para números pequenos"
                    )
                else:
                    interpretation = (
                        "🔍 Complexidade específica - Requer análise detalhada"
                    )

                print(f"   💡 Interpretação: {interpretation}")

        except Exception as e:
            print(f"   ❌ Erro ao analisar: {e}")
            results[func_name] = "Erro"

        print()

    # Análise comparativa específica
    print("🎯 ANÁLISE COMPARATIVA DOS ALGORITMOS DE MULTIPLICAÇÃO\n")

    karatsuba_complexity = results.get("karatsuba_multiply", "N/A")
    traditional_complexity = results.get("traditional_multiply", "N/A")

    print(f"📊 Resultados da Análise:")
    print(f"   • Algoritmo de Karatsuba: {karatsuba_complexity}")
    print(f"   • Multiplicação tradicional: {traditional_complexity}")

    # Comparação teórica vs prática
    print(f"\n📚 COMPARAÇÃO TEÓRICA vs PRÁTICA:")
    print(f"   • Teórico - Karatsuba: O(n^log₂3) ≈ O(n^1.585)")
    print(f"   • Teórico - Tradicional: O(n²)")
    print(f"   • Prático - Karatsuba: {karatsuba_complexity}")
    print(f"   • Prático - Tradicional: {traditional_complexity}")

    # Análise de eficiência
    print(f"\n⚡ ANÁLISE DE EFICIÊNCIA:")

    if "karatsuba_multiply" in results and "traditional_multiply" in results:
        karatsuba = str(results["karatsuba_multiply"])
        traditional = str(results["traditional_multiply"])

        if "log" in karatsuba.lower() or "1.585" in karatsuba:
            print("   🚀 Karatsuba mostra complexidade logarítmica - Excelente!")
        elif "n^2" in traditional.lower() or "n²" in traditional:
            print("   ⚠️  Multiplicação tradicional mostra complexidade quadrática")

        # Comparar com outros algoritmos
        if "merge_sort" in results:
            merge_complexity = results["merge_sort"]
            print(f"   📊 Merge Sort: {merge_complexity} (para comparação)")

        if "bubble_sort" in results:
            bubble_complexity = results["bubble_sort"]
            print(f"   📊 Bubble Sort: {bubble_complexity} (para comparação)")

    # Recomendações
    print(f"\n💡 RECOMENDAÇÕES:")
    print(f"   • Para números pequenos (< 10 dígitos): Use multiplicação tradicional")
    print(f"   • Para números grandes (> 100 dígitos): Use algoritmo de Karatsuba")
    print(
        f"   • Para números muito grandes (> 1000 dígitos): Considere algoritmos mais avançados"
    )

    return results


def benchmark_performance():
    """
    Executa um benchmark de performance para validar os resultados.
    """
    print("\n" + "=" * 60)
    print("🏃 BENCHMARK DE PERFORMANCE")
    print("=" * 60)

    from main import karatsuba_multiply, traditional_multiply

    # Testar com números de diferentes tamanhos
    test_cases = [
        (123, 456, "Pequenos (3 dígitos)"),
        (12345, 67890, "Médios (5 dígitos)"),
        (123456789, 987654321, "Grandes (9 dígitos)"),
        (12345678901234567890, 98765432109876543210, "Muito grandes (20 dígitos)"),
    ]

    for x, y, description in test_cases:
        print(f"\n🔍 Testando: {description}")
        print(f"   Números: {x} × {y}")

        # Teste Karatsuba
        start_time = time.time()
        karatsuba_result = karatsuba_multiply(x, y)
        karatsuba_time = time.time() - start_time

        # Teste tradicional
        start_time = time.time()
        traditional_result = traditional_multiply(x, y)
        traditional_time = time.time() - start_time

        # Verificar se os resultados coincidem
        results_match = karatsuba_result == traditional_result

        print(f"   Resultado Karatsuba: {karatsuba_result}")
        print(f"   Resultado Tradicional: {traditional_result}")
        print(f"   Tempo Karatsuba: {karatsuba_time:.6f} segundos")
        print(f"   Tempo Tradicional: {traditional_time:.6f} segundos")
        print(f"   Resultados coincidem: {'✅ Sim' if results_match else '❌ Não'}")

        if karatsuba_time > 0 and traditional_time > 0:
            if karatsuba_time < traditional_time:
                speedup = traditional_time / karatsuba_time
                print(f"   🚀 Karatsuba foi {speedup:.2f}x mais rápido!")
            else:
                slowdown = karatsuba_time / traditional_time
                print(f"   🐌 Karatsuba foi {slowdown:.2f}x mais lento")


def main():
    """
    Função principal.
    """
    try:
        print(
            "🚀 Iniciando análise da complexidade Big-O do algoritmo de Karatsuba...\n"
        )

        # Analisar complexidade Big-O
        results = analyze_karatsuba_bigO()

        # Executar benchmark de performance
        benchmark_performance()

        print("\n" + "=" * 60)
        print("🎉 ANÁLISE BIG-O CONCLUÍDA COM SUCESSO!")
        print("=" * 60)

        # Salvar resultados em arquivo
        with open("exports/karatsuba_bigO_analysis.txt", "w", encoding="utf-8") as f:
            f.write("ANÁLISE BIG-O - ALGORITMO DE KARATSUBA\n")
            f.write("=" * 50 + "\n\n")
            f.write(f"Data da análise: {__import__('datetime').datetime.now()}\n\n")

            f.write("RESULTADOS DA ANÁLISE:\n")
            for func_name, complexity in results.items():
                f.write(f"  {func_name}: {complexity}\n")

            f.write(
                f"\nComplexidade do Algoritmo de Karatsuba: {results.get('karatsuba_multiply', 'N/A')}\n"
            )
            f.write(
                f"Complexidade da Multiplicação Tradicional: {results.get('traditional_multiply', 'N/A')}\n"
            )

        print(f"\n💾 Resultados salvos em: exports/karatsuba_bigO_analysis.txt")

    except Exception as e:
        print(f"❌ Erro durante a análise: {e}")
        print("Verifique se o projeto BigOComplex está configurado corretamente.")


if __name__ == "__main__":
    main()
