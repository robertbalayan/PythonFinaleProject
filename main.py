from random import randint

# class Base:
#     def __init__(self, name1, name2, name3, name4, name5):
#         self.man1 = name1
#         self.man2 = name2
#         self.man3 = name3
#         self.man4 = name4
#         self.man5 = name5
names_list = ["Ալեքսանդր", "Արամ", "Անահիտ", "իրինա", "Նարինե", "Արմեն", "Հայկ", "Սիլվա", "Սանասար", "Բաղդասար"]
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








