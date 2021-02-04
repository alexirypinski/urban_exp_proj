"""this is the box in which we will conduct all of the previous analysis but for each separate climate"""

temperate_names = ['Beijing', 'Minneapolis', 'Montreal', 'Saint Petersburg', 'Tianjin', 'Warsaw']
tropical_names = ['Bamako', 'Bangkok', 'Belo Horizonte', 'Caracas', 'Lagos', 'Mumbai']
desert_names = ['Baghdad', 'Cairo', 'Jaipur', 'Karachi', 'Khartoum', 'Riyadh']
semiarid_names = ['Accra', 'Ahmedabad','Kabul', 'Lahore', 'Luanda', 'Tehran']
subtropical_names = ['Buenos Aires', 'Changzhou', 'Kanpur', 'Philadelphia', 'Sydney', 'Wuhan']
mediterranean_names = ['Algiers', 'Istanbul',  'Los Angeles', 'Madrid', 'Tashkent', 'Tel Aviv']
master_names = [temperate_names, tropical_names, desert_names, semiarid_names, subtropical_names, mediterranean_names]

"""first we find the metrics for the clim groups"""
counts_clim_groups = [select_inds_by_name(clim_names, habibi, select_time(counts_lst)) for clim_names in master_names]
ratio_clim_groups = [select_inds_by_name(clim_names, habibi, select_time(ratio_lst)) for clim_names in master_names]
decay_clim_groups = [select_inds_by_name(clim_names, habibi, select_time(decay_lst)) for clim_names in master_names]
metric_groups = [counts_clim_groups, ratio_clim_groups, decay_clim_groups]

counts_clim_groups_op = [select_inds_by_name(clim_names, habibi, select_time(counts_lst_op)) for clim_names in master_names]
ratio_clim_groups_op = [select_inds_by_name(clim_names, habibi, select_time(ratio_lst_op)) for clim_names in master_names]
decay_clim_groups_op = [select_inds_by_name(clim_names, habibi, select_time(decay_lst_op)) for clim_names in master_names]   
metric_groups_op = [counts_clim_groups_op, ratio_clim_groups_op, decay_clim_groups_op]

"""next, we find the temperature corrs and r2 values for the clim groups"""
clim_slopes = [select_inds_by_name(clim_names, habibi, slopeval) for clim_names in master_names]
clim_r2s = [select_inds_by_name(clim_names, habibi, r2val) for clim_names in master_names]

"""finally, we regress the previous two across clim groups"""

"""dim 1: which metric
   dim 2: which climate group
   dim 3: slope or r2 regressed against
   dim 4: slope, r^2-value or p-value
"""

regressions = []
regressions_op = []
for i in range(3):
    inner_lst = []
    inner_lst_op = []
    for j in range(len(metric_groups[i])):
        inner_lst += [calc_heat_regressions(metric_groups[i][j], clim_slopes[j], clim_r2s[j])]
        inner_lst_op += [calc_heat_regressions(metric_groups_op[i][j], clim_slopes[j], clim_r2s[j])]
    regressions += [inner_lst]
    regressions_op += [inner_lst_op]
