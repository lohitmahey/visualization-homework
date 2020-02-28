#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import os


def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')


data = pd.read_csv('data/diabetes.data', sep='\\s+', header=0)

pretty_print("Diabetes dataframe", data.to_string())
pretty_print("Diabetes columns", data.columns)

os.makedirs('plots', exist_ok=True)

# Plotting line chart
plt.plot(data['AGE'], color='red')
plt.title('Age by Index')
plt.xlabel('Index')
plt.ylabel('Age')
plt.savefig(f'plots/diabetes_age_plot.png', format='png')
plt.clf()

# Plotting histogram
plt.hist(data['BMI'], bins=3, color='g')
plt.title('BMI')
plt.xlabel('BMI')
plt.ylabel('Count')
plt.savefig(f'plots/diabetes_bmi_hist.png', format='png')
plt.clf()

# Plotting scatterplot
plt.scatter(data['AGE'], data['BMI'], color='b')
plt.title('Age to BMI')
plt.xlabel('Age')
plt.ylabel('BMI')
plt.savefig(f'plots/diabetes_age_bmi_scatter.png', format='png')

plt.close()