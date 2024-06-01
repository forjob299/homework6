# Работа со словарями:
print('# Работа со словарями:')
my_dict = {'Иван' : 1970, 'Павел' : 1982, 'Петр' : 2001, 'Bee' : 2011}
bee = my_dict.pop('Bee')
data = {'Dict: ' : my_dict,
        'Existing value: ': my_dict['Петр'],
        'Not existing value: ' : my_dict.get('Denis', 'Такого user нет'),
        'Deleted value: ' : bee}
print(list(data.keys())[0], list(data.values())[0],'\n' +
      list(data.keys())[1], list(data.values())[1],'\n' +
      list(data.keys())[2], list(data.values())[2],'\n' +
      list(data.keys())[3], list(data.values())[3])

my_dict['Alla'] = 1999
my_dict.update({'Alex' : 1977,
                'Ben' : 1908})
print('Modified dictionary: ', my_dict)

# Работа с множествами:
print('\n' + '# Работа с множествами:')
my_set = {2, 12.5, 'Alex', True, 2, 2, True, 'Alex'}
print('Set: ', my_set)
numbers = [0, 2, 3, 4]
my_set.discard('Alex')
for i in numbers:
    my_set.add(i)
print('Modified set:', my_set)










