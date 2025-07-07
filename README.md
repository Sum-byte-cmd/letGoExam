# Letgo "Bike" Arama ve Favorilere Ekleme Test Otomasyonu

Bu doküman, Selenium ve Python kullanılarak geliştirilen, Letgo web sitesinde "bike" anahtar kelimesiyle arama yapan, herhangi bir filtre uygulayan ve çıkan ilk sonucu favorilere ekleyen test otomasyonunun kullanımını ve kurulumunu açıklamaktadır.

## Amaç

- Letgo web sitesinde "bike" araması yapmak
- Rastgele veya belirli bir filtre uygulamak (örneğin, fiyat aralığı, kategori, konum vs.)
- Arama sonuçlarında çıkan ilk ürünü favorilere eklemek
- Bu süreci otomatikleştirmek ve doğrulamak

## Gereksinimler

- Python 3.x
- Selenium (`pip install selenium`)
- WebDriver (örn. ChromeDriver veya GeckoDriver)
- Letgo web sitesinde giriş yapılabilen bir kullanıcı hesabı

## Kurulum

1. **Gerekli Kütüphanelerin Kurulumu**
    ```bash
    pip install selenium
    ```

2. **WebDriver İndirme**
    - Tarayıcınıza uygun WebDriver'ı indirin ve PATH değişkenine ekleyin.
    - [ChromeDriver](https://sites.google.com/chromium.org/driver/)
    - [GeckoDriver](https://github.com/mozilla/geckodriver/releases)

3. **Letgo Hesabı**
    - Favorilere eklemek için giriş yapılması gerekmektedir.
