from collections import UserString


class NumberString(UserString):
    def number_count(self):
        return len([i for i in self.data if i.isdigit()])


sttest = NumberString("1231dsada254")


print(sttest)
print(sttest.number_count())
