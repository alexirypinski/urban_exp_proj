heat_measures = pd.read_excel("~/downloads/LST_MODIS_KelvinUnits.xlsx", sheetname = "Sheet1")
time_array = [i for i in range(17)]   

"""HERE, WE GENERATE 3 THINGS FROM THE HEAT MEASUREMENT: (1) SLOPE OF CORRELATION, (2) R^2
measurement (3) P-value""" 

slopeval = []
r2val = []
pval = []

for item, row in heat_measures.T.iteritems():
    regresso = scipy.stats.linregress(time_array, row)
    slopeval += [regresso[0]]
    r2val += [regresso[2]**2]
    pval += [regresso[3]]

    
