import streamlit as st

st.title("Yatırım Profili Anketi")

# Kişisel Bilgiler
yas = st.number_input("Yaşınız:", min_value=18)
cinsiyet = st.selectbox("Cinsiyet:", ["Erkek", "Kadın"])
egitim_seviyesi = st.selectbox("Eğitim Seviyesi:", ["Lise", "Lisans", "Yüksek Lisans", "Doktora"])
meslek = st.text_input("Meslek:")
yıllık_kazanc = st.number_input("Yıllık Kazanç:", min_value=0)

# Yatırım Deneyimi
yatirim_deneyimi = st.checkbox("Daha önce yatırım yaptınız mı?")
yatirim_deneyimi_yil = st.number_input("Yatırım deneyiminiz kaç yıl?", min_value=0)
yatirim_araclari = st.multiselect("Hangi yatırım araçlarını kullanıyorsunuz?", ["Hisseler", "Tahviller", "Fonlar"])

# Yatırım Hedefleri
yatirim_amaci = st.selectbox("Yatırım yaparken neyi amaçlıyorsunuz?", ["Emeklilik", "Ev alma", "Tatil", "Diğer"])
yatirim_hedef_suresi = st.number_input("Yatırım hedeflerinize ulaşmak için ne kadar zamanınız var?", min_value=1)
yatirim_hedef_kazanc = st.number_input("Yatırımlarınızdan ne kadar kazanç elde etmeyi umuyorsunuz?", min_value=0)

# Risk Toleransı
risk_toleransi = st.radio("Yatırımlarınızda ne kadar risk almaya hazırsınız?", ["Yüksek", "Orta", "Düşük"])
finansal_kayip_tepki = st.text_input("Geçmişte yaşadığınız finansal kayıplara nasıl tepki verdiniz?")
yatirim_dalgalanma_tahammul = st.radio("Yatırımlarınızda kısa vadeli dalgalanmalara ne kadar tahammülünüz var?", ["Yüksek", "Orta", "Düşük"])

# Yatırım Tercihleri
yatirim_araclari_tercih = st.multiselect("Hangi yatırım araçlarına ilgi duyuyorsunuz?", ["Hisseler", "Tahviller", "Fonlar", "Emtia", "Gayrimenkul"])
yatirim_stratejisi = st.selectbox("Ne tür bir yatırım stratejisi tercih edersiniz?", ["Aktif", "Pasif"])
yatirim_degisiklik_sikligi = st.radio("Ne kadar sıklıkla yatırımlarınızda değişiklik yapmayı düşünüyorsunuz?", ["Yüksek", "Orta", "Düşük"])

# Anketin Sonu
st.markdown("Anketi tamamladığınız için teşekkür ederiz.")
st.markdown("Cevaplarınız, yatırım profilinizi belirlemek ve size en uygun yatırım araçlarını önermek için kullanılacaktır.")

# Not
st.markdown("**Not:**")
st.markdown("Bu anket sadece bilgilendirme amaçlıdır ve yatırım tavsiyesi olarak yorumlanmamalıdır. Yatırım yapmadan önce lütfen bir finansal danışmana danışınız.")

