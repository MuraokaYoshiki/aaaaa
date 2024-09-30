#tukey.py
############# Tukey_Cramerの多重分析モジュール ########
# ind: Group index
# *args: data
def tukey_hsd( ind, *args ):
    import pandas as pd
    import numpy as np
    from statsmodels.stats.multicomp import pairwise_tukeyhsd

    data_arr = np.hstack( args ) 
    ind_arr = np.array([])
    for x in range(len(args)):
      ind_arr = np.append(ind_arr, np.repeat(ind[x], len(args[x]))) 
    print(pairwise_tukeyhsd(data_arr,ind_arr))
