import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def pie_chart_week_sales(checkout2_daily_volume_same_day_last_week,checkout1_daily_volume,checkout1_daily_volume_yesterday,checkout2_avg_last_week):
    # Valores conhecidos das três fatias
    same_day_last_week = checkout2_daily_volume_same_day_last_week.sum() / 7
    today_checkout1 = checkout1_daily_volume.sum() / 7
    yesterday_checkout1 = checkout1_daily_volume_yesterday.sum() / 7

    # Valor total desconhecido
    unk_vol_last_week = checkout2_avg_last_week.sum() - (same_day_last_week + today_checkout1 + yesterday_checkout1)

    # Criação do gráfico de pizza
    slices = [same_day_last_week, today_checkout1, yesterday_checkout1, unk_vol_last_week]
    labels = ['Day 3 - Last Week', 'Day 2', 'Day 1', 'Rest of the week']
    colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightgrey']

    plt.pie(slices, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)

    # Título do gráfico
    plt.title('Divisões no Total')

    # Exibição do gráfico
    plt.show()
