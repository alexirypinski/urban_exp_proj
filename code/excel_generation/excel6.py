"""writing the counts into a xlsx"""

import xlsxwriter

def get_counts(lst):
    city_lst = []
    for c in lst: 
        year_lst = []
        for y in c:
            discont_lst = []
            for d in y:
                discont_lst += [len(d)]
            year_lst += [discont_lst]
        city_lst += [year_lst]
    return city_lst

poopboy = xlsxwriter.Workbook('openSpaceCountsLists.xlsx')

habibi = ['Accra', 'Ahmedabad', 'Algiers', 'Baghdad', 'Bamako', 'Bangkok', 'Beijing', 'Belo_Horizonte', 'Buenos_Aires', 'Cairo', 'Caracas', 'Changzhou', 'Istanbul', 'Jaipur', 'Kabul', 'Karachi', 'Kanpur', 'Khartoum', 'Lagos', 'Lahore', 'Los_Angeles', 'Luanda', 'Madras', 'Minneapolis', 'Montreal', 'Mumbai', 'Philadelphia', 'Riyadh', 'Saint_Petersburg', 'Sydney', 'Tashkent', 'Tehran','Tel_Aviv', 'Tianjin', 'Warsaw', 'Wuhan']
lst = get_counts(all_threshes)

j = 0
for c in lst:
    sheet = poopboy.add_worksheet(habibi[j])
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
            sheet.write(i, k + 1, y[k])
            k += 1
        i += 1         
    j += 1
    

        
    
    
poopboy.close()

