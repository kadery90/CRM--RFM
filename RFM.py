import datetime as dt
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.5f' % x)
df_ = pd.read_excel(r"C:\Users\yildi\OneDrive\Masaüstü\datasets/online_retail_II.xlsx", sheet_name="Year 2010-2011")
df = df_.copy()
df.head()
df.shape

df.isnull().sum()

df.dropna(inplace=True)

df["Description"].nunique()

df["Description"].value_counts().head()

df.groupby("Description").agg({"Quantity": "sum"}).sort_values("Quantity", ascending=False).head(5)

df = df[~df["Invoice"].str.contains("C", na=False)]

df = df[(df['Quantity'] > 0)]
df = df[(df['Price'] > 0)]

df["TotalPrice"] = df["Quantity"] * df["Price"]

df["InvoiceDate"].max()
today_date = dt.datetime(2011, 12, 11)

rfm = df.groupby('Customer ID').agg({'InvoiceDate': lambda date: (today_date - date.max()).days,
                                                'Invoice': lambda num: num.nunique(),
                                                "TotalPrice": lambda TotalPrice: TotalPrice.sum()})

rfm.columns = ['recency', 'frequency', "monetary"]
rfm = rfm[(rfm['monetary'] > 0)]

rfm["recency_score"] = pd.qcut(rfm['recency'], 5, labels=[5, 4, 3, 2, 1])
rfm["frequency_score"] = pd.qcut(rfm["frequency"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5])
rfm["monetary_score"] = pd.qcut(rfm['monetary'], 5, labels=[1, 2, 3, 4, 5])

rfm["RFM_SCORE"] = (rfm['recency_score'].astype(str) +
                    rfm['frequency_score'].astype(str))

print(rfm.head())

seg_map = {
        r'[1-2][1-2]': 'hibernating',
        r'[1-2][3-4]': 'at_risk',
        r'[1-2]5': 'cant_loose',
        r'3[1-2]': 'about_to_sleep',
        r'33': 'need_attention',
        r'[3-4][4-5]': 'loyal_customers',
        r'41': 'promising',
        r'51': 'new_customers',
        r'[4-5][2-3]': 'potential_loyalists',
        r'5[4-5]': 'champions'
         }

rfm['segment'] = rfm['RFM_SCORE'].replace(seg_map, regex=True)
rfm = rfm[["recency", "frequency", "monetary", "segment"]]

rfm.head()

rfm[rfm["segment"] == "loyal_customers"].index

new_df = pd.DataFrame()
new_df["loyal_customers_id"] = rfm[rfm["segment"] == "loyal_customers"].index
new_df.to_csv("loyal_customers.csv")

rfm[["segment", "recency", "frequency", "monetary"]].groupby("segment").agg(["mean", "count"])

print(rfm[["segment", "recency", "frequency", "monetary"]].groupby("segment").agg(["mean", "count"]))


###############################################################
# cant_loose segmenti yüksek sıklıkla satın alma yapmaktadır. Bununla birlikte yeniliği düşüktür.
# Bu segmentteki müşterilerle kendimizi hatırlatmak üzere iletişime geçebiliriz.
# Son veya sık aldığı ürün kategorisine benzer ürün önerisi yapılabilir.
#
# new_customers segmenti yeni satınalma yapmışlardır, satış sonrası hizmet memnuniyetini
# yüksek seviyede tutmak üzere anket paylaşılabilir. Hoşgeldin hediyesi sunulabilir.
#
# champions segmenti en sık ve en yeni satın alma yapan segmenttir. Bu segmentle iletişim
# ödül kıvamında olmalıdır. En yüksek kazancı getirmektedir. 


###############################################################