__author__ = 'Jason'

import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np

path = '/Users/jason/Dropbox/Paper/6th/trial/data/data_raw.xlsx'
mypath = '/Users/jason/Dropbox/Paper/6th/trial/'

data1 = pd.ExcelFile(path)

def save_sheet(sheetname):
    data = data1.parse(sheetname)
    return data

def count(data):
    count_data = data.iloc[:,[1,4]]
    return count_data

def sum_count(sheet):
    sum = 0
    for i in sheet['dosage']:
        sum += i
    return sum

count_vijay1 = count(save_sheet('Vijay0409'))
count_vijay2 = count(save_sheet('Vijay1009'))
count_vijay3 = count(save_sheet('Vijay1109'))
count_han1 = count(save_sheet('Han0409'))
count_han2 = count(save_sheet('Han0509'))
count_han3 = count(save_sheet('Han1009'))
count_han4 = count(save_sheet('Han1109'))

#figure1 = plt.plot(count_vijay1['timestampTime'],count_vijay1['dosage'],count_vijay2['timestampTime'],count_vijay2['dosage'],count_vijay3['timestampTime'],count_vijay3['dosage'])
figure2 = plt.plot(count_han1['timestampTime'],count_han1['dosage'],count_han2['timestampTime'],count_han2['dosage'],count_han3['timestampTime'],count_han3['dosage'],count_han4['timestampTime'],count_han4['dosage'])
figure_axes = plt.gca()
figure_axes.set_ylim([0,40])
plt.show()
