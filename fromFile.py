def SaveFile(FilePath,ArrPlans):
    f = open(FilePath,"w",encoding="utf-8")

    ArrPlans = str(ArrPlans).replace("'",'"')
    f.write(str(ArrPlans))
    f.close()



def LoadFile(FilePath):
    f = open(FilePath,"r",encoding="utf-8")

    arr = f.read()
    return eval(arr)


def Name_From_Url(s):
    return s.split("/")[-1]

