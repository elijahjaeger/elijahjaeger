import matplotlib.pyplot as plt
import yfinance as yf
import seaborn as sns

#aesthetic changes for plot
plt.rcParams["font.size"] = 7
sns.set_style("dark")

def stock() 
#asks for values of which stock and how long do you want to graph.
ack = input("What ticker do you want?:\n")
time = input("How Much time do you want to plot?:\n")

#asks if stock comparison is wanted
#creates data for second stock if wanted
blank = ''
ask = input("Do you want to compare stocks(y/n):\n")
if ask == "y":
  ach = input("What ticker do you want to compare?:\n")
  alticker = yf.Ticker(ach)
  bool = True
  ticker2 = yf.Ticker(ach)
  ticker_df2 = ticker2.history(period=time)
  shares2 = ticker_df2.Close
elif ask == 'n':
  bool = False

print("Check Output screen for graph.")

#Pulls stock values and how far back you want to pull.
ticker = yf.Ticker(ack)
ticker_df = ticker.history(period=time)

#shares function decides which data type you want to pull
shares1 = ticker_df.Close
#creates lineplot and assigns data
fig, ax = plt.subplots()

ax.plot(shares1, color='blue', label=ack)
if bool == True:
  ax.plot(shares2, color='red', label=ach)
  plt.title(ack + " / " + ach + " Closing Value(USD)")
elif bool == False:
  plt.title(ack + " Closing Value(USD)")
ax.legend(loc='upper right')

plt.show()
