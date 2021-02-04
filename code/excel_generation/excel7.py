import xlsxwriter

dumbo = xlsxwriter.Workbook('openSpaceVarianceMaximizingThresholds.xlsx')

habibi = ['Accra', 'Ahmedabad', 'Algiers', 'Baghdad', 'Bamako', 'Bangkok', 'Beijing', 'Belo_Horizonte', 'Buenos_Aires', 'Cairo', 'Caracas', 'Changzhou', 'Istanbul', 'Jaipur', 'Kabul', 'Karachi', 'Kanpur', 'Khartoum', 'Lagos', 'Lahore', 'Los_Angeles', 'Luanda', 'Madras', 'Minneapolis', 'Montreal', 'Mumbai', 'Philadelphia', 'Riyadh', 'Saint_Petersburg', 'Sydney', 'Tashkent', 'Tehran','Tel_Aviv', 'Tianjin', 'Warsaw', 'Wuhan']

i = 0
sht = dumbo.add_worksheet('All')
for c in max_indices: 
    sht.write(i, 0, habibi[i])
    j = 0
    while j < len(c):
        year = c[j]
        sht.write(i, j + 1, year)
        j += 1
    i += 1
    
    
poopboy.close()


"""Find the variances associated with each discontinuity threshold"""

dumbo = xlsxwriter.Workbook('allPatchesOpenSpace.xlsx')

habibi = ['Accra', 'Ahmedabad', 'Algiers', 'Baghdad', 'Bamako', 'Bangkok', 'Beijing', 'Belo_Horizonte', 'Buenos_Aires', 'Cairo', 'Caracas', 'Changzhou', 'Istanbul', 'Jaipur', 'Kabul', 'Karachi', 'Kanpur', 'Khartoum', 'Lagos', 'Lahore', 'Los_Angeles', 'Luanda', 'Madras', 'Minneapolis', 'Montreal', 'Mumbai', 'Philadelphia', 'Riyadh', 'Saint_Petersburg', 'Sydney', 'Tashkent', 'Tehran','Tel_Aviv', 'Tianjin', 'Warsaw', 'Wuhan']



for i in range(len(all_threshes)): 
    sht = dumbo.add_worksheet(habibi[i])
    sht.write(0, 0, "t1")
    sht.write(17, 0, "t2")
    sht.write(34, 0, "t3")
    """time period"""
    for j in range(3):
        """all thresholds"""
        for k in range(len(all_threshes[i][j])):
            """all patches for a threshold"""
            for l in range(len(all_threshes[i][j][k])):
                sht.write(j * 17 + k, l + 1, all_threshes[i][j][k][l])
    
    
dumbo.close()
