import json
import time
import datetime
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets


with open("file.json","r",encoding="utf-8") as f:
    data = json.load(f)
#print(data["作業"])

'''for line in data.keys():
    print(line)
    for a,b in data[line].items():
        print(a)
        print(str(b))'''
        
def get_time(): #取得當前時間
    localtime = time.localtime()
    result = time.strftime("%Y.%m.%d.%H.%M", localtime) #年.月.日.時.分
    return result

def new_data(key , val): #新增新的數據
    dat = {}
    dat[key] = val
    return dat
    
def new_work(data , newdata , work): #新增新的工作並加入一項據
    data[work] = newdata
    return data

def add_data_to_work(data , key, work, val): #增加新的數據進去工作
    newdata = new_data(key, val)
    
    if work in data:
        data[work].update(newdata)
    else:
        new_work(data, newdata , work)

def add_work(data , work, deadline, importance): #按新增可以直接增加工作跟基本數據
    add_data_to_work(data, "deadline" , work, deadline)
    add_data_to_work(data, "important" , work, importance)
    data[work]["important"]=int(data[work]["important"]) # str to int
    judge_urgent(data)

    

def start_work(data , work): #開始工作
    now = get_time()
    newdata = new_data("nowtime",now)
    data[work].update(newdata)

    localtime = time.localtime()
    result = time.strftime("%U", localtime) # 哪個禮拜
    whichWeek = new_data("whichWeek", result)
    data[work].update(whichWeek)

    result2 = time.strftime("%w", localtime) # 星期幾
    whichWeekDay = new_data("whichWeekDay", result2)
    data[work].update(whichWeekDay)

    start = new_data("start", 1)
    data[work].update(start)
    

def end_work(data , work): #結束工作
    now = get_time()
    newdata = new_data("endtime",now)
    data[work].update(newdata)
    time_lag(data , work)
    data[work]["start"] = 0
    
    
def time_lag(data ,work):
    start = data[work]["nowtime"]
    end = data[work]["endtime"]
    start = start.split(".")
    end = end.split(".")
    d1 = datetime.datetime((int)(start[0]),(int)(start[1]),(int)(start[2]),(int)(start[3]),(int)(start[4]))
    d2 = datetime.datetime((int)(end[0]),(int)(end[1]),(int)(end[2]),(int)(end[3]),(int)(end[4]))
    interval = d2 - d1
    newdata = new_data("usetime_seconds",interval.seconds) #秒數1分鐘改一次
    data[work].update(newdata)
    newdata = new_data("usetime_days",interval.days)
    data[work].update(newdata)
    
def judge_urgent(data):
    now = get_time()
    
    for k in data:
        deadline = data[k]["deadline"] #截止時間
        start = now.split(".")
        end = deadline.split(".")
        d1 = datetime.datetime((int)(start[0]),(int)(start[1]),(int)(start[2]),(int)(start[3]),(int)(start[4]))
        d2 = datetime.datetime((int)(end[0]),(int)(end[1]),(int)(end[2]),(int)(end[3]),(int)(end[4]))
        interval = d2 - d1
        if interval.days >= 3:
            data[k]["urgent"] = 0 # not urgent
        else:
            data[k]["urgent"] = 1 # urgent

def get_total_data(flag):
    y_t = [0, 0, 0, 0]
    # print(data)

    # get today's time
    localtime = time.localtime()
    # year.month.day.week
    today = time.strftime("%Y.%m.%d.%U", localtime)
    today = today.split(".")

    for thing in data:
        if "endtime" in data[thing]:
            start_date = data[thing]["nowtime"]
            start_date = start_date.split(".")

            if flag==0: # Day
                year_j = today[0]==start_date[0]
                month_j = today[1]==start_date[1]
                day_j = today[2]==start_date[2]
                judge = year_j and month_j and day_j
            elif flag==1: # Week
                year_j = today[0]==start_date[0]
                week_j = today[3]==data[thing]["whichWeek"]
                judge = year_j and week_j
            elif flag==2: # Month
                year_j = today[0]==start_date[0]
                month_j = today[1]==start_date[1]
                judge = year_j and month_j
            elif flag==3: # Year
                judge = today[0]==start_date[0]

            if judge:
                i=0
                if data[thing]["important"]==1 and data[thing]["urgent"]==1:
                    i=0
                elif data[thing]["important"]==1 and data[thing]["urgent"]==0:
                    i=1
                elif data[thing]["important"]==0 and data[thing]["urgent"]==1:
                    i=2
                elif data[thing]["important"]==0 and data[thing]["urgent"]==0:
                    i=3
                y_t[i]+=data[thing]["usetime_seconds"]
    for i in range(4):
        y_t[i]/=3600
    return y_t

# time: 1->week, 2->month, 3->year
# type: 0->im_ur, 1->im_nur, 2->nim_ur, 3->nim_nur
def get_specific_data(flag):
    # get today's time
    localtime = time.localtime()
    # year.month.day.week
    today = time.strftime("%Y.%m.%d.%U.%a", localtime)
    today = today.split(".")
    y=[]

    if flag==1:
        y = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
    elif flag==2:
        y = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    elif flag==3:
        y = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    for thing in data:
        row=0
        col=0
        if "endtime" in data[thing]:
            start_date = data[thing]["nowtime"]
            start_date = start_date.split(".")

            if flag==1: # Week
                year_j = today[0]==start_date[0]
                week_j = today[3]==data[thing]["whichWeek"]
                judge = year_j and week_j
            elif flag==2: # Month
                year_j = today[0]==start_date[0]
                month_j = today[1]==start_date[1]
                judge = year_j and month_j
            elif flag==3: # Year
                judge = today[0]==start_date[0]
            
            if judge:
                row=0
                if data[thing]["important"]==1 and data[thing]["urgent"]==1:
                    row=0
                elif data[thing]["important"]==1 and data[thing]["urgent"]==0:
                    row=1
                elif data[thing]["important"]==0 and data[thing]["urgent"]==1:
                    row=2
                elif data[thing]["important"]==0 and data[thing]["urgent"]==0:
                    row=3
            else:
                continue

            if flag==1: # week
                col=int(data[thing]["whichWeekDay"])
            elif flag==2: # month
                if int(today[2])>=7:
                    col=0
                elif int(today[2])>7 and int(today[2])<=14:
                    col=1
                elif int(today[2])>14 and int(today[2])<=21:
                    col=2
                elif int(today[2])<21:
                    col=3
            elif flag==3: # year
                col=int(start_date[1])-1
            y[row][col]+=data[thing]["usetime_seconds"]

    for i in range(4):
        for j in range(len(y[i])):
            y[i][j]/=3600
    return y

def get_display_data(container, importance, urgency):
    # container.clear()
    for thing in data:
        imp = data[thing]["important"] == importance
        urg = data[thing]["urgent"] == urgency
        if "endtime" not in data[thing] and imp and urg:
            #新建個按鈕
            btn = QPushButton(thing)
            btn.setGeometry(QtCore.QRect(10, 10, 525, 70))
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
            sizePolicy.setHorizontalStretch(10)
            sizePolicy.setVerticalStretch(50)
            sizePolicy.setHeightForWidth(btn.sizePolicy().hasHeightForWidth())
            btn.setSizePolicy(sizePolicy)
            btn.setStyleSheet("QPushButton {\n"
    "    background-color: #FFF;\n"
    "    border: 0px;\n"
    "    border-radius: 2px;\n"
    "    margin-bottom:3px;\n"
    "}")
            #新建個Item
            item = QListWidgetItem()
            #將item新增到list
            container.addItem(item)
            #將widget新增到item
            container.setItemWidget(item,btn)
            # btn.clicked.connect(lambda:timer(thing))
# todo
# def timer(thing):
#     if "start" not in data[thing]:
#         start_work(data, thing)
#         print(f"start{thing}")
#     elif data[thing]["start"]==1:
#         end_work(data, thing)
#         print(f"end{thing}")

with open("file.json","w",encoding="utf-8") as f:
    json.dump(data,f,ensure_ascii=False,indent = 4)