from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def elementary(start_date, end_date, work_day):
    total_days = 0
    total_work_hours = 0

    temp_day = start_date
    while temp_day <= end_date:
        if temp_day.weekday() < work_day:
            if not (temp_day.month >= 6 and temp_day.month < 9):
                total_work_hours += 4
                total_days += 1
        temp_day += timedelta(days=1)
    print("\n------Бага анги------")
    print(start_date)
    print(end_date)
    weeks = count_weeks(start_date, end_date)
    fav_hours = weeks * 4
    print("7 хоногийн тоо: ", weeks)
    print("Нийт хичээлийн өдөр: ",total_days)
    print("Нийт хичээлийн цаг: ", total_work_hours)
    print("Сонирхолтой хичээлийн цаг: ", fav_hours)
    
def middle(start_date, end_date, work_day, work_hours):
    total_days = 0
    total_work_hours = 0
    
    start_date = datetime(start_date.year, 9, 1)
    
    temp_day = start_date
    while temp_day <= end_date:
        if temp_day.weekday() < work_day:
            if not (temp_day.month >= 6 and temp_day.month < 9):
                total_days += 1
                total_work_hours += 6
        temp_day += timedelta(days=1)
    
    print("\n------Дунд анги------")
    print(start_date)
    print(end_date)
    print("Нийт хичээлийн өдөр: ",total_days)
    weeks = count_weeks(start_date, end_date)
    if work_hours == 1:
        total_work_hours = weeks * 34
    fav_hours = weeks * 4
    print("7 хоногийн тоо: ", weeks)
    print("Нийт хичээлийн цаг: ", total_work_hours)
    print("Сонирхолтой хичээлийн цаг: ", fav_hours)

def high(start_date, end_date, work_day):
    total_days = 0
    total_work_hours = 0
    start_date = datetime(start_date.year, 9, 1)

    temp_day = start_date
    while temp_day <= end_date:
        if temp_day.weekday() < work_day:
            if not (temp_day.month >= 6 and temp_day.month < 9):
                total_work_hours += 4
                total_days += 1
        temp_day += timedelta(days=1)
        
    print("\n------Ахлах анги------")
    print(datetime(start_date.year, 9, 1))
    print(end_date)
    weeks = count_weeks(start_date, end_date)
    fav_hours = weeks * 4
    print("7 хоногийн тоо: ", weeks)
    print("Нийт хичээлийн өдөр: ",total_days)
    print("Нийт хичээлийн цаг: ", total_work_hours)
    print("Сонирхолтой хичээлийн цаг: ", fav_hours)


def univ(start_date, end_date, work_day):
    total_days = 0
    work_hours = 0
    practice_hours = 0
    duration = (end_date.year - start_date.year)
    start_date = datetime(start_date.year, 9, 1)
    practice_hours += 3 * work_day * 8 * duration
    temp_day = start_date
    while temp_day <= end_date:
        if temp_day.weekday() < work_day:
            if not (temp_day.month >= 6 and temp_day.month < 9):
                work_hours += 3
                total_days += 1
        temp_day += timedelta(days=1)
        
    print("\n------Дээд сургууль------")
    print(start_date)
    print(end_date)
    weeks = count_weeks(start_date, end_date)
    print("7 хоногийн тоо: ", weeks)
    print("Нийт хичээлийн өдөр: ",total_days)
    print("Нийт хичээлийн цаг: ", work_hours)
    print("Нийт дадлагын цаг:", practice_hours)
    print("Дадлагын цагийн эзлэх хувь: ", round(practice_hours/work_hours*100, 2), "%")

def find_monday(date):
    while date:
        if date.weekday() == 0:
            monday = date
            print("Эхний Даваа гараг: ", monday)
            break
        date += timedelta(days=1)
    return monday

def count_weeks(start_date, end_date):
    temp_year = start_date.year
    total_days = 0
    weeks = 0
    
    while temp_year <= end_date.year-1:
        year_weeks = 0
        year_days = 0
        start_date = datetime(temp_year, 9, 1)
        monday = find_monday(start_date)
        year_end = datetime(temp_year+1, 5, 31)   
        while monday <= year_end:
            year_days += 1
            monday += timedelta(days=1)     
        year_weeks += year_days // 7
        weeks += year_weeks
        print(year_weeks, "Долоо хоног")
        print("Хичээлийн өдөр", year_days)

        total_days += year_days
        temp_year += 1
    print("Нийт өдөр:", total_days)
    return weeks

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