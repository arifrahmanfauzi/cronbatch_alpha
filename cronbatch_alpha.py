

def cronbatch_alpha(df):
    itemscores = np.asarray(df.iloc[:,:-1])
    itemvars = itemscores.var(axis=0, ddof=0)
    tscores = itemscores.sum(axis=0)
    nitems = itemscores.shape[1]
    nitems_row = itemscores.shape[0]
    
    total = itemscores.sum(axis=1)**2
    total_kuadrat_baris = total.sum()

    total_varians = (total_kuadrat_baris - ((itemscores.sum()**2) / nitems_row)) / nitems_row
    result = (nitems / (nitems-1)) * (1 - (itemvars.sum() / total_varians))

    return result