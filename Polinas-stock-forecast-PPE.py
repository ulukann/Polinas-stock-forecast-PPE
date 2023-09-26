import datetime as dt
from typing import Any
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from lifetimes import BetaGeoFitter
from lifetimes import GammaGammaFitter
from lifetimes.plotting import plot_period_transactions
import matplotlib.pyplot as plt
from pandas import DataFrame, Series
from sklearn.metrics import mean_squared_error, mean_absolute_error


pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
pd.set_option('display.float_format', lambda x: '%.4f' % x)
pd.set_option('display.max_rows', None)


df = pd.read_excel("osman/otomat/otomat_34.xlsx")

df.head()

df.columns

df.columns = ['İŞLEM_NO', 'MAKINE_YERI', 'KART_ID', 'ÜRÜN', 'MIKTAR', 'FIYAT', 'POZISYON', 'TARIH']

df.describe().T

today_date = dt.datetime(2023, 9, 1)

df.isnull().sum()


kart_id_notna = df['KART_ID'].dropna()  # Boş olmayan KartId değerlerini alıyoruz.
for i, row in df.iterrows():
    if pd.isna(row['KART_ID']):
        random_index = np.random.randint(0, len(kart_id_notna))  # Rastgele bir indeks seçiyoruz.
        random_value = kart_id_notna.iloc[random_index]  # Seçilen indeksteki değeri alıyoruz.
        df.at[i, 'KART_ID'] = random_value



cltv_df = df.groupby(["KART_ID", "ÜRÜN", "POZISYON"]).agg(
    {'TARIH': [lambda Tarih: (Tarih.max() - Tarih.min()).days,
                     lambda Tarih: (today_date - Tarih.min()).days],
     'İŞLEM_NO': lambda işlem_no: işlem_no.nunique(),
     'FIYAT': lambda Fiyat: Fiyat.sum()})

df["İŞLEM_NO"].nunique()

cltv_df.columns = cltv_df.columns.droplevel(0)

cltv_df.columns = ['recency', 'T', 'frequency', 'monetary']

cltv_df["monetary"] = cltv_df["monetary"] / cltv_df["frequency"]

cltv_df["recency"] = cltv_df["recency"] / 7

cltv_df["T"] = cltv_df["T"] / 7

cltv_df.describe().T

df_ = cltv_df.groupby(["frequency", "recency", "T"]).size().reset_index()

bgf = BetaGeoFitter(penalizer_coef=0.001)


bgf.fit(df_['frequency'],
        df_['recency'],
        df_['T'])

df_.describe().T

df_['frequency'].max()

bgf.conditional_expected_number_of_purchases_up_to_time(1,
                                                        cltv_df['frequency'],
                                                        cltv_df['recency'],
                                                        cltv_df['T']).sort_values(ascending=False).head(10)

bgf.predict(4,
            cltv_df['frequency'],
            cltv_df['recency'],
            cltv_df['T']).sort_values(ascending=False).head(10)

cltv_df["expected_purc_1_week"] = bgf.predict(1,
                                              cltv_df['frequency'],
                                              cltv_df['recency'],
                                              cltv_df['T'])


tahmin = bgf.conditional_expected_number_of_purchases_up_to_time(4,
                                                        cltv_df['frequency'],
                                                        cltv_df['recency'],
                                                        cltv_df['T']).sort_values(ascending=False).head(10)



multi_column_series = pd.Series(tahmin, name='example_series')

rf = pd.DataFrame(multi_column_series)

rf = rf.reset_index()

rf.columns = ['KART_ID', 'ÜRÜN',"POZISYON", "TAHMİN"]

rf.head()

rf.groupby(["ÜRÜN", "POZISYON"]).agg("sum")

rf.groupby("ÜRÜN").agg("sum")

df.head()

rf.head()

rf.shape

df.groupby("ÜRÜN").agg("sum", "MIKTAR")


plot_period_transactions(bgf)
plt.show()

plot_period_transactions(bgf, title='Müşteri Tekrar Satın Alma İşlemleri', xlabel='Dönem', ylabel='Müşteri Sayısı')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()



cltv_df['frequency'].head()
gercek_satinalmalar = cltv_df['frequency'].values
tahmini_satinalmalar = bgf.conditional_expected_number_of_purchases_up_to_time(
    t=1,
    frequency=cltv_df['frequency'],
    recency=cltv_df['recency'],
    T=cltv_df['T']
).values

rmse = np.sqrt(mean_squared_error(gercek_satinalmalar, tahmini_satinalmalar))

mae = mean_absolute_error(gercek_satinalmalar, tahmini_satinalmalar)

print("RMSE:", rmse)
print("MAE:", mae)






















































