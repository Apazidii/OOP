import json
class Plan:
    def __init__(self, Date, Time, Importance, Period, StopPeriod, Text):
        self.Date = Date
        self.Time = Time
        self.Importance = Importance
        self.Period = Period
        self.StopPeriod = StopPeriod
        self.Text = Text

    def toJSON(self):
        with open("saves/testjson.json", "a", encoding="utf-8") as write_file:
            json.dump(eval(json.dumps(self, default=lambda o: o.__dict__,
                                      sort_keys=True, indent=4),), write_file)