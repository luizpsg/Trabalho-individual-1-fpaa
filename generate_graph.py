#!/usr/bin/env python3
"""
Script para gerar uma imagem do grafo de fluxo do algoritmo de Karatsuba.
Este script cria uma visualização gráfica do fluxo de controle da função.
"""

try:
    from graphviz import Digraph
    import os

    def create_karatsuba_flowchart():
        """
        Cria o grafo de fluxo do algoritmo de Karatsuba.
        """
        # Criar o grafo
        dot = Digraph(comment="Grafo de Fluxo - Algoritmo de Karatsuba")
        dot.attr(rankdir="TB")

        # Definir estilos
        dot.attr(
            "node", shape="box", style="rounded,filled", fontname="Arial", fontsize="10"
        )

        # Adicionar nós
        dot.node("A", "Entrada da função", fillcolor="#e1f5fe")
        dot.node("B", "x < 10 ou y < 10?", fillcolor="#fff3e0", shape="diamond")
        dot.node("C", "Retorno: x * y", fillcolor="#c8e6c9")
        dot.node("D", "Calcular n = max dígitos", fillcolor="#f5f5f5")
        dot.node("E", "n é ímpar?", fillcolor="#fff3e0", shape="diamond")
        dot.node("F", "n = n + 1", fillcolor="#f5f5f5")
        dot.node("G", "Calcular divisor = 10^(n/2)", fillcolor="#f5f5f5")
        dot.node("H", "Dividir números em partes", fillcolor="#f5f5f5")
        dot.node("I", "Chamada recursiva:\nkaratsuba(a, c)", fillcolor="#f3e5f5")
        dot.node("J", "Chamada recursiva:\nkaratsuba(b, d)", fillcolor="#f3e5f5")
        dot.node("K", "Chamada recursiva:\nkaratsuba(a+b, c+d)", fillcolor="#f3e5f5")
        dot.node("L", "Calcular resultado final", fillcolor="#f5f5f5")
        dot.node("M", "Retorno do resultado", fillcolor="#c8e6c9")

        # Adicionar arestas
        dot.edge("A", "B")
        dot.edge("B", "C", "Sim")
        dot.edge("B", "D", "Não")
        dot.edge("D", "E")
        dot.edge("E", "F", "Sim")
        dot.edge("E", "G", "Não")
        dot.edge("F", "G")
        dot.edge("G", "H")
        dot.edge("H", "I")
        dot.edge("H", "J")
        dot.edge("H", "K")
        dot.edge("I", "L")
        dot.edge("J", "L")
        dot.edge("K", "L")
        dot.edge("L", "M")

        return dot

    def main():
        """
        Função principal que gera o grafo.
        """
        print("Gerando grafo de fluxo do algoritmo de Karatsuba...")

        # Criar o grafo
        dot = create_karatsuba_flowchart()

        # Salvar como PNG
        dot.render("exports/karatsuba_flowchart", format="png", cleanup=True)
        print("✓ Grafo salvo como 'exports/karatsuba_flowchart.png'")

        # Salvar como SVG (mais nítido)
        dot.render("exports/karatsuba_flowchart", format="svg", cleanup=True)
        print("✓ Grafo salvo como 'exports/karatsuba_flowchart.svg'")

        # Salvar como PDF
        dot.render("exports/karatsuba_flowchart", format="pdf", cleanup=True)
        print("✓ Grafo salvo como 'exports/karatsuba_flowchart.pdf'")

        print("\nArquivos gerados com sucesso!")
        print("Você pode incluir a imagem no README.md")

    if __name__ == "__main__":
        main()

except ImportError:
    print("❌ Erro: A biblioteca 'graphviz' não está instalada.")
    print("Para instalar, execute: pip install graphviz")
