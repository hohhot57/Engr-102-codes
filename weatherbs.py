from copy import deepcopy
import matplotlib.pyplot as plt
import numpy as np

# open file
with open("WeatherDataCLL.csv") as f:
    lines = [line.strip().split(",") for line in f]

header = lines.pop(0)
# convert header into a dict with index as value
header = {x: i for i, x in enumerate(header)}

# plot 4 graphs

# the first graph has 2 lines
# one for the maximum temperature and 1 for the average wind speed
# x axis is the date
# y axis is the temperature and wind speed
# the left y axis is the temperature
# the right y axis is the wind speed
max_temp = [float(x[header["Maximum Temperature (F)"]]) for x in lines]
avg_wind = [float(x[header["Average Daily Wind Speed (mph)"]]) for x in lines]
dates = [x[header["Date"]] for x in lines]
#print(avg_wind)
#print(dates)
plt.subplot(2, 2, 1)


plt.title("Maximum Temperature and Average Wind Speed")
# the x axis is the dates
# have 6 ticks on the x axis
x = np.arange(len(dates))
#plt.xticks(x[:: len(dates) // 6], dates[:: len(dates) // 6], rotation=15)

# the left y axis is the max temp
plt.plot( max_temp, label="Maximum Temperature (F)", color="r")
plt.ylabel("Maximum Temperature (F)")
plt.xlabel("Date")

plt_lines1, plt_labels1 = plt.gca().get_legend_handles_labels()

plt.twinx()
plt.plot(x, avg_wind, label="Average Daily Wind Speed (mph)", color="b")

plt_lines2, plt_labels2 = plt.gca().get_legend_handles_labels()
plt_lines = plt_lines1 + plt_lines2
plt_labels = plt_labels1 + plt_labels2
plt.legend(plt_lines, plt_labels, loc=0)


# the second graph is a histogram of the average wind speed
# the x axis is the wind speed
# the y axis is the number of days with that wind speed

plt.subplot(2, 2, 2)
plt.title("Histogram of Average Wind Speed")
# get the average wind speed from 0 to 20 mph
# make hisogram with green bars and black edges
plt.hist(avg_wind, bins=28, color="g", edgecolor="k")
# make the x axis go from 0 to 20 mph
plt.xlim(0, 20)
plt.ylim(0, 100)


plt.xlabel("Average Daily Wind Speed (mph)")
plt.ylabel("Number of Days")


# the third graph is a scatter plot of the
# average wind speed and minimum temperature
# one on each axis
min_temp = [float(x[header["Minimum Temperature (F)"]]) for x in lines]

plt.subplot(2, 2, 3)
plt.title("Scatter plot of average wind speed vs minimum temperature")
plt.scatter(min_temp, avg_wind, color="k", marker=".")
plt.xlabel("Minimum Temperature (F)")
plt.ylabel("Average Wind Speed (mph)")

# the fourth graph is a bar chart
# withe one point for each day, each month from all 3 years
# the x axis is the month
# the y axis is the average temperature for that month
# there are 2 lines 1 for the highs and 1 for the lows

plt.subplot(2, 2, 4)
plt.title("Temperature by month")
plt.xlabel("Month")
plt.ylabel("Average Temperature (F)")

# get the average temp for each month
avg_temps = {
    "1": ["1", {}],
    "2": ["2", {}],
    "3": ["3", {}],
    "4": ["4", {}],
    "5": ["5", {}],
    "6": ["6", {}],
    "7": ["7", {}],
    "8": ["8", {}],
    "9": ["9", {}],
    "10": ["10", {}],
    "11": ["11", {}],
    "12": ["12", {}],
}

low_temps = deepcopy(avg_temps)
high_temps = deepcopy(avg_temps)
# get the average high and low for each month
for line in lines:
    month, _, year = line[header["Date"]].split("/")
    # check if the year is in the avg_temps[month][1] dict
    # if not add it and add the temperature to a list for the value
    if year not in avg_temps[month][1]:
        avg_temps[month][1][year] = [float(line[header["Average Temperature (F)"]])]
        low_temps[month][1][year] = [float(line[header["Minimum Temperature (F)"]])]
        high_temps[month][1][year] = [float(line[header["Maximum Temperature (F)"]])]
    else:
        avg_temps[month][1][year].append(float(line[header["Average Temperature (F)"]]))
        low_temps[month][1][year].append(float(line[header["Minimum Temperature (F)"]]))
        high_temps[month][1][year].append(
            float(line[header["Maximum Temperature (F)"]])
        )

# get the average of the list for each year
for _, month in avg_temps.items():
    for year, temps in month[1].items():
        month[1][year] = sum(temps) / len(temps)
    month[1] = sum(month[1].values()) / len(month[1])

for _, month in low_temps.items():
    for year, temps in month[1].items():
        month[1][year] = min(temps)
    month[1] = min(month[1].values())

for _, month in high_temps.items():
    for year, temps in month[1].items():
        month[1][year] = max(temps)
    month[1] = min(month[1].values())

# plot the average temp for each month as a bar graph
# the x axis is the month
# the y axis is the average temperature for that month
# it will be yellow
plt.bar(
    [x[0] for x in avg_temps.values()],
    [x[1] for x in avg_temps.values()],
    color="y",
    label="Average Temperature",
)
#plt.xticks(rotation=45)

# plot the average low for each month
plt.plot(
    [x[0] for x in low_temps.values()],
    [x[1] for x in low_temps.values()],
    label="Low T",
    color="b",
)
# plot the average high for each month
plt.plot(
    [x[0] for x in high_temps.values()],
    [x[1] for x in high_temps.values()],
    label="High T",
    color="r",
)
plt.legend()


# increase hspace and the bottom spacing
plt.subplots_adjust(bottom=0.2, hspace=0.5)
# undereach of the 4 different graphs put
# 1, 2, 3, 4 based off the order they are in
plt.figtext(0.30, 0.5, "Plot 1", ha="center", va="center", fontsize=15)
plt.figtext(0.72, 0.5, "Plot 2", ha="center", va="center", fontsize=15)
plt.figtext(0.30, 0.05, "Plot 3", ha="center", va="center", fontsize=15)
plt.figtext(0.72, 0.05, "Plot 4", ha="center", va="center", fontsize=15)

plt.show()