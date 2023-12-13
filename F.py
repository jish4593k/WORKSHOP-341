import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import seaborn as sns
import torch
from tkinter import *
from tkinter import ttk

def array(data):
    aux = data

    aux = aux.interpolate()
    arr = np.array(aux)
    return arr



def plot_original_vs_estimated(original, estimated, model_name):
    plt.plot(original, label='Original Doses')
    plt.plot(estimated, label='Estimated Doses (' + model_name + ' model)')
    plt.xlabel('Days')
    plt.ylabel('Doses')
    plt.title('Original vs Estimated Doses using ' + model_name + ' model')
    plt.legend()
    plt.show()

def plot_derivatives(dx, d2x, model_name):
    plt.plot(dx, label='First Derivative')
    plt.plot(d2x, label='Second Derivative')
    plt.xlabel('Days')
    plt.ylabel('Derivatives')
    plt.title('First and Second Derivatives using ' + model_name + ' model')
    plt.legend()
    plt.show()

def perform_statistical_analysis(data, model_name):
    mean_doses = np.mean(data)
    std_doses = np.std(data)
    
    print("Statistical Analysis using " + model_name + " model:")
    print("Mean of Doses: {:.2f}".format(mean_doses))
    print("Standard Deviation of Doses: {:.2f}".format(std_doses))
    print()


def show_original_vs_estimated_gui(original, estimated, model_name):
    top = Tk()
    top.title("Original vs Estimated Doses")

    plt.figure(figsize=(8, 4))
    plt.plot(original, label='Original Doses')
    plt.plot(estimated, label='Estimated Doses (' + model_name + ' model)')
    plt.xlabel('Days')
    plt.ylabel('Doses')
    plt.title('Original vs Estimated Doses using ' + model_name + ' model')
    plt.legend()

    canvas = FigureCanvasTkAgg(plt.gcf(), master=top)
    canvas.draw()
    canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=1)

    top.mainloop()

vacinas_detalhe = pd.read_csv(os.path.join(os.getcwd(), "vacinas.csv"))




plot_original_vs_estimated(doses1, doses1_est, 'Sigmoid')
plot_original_vs_estimated(doses2, doses2_est, 'Sigmoid')


dx1, d2x1 = derivative(doses1)
dx2, d2x2 = derivative(doses2)
plot_derivatives(dx1, d2x1, 'Sigmoid')
plot_derivatives(dx2, d2x2, 'Sigmoid')


perform_statistical_analysis(doses1, 'Sigmoid')
perform_statistical_analysis(doses2, 'Sigmoid')


show_original_vs_estimated_gui(doses1, doses1_est, 'Sigmoid')
show_original_vs_estimated_gui(doses2, doses2_est, 'Sigmoid')

