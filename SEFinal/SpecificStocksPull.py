import pandas as pd
import matplotlib.pyplot as plt

def create_graph_for_pulled_data(stock, time):

    read = pd.read_csv(f"{stock}_{time}.csv")

    pulled_Data_to_Dataframe = pd.DataFrame(read)

    plt.figure(figsize=(10, 6))

    plt.plot(pulled_Data_to_Dataframe['Date'], pulled_Data_to_Dataframe['Close'], linestyle='-', color='DarkSlateGrey', label = 
                                                                                f'{stock.upper()} price during the past {time}')

    
    plt.xlabel('Date')
    plt.ylabel('Closing price ($)')

    plt.legend()
    return plt.show()
