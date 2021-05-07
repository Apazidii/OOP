import datetime

import calendar

def Periods(a,b,period):

    def add_months(sourcedate, months):
        month = sourcedate.month - 1 + months
        year = sourcedate.year + month // 12
        month = month % 12 + 1
        day = min(sourcedate.day, calendar.monthrange(year,month)[1])
        return datetime.date(year, month, day)




    k = a
    res = []
    while k<=b:
        res.append(k)
        if period =="EveryDay":
            k = k+datetime.timedelta(days=1)
        elif period =="EveryWeek":
            k = k + datetime.timedelta(weeks=1)
        elif period =="EveryMouth":
            k = add_months(k,1)
    return res




