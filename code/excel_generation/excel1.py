"""new excel file with the correlations"""
import xlsxwriter

dumbo = xlsxwriter.Workbook('temperatureRegressions4.xlsx')

clim_names = ['Temperate', 'Tropical', 'Desert', 'Semiarid', 'Subtropical', 'Mediterranean']
habibi = ['Accra', 'Ahmedabad', 'Algiers', 'Baghdad', 'Bamako', 'Bangkok', 'Beijing', 'Belo_Horizonte', 'Buenos_Aires', 'Cairo', 'Caracas', 'Changzhou', 'Istanbul', 'Jaipur', 'Kabul', 'Karachi', 'Kanpur', 'Khartoum', 'Lagos', 'Lahore', 'Los_Angeles', 'Luanda', 'Madras', 'Minneapolis', 'Montreal', 'Mumbai', 'Philadelphia', 'Riyadh', 'Saint_Petersburg', 'Sydney', 'Tashkent', 'Tehran','Tel_Aviv', 'Tianjin', 'Warsaw', 'Wuhan']
regressed_names = ['Temp. corr', 'Temp. r^2']
slope_or_p_names = ['slope', 'r^2 value', 'p-value']

sht1 = dumbo.add_worksheet('Temp. Corrs. and R2 Vals.')
sht2 = dumbo.add_worksheet('Urban & Suburban')
sht3 = dumbo.add_worksheet('Open Space')
sht4 = dumbo.add_worksheet('Clim. Regressions, Urb+Sub')
sht5 = dumbo.add_worksheet('Clim. Regressions, OP')

sht1.write(1, 0, "Slope")
sht1.write(2, 0, "r^2 value")
sht1.write(3, 0, "p-value")
i = 0
for name in habibi:
    sht1.write(0, i + 1, name)
    sht1.write(1, i + 1, corrval[i])
    sht1.write(2, i + 1, r2val[i])
    sht1.write(3, i + 1, pval[i])
    i += 1

sht2.write(1, 0, "Counts")
sht2.write(3, 0, "Ratios")
sht2.write(5, 0, "Decay")
sht2.write(0, 2, "Temp. slope")
sht2.write(0, 3, "Temp. R^2")

j = 1
for metric in metrics_lst:
    i = 2
    for regressed in regressed_lst:
        result = scipy.stats.linregress(regressed, metric)
        sht2.write(j, i, result[0] )
        sht2.write(j, 1, "regression slope")
        sht2.write(j + 1, i, result[2])
        sht2.write(j + 1, 1, "r^2 value")
        sht2.write(j + 2, i, result[3])
        sht2.write(j + 2, 1, "p-value")
        i += 1
    j += 3

sht3.write(1, 0, "Counts")
sht3.write(3, 0, "Ratios")
sht3.write(5, 0, "Decay")
sht3.write(0, 2, "Temp. slope")
sht3.write(0, 3, "Temp. R^2")

j = 1
for metric in metrics_lst_op:
    i = 2
    for regressed in regressed_lst:
        result = scipy.stats.linregress(regressed, metric)
        sht3.write(j, i, result[0] )
        sht3.write(j, 1, "Regression slope")
        sht3.write(j + 1, i, result[2])
        sht3.write(j + 1, 1, " r^2-value")
        sht3.write(j + 2, i, result[3])
        sht3.write(j + 2, 1, " p-value")
        i += 1
    j += 3

"""dim 1: which metric
   dim 2: which climate group
   dim 3: slope or r2
   dim 4: slope or r^2 or p-value 
"""

for i in range(len(regressions)):
    for j in range(len(regressions[i])):
        for k in range(len(regressions[i][j])):
            for l in range(len(regressions[i][j][k])):
                sht4.write(6*j + 3*k + l + 1, 3 + i, regressions[i][j][k][l])
                sht5.write(6*j + 3*k + l + 1, 3 + i, regressions_op[i][j][k][l])
                
    
sht4.write(0, 3, "Counts")
sht5.write(0, 3, "Counts")
sht4.write(0, 4, "Ratios")
sht5.write(0, 4, "Ratios")
sht4.write(0, 5, "Decay")
sht5.write(0, 5, "Decay")

for j in range(len(regressions[1])):
    sht4.write(6*j + 1, 0, clim_names[j])
    sht5.write(6*j + 1, 0, clim_names[j])
               
for j in range(len(regressions[1])):
    for k in range(len(regressions[1][1])):
        sht4.write(6*j + 3*k + 1, 1, regressed_names[k])
        sht5.write(6*j + 3*k + 1, 1, regressed_names[k])

for j in range(len(regressions[1])):
    for k in range(len(regressions[1][1])):
        for l in range(len(regressions[1][1][1])):
            sht4.write(6*j + 3*k + l + 1, 2, slope_or_p_names[l])
            sht5.write(6*j + 3*k + l + 1, 2, slope_or_p_names[l])
                     
dumbo.close()
