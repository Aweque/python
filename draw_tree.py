def draw_tree (pairs:list, ball_sym = 'o'):
    
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
    import random
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
                
    #prints all cones of christmas tree
    for top, bottom in pairs:
        for i in range (top, bottom+1, 2):
            #prints stars i times and center it on the width_t
            print (''.join(random.choices(i*'*'+4*ball_sym, k = i)).center(width_t))
    if width_t: #cheking if the program working correct and call function for draw trunk
        draw_trunk (width_t)


def draw_trunk(wid):    
    '''
    Draw Christmas tree trunk with the given width of tree.
    '''
    print (("||").center(wid))

#given_tree = [[2, 16], [8, 26], [16, 36]]
#draw_tree(given_tree, "☯")