# Д.з.
# Прочитати текстовий csv-файл.
# Підрахувати для кожного прізвища з першого стовпця суму чисел зі второго стовпця
# Зберегти результат у  csv-файл, де стовпці відокремлені табуляцією.

# код має бути об'єктом, який опрацьовує ім'я файла для зчитування в методі init()
# в  якому здійснюються дві дії:
#  1)  зчитування файлу
#  2)  очистка даних  -   якщо у зчитаному рядку більше 2-х елементів,  або  менше 2-х елементів, такий рядок ігнорується

# за зчитування даних і за очистку даних відповідають два окремих методи, імена яких починаються з одного підкреслення.

# Крім цього,, клас має ще два методи:

# calculate()
# to_csv()
# які відповідно роблять обчислення суми по кожному прізвищу і збереження результату у файл.

# Не забуваємо про PEP-8

class SumToCsv: #модуль для підрахунку суми витрат різних людей

    def __init__(self, name_in): #під час виклику виконує читання файлу та викидає всі неповні або переповненні рядки
        self._read_file(name_in)
        self._clean_info()
        
    def _read_file(self, file_name):
        '''method for reading the file'''
        try:
            self.data_from_file = open(file_name, #відкриваємо файл 
            encoding='utf-8', ) #вказуємо кодування
            self.result = [] #список з усіма іменами із файлу, під час створення пустий
            self.column_name = self.data_from_file.readline().strip('\n').split(',') #читаємо перший рядок, де вказані назви усіх колонок 
            for line in self.data_from_file: #для кожної лінії у файлу
                keys = line.strip('\n').split(",") #видаляємо перенос строки і розбиваємо на окремі колонки
                self.result.append(keys)     #додаємо результат у кінцевий список
        except FileNotFoundError: #якщо файл не знайдений - видаємо повідомлення про помилку
            print ("Заданий файл не знайдений")
            

    def _clean_info(self):
        """method for deleting strings that hasn't two parameters"""
        for element in self.result[::-1]: #проходимось по всім елементам списку
            if len(element) != 2 or element[1]==(''): #якщо у рядку не два елементи або останній порожній, то такий елемент видаляємо
                self.result.remove(element)
            else:    
                try:
                    element[1]=int(element[1]) #переводимо другий елемент у число
                except ValueError:
                    self.result.remove(element) #якщо другий елемент не число - також його видаляємо

    def calculate(self):
        '''method for calculating sum of all spendings'''
        self.result_dict = dict() #результати записуються у словник, який на початку порожній
        for element, total_sum in self.result: #для всіх елементів, які є у списку з даними робимо наступне
            if element in self.result_dict: #перевіряємо чи є прізвище у кінцевому словнику
                self.result_dict[element] += total_sum #якщо є, то до суми витрат додаємо відповідну суму
            else:
                self.result_dict.setdefault(element,total_sum) #якщо немає, то створюємо запис у словнику із відповідним значенням
    
    def info_to_csv(self):
        '''method for writing data to file csv'''
        with open('out_sum.csv', 'w') as csvfile: #відкриваємо файл
            csvfile.write(self.column_name[0] + '\t'+ self.column_name[1]+ '\n') #записуємо назви колонок
            for key in self.result_dict.keys(): #для всіх ключів у словнику
                csvfile.write(key + '\t'+ str(self.result_dict[key]) + '\n') #записуємо результати у файл
        

if __name__ == "__main__":
    file_name = "data.csv"
    information = SumToCsv(file_name) 
    information.calculate()
    information.info_to_csv()
