import pandas as pd
import numpy as np

def dict_reverse_lookup(dict, query):
    for key, value in dict.items():
        if value == query: return key
    return None

def RGB_string2tuple(string):
    lst = string.split(", ")
    return tuple([int(el) for el in lst])

class DMCLookup():
    def __init__(self, path="lookup_tables/dmc_lookup.xlsx") -> None:
        df = pd.read_excel(path)
        id_RGB_dict = dict(zip(df.Number, df.RGB))
        self.id_RGB_dict = id_RGB_dict
        RGB_id_array = np.empty((256,256,256), dtype=str)
        for i in range(256):
            for j in range(256):
                for k in range(256):
                    id = dict_reverse_lookup(id_RGB_dict, (i,j,k))
                    RGB_id_array[i,j,k] = str(id) if id else ""
        self.RGB_id_array = RGB_id_array
    
    def id2RGB(self, id):
        return self.id_RGB_dict[id]

    def RGB2id(self, RGB):
        id = self.RGB_id_array[(RGB[0], RGB[1], RGB[2])]
        if id: return id 
        return None

    def n_closest_colors(self, n, rgb):
        red, green, blue = rgb
        
        Rmin = min(0, red - n)
        Gmin = min(0, green - n)
        Bmin = min(0, blue - n)

        Rmax = max(255, red + n)
        Gmax = max(255, green + n)
        Bmax = max(255, blue + n)

        close = []

        for i in range(Rmin, Rmax):
            for j in range(Gmin, Gmax):
                for k in range(Bmin, Bmax):
                    id = self.RGB_id_array[i,j,k]
                    close.append(id) if id else None
        return close
