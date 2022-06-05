import draw_tree as dt 
#functions for drawing christmas tree is in file draw_tree.py
#two function are there, draw_tree which draw tree and draw_trunk, which draw trunk in case of correct working
    
def  make_pairs(seq):
    ''' make and return the list of pairs, with the quantity of stars in top and bootom of trapecia'''
    result = [] #resulting list
    flag_er = 0 #flag for value error in open file
    #open_file_symb()
    ball_symbols = ['✝️','☪️','🕉','☸️','🕎','☯️','✡️','☦️']
    b_symb = ""
    for line in seq: #for each line in the file make the further
            keys = line.strip('\n').split(", ") #read line
            if keys[0] in ball_symbols:
                b_symb = keys[0]
                print (b_symb, "-ось він")
            else:
                try:
                    for j in range(2):      #makes string numbers as int
                        keys[j] = int(keys[j])
                    result.append(keys)     #adding results to the final list
                except ValueError:
                    flag_er = 1 #for error value error making a flag
    if flag_er: 
        #print the message about error in values
        print ("У файлі даних є помилка. Дані мають бути числами і мають бути записані через кому")
        result = []
    print (result, b_symb)        
    return (result, b_symb)


def open_file(filename):
    ''' trying to open file, if it does not exist prints message about this 
    returns lines for making each cone of tree or empty list in case of error'''
    try:
        fin = open(filename, 'r', encoding='utf-8')
        return make_pairs(fin)
    except FileNotFoundError:
        print ("Заданий файл не знайдений")
        return []

def open_file_symb():
    ''' trying to open file, if it does not exist prints message about this 
    returns lines for making each cone of tree or empty list in case of error'''
    try:
        f_name = r"D:\myfiles\python\lesson_8\symbol.txt"
        with open (f_name, 'r', encoding='utf-8') as symb:
            for line in symb:
                print (line)
    except FileNotFoundError:
        print ("Заданий файл не знайдений")
        return []


def enter_file_name():
    '''getting file name from command line as a parameter. If it does not exist ask to print way to file via input.
    Returns way to file'''
    import sys
    name_file = sys.argv
    try:
        file_name = open(name_file[1])
        return open_file(name_file[1])
    except FileNotFoundError:
        file_name = r"D:\myfiles\python\lesson_8\tree.txt"
        #file_name = input ("Введіть шлях до файлу, де вказані параметри ялинки: ")
    except IndexError:
        file_name = r"D:\myfiles\python\lesson_8\tree.txt"
        #file_name = input ("Введіть шлях до файлу, де вказані параметри ялинки: ")
    return open_file(file_name)

if __name__ == "__main__":
    
    #f_name = r"D:\myfiles\python\lesson_8\tree.txt"
    brunches = enter_file_name()
    dt.draw_tree(brunches)
