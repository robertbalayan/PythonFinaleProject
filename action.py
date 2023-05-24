from random import randint

names_list = ["Ալեքսանդր", "Արամ", "Անահիտ", "Իրինա", "Նարինե", "Արմեն", "Հայկ", "Սիլվա", "Սանասար", "Բաղդասար"]
picked_names_set = set()
picked_ages_list = []
while len(picked_names_set) < 5:
    random_index = randint(0, len(names_list)-1)
    picked_names_set.add(names_list[random_index])
for j in range(5):
    random_age = randint(20, 40)
    picked_ages_list.append(random_age)
name_age_dict = dict(zip(picked_names_set, picked_ages_list))
print(name_age_dict)
n = 0

class Base:

    def __init__(self, name1, name2, name3, name4, name5):
        self.man1 = name1
        self.man2 = name2
        self.man3 = name3
        self.man4 = name4
        self.man5 = name5
        self.list = [self.man1, self.man2, self.man3, self.man4, self.man5]
        self.K = None

class Realist(Base):
    def Barev(self):
        for self.K in self.list:
            print(f"{self.man1}\nՈղջույն {self.list[self.list.index(self.K) + 1]}")
            print(f"{self.list[self.list.index(self.K) + 1]}\nԲարև {self.man1}")
            if self.K == self.man4:
                break




for Name in name_age_dict:
    if n == 0:
        name1 = Name
    elif n == 1:
        name2 = Name
    elif n == 2:
        name3 = Name
    elif n == 3:
        name4 = Name
    else:
        name5 = Name
    n += 1

arajin = Realist(name1, name2, name3, name4, name5)
arajin.Barev()

