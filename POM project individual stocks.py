import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import log10, floor
import pandas_datareader.data as web
import datetime
import os
from scipy.stats import skew
os.environ["IEX_API_KEY"] = "pk_427ed136665b4a2fbb5adc15d2fdc37c"
#defines rounding function
def Round_sig(x, sig=2):
    return round(x, sig-int(floor(log10(abs(x))))-1)

#sorting the stock prices
start = datetime.datetime(2018, 7, 1)
end = datetime.datetime(2019, 6, 28)

bp_df = web.DataReader("BP.L", 'yahoo', start=start, end=end)
gsk_df = web.DataReader("GSK.L", 'yahoo', start=start, end=end)
ocdo_df = web.DataReader("OCDO.L", 'yahoo', start=start, end=end)
rbs_df = web.DataReader("RBS.L", 'yahoo', start=start, end=end)
svt_df = web.DataReader("SVT.L", 'yahoo', start=start, end=end)
iii_df = pd.read_csv("iii (1).csv", parse_dates=['Date'])


#closes

bp_close = bp_df["Adj Close"]
gsk_close = gsk_df["Adj Close"]
ocdo_close = ocdo_df["Adj Close"]
rbs_close = rbs_df["Adj Close"]
svt_close = svt_df["Adj Close"]
iii_close = iii_df["Adj Close"]

# calculates adjusted returns close prices and append the returns as a new column
# column in the dataframe  

bp_df["PCTReturns"] = bp_df["Adj Close"].pct_change()
gsk_df["PCTReturns"] = gsk_df["Adj Close"].pct_change()
ocdo_df["PCTReturns"] = ocdo_df["Adj Close"].pct_change()
rbs_df["PCTReturns"] = rbs_df["Adj Close"].pct_change()
svt_df["PCTReturns"] = svt_df["Adj Close"].pct_change()
iii_df["PCTReturns"] = iii_df["Adj Close"].pct_change()


#plots distribution of adjusted returns

#ftse100

#calculates mean pct stock returns annual

bpmean_returns = np.mean(bp_df["PCTReturns"])
print("BP mean annual stock returns are")
print(Round_sig(bpmean_returns, 3)*100)

gskmean_returns = np.mean(gsk_df["PCTReturns"])
print("GSK mean annual stock returns are")
print(Round_sig(gskmean_returns, 3)*100)

ocdomean_returns = np.mean(ocdo_df["PCTReturns"])
print("OCDO mean annual stock returns are")
print(Round_sig(ocdomean_returns, 3)*100)

rbsmean_returns = np.mean(rbs_df["PCTReturns"])
print("RBS mean annual stock returns are")
print(Round_sig(rbsmean_returns, 3)*100)

svtmean_returns = np.mean(svt_df["PCTReturns"])
print("SVT mean annual stock returns are")
print(Round_sig(svtmean_returns, 3)*100)

iiimean_returns = np.mean(iii_df["PCTReturns"])
print("3i mean annual stock returns are")
print(Round_sig(iiimean_returns, 3)*100)


#total mean returns

totmean_returns = 0.1426
print("The mean annual portfolio returns are")
print(totmean_returns)

#variance of stock 

bpvariance = np.std(bp_df["PCTReturns"])**2
print("Variance of BP")
print(Round_sig(bpvariance, 3))

gskvariance = np.std(gsk_df["PCTReturns"])**2
print("Variance of GSK")
print(Round_sig(gskvariance, 3))

ocdovariance = np.std(ocdo_df["PCTReturns"])**2
print("Variance of OCDO")
print(Round_sig(ocdovariance, 3))

rbsvariance = np.std(rbs_df["PCTReturns"])**2
print("Variance of RBS")
print(Round_sig(rbsvariance, 3))

svtvariance = np.std(svt_df["PCTReturns"])**2
print("Variance of SVT")
print(Round_sig(svtvariance, 3))

iiivariance = np.std(iii_df["PCTReturns"])**2
print("Variance of 3i")
print(Round_sig(iiivariance, 3))

#total variance
totalvariance = 0.000268
print("Total Variance is")
print(totalvariance)


#annualised volatility of returns

bpvol = np.std(bp_df["PCTReturns"]) * np.sqrt(252)
print("BP annualised volatility is")
print(Round_sig(bpvol, 3))

gskvol = np.std(gsk_df["PCTReturns"]) * np.sqrt(252)
print("GSK annualised volatility is")
print(Round_sig(gskvol, 3))

ocdovol = np.std(ocdo_df["PCTReturns"]) * np.sqrt(252)
print("OCDO annualised volatility is")
print(Round_sig(ocdovol, 3))

rbsvol = np.std(rbs_df["PCTReturns"]) * np.sqrt(252)
print("RBS annualised volatility is")
print(Round_sig(rbsvol, 3))

svtvol = np.std(svt_df["PCTReturns"]) * np.sqrt(252)
print("SVT annualised volatility is")
print(Round_sig(svtvol, 3))

iiivol = np.std(iii_df["PCTReturns"]) * np.sqrt(252)
print("3i annualised volatility is")
print(Round_sig(iiivol, 3))

totalvol = 0.25
print("Total annualised volatility is")
print(totalvol)

#skewness

bpskew = skew(bp_df['PCTReturns'].dropna())
print("BP skewness of returns are")
print(Round_sig(bpskew, 3))

gskskew = skew(gsk_df['PCTReturns'].dropna())
print("GSK skewness of returns are")
print(Round_sig(gskskew, 3))

ocdoskew = skew(ocdo_df['PCTReturns'].dropna())
print("OCDO skewness of returns are")
print(Round_sig(ocdoskew, 3))

rbsskew = skew(rbs_df['PCTReturns'].dropna())
print("RBS skewness of returns are")
print(Round_sig(rbsskew, 3))

svtskew = skew(svt_df['PCTReturns'].dropna())
print("SVT skewness of returns are")
print(Round_sig(svtskew, 3))

iiiskew = skew(iii_df['PCTReturns'].dropna())
print("3i skewness of returns are")
print(Round_sig(iiiskew, 3))


