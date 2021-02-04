import xlsxwriter

habibti = ['Accra', 'Ahmedabad', 'Algiers', 'Baghdad', 'Bamako', 'Bangkok', 'Beijing', 'Belo_Horizonte', 'Buenos_Aires', 'Cairo', 'Caracas', 'Changzhou', 'Istanbul', 'Jaipur', 'Kabul', 'Karachi', 'Kanpur', 'Khartoum', 'Lagos', 'Lahore', 'Los_Angeles', 'Luanda', 'Madras', 'Minneapolis', 'Montreal', 'Mumbai', 'Philadelphia', 'Riyadh', 'Saint_Petersburg', 'Sydney', 'Tashkent','Tehran', 'Tel_Aviv', 'Tianjin', 'Warsaw', 'Wuhan']


dick_head = xlsxwriter.Workbook('decayMetricsOpenSpace.xlsx')



b = decay_metric(get_magic_thresh(sorted_nice_cities), sorted_nice_cities, root_lst)

z = dick_head.add_worksheet('Decay')

def write_new_excel(a, wkst):
    for j in range(len(a)):
        for i in range(len(a[j])):
            wkst.write(j + 1, i + 1, a[j][i])
    for j in range(len(a)):
        wkst.write(j + 1, 0, habibti[j])
            

        
write_new_excel(b, z)
    
dick_head.close()
