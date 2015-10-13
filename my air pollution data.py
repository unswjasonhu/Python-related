__author__ = 'Jason'

import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np

path = '/Users/jason/Dropbox/Paper/6th/trial/data/cleandata.xlsx'

#data = pd.read_excel(path,sheetname=['Vijay1','Vijay2','Han1','Han2','Jason1','Jason2','Xiaohong1','Xiaohong2','Kehu1','Kehu2'])
data1 = pd.ExcelFile(path)
#print data1.sheet_names
def save_sheet(sheetname):
    data = data1.parse(sheetname)
    return data

def count(data):
    count_data = data.iloc[:,[0,3]]
    return count_data

def sum_count(sheet):
    sum = 0
    for i in sheet['dosage']:
        sum += i
    return sum

count_vijay1 = count(save_sheet('Vijay1'))
count_vijay2 = count(save_sheet('Vijay2'))
count_han1 = count(save_sheet('Han1'))
count_han2 = count(save_sheet('Han2'))
count_jason1 = count(save_sheet('Jason1'))
count_jason2 = count(save_sheet('Jason2'))
count_xiaohong1 = count(save_sheet('Xiaohong1'))
count_xiaohong2 = count(save_sheet('Xiaohong2'))
count_kehu1 = count(save_sheet('Kehu1'))
count_kehu2  = count(save_sheet('Kehu2'))
#print count_vijay2
#print count_xiaohong1
#print count_xiaohong2
#figure1 = plt.plot(count_vijay1['timestampTime'],count_vijay1['dosage'],count_vijay2['timestampTime'],count_vijay2['dosage'])
#plt.legend(figure1,['Day1','Day2'])
#plt.plot(count_han1['timestampTime'],count_han1['dosage'],count_han2['timestampTime'],count_han2['dosage'])
#plt.plot(count_jason1['timestampTime'],count_jason1['dosage'],count_jason2['timestampTime'],count_jason2['dosage'])
#plt.plot(count_xiaohong1['timestampTime'],count_xiaohong1['dosage'],count_xiaohong2['timestampTime'],count_xiaohong2['dosage'])
#plt.plot(count_kehu1['timestampTime'],count_kehu1['dosage'],count_kehu2['timestampTime'],count_kehu2['dosage'])
#plt.plot(count_vijay1['timestampTime'],count_vijay1['dosage'],count_jason1['timestampTime'],count_jason1['dosage'],count_xiaohong1['timestampTime'],count_xiaohong1['dosage'],count_kehu1['timestampTime'],count_kehu1['dosage'])
#figure_vijay = plt.plot(count_vijay1['timestampTime'],count_vijay1['dosage'])
#plt.legend(figure_vijay,['Driving person 1'])
#figure_han = plt.plot(count_han1['timestampTime'],count_han1['dosage'])
#plt.legend(figure_han,['Driving person 2'])
#figure_jason = plt.plot(count_jason1['timestampTime'],count_jason1['dosage'])
#plt.legend(figure_jason,['Bicyling person '])
#figure_xiaohong = plt.plot(count_xiaohong1['timestampTime'],count_xiaohong1['dosage'])
#plt.legend(figure_xiaohong,['Walking person 1'])
#figure_kehu = plt.plot(count_kehu1['timestampTime'],count_kehu1['dosage'])
#plt.legend(figure_kehu,['Walking person 2'])
#plt.show()

#print sum_count(count_vijay1)
#print sum_count(count_han1)
#print sum_count(count_jason1)
#print sum_count(count_xiaohong1)
#print sum_count(count_kehu1)

total_dosage = (sum_count(count_vijay1),sum_count(count_han1),sum_count(count_jason1),sum_count(count_xiaohong1),sum_count(count_kehu1))
print total_dosage
fig, ax = plt.subplots()
ind = np.arange(5)
figure_tatal = ax.bar(ind,total_dosage,0.35,color= 'r')
plt.show()