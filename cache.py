#Fully associative memory cache simulator

class Slot(object):

    def __init__(self, id, timestamp):
        self.timestamp = timestamp
        self.id = id
        self.data = []

    def getval(self):
        return self.data[-1] if len(self.data) > 0 else -1

    def addval(self, new):
        self.data.append(new)

    def hasseen(self, num):
        return num in self.data


class FACache(object):

    def __init__(self, numslots):
        self.timestamp = 0
        self.slots = []
        for i in range(numslots):
            self.slots.append(Slot(id=i, timestamp=self.timestamp))
            self.timestamp += 1

    def getlruslot(self):
        min = 9999999
        for slot in self.slots:
            if slot.timestamp < min:
                minslot = slot
                min = minslot.timestamp
        # print(f"Min slot is slot# {minslot.id} with timestamp {min}")
        return minslot

    def addval(self, newval):

        # Handle hit
        for slot in self.slots:
            if slot.getval() == newval:
                print(f"{newval} HIT slot id {slot.id}")
                slot.timestamp = self.timestamp
                self.timestamp += 1
                return

        # Handle miss
        capacitymiss = any([s.hasseen(newval) for s in self.slots])
        slot = self.getlruslot()
        slot.addval(newval)
        slot.settimestamp = self.timestamp
        self.timestamp += 1
        print(f" {newval} Capacity miss, value added to slot {slot.id} with timestamp {self.timestamp}" if capacitymiss else f" {newval} Compulsory miss, value added to slot {slot.id} with timestamp {self.timestamp}")
        return

tags = [1285,1550,1673,359,777,1992,1285,1746,1550,1627,1990,1746,1636,1227,359,1227,1992,1285,777,1636,1990,1746,1272,359]
c1 = FACache(numslots=8)
for tag in tags:
    c1.addval(tag)



