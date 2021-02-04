"""we regress the metrics against the temperature correlations 
(try to reuse all of the code from the open-space and urban+suburban correlations)"""

counts_lst = get_counts(get_magic_thresh(sorted_nice_cities, 1.5))
counts_lst_op = get_counts(get_magic_thresh(sorted_nice_cities_op, 1.3))

ratio_lst = get_ratios(get_magic_thresh(sorted_nice_cities, 1.5))
ratio_lst_op = get_ratios(get_magic_thresh(sorted_nice_cities_op, 1.3))

decay_lst = decay_metric(get_magic_thresh(sorted_nice_cities, 1.5), sorted_nice_cities, root_lst)
decay_lst_op = decay_metric(get_magic_thresh(sorted_nice_cities_op, 1.3), sorted_nice_cities_op, root_lst)
                         
metrics_lst = [select_time(counts_lst), select_time(ratio_lst), select_time(decay_lst)]
metrics_lst_op = [select_time(counts_lst_op), select_time(ratio_lst_op), select_time(decay_lst_op)]

regressed_lst = [slopeval, r2val]                         
