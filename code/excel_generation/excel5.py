"""calculating the vars and then writing them into an xlsx"""
import xlsxwriter

poopboy = xlsxwriter.Workbook('urbanSuburbanVarsLists.xlsx')

habibi = ['Accra', 'Ahmedabad', 'Algiers', 'Baghdad', 'Bamako', 'Bangkok', 'Beijing', 'Belo_Horizonte', 'Buenos_Aires', 'Cairo', 'Caracas', 'Changzhou', 'Istanbul', 'Jaipur', 'Kabul', 'Karachi', 'Kanpur', 'Khartoum', 'Lagos', 'Lahore', 'Los_Angeles', 'Luanda', 'Madras', 'Minneapolis', 'Montreal', 'Mumbai', 'Philadelphia', 'Riyadh', 'Saint_Petersburg', 'Sydney', 'Tashkent', 'Tehran','Tel_Aviv', 'Tianjin', 'Warsaw', 'Wuhan']
lst = get_vars(make_full_discont_list(sorted_nice_cities, discont_lst))

j = 0
for c in lst:
    sheet = poopboy.add_worksheet(habibi[j])
    sheet.write(1, 0, "t1")
    sheet.write(2, 0, "t2")
    sheet.write(3, 0, "t3")
    a = 1.2
    b = 1
    while a < 2.05:
        sheet.write(0, b, a)
        a += 0.05
        b += 1
    i = 1
    for y in c:
        k = 0
        while k < len(y):
            if not np.isnan(y[k]):
                sheet.write(i, k + 1, y[k])
            else:
                sheet.write(i, k + 1, 0)
            k += 1
        i += 1         
    j += 1


    
    
poopboy.close()
