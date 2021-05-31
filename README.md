# Eba Otomatik Derse Girici

NOT: 
Bu uygulamayı geliştirme amacımız asla bir kişiyi etkilemek için değildir ve olmayacaktır. 
Ne olursa olsun derslerinize girin arkadaşlar. Unutmayın, yarının geleceği sizlersiniz. <3 

Öğrenciler için ebadaki derslere otomatik girmeye sağlayan bir python programı.

Lütfen kullanmadan önce `selenium` modülünün python sürümünüze indirmeyi unutmayın: [PyPi](https://pypi.org/project/selenium/)

## Bilinen Hatalar
- ```py
    selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version x
    Current browser version is x.y.z with binary path C:\Program Files (x86)\Google\Chrome\Application\chrome.exe
    ```
    + Bu hata ile karşılaşıyorsanız büyük ihtimal chrome sürümünüz eski. [Burdan](https://chromedriver.chromium.org/downloads) chrome sürümünüze uygun sürümü indirip `Driver` klasörünün içine atınız.
- Bat/Sh Dosyası Açıldığı Anda Kapanıyor - Hata Veriyor
    + Bu durumda birkaç olasılık var;
        + Python3 kullanmıyorsunuz.
        + Python `PATH` üzerinde yok.
        + Python yüklü değil.
        + Selenium yüklü değil.
    - Windows için;
        + ```py
            # Eğer Python3 Kurduğunuzdan Eminseniz;
            # py -3 main.py
            # Bu şekilde çalıştırmayı deneyiniz.
            ```

## Kurulum
+ Python3 kurulu değilse kurunuz.
    - Python3.8 ve Python3.9 sürümlerinde denendi ve çalıştığı doğrulandı.
    - Lütfen olabildiğince güncel bir sürüm ile kullanınız.
+ Selenium modülünü python için kurunuz.
    - `pip install selenium` ya da `py -3 -m pip install -U selenium`
+ Bilgileri doldurunuz.
    - `ayar.json` Dosyasındaki TC ve Şifre kısmını doldurunuz.
    - Bu program tamamen açık kaynaklıdır. bilgilerinizin çalınmasına korkmanıza gerek yoktur.
+ Dosyayı çalıştırın.
    - İsterseniz `start.bat` dosyasını çalıştırın,
    - İstersenizde `python main.py` ya da `py -3 main.py` şeklinde dosyayı çalıştırın.

# Not:
Browser üzerinde tek seferlik izin alarmı çıkabilir. `Bir daha sorma` seçeneğini işaretleyerek, sonraki derse girişinde tekrar basmanıza gerek kalmaz.

## Linux/MacOs İçin Ek Not:
Eba ders uygulaması sadece windows için çalıştığı için linux/macOs için bir driver koymadık. bir yolunu bulduysanız [burdan](https://chromedriver.chromium.org/downloads) kendi işletim sisteminiz için olan bir driveri indirip `Driver` klasörüne atınız.


İletişim için:
Email: bilaltaner2004@gmail.com
Discord: shynox#4601
