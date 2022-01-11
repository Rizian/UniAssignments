import csv
import statistics as st
import pandas as pd
import datetime
import pygal

filename = 'activity.csv'
with open(filename) as f:
    reader = csv.reader(f)
    headerRow = next(reader)
    
    wr = open('newActivity.csv','w')
    wr.write(str(headerRow[0])+","+str(headerRow[1])+","+str(headerRow[2])+",day")
    wr.write("\n")
    
    n=0
    for row in reader:
        if (row[0] == 'NA'):
            row[0] = 0
            n+=1
        if pd.to_datetime(row[1]).weekday() >= 5:
            day = "Weekend"
        else:
            day = "Weekday"
        wr.write(str(row[0])+","+str(row[1])+","+str(row[2])+","+str(day))
        wr.write("\n")
        
    wr.close()
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

    print("Mean :", round(st.mean(listTotal), 2))
    med = sorted(listTotal)
    print("Median :", st.median(med))

    hist = pygal.Bar()
    hist.title = "Total steps taken per day"
    hist.x_title = "Steps per day"
    hist.x_labels = listDate
    hist.add("Total number of steps", listTotal)
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

    line = pygal.Line()
    line.title = "Average Steps per Interval"
    line.x_title = "Time of Day / Minutes (in 5-min intervals)"
    line.x_labels = listInterval
    line.y_title = "Average Number of Steps"
    line.add("Weekdays", listAverageStepsWeekday)
    line.add("Weekends", listAverageStepsWeekend)
    line.render_to_file('AverageSteps.svg')
