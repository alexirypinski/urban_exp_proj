"""find the counts metrics for every city and every year"""

"""THIS ONE IS FOR THE ANALYSIS IN WHICH WE ONLY CONSIDER THE T3"""

counts_lst2 = get_counts(get_magic_thresh(sorted_nice_cities, 1.5))
counts_lst_op2 = get_counts(get_magic_thresh(sorted_nice_cities_op, 1.3))

counts_lst_temperate2 = select_time(get_counts(get_magic_thresh(temperate, 1.5)))
counts_lst_tropical2 = select_time(get_counts(get_magic_thresh(tropical, 1.5)))
counts_lst_desert2 = select_time(get_counts(get_magic_thresh(desert, 1.5)))
counts_lst_semiarid2 = select_time(get_counts(get_magic_thresh(semiarid, 1.5)))
counts_lst_subtropical2 = select_time(get_counts(get_magic_thresh(subtropical, 1.5)))
counts_lst_mediterranean2 = select_time(get_counts(get_magic_thresh(mediterranean, 1.5)))

counts_lst_op_temperate2 = select_time(get_counts(get_magic_thresh(temperate_op, 1.3)))
counts_lst_op_tropical2 = select_time(get_counts(get_magic_thresh(tropical_op, 1.3)))
counts_lst_op_desert2 = select_time(get_counts(get_magic_thresh(desert_op, 1.3)))
counts_lst_op_semiarid2 = select_time(get_counts(get_magic_thresh(semiarid_op, 1.3)))
counts_lst_op_subtropical2 = select_time(get_counts(get_magic_thresh(subtropical_op, 1.3)))
counts_lst_op_mediterranean2 = select_time(get_counts(get_magic_thresh(mediterranean_op, 1.3)))
