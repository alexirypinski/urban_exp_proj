"""new excel file with the correlations"""
import xlsxwriter

dumbo = xlsxwriter.Workbook('correlationsByClimateFinal.xlsx')
habibi = ['Accra', 'Ahmedabad', 'Algiers', 'Baghdad', 'Bamako', 'Bangkok', 'Beijing', 'Belo_Horizonte', 'Buenos_Aires', 'Cairo', 'Caracas', 'Changzhou', 'Istanbul', 'Jaipur', 'Kabul', 'Karachi', 'Kanpur', 'Khartoum', 'Lagos', 'Lahore', 'Los_Angeles', 'Luanda', 'Madras', 'Minneapolis', 'Montreal', 'Mumbai', 'Philadelphia', 'Riyadh', 'Saint_Petersburg', 'Sydney', 'Tashkent', 'Tehran','Tel_Aviv', 'Tianjin', 'Warsaw', 'Wuhan']

sht = dumbo.add_worksheet('Correlations')
sht.write(1, 0, "Temperate")
sht.write(2, 0, "Tropical")
sht.write(3, 0, "Desert")
sht.write(4, 0, "Semiarid")
sht.write(5, 0, "Subtropical")
sht.write(6, 0, "Mediterranean")

sht.write(0, 1, "Counts")
sht.write(0, 2, "Ratios")
sht.write(0, 3, "Decay")

sht.write(1,1, counts_corr_temperate2)
sht.write(1,2, ratio_corr_temperate2)
sht.write(1,3, decay_corr_temperate2)

sht.write(2,1, counts_corr_tropical2)
sht.write(2,2, ratio_corr_tropical2)
sht.write(2,3, decay_corr_tropical2)

sht.write(3,1, counts_corr_desert2)
sht.write(3,2, ratio_corr_desert2)
sht.write(3,3, decay_corr_desert2)

sht.write(4,1, counts_corr_semiarid2)
sht.write(4,2, ratio_corr_semiarid2)
sht.write(4,3, decay_corr_semiarid2)

sht.write(5,1, counts_corr_subtropical2)
sht.write(5,2, ratio_corr_subtropical2)
sht.write(5,3, decay_corr_subtropical2)

sht.write(6,1, counts_corr_mediterranean2)
sht.write(6,2, ratio_corr_mediterranean2)
sht.write(6,3, decay_corr_mediterranean2)

dumbo.close()
