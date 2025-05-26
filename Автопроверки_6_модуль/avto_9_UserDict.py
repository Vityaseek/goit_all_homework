from collections import UserDict

dict = {'k': 9, 's': 5}


class LookUpKeyDict(UserDict):
    def lookup_key(self, value):
        res = []
        for key, val in self.data.items():
            if val == value:
                res.append(key)
        return res


newdict = LookUpKeyDict(dict)

print(dict)
print(newdict)
print(newdict.lookup_key(5))
