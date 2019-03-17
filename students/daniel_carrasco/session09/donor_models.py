import donor_database as ddb


class Donor:
    def __init__(self, name=None):
        self.name = name
        ddb.Donor_Database(name)

    @property
    def donations(self):
        return ddb.Donor_Database(self.name).donations()

    @donations.setter
    def donations(self, val):
        ddb.Donor_Database(self.name).donations(val)

    @property
    def counter(self):
        return ddb.Donor_Database(self.name).counter()

    @counter.setter
    def counter(self, val):
        ddb.Donor_Database(self.name).counter(val)

    @staticmethod
    def showallnames():
        return [i for i in iter(ddb.Donor_Database.data)]

    @staticmethod
    def showalldonations():
        return [ddb.Donor_Database.data[i][0]
                for i in iter(ddb.Donor_Database.data)]

    @staticmethod
    def showallcounts():
        return [ddb.Donor_Database.data[i][1]
                for i in iter(ddb.Donor_Database.data)]

    @staticmethod
    def showavg():
        return [ddb.Donor_Database.data[i][0] / ddb.Donor_Database.data[i][1]
                for i in iter(ddb.Donor_Database.data)]
