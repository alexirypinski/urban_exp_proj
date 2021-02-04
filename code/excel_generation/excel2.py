import matplotlib.pyplot as plt 

def identify_lengths(lst, year): 
    city_index = 0 
    city_lst = []
    while city_index < 34: 
        length_list = []
        for discont in lst: 
            length_list += [len(discont[city_index][year])]
        city_lst += [length_list]
        city_index += 1
    return city_lst

x = np.linspace(1.2, 1.80, num=12)
y = [identify_lengths(final_discont_cities_lst, i) for i in range(3)]
z = ['Accra', 'Ahmedabad', 'Algiers', 'Baghdad', 'Bamako', 'Bangkok', 'Beijing', 'Belo_Horizonte', 'Buenos_Aires', 'Cairo', 'Caracas', 'Changzhou', 'Istanbul', 'Jaipur', 'Kabul', 'Kanpur', 'Khartoum', 'Lagos', 'Lahore', 'Los_Angeles', 'Luanda', 'Madras', 'Minneapolis', 'Montreal', 'Mumbai', 'Philadelphia', 'Riyadh', 'Saint_Petersburg', 'Sydney', 'Tashkent', 'Tel_Aviv', 'Tianjin', 'Warsaw', 'Wuhan']

def draw_graphs(name_list, x1, y1, string): 
    j = 0
    for i in name_list: 
        plt.plot(x, y[0][j], 'ro-')
        plt.plot(x, y[1][j], 'bo-')
        plt.plot(x, y[2][j], 'go-')
        plt.xlabel(i)
        plt.savefig(i + '_counts' + string)
        plt.show()
        j += 1
        
draw_graphs(z, x, y, 'URB')
