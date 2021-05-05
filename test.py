import json
import classes
class J:
    name = "alex"
    age =18
    sex = "man"
    def __init__(self, name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def toJSON(self):

        with open("testjson.json", "a") as write_file:
            json.dump(eval (json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)), write_file)


pla.toJSON()




