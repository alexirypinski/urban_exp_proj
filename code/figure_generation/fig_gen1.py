"""here, we create the scatterplots of temperature slopes vs the metrics for each climate type. 
we will create them in the following hierarchical order:
for each climate type:
    for each of US or OS:
      for each metric in order counts ratio decay:
"""

temperate_names = ['Beijing', 'Minneapolis', 'Montreal', 'Saint Petersburg', 'Tianjin', 'Warsaw']
tropical_names = ['Bamako', 'Bangkok', 'Belo Horizonte', 'Caracas', 'Lagos', 'Mumbai']
desert_names = ['Baghdad', 'Cairo', 'Jaipur', 'Khartoum', 'Riyadh']
semiarid_names = ['Accra', 'Ahmedabad','Kabul', 'Lahore', 'Luanda', 'Tehran']
subtropical_names = ['Buenos Aires', 'Changzhou', 'Kanpur', 'Philadelphia', 'Sydney', 'Wuhan']
mediterranean_names = ['Algiers', 'Istanbul',  'Los Angeles', 'Madrid', 'Tashkent', 'Tel Aviv']
master_names = [temperate_names, tropical_names, desert_names, semiarid_names, subtropical_names, mediterranean_names]
climate_names = ["Temperate", "Tropical", "Desert", "Semiarid", "Subtropical", "Mediterranean"]
metric_names = ['Ratios', 'Counts', 'Decay']

counts_clim_groups = [select_inds_by_name(clim_names, habibi, select_time(counts_lst)) for clim_names in master_names]
ratio_clim_groups = [select_inds_by_name(clim_names, habibi, select_time(ratio_lst)) for clim_names in master_names]
decay_clim_groups = [select_inds_by_name(clim_names, habibi, select_time(decay_lst)) for clim_names in master_names]
metric_groups = [counts_clim_groups, ratio_clim_groups, decay_clim_groups]

counts_clim_groups_op = [select_inds_by_name(clim_names, habibi, select_time(counts_lst_op)) for clim_names in master_names]
ratio_clim_groups_op = [select_inds_by_name(clim_names, habibi, select_time(ratio_lst_op)) for clim_names in master_names]
decay_clim_groups_op = [select_inds_by_name(clim_names, habibi, select_time(decay_lst_op)) for clim_names in master_names]   
metric_groups_op = [counts_clim_groups_op, ratio_clim_groups_op, decay_clim_groups_op]

clim_slopes = [select_inds_by_name(clim_names, habibi, slopeval) for clim_names in master_names]
clim_r2s = [select_inds_by_name(clim_names, habibi, r2val) for clim_names in master_names]


for i in range(len(metric_groups)):
    for j in range(len(metric_groups[i])):
            plt.scatter(metric_groups[i][j], clim_slopes[j])
            plt.savefig("scatterplot_" + metric_names[i] + "_" + climate_names[j])
            plt.clf()
  
for i in range(len(metric_groups)):
    for j in range(len(metric_groups[i])):
            plt.scatter(metric_groups_op[i][j], clim_slopes[j])
            plt.savefig("scatterplot_" + metric_names[i] + "_" + climate_names[j] + "_op")
            plt.clf()
