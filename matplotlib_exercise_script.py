#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import os


def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')


insurance = pd.read_csv(filepath_or_buffer='data/insurance.csv',
                      sep=',',
                      header=0)

pretty_print("insurance dataframe", insurance.to_string())
pretty_print("insurance columns", insurance.columns)

os.makedirs('plots', exist_ok=True)

# Plotting line chart
plt.plot(insurance['charges'], color='red')
plt.title('Charges by Index')
plt.xlabel('Index')
plt.ylabel('Charges')
plt.savefig(f'plots/charges_plot.png', format='png')
plt.clf()

# Plotting histogram
plt.hist(insurance['bmi'], bins=3, color='g')
plt.title('BMI')
plt.xlabel('BMI')
plt.ylabel('Count')
plt.savefig(f'plots/bmi_hist.png', format='png')
plt.clf()

# Plotting scatterplot
plt.scatter(insurance['age'], insurance['charges'], color='b')
plt.title('Age to Charges')
plt.xlabel('Age')
plt.ylabel('Charges')
plt.savefig(f'plots/age_charge_scatter.png', format='png')

plt.close()