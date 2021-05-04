from selenium import webdriver
from datetime import datetime as dt
import datetime, time, json

browser = webdriver.Chrome(r"Driver\chromedriver")
browser.maximize_window()
browser.get("https://giris.eba.gov.tr/EBA_GIRIS/student.jsp")

def giris_bilgileri_al():
    with open("./ayar.json", "r", encoding="utf-8") as f:
        config = json.load(f)
        f.close()
    
    return config['TC'], config['Sifre']

while 1:
    print('Ebaya Giriş Yapılıyor...')
    time.sleep(2)

    kimlik, sifre = giris_bilgileri_al()

    browser.find_element_by_name("tckn").send_keys(kimlik)
    browser.find_element_by_name("password").send_keys(sifre)

    time.sleep(2)
    giris = browser.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[2]/form/div[5]/button")
    giris.click()

    try:
        alert = browser.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[2]/div")
        if alert.text.strip() in ('Kullanıcı adınız veya şifreniz yanlış.', 'Lütfen kendinize uygun giriş seçeneğinden giriniz.'):
            print('Şifre veya T.C kimlik numarası hatalı!')
            print('5 Saniye İçinde Tekrar Denencek. Lütfen Şifre veya TC Kimlik Numaranızı Düzeltin.')

            kimlik, sifre = giris_bilgileri_al()
            time.sleep(5)
            continue

    except Exception:
        print('Giriş Yapıldı. Lütfen Bekleyiniz.')
        break

while 1:
    print("Lütfen 10 Saniye Bekleyiniz.")
    time.sleep(10)

    try:
        zaman = browser.find_element_by_xpath('//*[@id="live-times"]').text
    except Exception:
        print('Şuan Canlı Dersiniz Yok Gibi Görünüyor. 5 Saniye Sonra Tekrar Denenicek.')
        time.sleep(5)

        browser.refresh()
        continue

    sonuc = zaman.split(" - ")
    print('Süre Hesaplanıyor...', sonuc)

    baslangic = sonuc[0].split(".")
    bitis = sonuc[1].split(".")

    baslangic_saat, baslangic_dakika = datetime.timedelta(hours=int(baslangic[0])), datetime.timedelta(minutes=int(baslangic[1]))
    baslangic_toplama = (baslangic_saat + baslangic_dakika)

    bitis_saat, bitis_dakika = datetime.timedelta(hours=int(bitis[0])), datetime.timedelta(minutes=int(bitis[1]))
    bitis_toplama = (bitis_saat + bitis_dakika)

    ekleme = (datetime.datetime.utcnow() + datetime.timedelta(hours=3))
    ekleme_timedelta = datetime.timedelta(hours=ekleme.hour, minutes=ekleme.minute, seconds=ekleme.second)

    if ekleme_timedelta < bitis_toplama and ekleme_timedelta >= baslangic_toplama:
        print('Ders Zamanı Tespit Edildi. Derse Giriş Yapılıyor...')
        browser.refresh()

        ders = browser.find_element_by_xpath("//*[@id='joinMeeting']")
        browser.execute_script("arguments[0].click();", ders)

        time.sleep(1)

        katıl = browser.find_element_by_xpath("//*[@id='join']")
        katıl.click()

        time.sleep(3)
        print("POP-UP Bekleniyor...")
        time.sleep(int(browser.find_element_by_xpath("//*[@id='remaining_time_popup_text']").text) + 10)

        ekleme = (datetime.datetime.utcnow() + datetime.timedelta(hours=3))
        ekleme_timedelta = datetime.timedelta(hours=ekleme.hour, minutes=ekleme.minute, seconds=ekleme.second)

        beklencek = (bitis_toplama - ekleme_timedelta).total_seconds() + 5

        print(f"{beklencek} Saniye Sonra Derse Süresi Biticek.")
        time.sleep(beklencek)
        browser.refresh()
        continue
    else:
        print('Ders Zamanı Tespit Edilemedi. 5 Saniye Sonra Yenilenip Tekrar Denenicek...')
        time.sleep(5)

        browser.refresh()
        continue
