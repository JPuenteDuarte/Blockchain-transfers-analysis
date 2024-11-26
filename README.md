# Blockchain-transfers-analysis

### Javier Puente Duarte

<br/><br/>


This project provides tools to read, parse, calculate and represent raw json block files and transactions files from the Bitcoin blockchain in Python 3 language. This allows the user to navigate Bitcoin fundamental transaction data from the source by either applying the basic functions contained in this project or creating new ones based on these parsing tools.



The Bitcoin block generation time, which is the time that the block discovery process takes in average, is 10 minutes. This is the amount of time each block takes in average to be mined. Since the May 2020 halving, the reward of mining one block was set to 6.25 bitcoins. These premises are relevante since they allow us to calculate the speed at which one Bitcoin is mined, which is about 6.25 bitcoins/10 minutes = 37.5 seconds.

The plot below serves as an example of the mining speeds described, with blocks being mined after very different time periods, yet averaging about 600 seconds:

<br/><br/>

![Alt text](plot_1.png?raw=true "Title")
<br/><br/>

There are however other simple metrics available in this project. Some of them relate to the value of the transactions on each block or to the number of those transactions. The latter can be obtained either as a metric relative to blocks or to actual hours as seen below:

![Alt text](plot_2.png?raw=true "Title")
<br/><br/>
