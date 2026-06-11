import pandas as pd

df = pd.read_excel(r"C:\Users\emirb\Desktop\Airline_Operations_Analytics.xlsx", sheet_name="Delay_Reasons_Data")

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

print("        --- TABLO İSTATİSTİKLERİ ---")
print(df.describe())
print("-" * 30)

kritik_rotarlar = []

for rotar_dakikasi in df["Delay_Minutes"]:
    if rotar_dakikasi > 30:
        kritik_rotarlar.append("Kritik Rötar")
    elif rotar_dakikasi > 15:
        kritik_rotarlar.append("Orta Derece Rötar")
    else:
        kritik_rotarlar.append("Normal / Zamanında")

print("--- İLK 10 UÇUŞUN RÖTAR DURUMU  ---")
for durum in kritik_rotarlar[:10]:
    print(durum)

kritik_sayisi = 0
toplam_ucus = len(kritik_rotarlar)

for durum in kritik_rotarlar:
    if durum == "Kritik Rötar":
        kritik_sayisi = kritik_sayisi + 1

kritik_orani = (kritik_sayisi / toplam_ucus) * 100

print("-" * 30)
print(f"Toplam Uçuş Sayısı: {toplam_ucus}")
print(f"Kritik Rötar Yapan Uçuş Sayısı: {kritik_sayisi}")
print(f"Kritik Rötar Oranı: %{kritik_orani:.2f}") 
print("-" * 30)