import csv
import statistics as st
import pandas as pd
import datetime
import pygal

filename = "activity.csv"
with open(filename) as f:
    reader = csv.reader(f)
    headerRow = next(reader)
    
    newfile = open('newActivity.csv','w')
    newfile.write(str(headerRow[0])+","+str(headerRow[1])+","+str(headerRow[2])+",day")
    newfile.write("\n")
    
    n = 0
    for row in reader:
        # changes the missing data for number of steps to value of '0'
        if (row[0] == 'NA'):
            row[0] = 0
            n+=1
        # creates a new "day of the week" column based on the date
        if pd.to_datetime(row[1]).weekday() >= 5:
            day = "Weekend"
        else:
            day = "Weekday"
        newfile.write(str(row[0])+","+str(row[1])+","+str(row[2])+","+str(day))
        newfile.write("\n")
        
    newfile.close()
    print("The total number of missing values in the dataset is:", n)
    
filename = "newActivity.csv"
with open(filename) as f:
    reader = csv.reader(f)
    headerRow = next(reader)

    dictDate = {}
    dictInterval = {}
    dictIntervalWeekday = {}
    dictIntervalWeekend = {}

    for row in reader:
        steps = row[0]   
        date = row[1]
        interval = int(row[2])
        day = row[3]

        # Dicts where all the values are stored, unseparated
        dictDate.setdefault(str(date), [])
        dictDate[str(date)].append(int(steps))

        dictInterval.setdefault(interval, [])
        dictInterval[interval].append(int(steps))

        # Separates the values into respective dicts depending on whether the date was a weekday or a weekend
        if day == "Weekday":
            dictIntervalWeekday.setdefault(interval, [])
            dictIntervalWeekday[interval].append(int(steps))
        elif day == "Weekend":
            dictIntervalWeekend.setdefault(interval, [])
            dictIntervalWeekend[interval].append(int(steps))

    listDate = []
    listTotal = []

    for i in dictDate.keys():
        listDate.append(i)
        listTotal.append(sum(dictDate.get(i)))

    med = sorted(listTotal)
    print("Mean :", round(st.mean(listTotal), 2))
    print("Median :", st.median(med))

    # creates the histogram
    hist = pygal.Bar()
    hist.title = "Total Steps Taken per Day"
    hist.x_title = "Steps per day"
    hist.x_labels = listDate
    hist.add("Total Number of Steps", listTotal)
    hist.render_to_file('ActivityChart.svg')

    listInterval = []
    listAverageSteps = []
    listAverageStepsWeekday = []
    listAverageStepsWeekend = []

    for i in dictInterval.keys():
        listInterval.append(i)
        avg = st.mean(dictInterval.get(i))
        avg = round(avg, 2)
        listAverageSteps.append(avg)

    for i in dictIntervalWeekday.keys():
        avg = st.mean(dictIntervalWeekday.get(i))
        avg = round(avg, 2)
        listAverageStepsWeekday.append(avg)

    for i in dictIntervalWeekend.keys():
        avg = st.mean(dictIntervalWeekend.get(i))
        avg = round(avg, 2)
        listAverageStepsWeekend.append(avg)

    print("Max :", max(listAverageSteps))
    print("Most Active Interval :", listInterval[listAverageSteps.index(max(listAverageSteps))])

    # creates the line graph
    line = pygal.Line()
    line.title = "Average Steps per Interval"
    line.x_title = "Time of Day / Minutes (in 5-min intervals)"
    line.x_labels = listInterval
    line.y_title = "Average Number of Steps"
    line.add("Weekdays", listAverageStepsWeekday)
    line.add("Weekends", listAverageStepsWeekend)
    line.render_to_file('AverageSteps.svg')
