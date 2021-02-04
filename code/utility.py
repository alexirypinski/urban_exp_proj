import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from scipy.stats import iqr
from operator import itemgetter
import scipy.stats

threshold_lst = []
thresh = 1.2
while thresh <= 1.8:
    threshold_lst.append(thresh)
    thresh += 0.05

def make_nice(a, i): 
    """Creates a list of lists of the city data with the nAn values masked"""
    temp = a.iloc[:,i]
    poop = temp[~pd.isnull(temp)]
    return poop 
        
def get_thresh_value(index): 
    return threshold_lst[index]

def identify_discontinuities (threshold, lst): 
    counter = 0 
    a = []
    while counter < len(lst) - 2: 
        if lst[counter + 1]/ lst[counter] >= threshold:
            a.append(lst[counter + 1])
        counter = counter + 1   
    return a 

def get_argmin(lst):
    return min(enumerate(lst), key=itemgetter(1))[0]

"""let lst1 be a sublist of lst2. let data be a list of data such that the i-th entry
corresponds to the data about the city of the i-th name in lst2. this function selects
all of the datasets in data corresponding to the names in lst1. note that we assume that
lst1 is in the same order as lst2"""

def select_inds_by_name(lst1, lst2, data):
    returned = []
    for target_name in lst1:
        ind = 0
        for name in lst2:
            if target_name == name:
                returned += [data[ind]]
            else:
                ind += 1
    return returned


"""we write a program that takes the discontinuity lists for different discontinuities from 1.2
to 2.0 and selects the variance maximizing indices."""

discont_lst = []
ind = 1.2
while ind < 2.05:
    discont_lst += [ind]
    ind += 0.05


def make_full_discont_list(lst, discont_lst):
    city_lst = []
    for c in lst:
        year_lst = []
        for y in c:
            disconts = []
            for d in discont_lst:
                disconts += [identify_discontinuities(d, y)]
            year_lst += [disconts]
        city_lst += [year_lst]
    return city_lst

def get_vars(lst):
    city_lst = []
    for c in lst:
        year_lst = []
        for y in c:
            discont_lst = []
            for d in y:
                discont_lst += [np.var(d)]
            year_lst += [discont_lst]
        city_lst += [year_lst]
    return city_lst
            

def maximizing_indices(var_lst, discont_lst):
    city_lst = []
    for c in var_lst:
        year_lst = []
        for y in c:
            maxind = 0  
            preval = y[0]
            for d in range(len(y)):
                if y[d] > preval:
                    maxind = d
                    preval = y[d]
            year_lst += [discont_lst[maxind]]
        city_lst += [year_lst]
    return city_lst

    
def get_ratios(lst): 
    new_lst = []
    for c in lst: 
        city_lst = []
        for y in c: 
            i = (y[len(y) - 1]) / y[0]
            city_lst += [i] 
        new_lst += [city_lst]
    return new_lst

def get_counts(lst): 
    new_lst = []
    for c in lst: 
        city_lst = []
        for y in c: 
            i = len(y)
            city_lst += [i] 
        new_lst += [city_lst]
    return new_lst

def flatten_inner(lst):
    returned = []
    for outer in lst:
        for inner in outer:
            returned += [inner]
    return returned

def select_the_following(inds, lst):
    returned = []
    for i in inds:
        returned += [lst[i]]
    return returned

def get_ind_lst(input_lst, name_lst):
    returned = []
    for inp in input_lst:
        ind = 0
        for name in name_lst:
            if name == inp:
                returned += [ind]
            else:
                ind += 1
    return returned

def gen_spearman_correlations1(valueset1, valueset2):
    cities_table = []
    r_coeff_table = []
    for i in range(len(valueset1)):
        c = valueset1[i]
        r_val = scipy.stats.spearmanr(valueset1[i], valueset2[i])[1]
        city_corr = scipy.stats.spearmanr(valueset1[i], valueset2[i])[0]
        cities_table += [city_corr]
        r_coeff_table += [r_val]
    return cities_table, 

def gen_spearman_correlations(valueset1, valueset2):
    return scipy.stats.spearmanr(valueset1, valueset2)[0]
