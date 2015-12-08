import pandas as pd
import os
import time
from datetime import datetime
import matplotlib.pyplot as plt

path="/home/ubu/Downloads/intraQuarter"
def Key_Stats(xlist,ylist):
    #xlist=[]
    statspath=path+'/_KeyStats'
    df = pd.DataFrame(columns=[
                               #'TotalDebtEquity_hdr',
                               'Revenue_hdr',
                               'RevenuePerShare_hdr'
                               #'GrossProfit_hdr',
                               #'NYSEShare_hdr'
                               ])
    stock_list=[x[0] for x in os.walk(statspath)]
    #print(stock_list)
    for each_dir in stock_list[1:]:
        if (each_dir == statspath + '/a'):
            #print (each_dir)
            each_file = os.listdir(each_dir)
            #print(each_file)
            #xlist=[]
            #ylist=[]
            for file in each_file:
                
                #print(file)
                #try:
                    date_stamp = datetime.strptime(file, '%Y%m%d%H%M%S.html')
                    unix_time = time.mktime(date_stamp.timetuple())
                    full_file_path=each_dir +'/'+file
                    #print(full_file_path)
                    source=open(full_file_path, 'r').read()
                    #TotalDebtEquity=source.split('Total Debt/Equity (mrq):</td><td class="yfnc_tabledata1">')[1].split('</td>')[0]
                    #print(TotalDebtEquity)
                    Revenue=source.split('Revenue (ttm):</td><td class="yfnc_tabledata1">')[1].split('</td>')[0].split('B')[0]   
                    RevenuePerShare=source.split('Revenue Per Share (ttm):</td><td class="yfnc_tabledata1">')[1].split('</td>')[0]
                    
                    xlist.append(Revenue)
                    ylist.append(RevenuePerShare)
                    #print (xlist)
                    
                    #GrossProfit=source.split('Gross Profit (ttm):</td><td class="yfnc_tabledata1">')[1].split('</td>')[0].split('B')[0]
                    #Gross Profit (ttm)&sup2;:</td><td class="yfnc_tabledata1"
                    #GrossProfit=source.split('Gross Profit (ttm)&sup2;:</td><td class="yfnc_tabledata1">')[1].split('</td>')[0].split('B')[0]    
                    #print(GrossProfit)
                    #NYSEShare=source.split('<span class="time_rtq_ticker"><span id="yfs_l84_abbv">')[1].split('</span>')[0]
                    #print(NYSEShare)
                    #X_revenue.extend(Revenue)
                    #xaxis=([1,2,3,])
                    
                    df=df.append({
                            #'TotalDebtEquity_hdr':TotalDebtEquity,
                            'Revenue_hdr':Revenue,
                            'RevenuePerShare_hdr':RevenuePerShare
                             # 'GrossProfit_hdr':GrossProfit,
                             #'NYSEShare_hdr':NYSEShare,
                             },
                             ignore_index=True)
                    df.to_csv('keystats.csv')
            return (xlist,ylist)
            
                    
                #except Exception as e:
                    #pass
        
        
                


x=[]
y=[]
xlist,ylist = Key_Stats(x,y)
##print(xlist,ylist)
#plt.plot(xlist,ylist)
#plt.bar(xlist,ylist)
plt.scatter(xlist,ylist, label='skitscat', color='k', s=25, marker="o")
plt.xlabel('Revenue')
plt.ylabel('Revenue Per Share')
plt.title("Rvene Vs Revenue Per Share")
plt.legend()
plt.show()
