import draw_tree_classes as dt 
#functions for drawing christmas tree is in file draw_tree.py
#three function are there, draw_tree which draw tree and draw_trunk, which draw trunk in case of correct working 
# and get_biggest_number for definding the greatest number for centring christmas_tree


def enter_file_name():
    '''getting file name from command line as a parameter. If it does not exist ask to print way to file via input.
    Returns way to file'''
    import sys
    name_file = sys.argv
    try:
        file_name = open(name_file[1])
        return open_file(name_file[1])
    except FileNotFoundError:
        file_name = input ("Введіть шлях до файлу, де вказані параметри ялинки: ")
    except IndexError:
        file_name = input ("Введіть шлях до файлу, де вказані параметри ялинки: ")
    return open_file(file_name)

def open_file(filename):
    ''' trying to open file, if it does not exist prints message about this 
    returns lines for making each cone of tree or empty list in case of error'''
    try:
        fin = open(filename, 'r', encoding='utf-8')
        return make_pairs(fin)
    except FileNotFoundError:
        print ("Заданий файл не знайдений")
        return []

def  make_pairs(seq):
    ''' make pairs, with the quantity of stars in top and bootom of trapecia
    returning the list of all trapezias in christmass tree, width of the tree for centring and symbol for ball
    '''
    result = [] #resulting list
    flag_er = 0 #flag for value error in open file
    b_symb = get_spec_symbol(seq) #read first line for definding special symbol
    for line in seq: #for each line in the file make the further
            keys = line.strip('\n').split(", ") #read line
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
    width_tree = dt.get_biggest_number(result) #definding the greatest number for centring christmas_tree
    
    return result, width_tree, b_symb

def get_spec_symbol(seq):
    '''getting the special symbol, that will be an christmass ball'''
    return seq.readline().strip('\n')

if __name__ == "__main__":
    
    #f_name = r"D:\myfiles\python\lesson_8\tree.txt"
    brunches = enter_file_name()
    dt.draw_tree(*brunches)
