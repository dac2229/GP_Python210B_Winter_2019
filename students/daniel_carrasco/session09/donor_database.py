class Donor_Database:
    data = {}

    def __init__(self, name=""):
        self.name = name
        if name != "":
            try:
                self.data[name]
            except KeyError:
                self.data.update({name: [0, 0]})

    def donations(self, amount=0):
        current_donation = self.data[self.name][0]
        current_count = self.data[self.name][1]
        if amount == 0:
            self.data.update(
                {self.name: [amount + current_donation, 1]})
        else:
            add_count = 1
            self.data.update(
                {self.name: [amount + current_donation, current_count + add_count]})
        return self.data[self.name][0]

    def counter(self, count=None):
        if count is not None:
            current_donation = self.data[self.name][0]
            self.data.update({self.name: [current_donation, count]})
        return self.data[self.name][1]

    @staticmethod
    def showallnames():
        return [i for i in iter(Donor_Database.data)]

    @staticmethod
    def showalldonations():
        return [Donor_Database.data[i][0]
                for i in iter(Donor_Database.data)]

    @staticmethod
    def showallcounts():
        return [Donor_Database.data[i][1]
                for i in iter(Donor_Database.data)]

    @staticmethod
    def showavg():
        return [Donor_Database.data[i][0] / Donor_Database.data[i][1]
                for i in iter(Donor_Database.data)]
