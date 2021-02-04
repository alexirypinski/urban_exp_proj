"""find the decay metric for every city and every year""" 
decay_lst2 = decay_metric(get_magic_thresh(sorted_nice_cities, 1.5), sorted_nice_cities, root_lst)
decay_lst_op2 = decay_metric(get_magic_thresh(sorted_nice_cities_op, 1.3), sorted_nice_cities_op, root_lst)

decay_lst_temperate2 = select_time(decay_metric(get_magic_thresh(temperate, 1.5), temperate, root_lst))
decay_lst_tropical2 = select_time(decay_metric(get_magic_thresh(tropical, 1.5), tropical, root_lst))
decay_lst_desert2 = select_time(decay_metric(get_magic_thresh(desert, 1.5), desert, root_lst))
decay_lst_semiarid2 = select_time(decay_metric(get_magic_thresh(semiarid, 1.5), semiarid, root_lst))
decay_lst_subtropical2 = select_time(decay_metric(get_magic_thresh(subtropical, 1.5), subtropical, root_lst))
decay_lst_mediterranean2 = select_time(decay_metric(get_magic_thresh(mediterranean, 1.5), mediterranean, root_lst))

decay_lst_op_temperate2 = select_time(decay_metric(get_magic_thresh(temperate_op, 1.3), temperate_op, root_lst))
decay_lst_op_tropical2 = select_time(decay_metric(get_magic_thresh(tropical_op, 1.3), tropical_op, root_lst))
decay_lst_op_desert2 = select_time(decay_metric(get_magic_thresh(desert_op, 1.3), desert_op, root_lst))
decay_lst_op_semiarid2 = select_time(decay_metric(get_magic_thresh(semiarid_op, 1.3), semiarid_op, root_lst))
decay_lst_op_subtropical2 = select_time(decay_metric(get_magic_thresh(subtropical_op, 1.3), subtropical_op, root_lst))
decay_lst_op_mediterranean2 = select_time(decay_metric(get_magic_thresh(mediterranean_op, 1.3), mediterranean_op, root_lst))
