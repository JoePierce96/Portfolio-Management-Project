import pandas as pd
import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import glob
sns.set(style='ticks')

start = datetime.datetime(2018, 7, 1)
end = datetime.datetime(2019, 6, 30)

#dataframe of each stock

bp_df = web.DataReader("BP.L", 'yahoo', start=start, end=end)
gsk_df = web.DataReader("GSK.L", 'yahoo', start=start, end=end)
ocdo_df = web.DataReader("OCDO.L", 'yahoo', start=start, end=end)
rbs_df = web.DataReader("RBS.L", 'yahoo', start=start, end=end)
svt_df = web.DataReader("SVT.L", 'yahoo', start=start, end=end)
iii_df = pd.read_csv("iii (1).csv", parse_dates=['Date'])

#close of each stock

bp_close = bp_df["Adj Close"]
gsk_close = gsk_df["Adj Close"]
ocdo_close = ocdo_df["Adj Close"]
rbs_close = rbs_df["Adj Close"]
svt_close = svt_df["Adj Close"]
iii_close = iii_df["Adj Close"]


#adding normalised returns for portfolio

#adding portfolio weights

#portfolio position value column

#comparison of returns for portfolio

pt_comp = web.DataReader(['BP.L', 'III.L', 'GSK.L', 'OCDO.L', 'RBS.L', 'SVT.L'], 'yahoo',start=start,end=end) ['Adj Close']

#Percentage returns of each stock 

pt_rets = pt_comp.pct_change()

#correlation between stocks 

corr = pt_rets.corr()


#corrlation heat map


ax = sns.heatmap(corr)
plt.colorbar()
plt.xticks(range(len(corr)), corr.columns)
plt.yticks(range(len(corr)), corr.columns)






# adjusting size of 