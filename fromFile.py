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



def SaveFile(FilePath,ArrPlans):
    f = open(FilePath,"w",encoding="utf-8")

    ArrPlans = str(ArrPlans).replace("'",'"')
    ArrPlans = ArrPlans.replace("}, {","},\n{")
    f.write(str(ArrPlans))
    f.close()



def LoadFile(FilePath):
    f = open(FilePath,"r",encoding="utf-8")

    arr = f.read()
    arr = arr.replace("},\n{","}, {")
    return eval(arr)


def Name_From_Url(s):
    return s.split("/")[-1]


