even =''
odd=''
for index, char in enumerate (['Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',]):
    if (index % 2 == 0):
        even += char
    else: odd += char
print (odd)