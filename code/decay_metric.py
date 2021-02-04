import sympy as sp
import numpy as np

"""UTILITY FUNCTIONS FOR DECAY METRIC"""

"""Given a list of patch data and a threshold, find the indices in the list of city data 
at which the patch data is dicontinuous with respect to the given threshold"""
def get_discont_indices(city_lst, thresh): 
    i = 0 
    index_lst = []
    while i < len(lst) - 2: 
        if city_lst[i + 1] / city_lst[i] >= thresh:  #if the ratio of patch size for subsequent patches falls above thresh
            index_lst.append(i + 1) #add the index of the larger one
        i += 1   
    return a 


"""Takes as input the discontinuity indices list and tells us the number of patches between each discontinuity.
"""
def get_discont_lengths(lst): 
    lengths = [lst[0]] #length to the first element of list
    for i in range(2, len(lst)):
        temp_len = lst[i] - lst[i - 1] #length between subsequent elements
        lengths += [temp_len]
    return lengths
        


"""CALCULATING DECAY METRIC"""    

"""Here, we implement the decay metric for a list of patches - a number roughly measuring the deviation
of the ditribution of discontinuities in the city's patch data from a chosen 'ideal' distribution
of discontinuities based on a simple geometric progression of length between discontinuities."""
    


#Creating the polynomials to solve for their unique positive real root. We only need up to 13th power
#because this is the max number of discontinuities in our data.
x = sp.Symbol('x')
p0 = -1
p1 = -1 + x 
p2 = -1 + x + x**2
p3 = p2 + x**3
p4 = p3 + x**4
p5 = p4 + x**5
p6 = p5 + x**6
p7 = p6 + x**7
p8 = p7 + x**8 
p9 = p8 + x**9
p10 = p9 + x**10
p11 = p10 + x**11
p12 = p11 + x**12
p13 = p12 + x*13
poly_list =  [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13]

#Solving the above polynomials for their positive real roots 
root_lst = []
for poly in poly_list: 
    sols = sp.solveset(poly, x)
    for root in sols: 
        if (sp.re(root) > 0 and sp.im(root) == 0): #if it has positive real part and no imaginary part
            root_lst += [float(root)] 
            break



""" A function that gets the decay metric, which is the average over all discontinuity 
    brackets of the difference between the ideal decay and the actual decay
    
    inputs:
    - discont_lst: a list of discontinuities 
    - city_lst: a python list of city patch data 
    - roots_list: roots of polynomials that give the ratios with which we calculate the ideal distribution of discontinuities"""
   
def calculate_decay_metric(discont_lst, city_data_lst, roots_lst):
    
    
    """(1) calculating the actual length between in disconts in the data"""
    

    discont_indices = get_discont_indices(city_lst)  #indices of discontinuities in the city data
    
    real_disconts = []
    for i in range(len(discont_indices) - 1): #for each discontinuity except for the last one (we'll take care of it below)
        upper = discont_indices[i + 1] 
        lower = discont_indices[i]
        real_disconts += [upper - lower] # add to real disconts length between the i-th and the i+1-th discontinuity
        
    
    real_disconts += [len(city_data_lst) - 1 - discont_indices[len(discont_indices) - 1]] # the last discont len
    

    """(2) Creatingthe ideal disconts based on the ideal decay coefficients"""
    
    ideal_disconts = [] 
    decay_coeff = roots_lst[len(discont_indices) + 1] #decay coefficient that generates our ideal geometric discontinuity distribution
        
    for k in range(1, len(discont_indices) +  2): #for each number in the list of 
        ideal_disconts += [len(discont_lst) * decay_coeff**k] #add ideal discont to list
            

    """(3) calculates the final average of the pairwise differences between the ideal distribution
    of discontinuities and the real distribution of discontinuities"""
    
    pairwise_diffs = 0
    for j in range(len(ideal_disconts)): #for each j indexing the number of ideal discontinuities 
        pairwise_diffs += abs(real_disconts[j] - ideal_disconts[j]) #calculates difference between the indexes of ideal and real discontinuities

    return pairwise_diffs / (len(discont_indices) + 1) #returns pairwise differences normalized by number of discontinuities
    
    
    """Calculates the decay metric over each city dataset in the sample.
    
       inputs:
        - discont_data array of discontinuity data for the cities in question
        - city_data: array of raw patch data for cities in question
        - root_lst: sufficiently large list of roots for the number of discontinuities in question 
        
    """
    
    def decay_metric(discont_lst, city_data, root_lst):
        outer = [] #outer layer indexed by city
        i = 0
        while i < len(city_data): 
            inner = []
            j = 0
            while j < len(nice_lst[i]): #inner layer indexed by time
                inner += [calculate_decay_metric(discont_data[i][j], city_data[i][j], root_lst)] #calculate decay metric
                j += 1
            i += 1
            outer += [inner]
        return np.array(final) #convert to np array and return

 
