# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Bobby Hao
# Section:      525
# Assignment:   THE ASSIGNMENT bubba Lab 12.2
# Date:         11/20/2022
import numpy as jk
import matplotlib.pyplot as plt
from decimal import Decimal #using Decimal to save good decimal places
import csv#to read the excel 
from math import *#for any math related calc
import pandas 
from copy import deepcopy
#import weather_data

#weather_date

infile = open ('WeatherDataCLL.csv',)
readline = csv.reader(infile, delimiter=',')#read excel and use delimiter to specify the boundary between separate, 
                                                #independent regions in plain text with commas
percip = []
diffdates = []
temperature_H=[]
temperature_L = []
wind=[]
'''Create a line graph that shows both the maximum temperature and average wind speed plotted 
over the period of time. Both lines should be plotted on the same graph, with date on the x-axis, 
and different y axes for the two different measurements. (Please do not spend time dealing 
with “date data type.” Please just consider the dates in the data to be strings, or, you may 
simply consider the days as integers for plotting.) '''

for row in readline:
    if row[4] != 'Maximum Temperature (F)':#get max temp to temperature_H list
        temperature_H.append(float(row[4]))
    if row[5] != 'Minimum Temperature (F)':#min temp to t_L list
        temperature_L.append(float(row[5]))
    if row[2] != 'Precipitation (in)':#prec list
        percip.append(float(row[2]))
    if row[0] != 'Date':
        diffdates.append(row[0])#split values
    if row[1] != 'Average Daily Wind Speed (mph)':
        wind.append(float(row[1]))

#print(wind)

temperature_MAX = max(temperature_H)#using function max to find max temp
teamperature_min = min(temperature_L)#using min to ~
percip_average = sum(percip)/len(percip)#avg = sum/len
#avg_wind = sum(wind)/len(wind)

plt.subplot(2, 2, 1)

#plt.title("Maximum Temperature and Average Wind Speed")
plt.plot(temperature_H,"r-",label="maxtemp")
plt.plot(wind,"b-",label ="avg windspeed")
#print(f'3-year maximum temperature: {int(round(temperature_MAX,0))} F')#had to convert to int b/c round 0 still gives 1 decimal place
#print(f'3-year minimum temperature: {int(round(teamperature_min,0))} F')
#print(f'3-year average precipitation: {round(percip_average,3)} inches')#good rounding
#print(f'avg wind speed = {round(avg_wind,3)}')
#plt.twinx()
#plt.twiny()
#plt.ylim(0, 100)
plt.title('Maximum Temperature and Average Windspeed')
plt.xlabel('date')
plt.ylabel('Maximum Temperature F')
plt.legend(["Max temp","Avg windspeed"],loc = "upper left")


#histogram, second graph
'''create a histogram of the average wind speed. The x axis should cover a reasonable range of 
average wind speeds, and the y axis should show the number of days that had an average wind 
speed in the specific range. '''
plt.subplot(2, 2, 2)
plt.title("Histogram of Average Wind Speed")
plt.hist(wind, bins=28, color="g", edgecolor="k")

plt.xlim(0, 20)# x limit from 0 to 20
plt.ylim(0, 100)# y limit from 0 to 100


plt.xlabel("Average Daily Wind Speed, mph")
plt.ylabel("Number of Days")


#third graph Create a scatterplot indicating the relationship (or lack thereof) between average wind speed 
#and minimum temperature (one on each axis).


plt.subplot(2, 2, 3)
plt.title("Average Wind Speed vs Minimum Temperature")
plt.scatter(temperature_L, wind, color="k", marker=".")
plt.xlabel("Minimum Temperature, F")
plt.ylabel("Average Wind Speed, mph")

#fourth 
'''Create a bar chart, with one bar per calendar month (each month from all 3 years), showing the 
average temperature, along with lines indicating the highest high and lowest low temperatures 
from that month. 
a. Note: You may want to create new lists of data, but you may find it useful to use the 
max/min/sum functions on lists. 
b. This is a great problem to practice using dictionaries! '''
#strings = file.read()
refile = open ('WeatherDataCLL.csv',)
lines = [line.strip().split(",") for line in refile]

first_line = lines.pop(0)#convert to dictionary

first_line = {value: i for i, value in enumerate(first_line)}#enumerate makes values in first_line easier to access

plt.subplot(2, 2, 4)
plt.xlabel("Month")
plt.ylabel("Average Temperature (F)")
plt.title("Temperature by month")

#average temps
temperature_AVG = {"1": ["1", {}],"2": ["2", {}],"3": ["3", {}],"4": ["4", {}],"5": ["5", {}],"6": ["6", {}],"7": ["7", {}],"8": ["8", {}],"9": ["9", {}],"10": ["10", {}],"11": ["11", {}],"12": ["12", {}],
}
# find hig & low temps
temperature_LOW_L = deepcopy(temperature_AVG)#deep copy creates a new compound object before inserting copies of the items 
                                                #found in the original into it in a recursive manner.
temperature_High_H = deepcopy(temperature_AVG)

for line in lines:
    month, _, year = line[first_line["Date"]].split("/")#add temp to year if not in dict
    if year not in temperature_AVG[month][1]:
        temperature_AVG[month][1][year] = [float(line[first_line["Average Temperature (F)"]])]
        temperature_LOW_L[month][1][year] = [float(line[first_line["Minimum Temperature (F)"]])]
        temperature_High_H[month][1][year] = [float(line[first_line["Maximum Temperature (F)"]])]
    else:
        temperature_AVG[month][1][year].append(float(line[first_line["Average Temperature (F)"]]))
        temperature_LOW_L[month][1][year].append(float(line[first_line["Minimum Temperature (F)"]]))
        temperature_High_H[month][1][year].append(
            float(line[first_line["Maximum Temperature (F)"]])
        )

#find avg of the lists
for _, month in temperature_AVG.items():
    for year, temps in month[1].items():
        month[1][year] = sum(temps) / len(temps)
    month[1] = sum(month[1].values()) / len(month[1])
for _, month in temperature_High_H.items():
    for year, temps in month[1].items():
        month[1][year] = max(temps)
    month[1] = min(month[1].values())
for _, month in temperature_LOW_L.items():
    for year, temps in month[1].items():
        month[1][year] = min(temps)
    month[1] = min(month[1].values())




plt.bar(#bar graph
    [x[0] for x in temperature_AVG.values()],
    [x[1] for x in temperature_AVG.values()],
    color="y",#yellow bar
    label="Average Temperature",
)


plt.plot(#plot monthly temperature low
    [x[0] for x in temperature_LOW_L.values()],
    [x[1] for x in temperature_LOW_L.values()],
    color="b"#blue line
)

plt.plot(#plot mothly temperature high 
    [x[0] for x in temperature_High_H.values()],
    [x[1] for x in temperature_High_H.values()],
    color="r"#red line
)
plt.legend(["Low T","High T"],loc = "upper left")#put the legend on the upper left corner



plt.subplots_adjust(bottom=0.2, hspace=0.45)#fix graph spacing
#write plot 1 through plot 4 on the graph
plt.figtext(0.30, 0.52, "Plot 1", ha="center", va="center", fontsize=20)
plt.figtext(0.73, 0.52, "Plot 2", ha="center", va="center", fontsize=20)
plt.figtext(0.30, 0.09, "Plot 3", ha="center", va="center", fontsize=20)
plt.figtext(0.73, 0.09, "Plot 4", ha="center", va="center", fontsize=20)

























plt.show()
infile.close()#close file

refile.close()