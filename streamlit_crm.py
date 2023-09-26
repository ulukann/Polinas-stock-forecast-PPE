import datetime as dt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from lifetimes import BetaGeoFitter
from lifetimes import GammaGammaFitter
from lifetimes.plotting import plot_period_transactions
import streamlit as st
import warnings
import datetime
from datetime import date
from datetime import datetime
from PIL import Image
from PIL import Image, ImageDraw
import time
import math
import matplotlib.patches as patches
import json
from streamlit_lottie import st_lottie
import requests
import base64
import plotly.express as px

import streamlit as st
import time

st.set_page_config(page_title="Polinas_CRM", page_icon=":chart_with_upwards_trend:", layout="wide")

warnings.filterwarnings("ignore")

df = pd.read_excel("osman/otomat/otomat_34.xlsx")

st.markdown("<h1 style='text-align: center;'>  ' POLİNAS PLASTİK ' </h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'> - OTOMAT MAKİNESİ STOK TAHMİNİ -</h2>", unsafe_allow_html=True)

# st.sidebar.subheader("Personal Protective Equipment CRM Analysis")

# İlk yarıya içerik ekleyin
#st.sidebar.image("osman/otomat/worker_vahit.png", use_column_width=True)
#st.sidebar.write("Bu üst yarının içeriği.")
# İlk yarıya içerik ekleyin
st.sidebar.image("osman/otomat/vahit_work.png", use_column_width=True)
# st.sidebar.write("Üst sidebar için not.")


# st.sidebar.markdown("<h1 style='text-align: center;'> PYT </h1>", unsafe_allow_html=True)
image_path = "osman/otomat/200w.gif"
st.sidebar.image(image_path, use_column_width=True)


# vahit = "osman/otomat/vahit_worker.png"
# st.sidebar.image(vahit, use_column_width=True)


menu_options = ["Giriş", "Veri Seti ve Çalışma Hakkında Genel Bilgilendirme", "Stok Tahmin Merkezi"]
st.sidebar.markdown("<h2> -Veri Good- </h2>", unsafe_allow_html=True)
page = st.sidebar.radio("Sayfa Menüsü", menu_options)

with st.sidebar:
    st.audio("osman/otomat/SnapInsta.io - Legends Are Made (128 kbps).mp3", format="audio/mp3")
st.sidebar.write("This is how legends are made")

## Analog Saat

# import streamlit as st
# import datetime
# import matplotlib.pyplot as plt
# import matplotlib.patches as patches
# import math
#
#
# # Şu anki zamanı alın
# suanki_zaman = datetime.datetime.now()
#
# # Zamanı düzenleyin
# saat = suanki_zaman.hour % 12
# dakika = suanki_zaman.minute
#
# # Canvas'ı oluşturun
# fig, ax = plt.subplots(figsize=(2, 2))
# ax.set_aspect("equal")
# ax.set_facecolor("lightgray")
# ax.add_patch(patches.Circle((0.5, 0.5), 0.4, linewidth=2, edgecolor="black", facecolor="white"))
# ax.plot(0.5, 0.5, 'ro', markersize=6)
#
# # Saat işaretçisi
# saat_aci = math.radians(90 - (saat + dakika / 60) * 360 / 12)
# ax.plot([0.5, 0.5 + 0.3 * math.cos(saat_aci)], [0.5, 0.5 + 0.3 * math.sin(saat_aci)], color="black", linewidth=4)
#
# # Dakika işaretçisi
# dakika_aci = math.radians(90 - dakika * 360 / 60)
# ax.plot([0.5, 0.5 + 0.4 * math.cos(dakika_aci)], [0.5, 0.5 + 0.4 * math.sin(dakika_aci)], color="black", linewidth=2)
#
# ax.set_xticks([])
# ax.set_yticks([])
# ax.set_xticklabels([])
# ax.set_yticklabels([])
#
# st.sidebar.pyplot(fig)

if page == "Giriş":



    def load_lottiefile(filepath: str):
        with open(filepath, "r") as f:
            return json.load(f)

    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()


    col1, col2, col3 = st.columns([2,2,2])

    loti = load_lottieurl("https://lottie.host/9e67d435-232f-4c2f-a1f3-435b4afafb3a/irzHEOMqqm.json")
    loti3 = load_lottieurl("https://lottie.host/3a6eecc8-137e-4af1-b94b-e14cca61014e/utMdcpPfdG.json")
    with col1:
        st_lottie(loti, width=200, height=200)
    with col2:
        st.image("osman/otomat/polinas.jpg")
    with col3:
        st_lottie(loti3, width=200, height=200)

########################################################################################################################

    st.markdown("<h2 style='text-align:center;'> GİRİŞ </h2>", unsafe_allow_html=True)

    st.write(
        """Bu çalışmanın sunumu 3 sayfadan oluşmaktadır. Sayfalara sol menüden erişebilirsiniz.""")
    st.write("""1. Giriş""")
    st.write("""2. Veri Seti ve Çalışma Hakkında Genel Bilgilendirme""")
    st.write("""3. Stok Tahmin Merkezi""")

    st.write(
        """Fabrikada kullanılan kişisel koruyucu donanım otomatlarına ait veriler ile çalışma yapılmıştır.""")
    st.write(
        """Veri Seti ve Çalışma Hakkında Genel Bilgilendirme sayfasında veri ile ilgili bilgileri görebilirsiniz ve grafikleri inceleyebilirsiniz.""")
    st.write(
        """Tahminleme sayfasında önümüzdeki tarihlerde kaç adet kullanım olacağını tarih bazlı ve departman bazlı görebilirsiniz.""")



    gif_path = "osman/otomat/khaby-really.gif"

    checkbox_value = st.checkbox("Sende stok bitti diye ağlayanlardan mısın? Çözümünü bulmak ister misin?")
    if checkbox_value:
        slider_value = st.slider("Ne Kadar istersin?", 0, 100)
        if slider_value == 0:
            st.write("""Çözüme ne kadar ihtiyacın var?""")
        elif slider_value < 95:
            st.error('This is an error', icon="🔥")
            st.write("""Yeteri kadar yok gibi.""")
            st.write("""Tekrar düşünüp bir kez daha dene.""")
        else:
            st.write("""Çözüm ayağına geldi.""")
            st.balloons()
            st.image(gif_path, use_column_width=True)

    metin = "[Ekibimize ait videomuz için tıklayın.](https://www.youtube.com/watch?v=CzN6zVmWSZE)"

    # Metni görüntüle
    st.markdown(metin, unsafe_allow_html=True)

elif page == "Veri Seti ve Çalışma Hakkında Genel Bilgilendirme":


    st.markdown("<h3 style='text-align:center;'>  ELİMİZDEKİ VERİ HAKKINDA GENEL BİLGİLENDİRME </h3>", unsafe_allow_html=True)
    st.dataframe(df,use_container_width=True, hide_index=True, height= 300)
    st.write("""Veri toplam 2 yıllık süreyi içermektedir. İki yıl içerisinde kullanılan toplam kişisel koruyucu donanım miktarlarına ait grafik aşağıdadır.""")


    df = pd.read_excel("osman/otomat/otomat_34.xlsx")

    urun_df = df.groupby("ÜRÜN")["MIKTAR"].sum()

    multi_1 = pd.Series(urun_df, name='example_series')

    urun_df = pd.DataFrame(multi_1)

    urun_df = urun_df.reset_index()

    urun_df.columns = ['ÜRÜN', "MİKTAR"]


    st.bar_chart(data=urun_df, x='ÜRÜN', y="MİKTAR", color="#8b3a3a", width=50, height=500, use_container_width=True)

    dep_df = df.groupby(["ÜRÜN", "POZISYON"])["MIKTAR"].sum()

    multi_2 = pd.Series(dep_df, name='example_series')

    dep_df = pd.DataFrame(multi_2)

    dep_df = dep_df.reset_index()

    dep_df.columns = ['ÜRÜN', "POZISYON", "MİKTAR"]

    dep_df.head()

    dep_df = dep_df.groupby("POZISYON").agg("MİKTAR").sum()

    dep_df = dep_df.reset_index()

    dep_df.columns = ["POZISYON", "MİKTAR"]

    st.write("""Departman bazlı kullanım için aşağıdaki grafiği inceleyebilirsiniz.""")

    st.bar_chart(data=dep_df, x="POZISYON", y="MİKTAR", color="#8b3a3a", width=100, height=500, use_container_width=True)

    fig = px.pie(dep_df, values='MİKTAR', names='POZISYON', title='Departmana Göre KKD Kullanım Miktarı')

    # Streamlit uygulamasını oluşturun
    st.plotly_chart(fig)







elif page == "Stok Tahmin Merkezi":

    df.columns = df.columns.str.upper()
    df.columns = ['İŞLEM_NO', 'MAKINE_YERI', 'KART_ID', 'ÜRÜN', 'MIKTAR', 'FIYAT', 'POZISYON', 'TARIH']
    today_date = dt.datetime(2023, 9, 1)

    kart_id_notna = df['KART_ID'].dropna()  # Boş olmayan KartId değerlerini alıyoruz.
    for i, row in df.iterrows():
        if pd.isna(row['KART_ID']):
            random_index = np.random.randint(0, len(kart_id_notna))  # Rastgele bir indeks seçiyoruz.
            random_value = kart_id_notna.iloc[random_index]  # Seçilen indeksteki değeri alıyoruz.
            df.at[i, 'KART_ID'] = random_value

    cltv_df = df.groupby(["KART_ID", "ÜRÜN", "POZISYON"]).agg(
        {'TARIH': [lambda Tarih: (Tarih.max() - Tarih.min()).days,
                   lambda Tarih: (today_date - Tarih.min()).days],
         'İŞLEM_NO': lambda Invoice: Invoice.nunique(),
         'FIYAT': lambda Fiyat: Fiyat.sum()})

    cltv_df.columns = cltv_df.columns.droplevel(0)

    cltv_df.columns = ['recency', 'T', 'frequency', 'monetary']

    cltv_df["monetary"] = cltv_df["monetary"] / cltv_df["frequency"]

    cltv_df["recency"] = cltv_df["recency"] / 7

    cltv_df["T"] = cltv_df["T"] / 7

    st.markdown("<h2 style='text-align:center;'> - STOK TAHMİN MERKEZİ - </h2>", unsafe_allow_html=True)

    df_ = cltv_df.groupby(["frequency", "recency", "T"]).size().reset_index()

    bgf = BetaGeoFitter(penalizer_coef=0.001)

    bgf.fit(df_['frequency'],
            df_['recency'],
            df_['T'])

    tahmin_hafta = bgf.conditional_expected_number_of_purchases_up_to_time(1,
                                                            cltv_df['frequency'],
                                                            cltv_df['recency'],
                                                            cltv_df['T'])

    tahmin_ay = bgf.conditional_expected_number_of_purchases_up_to_time(4,
                                                                     cltv_df['frequency'],
                                                                     cltv_df['recency'],
                                                                     cltv_df['T'])

    tahmin_3ay = bgf.conditional_expected_number_of_purchases_up_to_time(4*3,
                                                            cltv_df['frequency'],
                                                            cltv_df['recency'],
                                                            cltv_df['T'])


    # data_12 = pd.Series(tahmin_3ay, name="example")
    # data_12 = pd.DataFrame(data_12)
    # data_12 = data_12.reset_index()
    # data_12 = round(data_12.groupby("ÜRÜN").agg("sum"), 0)
    # data_12.columns = ["Tahmin (Adet)"]


    data_12 = pd.Series(tahmin_3ay, name="example")
    data_12 = pd.DataFrame(data_12)
    data_12 = data_12.reset_index()
    data_12.head()
    data_12= round(data_12.groupby("ÜRÜN").agg("sum"), 0)
    data_12.columns = ["Tahmin (Adet)"]

    veri_1 = pd.Series(tahmin_hafta, name="example")
    data_1 = pd.DataFrame(veri_1)
    data_1 = data_1.reset_index()
    data_1.head()
    data_1= round(data_1.groupby("ÜRÜN").agg("sum"), 0)
    data_1.columns = ["Tahmin (Adet)"]


    veri_4 = pd.Series(tahmin_ay, name="example")
    data_4 = pd.DataFrame(veri_4)
    data_4 = round(data_4.reset_index(), 0)
    data_4.head()
    data_4= data_4.groupby("ÜRÜN").agg("sum")
    data_4.columns = ["Tahmin (Adet)"]

    veri_12_d = pd.Series(tahmin_3ay, name="example")
    veri_12_d = pd.DataFrame(veri_12_d)
    veri_12_d = veri_12_d.reset_index()
    veri_12_d = round(veri_12_d.groupby(["ÜRÜN", "POZISYON"]).agg("sum"), 0)
    veri_12_d.columns = ["Tahmin (Adet)"]

    veri_4_d = pd.Series(tahmin_ay, name="example")
    veri_4_d = pd.DataFrame(veri_4_d)
    veri_4_d = round(veri_4_d.reset_index(), 0)
    veri_4_d.head()
    veri_4_d= veri_4_d.groupby(["ÜRÜN", "POZISYON"]).agg("sum")
    veri_4_d.columns = ["Tahmin (Adet)"]

    veri_1_d = pd.Series(tahmin_hafta, name="example")
    veri_1_d = pd.DataFrame(veri_1_d)
    veri_1_d = veri_1_d.reset_index()
    veri_1_d.head()
    veri_1_d= round(veri_1_d.groupby(["ÜRÜN", "POZISYON"]).agg("sum"), 0)
    veri_1_d.columns = ["Tahmin (Adet)"]


    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()



    checkbox_value = st.checkbox("Ne kadar stok tutmalıyım?")
    if checkbox_value:
        secim = st.selectbox("Seçenekleri Seçin", ["Tahmin Türü Seç", "KKD Adet Tahmini", "Departman Bazlı Adet Tahmini"], index=0)
        gorsel = "osman/otomat/1.jpg"
        timegorsel = "osman/otomat/time.gif"
        gorsel = "osman/otomat/vahit_worker.png"
        if secim == "Tahmin Türü Seç":
            st.image("osman/otomat/tugce hoca.gif")
        if secim == "KKD Adet Tahmini":
            secim2 = st.selectbox("Tarih Seçin", ["Tarih Seç", "1 Hafta", "1 Ay", "3 Ay"])
            if secim2 == "Tarih Seç":
                st.image(timegorsel, use_column_width=True)
            elif secim2 == "1 Hafta":
                st.write("Bir hafta için stok tutman gereken ürün miktarları aşağıda verilmiştir.")
                st.dataframe(data_1)
            elif secim2 == "1 Ay":
                st.write("Bir ay için stok tutman gereken ürün miktarları aşağıda verilmiştir.")
                st.dataframe(data_4)
            else:
                st.write("Bir ay için stok tutman gereken ürün miktarları aşağıda verilmiştir.")
                st.dataframe(data_12)
        elif secim == "Departman Bazlı Adet Tahmini":
            secim3 = st.selectbox("Tarih Seçin", ["Tarih Seç", "1 Hafta", "1 Ay", "3 Ay"])
            if secim3 == "Tarih Seç":
                st.image(timegorsel, use_column_width=True)
            elif secim3 == "1 Hafta":
                st.write("Bir hafta için departman bazlı stok tutman gereken ürün miktarları aşağıda verilmiştir.")
                st.dataframe(veri_1_d)
            elif secim3 == "1 Ay":
                st.write("Bir ay için departman bazlı stok tutman gereken ürün miktarları aşağıda verilmiştir.")
                st.dataframe(veri_4_d)
            elif secim3 == "3 Ay":
                st.write("Üç ay için departman bazlı stok tutman gereken ürün miktarları aşağıda verilmiştir.")
                st.dataframe(veri_12_d)


































































