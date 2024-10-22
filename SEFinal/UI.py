import tkinter as tk
from PIL import Image, ImageTk
import yfinance as yf
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from SpecificStocksPull import create_graph_for_pulled_data

def open_Dumwin():
    win = tk.Tk()
    

    win.mainloop()
    


def create_csv(stock, time):
    """Fetch historical data for a stock and save it to a CSV file."""
    try:
        stock_name = yf.Ticker(stock)
        data = stock_name.history(period=time)
        
        if data.empty:
            return f"No data found for {stock} with the time frame '{time}'"
        
        # Convert data to a DataFrame
        df_data = pd.DataFrame(data)
        csv_filename = f"{stock}_{time}.csv"
        
        
        # Save to CSV
        df_data.to_csv(csv_filename, index=True)
        
        return (f"Data saved to {csv_filename}" , create_graph_for_pulled_data(stock, time))
    
    except Exception as e:
        return f"Error: {e}"

def show_sidebar(event):
    """Show the sidebar and hide the menu icon when hovering over the menu icon."""
    menu_icon.place_forget()
    sidebar.place(x=5, y=5)

def hide_sidebar(event):
    """Hide the sidebar and show the menu icon when moving away from the sidebar."""
    sidebar.place_forget()
    menu_icon.place(x=10, y=10)

########### HISTORY DATA WINDOW 
def run_historic_data_window():
    """Open a new window for historic data input."""
    hisWin = tk.Tk()
    hisWin.geometry('300x300')
 
    # Input fields for stock and time frame
    stock_label = tk.Label(hisWin, text="Enter stock symbol:")
    stock_label.pack(pady=5)
    stockinput = tk.Entry(hisWin, width=20)
    stockinput.pack(pady=5)

    time_label = tk.Label(hisWin, text="Enter time frame (e.g., 1mo, 3mo, 1y):")
    time_label.pack(pady=5)
    timeFrame = tk.Entry(hisWin, width=20)
    timeFrame.pack(pady=5)

    result_label = tk.Label(hisWin, text="")
    result_label.pack(pady=10)

    # Define command for the button
    def grab_data():
        stock = stockinput.get().strip()
        time = timeFrame.get().strip()
        result = create_csv(stock, time)
        result_label.config(text=result)

    # Button to trigger the graph creation
    getinfo = tk.Button(hisWin, text="Grab", compound="bottom", background='white', command=grab_data)
    getinfo.pack(pady=15)
    
    hisWin.mainloop()

# Create the main window
window = tk.Tk()
window.title('Landing Page')
window.geometry('900x600')

# Load and resize the image
examplegraph = Image.open('dummyGr.png')
resize_graph = examplegraph.resize((150, 100))
newimggr = ImageTk.PhotoImage(resize_graph)

# Buttons for stocks with images
stockbutton = tk.Button(window, text="Name of Stock", image=newimggr, compound='top')
stockbutton.place(x=80, y=50)
stockbutton1 = tk.Button(window, text="Name of Stock", image=newimggr, compound='top')
stockbutton1.place(x=370, y=50)
stockbutton2 = tk.Button(window, text="Name of Stock", image=newimggr, compound='top')
stockbutton2.place(x=660, y=50)
stockbutton3 = tk.Button(window, text="Name of Stock", image=newimggr, compound='top')
stockbutton3.place(x=80, y=290)
stockbutton4 = tk.Button(window, text="Name of Stock", image=newimggr, compound='top')
stockbutton4.place(x=370, y=290)
stockbutton5 = tk.Button(window, text="Name of Stock", image=newimggr, compound='top')
stockbutton5.place(x=660, y=290)

# Create a frame for the sidebar on the left
sidebar = tk.Frame(window, width=200, height=600, bd=2, relief='solid')

# Sidebar buttons or options
sidebar_button1 = tk.Button(sidebar, text="Trading Practice", relief="sunken", fg="Black", font=("Times", 12))
sidebar_button1.pack(pady=10, padx=10, fill='x')
sidebar_button2 = tk.Button(sidebar, text="TEMP LOAD DATA", relief="flat", command=run_historic_data_window, fg="Black", font=("Arial", 12))
sidebar_button2.pack(pady=10, padx=10, fill='x')
sidebar_button3 = tk.Button(sidebar, text="Option 3", relief="flat", fg="Black", font=("Arial", 12), command = open_Dumwin)
sidebar_button3.pack(pady=10, padx=10, fill='x')

# Menu icon button
menu_icon = tk.Button(window, text="☰", font=("Arial", 16), bg="grey", fg="DarkSlateGrey", relief="flat")
menu_icon.place(x=10, y=10)

# Bind events for sidebar and menu icon
menu_icon.bind("<Enter>", show_sidebar)
sidebar.bind("<Leave>", hide_sidebar)

# Set window background
window.config(background='DarkSlateGrey')

# Run the application
window.mainloop()


########## THIS IS THE TKINTER LANDING PAGE GRAPH COMPILING CODE

def graph_stuff():
    root = tk.Tk()
    root.title("Real-Time Stock Price")


    frame = tk.Frame(root)
    frame.pack()

    fig, ax = plt.subplots()

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.get_tk_widget().pack()

    def update_graph(stock_symbol):
        stock_data = yf.download(tickers=stock_symbol, period='1d', interval='1m')
        ax.clear()
        
        stock_data['Close'].plot(ax=ax, color='blue')
        

        ax.set_title(f'Real-Time Stock Price for {stock_symbol}')
        ax.set_xlabel('Time')
        ax.set_ylabel('Price (USD)')
        canvas.draw()

    def refresh_graph(stock_symbol):
        update_graph(stock_symbol)
        root.after(60000, refresh_graph, stock_symbol)


    root.mainloop()

######
