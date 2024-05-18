import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Exibindo os arquivos no diretório de entrada
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# Lendo os arquivos CSV
airports = pd.read_csv('../../marilenevalentevieiradelacerda/Desktop/python/airports.csv')
airlines = pd.read_csv('../../marilenevalentevieiradelacerda/Desktop/python/airlines.csv')
flights = pd.read_csv('../../marilenevalentevieiradelacerda/Desktop/python/flights.csv')
print (airports)
print (airlines)
print (flights)

# Lendo o arquivo CSV com especificação de dtype para evitar avisos de mistura de tipos
flight_df = pd.read_csv("/kaggle/input/flight-delays/flight.csv", dtype={'column_7': str, 'column_8': str}, low_memory=False)

# Plotando o gráfico de violino para comparação dos atrasos de chegada por companhia aérea
plt.figure(figsize=(12, 18))
sns.violinplot(data=flight_df, x='AIRLINE', y='ARRIVAL_DELAY', palette='set2')
plt.xlabel('Airline')
plt.ylabel('Arrival Delay (minutes)')
plt.title('Comparison of Arrival Delays by Airline (Violin Plot)')
plt.xticks(rotation=45)
plt.show()

# Calculando a média dos atrasos de chegada por companhia aérea
average_delay_by_airline = flight_df.groupby('AIRLINE')['ARRIVAL_DELAY'].mean().reset_index()

# Plotando o gráfico de barras para atrasos médios de chegada por companhia aérea
plt.figure(figsize=(12, 8))
sns.barplot(data=average_delay_by_airline, x='AIRLINE', y='ARRIVAL_DELAY', palette='viridis')
plt.xlabel('Airline')
plt.ylabel('Average Arrival Delay (minutes)')
plt.title('Average Arrival Delay by Airline')
plt.xticks(rotation=45)
plt.show()