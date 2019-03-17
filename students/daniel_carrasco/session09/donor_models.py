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


