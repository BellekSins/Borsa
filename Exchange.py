import yfinance as yf
import pandas as pd
import datetime as dt

symbol = input("Lütfen sembol giriniz: ")
aralık = input("Lütfen aralık giriniz: ")

zaman = dt.datetime.now().strftime("%d %m %Y %H.%M")
print(f"Zaman: {zaman}")

stock_data = yf.download(symbol, period= aralık+"d", interval="1d")

stock_data = stock_data.rename(columns={
    "date": "Tarih",
    "Open": "Açılış",
    "High": "En Yüksek",
    "Low": "En Düşük",
    "Close": "Kapanış",
    "Adj Close": "Düzeltilmiş Kapanış",
    "Volume": "Hacim"
})

filename = f"{symbol} son {aralık} gün {zaman}.xlsx"
writer = pd.ExcelWriter(filename, engine='xlsxwriter')

stock_data.to_excel(writer, sheet_name='Data')

workbook = writer.book

workbook.close()

print(f"{filename} dosyası başarıyla kaydedildi.")
