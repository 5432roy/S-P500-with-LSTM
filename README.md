# SP500-with-LSTM

## Description:
This repository hosts a project focused on developing a Long Short-Term Memory (LSTM) model. The objective of this model is to analyze and utilize data spanning the previous five years, alongside real-time news inputs from the internet, to accurately forecast market price trends.

## Approach
1. Get the historical data of the `S&P 500`, including opening price, closing price, and one day's high and low from the past 5 years.
2. Use a web crawler to fetch news from the internet that is related to the stock market randomly, and then feed the content to GPT, asking GPT to provide a score on a scale of 1 to 100 about the trend.

### Training
Using the data for `S&P 500` from the past 5 years to train

- Right now the model traced back 10 days as input
### Testing
Using the data for `Nasdaq 100` from the past 5 years for testing

## Sources
- [S&P 500 (SPX) Historical Data](https://www.nasdaq.com/market-activity/index/spx/historical?page=1&rows_per_page=10&timeline=y5)
- [NASDAQ-100 (NDX) Historical Data](https://www.nasdaq.com/market-activity/index/ndx/historical?page=1&rows_per_page=10&timeline=y5)
