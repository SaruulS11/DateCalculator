from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def elementary(start_date, end_date, work_day):
    print("\n------Бага анги------")
    count_weeks(start_date, end_date, work_day, 4)
    
def middle(start_date, end_date, work_day, work_hours):
    
    print("\n------Дунд анги------")
    count_weeks(start_date, end_date, work_day, 6)

def high(start_date, end_date, work_day):

    print("\n------Ахлах анги------")
    count_weeks(start_date, end_date, work_day, 6)


def univ(start_date, end_date, work_day):
    practice_hours = 0
    duration = (end_date.year - start_date.year)
    practice_hours += 3 * work_day * 8 * duration
    print("\n------Дээд сургууль------")
    
    work_hours = count_weeks(start_date, end_date, work_day, 3)
    print("Нийт дадлагын цаг:", practice_hours)
    print("Дадлагын цагийн эзлэх хувь: ", round(practice_hours/work_hours*100, 2), "%")

def find_monday(date):
    while date:
        if date.weekday() == 0:
            break
        date += timedelta(days=1)
    return date

def count_days(start_date):
    days = 0
    end_date = datetime(start_date.year+1, 5, 31)
    temp_day = start_date
    while temp_day <= end_date:
        if not (temp_day.month >= 6 and temp_day.month < 9):
            days += 1
        temp_day += timedelta(days=1)
    return days

def count_work_days(start_date, end_date, work_day):
    temp_day = start_date
    result = 0
    while temp_day <= end_date:
        if temp_day.weekday() < work_day:
            result += 1
        temp_day += timedelta(days=1)
    return result

def count_weeks(start_date, end_date, work_day, work_hours):
    temp_year = start_date.year
    total_working = 0
    total_days = 0
    weeks = 0
    angi=1
    
    while temp_year <= end_date.year-1:
        working = 0
        year_weeks = 0
        year_days = 0
        week_days = 0
        start_date = datetime(temp_year, 9, 1)
        begin = find_monday(start_date)
        year_end = datetime(temp_year+1, 5, 31)   
        year_days += count_days(start_date)
        working = count_work_days(start_date, year_end, work_day)
        while begin <= year_end:
            week_days += 1
            begin += timedelta(days=1)     
        year_weeks += week_days // 7
        weeks += year_weeks
        total_days += year_days
        total_working += working
        print(angi,"- р анги: ", start_date.year, "-", year_end.year, " | ",year_weeks, "долоо хоног |", year_days, "өдөр |", working, "ажлын өдөр")
        angi += 1
        temp_year += 1
    fav_hours = weeks * 4
    print("7 хоногийн тоо: ", weeks)
    print("Нийт өдөр:", total_days)
    print("Нийт ажлын өдөр:", total_working)
    print("Нийт хичээлийн цаг:", work_hours * total_working)
    print("Сонирхолтой хичээлийн цаг: ", weeks, "* 4 =",fav_hours)
    return work_hours*total_working

# Эхлэлийн огноо олгох
start_date = datetime(1978, 9, 1)
end_date = datetime(1993, 5, 31)
start_date1 = datetime(2006, 9, 1)
end_date1 = datetime(2022, 5, 31)

print("\nЭхний хугацаа: \n")
middle_start = datetime(start_date.year + 3, 5, 31)
elementary(start_date, middle_start, 6)
high_start = datetime(middle_start.year + 5, 5, 31)
middle(middle_start, high_start, 6, 1)
univ_start = datetime(high_start.year + 2, 5, 31)
high(high_start, univ_start, 6)
univ(univ_start, end_date, 6)

print("\nДараагийн хугацаа: \n")
middle_start1 = datetime(start_date1.year + 5, 5, 31)
elementary(start_date1, middle_start1, 5)
high_start1 = datetime(middle_start1.year + 4, 5, 31)
middle(middle_start1, high_start1, 5, 2)
univ_start1 = datetime(high_start1.year + 3, 5, 31)
high(high_start1, univ_start1, 5)
univ(univ_start1, end_date1, 5)

#2:36