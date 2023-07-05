import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def bar_chart_sales_quantity_comparation(checkout1_data, checkout2_data):
    # Define a largura das barras
    bar_width = 0.25

    # Define os índices para posicionar as barras
    index = np.arange(len(checkout1_data['time']))

    # Plot Yesterday - Checkout 1
    plt.bar(index, checkout1_data['yesterday'], bar_width, label='Day 1 - Yesterday - Checkout 1')

    # Plot Today - Checkout 1
    plt.bar(index + bar_width, checkout1_data['today'], bar_width, label='Day 2 - Today - Checkout 1')

    # Plot Today - Checkout 2
    plt.bar(index + 2 * bar_width, checkout2_data['today'], bar_width, label='Day 3 - Today - Checkout 2')

    # Configuração dos eixos e rótulos
    plt.xlabel('Time')
    plt.ylabel('Quantity')
    plt.title('Sales Quantity Comparison')
    plt.xticks(index + bar_width, checkout1_data['time'])
    plt.legend()

    # Exibe o gráfico
    plt.show()


def bar_chart_variation_comparation(checkout1_data, checkout1_daily_variation, checkout2_daily_variation):
    # Define a largura das barras
    bar_width = 0.35

    # Define os índices para posicionar as barras
    index = np.arange(len(checkout1_data['time']))

    # Plot Checkout 1
    plt.bar(index, checkout1_daily_variation, bar_width, label='Day 2 - Checkout 1')

    # Plot Checkout 2
    plt.bar(index + bar_width, checkout2_daily_variation, bar_width, label='Day 3 - Checkout 2')

    # Configuração dos eixos e rótulos
    plt.xlabel('Time')
    plt.ylabel('Daily Variation (%)')
    plt.title('Daily Variation in Sales Volume - today/Same Dat Last Week')
    plt.xticks(index + bar_width / 2, checkout1_data['time'])
    plt.legend()

    # Exibe o gráfico
    plt.show()
