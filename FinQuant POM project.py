import pandas as pd
import datetime
import pathlib
import quandl
from finquant.portfolio import build_portfolio


"""bp_df = pd.read_csv("XLON-BP_.csv", parse_dates=['Date'])
iii_df = pd.read_csv("XLON-III.csv", parse_dates=['Date'])
gsk_df = pd.read_csv("XLON-GSK.csv", parse_dates=['Date'])
ocdo_df = pd.read_csv("XLON-OCDO.csv", parse_dates=['Date'])
rbs_df = pd.read_csv("XLON-RBS.csv", parse_dates=['Date'])
svt_df = pd.read_csv("XLON-SVT.csv", parse_dates=['Date'])

portfolio = pd.concat([bp_df, iii_df, gsk_df, ocdo_df, rbs_df, svt_df], axis=1)"""


d = {
     0: {"Name": "BP.L", "Allocation": 1000000},
     1: {"Name": "III.L", "Allocation": 1000000},
     2: {"Name": "GSK.L", "Allocation": 1000000},
     3: {"Name": "OCDO.L", "Allocation": 1000000},
     4: {"Name": "RBS.L", "Allocation": 2000000},
     5: {"Name": "SVT.L", "Allocation": 1000000},
     }

pf_allocation = pd.DataFrame.from_dict(d, orient="index")

#set list of names based on names
names = pf_allocation["Name"].values.tolist()

#start/end date
start = datetime.datetime(2018, 7, 1)
end = datetime.datetime(2019, 6, 30)

#building portfolio

pf = build_portfolio(
        names=names, data_api="yfinance", pf_allocation=pf_allocation, start_date=start, end_date=end
)

print(pf.portfolio)

#the portfolio stock data, prices DataFrame
print(pf.data.head(3))

#print information and quantities of a given portfolio
print(pf)
pf.properties()

#annualised mean returns
print(pf.comp_mean_returns())

#plotting cumulative returns
pf.comp_cumulative_returns().plot().axhline(y=0, color="black", lw=3)
plt.show()

#log returns

pf.comp_daily_log_returns().plot().axhline(y=0, color="black")
plt.show()
