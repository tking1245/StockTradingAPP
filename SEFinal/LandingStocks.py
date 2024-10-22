import tkinter as tk
import numpy as np
import matplotlib as mpl
import pandas as pd
from datetime import date, timedelta
from matplotlib import pyplot as plt
import yfinance as yf

Start = date.today() - timedelta(7)
Start.strftime('%Y-%m-%d')

End = date.today() + timedelta(2)
End.strftime('%Y-%m-%d')


def run_Stock():
    LSWin = tk.Tk()

    


    LSWin.configure(bg = "grey25")
    LSWin.mainloop()
    return 




def closing_price(ticker):
    Asset = pd.DataFrame(yf.download(ticker, start=Start,
    end=End)['Adj Close'])     
    return Asset

TESLA = closing_price('TSLA')                  # CALL THE FUNCTION
AMAZON = closing_price('AMZN')
plt.plot(AMAZON)
plt.show()