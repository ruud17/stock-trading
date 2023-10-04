## Task: 
Implement a function to maximize profit from buying and selling stocks based on daily prices.

## Requirements:

The function should take a list of integers, prices, representing daily stock values.
Each item in the list corresponds to one day and represents the stock price for that day.
Calculate the maximum profit that can be obtained by buying and selling stocks based on the given rules.

#### **Rules**:
* Only one stock can be bought per day, based on the price for that day.
* If you decide to sell, all currently held stocks must be sold on the same day, based on the price for that day.
* On each day, you can choose one of the following actions:

  * Buy a stock
  * Sell all currently held stocks
  * Skip the action for that day
* If the stock prices are descending for the given sequence of days, return 0.

---
## Examples
### Example 1:
`input = [1,2,3,4,5]`

=> _output_ is **10**. 
To maximize profit, we should purchase stocks on the 1st, 2nd, 3rd, and 4th days, and then sell them on the 5th day.

_result = -1-2-3-4+5*4 = 10_

### Example 2:
`input = [5,4,3,2,1]
`
=> _output_ is **0**. 

To maximize profit, we should not buy any stocks because the values are decreasing each day.

### Example 3:
`input = [3,5,2,8,1,7,4]
` => _output_ is **20**. 

To maximize profit, we should buy stocks on day 1, 2, and 3, and sell them on day 4 when the price is 8. Then, we should buy a new stock for the price of 1 on another day and sell it a day after for the price of 7. The last stock value of 4 will not be considered, as there are no more days to sell it.

_result = -1-2-3-4+5*4 = 10_

