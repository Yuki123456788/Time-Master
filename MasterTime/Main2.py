import json
import data_process as dp

with open("file.json","r",encoding="utf-8") as f:
    data = json.load(f)

print("***[ Time Master ] ***")
choice = input("1:add new thing\n2:start doing thing\n0:exit\n")
while choice!='0':
    if choice=='1':
        work = input("New work : ")
        print("Deadline")
        year = input("Year(xxxx) : ")
        month = input("Month(xx) : ")
        day = input("Day(xx) : ")
        print("Time")
        hour = input("Hour(xx) : ")
        min = input("Minute(xx) : ")
        deadline = year+'.'+month+'.'+day+'.'+hour+'.'+min

        importance = input("\n0:not important\n1:important\n")

        dp.add_work(data, work, deadline, importance)
        with open("file.json","w",encoding="utf-8") as f:
            json.dump(data,f,ensure_ascii=False,indent = 4)     
    elif choice=='2':
        # todo
        which_work = input("Which work : ")
        dp.start_work(data, which_work)
        input("Press 1 when finished : ")
        dp.end_work(data, which_work)
        with open("file.json","w",encoding="utf-8") as f:
            json.dump(data,f,ensure_ascii=False,indent = 4)
    else:
        print("Invalid input, please input 1, 2 or 0\n")

    print("\n1:add new thing\n2:start doing thing\n0:exit")
    choice = input()