from datetime import datetime

def n_times_day(bday1, bday2, n=2):

    # TODO_B4

    return

def main():

    print("Lab03 B-1")
    print("Today's date and the day of the week:")

    # TODO_B1

    # Your output should be like:
    # 2020-08-03 20:19:19.806211
    # Monday

    print("Lab03 B-2")
    s = input('Enter your birthday in mm/dd/yyyy format: ') #'1/15/1997'
    print("Time until your next birthday and your current age are:")

    # TODO_B2

    # Your output should be like:
    # 280 days, 3:40:40.193789
    # 22

    print("Lab03 B-3")
    print("For people born on these dates:")
    bday1 = datetime(day=15, month=1, year=1997)
    bday2 = datetime(day=11, month=10, year=2003)
    print("Double Day is")

    # TODO_B3

    # Your output should be like:
    # 2020-01-01 00:00:00 (this is not the correct answer!)

    print("Lab03 B-4")
    print("Triple Day is ", n_times_day(bday1, bday2, n=3))

if __name__ == '__main__':
    main()