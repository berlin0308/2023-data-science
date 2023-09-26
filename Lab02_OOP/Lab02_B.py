import datetime

def n_times_day(bday1, bday2, n=2):

    x_day = datetime.datetime.now()
    n_times_day = None
    while n_times_day is None:
        # print(x_day)
        if (x_day-bday1).days*n == (x_day-bday2).days:
            # print((x_day-bday1).days)
            # print((x_day-bday2).days)
            n_times_day = x_day
        
        x_day = x_day - datetime.timedelta(days=1)

    n_times_day = n_times_day.replace(hour=0, minute=0, second=0, microsecond=0)
    print(n_times_day)

    return n_times_day

def main():

    print("\n\nLab03 B-1")
    print("Today's date and the day of the week:")

    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    today_date = datetime.datetime.now() 
    print(today_date)
    print(weekdays[today_date.weekday()])

    # Your output should be like:
    # 2020-08-03 20:19:19.806211
    # Monday

    print("\n\nLab03 B-2")
    s = input('Enter your birthday in mm/dd/yyyy format: ') #'1/15/1997'
    # s = '1/15/1997'
    # s = '11/15/1997'
    bd = datetime.datetime(year=int(s.split('/')[-1]),month=int(s.split('/')[-3]),day=int(s.split('/')[-2]))
    print("Birthday:",bd)

    print("Time until your next birthday and your current age are:")
    now = datetime.datetime.now()

    next_bd = bd
    if now.month > bd.month or (now.month == bd.month and now.day >= bd.day):
        next_bd = next_bd.replace(year=now.year+1)
    else:
        next_bd = next_bd.replace(year=now.year)

    # print("Next birthday:",next_bd,"\n")
    till_bd = next_bd - now
    print(till_bd)

    age = next_bd.year - bd.year -1
    print(age)

    # Your output should be like:
    # 280 days, 3:40:40.193789
    # 22

    print("\n\nLab03 B-3")
    # print("For people born on these dates:")
    bday1 = datetime.datetime(day=15, month=1, year=1997)
    bday2 = datetime.datetime(day=11, month=10, year=2003)

    # bday2 should earlier than bday1
    if bday2 > bday1:
        temp = bday1
        bday1 = bday2
        bday2 = temp

    # print(bday1,bday2)

    print("Double Day is")

    x_day = datetime.datetime.now()
    double_day = None
    while double_day is None:
        # print(x_day)
        if (x_day-bday1).days*2 == (x_day-bday2).days:
            # print((x_day-bday1).days)
            # print((x_day-bday2).days)
            double_day = x_day
        
        x_day = x_day - datetime.timedelta(days=1)

    double_day = double_day.replace(hour=0, minute=0, second=0, microsecond=0)
    print(double_day)

    # Your output should be like:
    # 2020-01-01 00:00:00 (this is not the correct answer!)

    print("\n\nLab03 B-4")
    print("Triple Day is ", n_times_day(bday1, bday2, n=3))

if __name__ == '__main__':
    main()