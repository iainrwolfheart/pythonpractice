import matplotlib.pyplot as plot

Year=[2010,2011,2012,2013,2014]
Rice=[20,30,40,30,50]

plot.xlabel("Year")
plot.ylabel("Rice")
plot.title("Rice Production")
plot.plot(Year, Rice)
plot.show()