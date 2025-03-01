import akshare as ak
import pandas as pd
import matplotlib.pyplot as plt

def compare_zh_index(symbols:list[str], date_range:list[str]):
    '''
    symbols(list(str)): symbols of the index
    date_range(list(str)): range of time are interested ["2023-1-1", "2024-1-1"]
    '''
    data = pd.DataFrame()
    start_date, end_date = date_range
    for symbol in symbols:

        df = ak.stock_zh_index_daily_em(symbol=symbol)
        df['date'] = pd.to_datetime(df['date'])

        df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]
        data[symbol] = df.set_index('date')['close']

    # normalize the data
    normalized = data / data.iloc[0] * 100

    # plot the comparison graph
    normalized.plot()
    plt.title('Chineese Index Comparison')
    plt.xlabel('Date')
    plt.ylabel('Index Value (%)')
    plt.grid(True)
    plt.legend(labels=[symbol+f" {normalized.iloc[-1][symbol] - 100:.0f}%" for symbol in symbols])
    plt.show()

if __name__ == '__main__':
    symbols = ['sh000300', 'sz399001', 'sz399006']
    date_range = ["2023-1-1", "2024-1-1"]
    compare_zh_index(symbols, date_range)