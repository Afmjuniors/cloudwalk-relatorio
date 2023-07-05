import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def line_chart_sales_comparation(checkout1_data, checkout2_data):
    # Define os índices para posicionar as linhas
    index = np.arange(len(checkout1_data['time']))

    # Plot Yesterday - Checkout 1 (linha)
    plt.plot(index, checkout1_data['yesterday'], marker='o', label='Day 1 - Yesterday - Checkout 1')

    # Plot Today - Checkout 1 (linha)
    plt.plot(index, checkout1_data['today'], marker='o', label='Day 2 - Today - Checkout 1')

    # Plot Today - Checkout 2 (linha)
    plt.plot(index, checkout2_data['today'], marker='o', label='Day 3 - Today - Checkout 2')

    # Configuração dos eixos e rótulos
    plt.xlabel('Time')
    plt.ylabel('Quantity')
    plt.title('Sales Quantity Comparison')
    plt.xticks(index, checkout1_data['time'])
    plt.legend()

    # Exibe o gráfico
    plt.show()


def line_charts_day_same_day(checkout1_data, checkout2_data):
    # Criação dos subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # Subplot para o Checkout 1
    ax1.plot(checkout1_data['today'], marker='o', label='Today - Checkout 1')
    ax1.plot(checkout1_data['same_day_last_week'], marker='o', label='Same Day Last Week - Checkout 1')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Quantity')
    ax1.set_title('Checkout 1')
    ax1.legend()

    # Subplot para o Checkout 2
    ax2.plot(checkout2_data['today'], marker='o', label='Today - Checkout 2')
    ax2.plot(checkout2_data['same_day_last_week'], marker='o', label='Same Day Last Week - Checkout 2')
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Quantity')
    ax2.set_title('Checkout 2')
    ax2.legend()

    # Ajusta a posição dos subplots
    plt.tight_layout()

    # Exibe o gráfico
    plt.show()


def line_chart_comparation_day_week_month(checkout1_data,
                                          checkout1_daily_volume, checkout2_daily_volume,
                                          checkout1_avg_last_week, checkout2_avg_last_week,
                                          checkout1_avg_last_month, checkout2_avg_last_month,
                                          checkout1_daily_volume_yesterday, checkout2_daily_volume_yesterday,
                                          checkout1_daily_volume_same_day_last_week,
                                          checkout2_daily_volume_same_day_last_week):
    # Define os índices para posicionar as linhas
    index = np.arange(len(checkout1_data['time']))

    # Plot  Grafico Linhas
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 15))

    # Subplot 1 - daily_volume
    ax1.plot(checkout1_daily_volume, label='Checkout 1 - Daily Volume')
    ax1.plot(checkout2_daily_volume, label='Checkout 2 - Daily Volume')
    ax1.plot(checkout1_avg_last_week, label='Checkout 1 - Avg Last Week')
    ax1.plot(checkout2_avg_last_week, label='Checkout 2 - Avg Last Week')
    ax1.plot(checkout1_avg_last_month, label='Checkout 1 - Avg Last Month')
    ax1.plot(checkout2_avg_last_month, label='Checkout 2 - Avg Last Month')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Volume')
    ax1.set_title('Comparison - Today')
    ax1.legend()

    # Subplot 2 - daily_volume_yesterday
    ax2.plot(checkout1_daily_volume_yesterday, label='Checkout 1 - Daily Volume')
    ax2.plot(checkout2_daily_volume_yesterday, label='Checkout 2 - Daily Volume')
    ax2.plot(checkout1_avg_last_week, label='Checkout 1 - Avg Last Week')
    ax2.plot(checkout2_avg_last_week, label='Checkout 2 - Avg Last Week')
    ax2.plot(checkout1_avg_last_month, label='Checkout 1 - Avg Last Month')
    ax2.plot(checkout2_avg_last_month, label='Checkout 2 - Avg Last Month')
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Volume')
    ax2.set_title('Comparison - (Yesterday)')
    ax2.legend()

    # Subplot 3 - daily_volume_same_day_last_week
    ax3.plot(checkout1_daily_volume_same_day_last_week, label='Checkout 1 - Daily Volume')
    ax3.plot(checkout2_daily_volume_same_day_last_week, label='Checkout 2 - Daily Volume')
    ax3.plot(checkout1_avg_last_week, label='Checkout 1 - Avg Last Week')
    ax3.plot(checkout2_avg_last_week, label='Checkout 2 - Avg Last Week')
    ax3.plot(checkout1_avg_last_month, label='Checkout 1 - Avg Last Month')
    ax3.plot(checkout2_avg_last_month, label='Checkout 2 - Avg Last Month')
    ax3.set_xlabel('Time')
    ax3.set_ylabel('Volume')
    ax3.set_title('Comparison - (Same Day Last Week)')
    ax3.legend()

    # Ajusta a posição dos subplots
    plt.tight_layout()

    # Exibe o gráfico
    plt.show()


def line_chart_comparation_week_month(checkout1_data, checkout1_avg_last_week, checkout2_avg_last_week,
                                      checkout1_avg_last_month,
                                      checkout2_avg_last_month):
    index = np.arange(len(checkout1_data['time']))
    # Dados para o gráfico
    avg_last_week_checkout1 = checkout1_avg_last_week
    avg_last_week_checkout2 = checkout2_avg_last_week
    avg_last_month_checkout1 = checkout1_avg_last_month
    avg_last_month_checkout2 = checkout2_avg_last_month

    # Configurações dos subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

    # Plot dos dados para o Checkout 1
    ax1.plot(index, avg_last_week_checkout1, label='Avg Last Week')
    ax1.plot(index, avg_last_month_checkout1, label='Avg Last Month')
    ax1.set_xlabel('Hour')
    ax1.set_ylabel('Volume')
    ax1.set_title('Checkout 1')
    ax1.legend()

    # Plot dos dados para o Checkout 2
    ax2.plot(index, avg_last_week_checkout2, label='Avg Last Week')
    ax2.plot(index, avg_last_month_checkout2, label='Avg Last Month')
    ax2.set_xlabel('Hour')
    ax2.set_ylabel('Volume')
    ax2.set_title('Checkout 2')
    ax2.legend()

    # Ajuste de layout
    plt.tight_layout()

    # Exibição dos subplots
    plt.show()
