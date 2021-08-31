from os import stat
import statistics
import pandas as pd
import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go
df = pd.read_csv('StudentsPerformance.csv')
df2 = df["gender","race/ethnicity","parental level of education","lunch","test preparation course","math score","reading score","writing score"].loc()
list = df2
mean = statistics.mean(list)
median = statistics.median(list)
mode = statistics.mode(list)
stDev = statistics.stdev(list)
firstStDev_start,firstStDev_end = mean-stDev,mean+stDev
secondStDev_start,secondStDev_end = mean-(2*stDev),mean+(2*stDev)
thirdStDev_start,thirdStDev_end = mean-(3*stDev),mean+(3*stDev)
listOfDataWithin1stStDev = [result for result in list if result>firstStDev_start and result<firstStDev_end]
listOfDataWithin2ndStDev = [result for result in list if result>secondStDev_start and result<secondStDev_end]
listOfDataWithin3rdStDev = [result for result in list if result>thirdStDev_start and result<thirdStDev_end]
print("mean is : ",mean)
print("mode is : ",mode)
print("median is : ",median)
print("Standard deviation is : ",stDev)
print('{}% of data lies within first standard deviation'.format(len(listOfDataWithin1stStDev)*100.0/len(list)))
print('{}% of data lies within second standard deviation'.format(len(listOfDataWithin2ndStDev)*100.0/len(list)))
print('{}% of data lies within third standard deviation'.format(len(listOfDataWithin3rdStDev)*100.0/len(list)))
fig = ff.create_distplot([list],["The Result"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.7],mode="lines",name=" mean"))
fig.add_trace(go.Scatter(x=[firstStDev_start,firstStDev_start],y=[0,0.7],mode="lines",name="First Standard Deviation Dtart"))
fig.add_trace(go.Scatter(x=[firstStDev_end,firstStDev_end],y=[0,0.7],mode="lines",name="First Standard Deviation End"))
fig.add_trace(go.Scatter(x=[secondStDev_start,secondStDev_start],y=[0,0.7],mode="lines",name="Second Standard Deviation Start"))
fig.add_trace(go.Scatter(x=[secondStDev_end,secondStDev_end],y=[0,0.7],mode="lines",name="Second Standard Deviation End"))
fig.show()