class Base:

    def __init__(self, name1, age, name_age_dict, name_list):
        self.man1 = name1
        self.age = age
        self.Dict = name_age_dict
        self.List = name_list



class FOol(Base):
    def __init__(self, name, age):
        Base.__init__(self, name, age, name_age_dict, name_list)

    def barev(self):
        for x in self.Dict:
            if self.age < self.Dict[x]:
                print(f"{self.man1}:\nՈղջույն {x}!")
            else:
                print(f"{self.man1}:\nԲարև {x}!")
            if self.List[2] == x or self.List[3] == x:#Fool
                print(f"{x}\nԲարև {self.man1}!\n")
                continue
            print(f"{x}:\nՈղջույն  {self.man1}!\n")

from random import randint

names_list = ["Ալեքսանդր", "Արամ", "Անահիտ", "Իրինա", "Նարինե", "Արմեն", "Հայկ", "Սիլվա", "Սանասար", "Բաղդասար"]
picked_names_set = set()
picked_ages_list = []
while len(picked_names_set) < 25:
    random_index = randint(0, len(names_list)-1)
    picked_names_set.add(names_list[random_index])
for j in range(5):
    random_age = randint(20, 40)
    picked_ages_list.append(random_age)
name_age_dict = dict(zip(picked_names_set, picked_ages_list))
print(name_age_dict)
name_list = []
for s in picked_names_set:
    name_list.append(s)
