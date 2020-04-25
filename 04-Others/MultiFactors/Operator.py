import numpy as np
import pandas as pd

class Op(object):
    
    def __init__(self):
        pass
    
    def Neutralize(method, alpha, start = 0, end = 0):
        print(method)
        if(method == 'test'):
            for ii in range(alpha.shape[0]):
                mean = np.nanmean(alpha[ii,:])
                alpha[ii,:] = alpha[ii,:] - mean
            
        if(method == "IND"):
            inds = pd.read_csv('groupdata.csv', index_col='date')
            #start = np.where(inds.index == start)[0].tolist()[0]
            #end = np.where(inds.index == end)[0].tolist()[0]
            for di in range(start, end+1):
                series = inds.iloc[di,:]
                for ind in series.unique():
                    cond = (series==ind)
                    mean = np.nanmean(alpha[di-start][cond])
                    alpha[di-start][cond] = alpha[di-start][cond] - mean
            '''
        if(method == "MV"):
            1
        else:
            print("No such Neutralization!!")
            '''
        return alpha
    
    def rank_col(data):
        return pd.DataFrame(data).rank(pct=True, axis=1)
    def rank_row(data):
        return pd.DataFrame(data).rank(pct=True, axis=0)
    def tsrank(data, window):
        rank = data.copy()
        rank.iloc[:window-1,:] = np.nan
        for ii in range(window, data.shape[0]+1):
            tmp = data.iloc[ii-window:ii,:]
            rank.iloc[ii-1,:] = Op.rank_row(tmp).iloc[-1]
        return rank