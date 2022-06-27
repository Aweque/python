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


import pandas as pd

class SumToCsv:

    def __init__(self, name_in):
        self._read_file(name_in)
        self._clean_info()
        
    def _read_file(self, file_name):
        self.data_from_file = pd.read_csv(file_name,
            encoding = 'utf-8',
            on_bad_lines='skip', )

    def _clean_info(self):
        self.data_from_file = self.data_from_file.dropna()

    def calculate(self):
        self.data_from_file = self.data_from_file.groupby('name').sum()
    
    def info_to_csv(self, name_out):
        self.data_from_file.to_csv(name_out, sep='\t')

if __name__ == "__main__":
    file_name = "data.csv"
    information = SumToCsv(file_name) 
    information.calculate()
    information.info_to_csv('out_sum.csv')
