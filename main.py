import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from pie_charts import pie_chart_week_sales

from line_charts import line_charts_day_same_day
from line_charts import line_chart_sales_comparation
from line_charts import line_chart_comparation_day_week_month
from line_charts import line_chart_comparation_week_month

from bar_charts import bar_chart_sales_quantity_comparation
from bar_charts import bar_chart_variation_comparation

# Carregar os dados do primeiro arquivo CSV
checkout1_data = pd.read_csv('checkout_1.csv')
checkout2_data = pd.read_csv('checkout_2.csv')

# =================================QUERIES================================================
# Volume total de vendas por dia
checkout1_daily_volume = checkout1_data[['today']].sum(axis=1)
checkout2_daily_volume = checkout2_data[['today']].sum(axis=1)
checkout1_daily_volume_yesterday = checkout1_data[['yesterday']].sum(axis=1)
checkout2_daily_volume_yesterday = checkout2_data[['yesterday']].sum(axis=1)
checkout1_daily_volume_same_day_last_week = checkout1_data[['same_day_last_week']].sum(axis=1)
checkout2_daily_volume_same_day_last_week = checkout2_data[['same_day_last_week']].sum(axis=1)
checkout1_avg_last_week = checkout1_data[['avg_last_week']].sum(axis=1)
checkout2_avg_last_week = checkout2_data[['avg_last_week']].sum(axis=1)
checkout1_avg_last_month = checkout1_data[['avg_last_month']].sum(axis=1)
checkout2_avg_last_month = checkout2_data[['avg_last_month']].sum(axis=1)

#  variação percentual diária em relação à média da semana
checkout1_daily_variation = (checkout1_daily_volume / checkout1_data['avg_last_week']) * 100
checkout2_daily_variation = (checkout2_daily_volume / checkout2_data['avg_last_week']) * 100

# =======================GRAFICOS ===================================================================

line_chart_comparation_day_week_month(checkout1_data,
                                      checkout1_daily_volume, checkout2_daily_volume,
                                      checkout1_avg_last_week, checkout2_avg_last_week,
                                      checkout1_avg_last_month, checkout2_avg_last_month,
                                      checkout1_daily_volume_yesterday, checkout2_daily_volume_yesterday,
                                      checkout1_daily_volume_same_day_last_week,
                                      checkout2_daily_volume_same_day_last_week)

bar_chart_variation_comparation(checkout1_data, checkout1_daily_variation, checkout2_daily_variation)

bar_chart_sales_quantity_comparation(checkout1_data, checkout2_data)

line_chart_sales_comparation(checkout1_data, checkout2_data)

line_charts_day_same_day(checkout1_data, checkout2_data)

pie_chart_week_sales(checkout2_daily_volume_same_day_last_week, checkout1_daily_volume,
                     checkout1_daily_volume_yesterday, checkout2_avg_last_week)

line_chart_comparation_week_month(checkout1_data, checkout1_avg_last_week, checkout2_avg_last_week,
                                  checkout1_avg_last_month,
                                  checkout2_avg_last_month)
