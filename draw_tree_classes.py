import random

class TreeTrapezia:
    '''class for trapezias in the tree. It has top and bottom width, which is given while definding, 
    special symbol for balls 'o', it can be changed,
    and function line, which make random line of given length with special symbol'''
    symb = str('o') #default special symbol is 'o'

    def __init__(self, lst): #make top and bottom width from list of two numbers
        self.top = lst[0]
        self.bottom = lst[1]
    
    def sym(self, sym): #function for changing special symbol for certain object
        self.symb = sym

    def line (self, line_length): # function for making random line of given length with special symbol
        tree_line = ''.join(random.choices(line_length*'*'+4*self.symb, k = line_length))
        return tree_line



def draw_tree (pairs:list, width_t:int, ball_sym = 'o'):
    
    '''
    Draw Christmas tree from the stars with given number of stars as a list of pairs with given width and possible ball symbol
    Restriction: All numbers in list is positive and even.
    >>> draw_tree ([[2,6],[4,8]],8, '☯')
       *☯
      *☯**
     *☯**☯*
      *☯☯*
     *☯****
    ****☯*☯*
    '''                     
    #prints all trapezias of christmas tree
    for nums in pairs:
        brunch = TreeTrapezia(nums)
        for i in range (brunch.top, brunch.bottom+1, 2):
            #prints stars i times and center it on the width_t
            brunch.sym(ball_sym)
            print (brunch.line(i).center(width_t))
    draw_trunk(width_t)


def draw_trunk(wid:int):    
    '''
    Draw Christmas tree trunk with the given width of tree.
    '''
    if wid: #cheking if the program working correct and call function for draw trunk
        print (("||").center(wid))

def get_biggest_number(pairs):
    width_t=0 #the biggest number
    for top, bottom in pairs:
        #replace the biggest number
        if bottom > width_t:
            width_t = bottom
    return width_t

#given_tree = [[2, 16], [8, 26], [16, 36]]
#for i in given_tree:
#    draw_tree(*i, 36, "☯")