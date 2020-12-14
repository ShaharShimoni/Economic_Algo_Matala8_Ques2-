# Economic_Algo_Matala8_Ques2

**Tender maximizes profit** <br />
The following class, represents a uniform distribution between low and high:<br />
class Uniform: <br />
low: float <br />
high: float <br />
I will perform a profit-maximization using the Myerson method, for the sale of one object: <br />
<br />
The function that performs the auction for one buyer:<br />
def max_revenue_auction (agent1: Uniform, value1: float): ...<br />
<br />
If the r(v) is greater than 0<br />
The object is sold to the buyer-The buyer pays r^-1(0)<br />
otherwise not sold.<br />
<br />
The following function performs the auction for two buyers:<br />
def max_revenue_auction (agent1: Uniform, agent2: Uniform,value1: float, value2: float): ...<br />
<br />
The person with the greatest value of r(v) wins the object and pays the greatest of:<br />
Threshold/r^-1(0)<br />
<br />
**I have attached tests to these functions:**<br />

For one player for example:<br />
<br />
 >>> Splits = Uniform ();<br />
 >>> Splits.low = 10;<br />
 >>> Splits.high = 30;<br />
  No agent wins

<br />
The value of r (v) <0<br />
And therefore does not buy the object.<br />
<br />
For two players,The following test is attached:<br />
<br />
 >>> Splits = Uniform ();<br />
 >>> Splits.low = 10;<br />
 >>> Splits.high = 30;<br />
 >>> Splits2 = Uniform ();<br />
 >>> Splits2.low = 20;<br />
 >>> Splits2.high = 40;<br />
 >>> max_revenue_auction2 (Splits, Splits2,23,27);<br />
    Agent 1 wins and pays 22<br />
<br />
The first person wins and pays the threshold value which is 22.<br />
<br />
