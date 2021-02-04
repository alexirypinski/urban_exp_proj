import xlsxwriter

poopboy = xlsxwriter.Workbook('analysis_citiesURB.xlsx')

habibti = ['Accra', 'Ahmedabad', 'Algiers', 'Baghdad', 'Bamako', 'Bangkok', 'Beijing', 'Belo_Horizonte', 'Buenos_Aires', 'Cairo', 'Caracas', 'Changzhou', 'Istanbul', 'Jaipur', 'Kabul', 'Kanpur', 'Khartoum', 'Lagos', 'Lahore', 'Los_Angeles', 'Luanda', 'Madras', 'Minneapolis', 'Montreal', 'Mumbai', 'Philadelphia', 'Riyadh', 'Saint_Petersburg', 'Sydney', 'Tashkent', 'Tel_Aviv', 'Tianjin', 'Warsaw', 'Wuhan']


def make_excel(a, wkst):
    listo = []
    i = 1.2 
    row = 1
    while i < 2.5: 
        wkst.write(row, 0, i)
        year = 0
        while year < 3:
            col = 0
            while col < len(identify_discontinuities(i, a[year])) - 1: 
                little = identify_discontinuities(i, a[year])
                wkst.write(row, col + 1, little[col])
                col += 1
            row += 1
            year += 1
        i += 0.05

        
j = 0
for z in sorted_nice_cities: 
    sht = poopboy.add_worksheet(habibti[j])
    make_excel(z, sht)
    j += 1
    
    
poopboy.close()
            
