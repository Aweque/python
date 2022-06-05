import sys

def draw_tree (pairs:list):
    '''
    Draw Christmas tree from the stars with given number of stars as a list of pairs
    Restriction: All numbers in list is positive and even. Returns the max width of pairs for drawing trunk
    >>> draw_tree ([[2,6],[4,8]])
       **
      ****
     ******
      ****
     ******
    ********
    '''
    #definding the greatest value of the tree
    #its neccesary for centring all the brunches and trunk
    # also reverse the top and bottom numbers if top>bottom 
    width_t=0 #the biggest number
    for top, bottom in pairs:
        #checking if bottom>top and reverse it if False
        if bottom < top:
            top, bottom = bottom, top
        
        #replace the biggest number
        if bottom > width_t:
            width_t = bottom
        
    #for top, bottom in pairs:
    for top, bottom in pairs:
        for i in range (top, bottom+1, 2):
            #prints stars i times and center it on the width_t
            print((i*'*').center(width_t))
    return width_t


def draw_trunk(wid):    
    '''
    Draw Christmas tree trunk with the given width of tree.
    '''
    if wid:
        print (("||").center(wid))

    
def make_pairs(filename):
    with open(filename) as fin:
        return add_nums_to_seq(fin)
    

def add_nums_to_seq(seq):
    result = []
    flag_er = 0
    for line in seq: #for each line in the file make the further
            keys = line.strip('\n').split(", ") #read line
            try:
                for j in range(2):      #makes string numbers as int
                    keys[j] = int(keys[j])
                result.append(keys)     #adding results to the final list
            except ValueError:
                flag_er = 1
    if flag_er:
        print ("У файлі даних є помилка. Дані мають бути числами і мають бути записані через кому")
        result = []        
    return result

if __name__ == "__main__":
    f_name = r"D:\myfiles\python\lesson_8\tree.txt"

    brunch_length = make_pairs(f_name)
    k=draw_tree(brunch_length)
    draw_trunk(k)