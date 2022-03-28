# def sort_(d, reverse = False):
#   return dict(sorted(d.items(), key = lambda x: x[1], reverse = reverse))
# dic1={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# print("ascending order:",sort_(dic1))
# print("descending order:",sort_(dic1, True))


#Sorted by keys:#

# incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
# for key in sorted(incomes):
#     print(key, ':', incomes[key])



#sorted by value:#

# incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
# def by_value(item):
#     return item[1]
# for k, v in sorted(incomes.items(), key=by_value):
#     print(k, ':', v)



#Reverse:#

# incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
# for key in sorted(incomes, reverse=True):
#     print(key, '->', incomes[key])