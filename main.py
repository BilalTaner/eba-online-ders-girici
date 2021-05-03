from selenium import webdriver
from datetime import datetime as dt
import datetime
import time

browser = webdriver.Chrome(r"Driver\chromedriver")
browser.maximize_window()

browser.get("https://giris.eba.gov.tr/EBA_GIRIS/student.jsp")

with open('Bilgiler/kimlik.txt', 'r') as file:
	kimlik = file.read().replace('\n', '')

with open('Bilgiler/şifre.txt', 'r') as file:
	sifre = file.read().replace('\n', '')

while True:


    print("Giriş yapılıyor...")

    time.sleep(3)

    tckimlikno = browser.find_element_by_name("tckn")
    ebasifre = browser.find_element_by_name("password")

    tckimlikno.send_keys(kimlik)
    ebasifre.send_keys(sifre)

    time.sleep(2)

    giris = browser.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[2]/form/div[5]/button")
    giris.click()

    try:
        alert = browser.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[2]/div")
        if alert.text.strip() == 'Kullanıcı adınız veya şifreniz yanlış.' or alert.text.strip() == 'Lütfen kendinize uygun giriş seçeneğinden giriniz.':
            print('Şifre veya T.C kimlik numarası hatalı!')
            continue

    except:
        break

time.sleep(10)
while True:
    zaman = browser.find_element_by_xpath('//*[@id="live-times"]').text
    sonuc = [zaman for zaman in zaman.split(" - ")]

    baslangic = sonuc[0].split(".")
    bitis = sonuc[1].split(".")

    baslangic_saat, baslangic_dakika = datetime.timedelta(hours=int(baslangic[0])), datetime.timedelta(minutes=int(baslangic[1]))
    baslangic_toplama = (baslangic_saat + baslangic_dakika)

    bitis_saat, bitis_dakika = datetime.timedelta(hours=int(bitis[0])), datetime.timedelta(minutes=int(bitis[1]))
    bitis_toplama = (bitis_saat + bitis_dakika)

    ekleme = (datetime.datetime.utcnow() + datetime.timedelta(hours=3))
    ekleme_timedelta = datetime.timedelta(hours=ekleme.hour, minutes=ekleme.minute, seconds=ekleme.second)

    if ekleme_timedelta < bitis_toplama and ekleme_timedelta >= baslangic_toplama:
        browser.refresh()

        ders = browser.find_element_by_xpath("//*[@id='joinMeeting']")
        ders.click()

        time.sleep(1)

        katıl = browser.find_element_by_xpath("//*[@id='join']")
        katıl.click()

        time.sleep(3)
        time.sleep(int(browser.find_element_by_xpath("//*[@id='remaining_time_popup_text']").text) + 10)

        if dt.now().minute == bitis[1] and dt.now().hour == bitis[0]:
            time.sleep(5)
            browser.refresh()
            continue

