import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scikits.statsmodels.api as sm
from sklearn.metrics import mean_absolute_error

def mean_absolute_percentage_error(y_true, y_pred):
    j = 0
    mean_errorab2 = 0
    for i in range(len(y_true)):
        mean_errorab1 = np.abs((y_true[i] - y_pred[i]) / y_true[i])
        mean_errorab2 += mean_errorab1
        j +=1
    mean_errorab = mean_errorab2 / j
    return mean_errorab

def mean_value(num,data):
    totalvalue = 0
    j=0
    for i in range(len(data)):
        if data['coreal'][i] == num:
            totalvalue += data['co'][i]
            j += 1
    meanvalue = totalvalue / j
    return meanvalue

#plt.title('Correlations between measurements from CO analyzer and One Node sensor')
plt.xlabel('True CO concentrations provided by CO analyzer Ecotech EC9830 (PPM)',fontsize = 15)
plt.ylabel('CO readings from one Node sensor (PPM)',fontsize = 15)
path = '/Users/jason/Dropbox/Paper/5th/revision/calibration/output21102015raw3.csv'
path1 ='/Users/jason/Dropbox/Paper/5th/revision/calibration/output21102015raw2.csv'
path2 = '/Users/jason/Dropbox/Paper/5th/revision/'

data = pd.read_csv(path)
data1 =pd.read_csv(path1)
#print data
mean1 = mean_value(40.89,data)
mean2 = mean_value(30.59,data)
mean3 = mean_value(20.48,data)
mean4 = mean_value(10.47,data)
mean5 = mean_value(5.46,data)
mean6 = mean_value(2.41,data)
meanx = [40.89,30.59,20.48,10.47,5.46,2.41]
meany = [mean1,mean2,mean3,mean4,mean5,mean6]
y = data['co']
x = data['coreal']
y1 =data1['co']
x1 =data1['coreal']
for index in range (len(x)):
    figure1 =plt.scatter(x[index],y[index],c='blue')
for index1 in range (len(meanx)):
    figure2  =plt.scatter(meanx[index1],meany[index1], c= 'red',marker ='v' ,s = 100)

results = sm.OLS(y,sm.add_constant(x)).fit()
results1 = sm.OLS(y1,sm.add_constant(x1)).fit()
print results.summary()
print results1.summary()
x_plot = np.linspace(0,45,100)
x1_plot = np.linspace(0,45,100)
figure3, = plt.plot(x_plot, x_plot*results.params[0] + results.params[1],color = 'blue')
figure4, = plt.plot(x1_plot, x1_plot*results1.params[0] + results1.params[1],color = 'red')
axes = plt.gca()
axes.set_ylim([0,45])
axes.set_xlim([0,45])
plt.text(5,41,'y = 1.021x - 0.776', fontsize = 15, color = 'blue')
plt.text(5,38,r'$R^2$=0.9953', fontsize = 15, color = 'blue')
plt.text(5,36,'MAE = 0.7662', fontsize = 15, color = 'blue')
plt.text(5,34,'MAPE = 0.1202', fontsize = 15, color = 'blue')
plt.text(5,30,'y = 0.9537x + 0.3019', fontsize = 15, color = 'red')
plt.text(5,27,r'$R^2$=0.9897', fontsize = 15, color = 'red')
plt.text(5,25,'MAE = 1.0886', fontsize = 15, color = 'red')
plt.text(5,23,'MAPE = 0.0621', fontsize = 15, color = 'red')
plt.legend([figure1,figure2,figure3,figure4],('All Points','Mean Values','Linear(All Values)','Linear(Mean Values)'),loc=4)

meanerror1 = mean_absolute_error(y,x)
meanerror2 = mean_absolute_error(y1,x1)
print meanerror2
print mean_absolute_percentage_error(x, y)
print mean_absolute_percentage_error(x1, y1)
plt.savefig(path2 + 'calibration_result.eps',format = 'eps', dpi = 2400)
plt.show()

