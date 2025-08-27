#!/usr/bin/env python3
"""
Script para analisar a complexidade ciclomática do algoritmo de Karatsuba
usando o projeto CyclomaticComplex.
"""

import sys
import os

# Adicionar o diretório CyclomaticComplex ao path
sys.path.append(os.path.join(os.path.dirname(__file__), "CyclomaticComplex"))

# Importar do projeto CyclomaticComplex
from CyclomaticComplex.main import measure_complexity, calculate_cyclomatic_complexity
import inspect


def analyze_karatsuba_complexity():
    """
    Analisa a complexidade ciclomática do algoritmo de Karatsuba.
    """
    print("=== ANÁLISE DA COMPLEXIDADE CICLOMÁTICA - ALGORITMO DE KARATSUBA ===\n")

    # Importar as funções do nosso algoritmo
    from main import karatsuba_multiply, traditional_multiply, compare_algorithms

    # Funções para análise
    functions_to_analyze = [
        ("karatsuba_multiply", karatsuba_multiply),
        ("traditional_multiply", traditional_multiply),
        ("compare_algorithms", compare_algorithms),
    ]

    print("📊 ANÁLISE DETALHADA DA COMPLEXIDADE CICLOMÁTICA\n")

    for func_name, func in functions_to_analyze:
        print(f"🔍 Analisando função: {func_name}")

        # Obter o código fonte
        try:
            source_code = inspect.getsource(func)
            complexity = measure_complexity(func)

            print(f"   📈 Complexidade Ciclomática: {complexity}")

            # Análise detalhada do código
            print(f"   📝 Código fonte:")
            print("   " + "=" * 50)

            # Mostrar o código com numeração de linhas
            lines = source_code.split("\n")
            for i, line in enumerate(lines, 1):
                if line.strip():  # Só mostrar linhas não vazias
                    print(f"   {i:2d}: {line}")

            print("   " + "=" * 50)

            # Interpretação da complexidade
            if complexity <= 3:
                interpretation = "Baixa - Código simples e fácil de manter"
            elif complexity <= 7:
                interpretation = "Média - Código moderadamente complexo"
            elif complexity <= 15:
                interpretation = "Alta - Código complexo, requer atenção"
            else:
                interpretation = (
                    "Muito alta - Código muito complexo, considere refatorar"
                )

            print(f"   💡 Interpretação: {interpretation}")

        except Exception as e:
            print(f"   ❌ Erro ao analisar: {e}")

        print()

    # Análise específica do algoritmo de Karatsuba
    print("🎯 ANÁLISE ESPECÍFICA DO ALGORITMO DE KARATSUBA\n")

    karatsuba_source = inspect.getsource(karatsuba_multiply)
    karatsuba_complexity = measure_complexity(karatsuba_multiply)

    print(f"📊 Complexidade Ciclomática Total: {karatsuba_complexity}")
    print(f"🔍 Análise do fluxo de controle:")

    # Contar estruturas de controle específicas
    if_count = karatsuba_source.count("if ")
    return_count = karatsuba_source.count("return ")
    recursive_calls = karatsuba_source.count("karatsuba_multiply(")

    print(f"   • Estruturas condicionais (if): {if_count}")
    print(f"   • Pontos de retorno: {return_count}")
    print(f"   • Chamadas recursivas: {recursive_calls}")

    # Análise dos caminhos de execução
    print(f"\n🛤️  CAMINHOS DE EXECUÇÃO POSSÍVEIS:")
    print(f"   • Caminho base (caso simples): 1")
    print(f"   • Caminhos condicionais: {if_count}")
    print(f"   • Total de caminhos: {karatsuba_complexity}")

    # Comparação com outros algoritmos
    print(f"\n📊 COMPARAÇÃO COM OUTROS ALGORITMOS:")
    print(f"   • Algoritmo de Karatsuba: {karatsuba_complexity}")
    print(f"   • Multiplicação tradicional: {measure_complexity(traditional_multiply)}")

    # Recomendações
    print(f"\n💡 RECOMENDAÇÕES:")
    if karatsuba_complexity <= 5:
        print("   ✅ Complexidade aceitável para um algoritmo recursivo")
    elif karatsuba_complexity <= 10:
        print("   ⚠️  Complexidade moderada, mas aceitável para este tipo de algoritmo")
    else:
        print("   🔴 Complexidade alta, considere simplificar o algoritmo")

    print(f"\n   📚 Para algoritmos de multiplicação:")
    print(f"      • Complexidade < 5: Excelente")
    print(f"      • Complexidade 5-10: Boa")
    print(f"      • Complexidade > 10: Pode ser melhorada")

    return karatsuba_complexity


def main():
    """
    Função principal.
    """
    try:
        complexity = analyze_karatsuba_complexity()

        print("\n" + "=" * 60)
        print("🎉 ANÁLISE CONCLUÍDA COM SUCESSO!")
        print(f"📊 Complexidade Ciclomática do Algoritmo de Karatsuba: {complexity}")
        print("=" * 60)

        # Salvar resultado em arquivo
        with open(
            "exports/karatsuba_complexity_analysis.txt", "w", encoding="utf-8"
        ) as f:
            f.write(
                f"Complexidade Ciclomática do Algoritmo de Karatsuba: {complexity}\n"
            )
            f.write(
                "Data da análise: " + str(__import__("datetime").datetime.now()) + "\n"
            )

        print(f"\n💾 Resultado salvo em: exports/karatsuba_complexity_analysis.txt")

    except Exception as e:
        print(f"❌ Erro durante a análise: {e}")
        print("Verifique se o projeto CyclomaticComplex está configurado corretamente.")


if __name__ == "__main__":
    main()
