import tkinter as tk
import yfinance as yf

def view_stock(ticker):
  stock = yf.Ticker(ticker)
  text.delete("1.0", "end")
  text.insert("1.0", f" - {stock.info['shortName']}\n - ({ticker})\n - Current Market Price: ${stock.info['regularMarketPrice']}\n")

app = tk.Tk()
app.title("Stock Viewer")
label = tk.Label(app, text="Stock Name:")
label.pack()
entry = tk.Entry(app)
entry.pack()
button = tk.Button(app, text="View", command=lambda: view_stock(entry.get()))
button.pack()
text = tk.Text(app)
text.pack()

app.mainloop()