# Appium ile Android Otomasyon Örneği

Bu proje, Appium ve Python kullanarak Android "ApiDemos" uygulaması üzerinde temel otomasyon senaryolarını gösteren bir başlangıç projesidir.

## 📝 Açıklama

Bu script, Appium'un `UiAutomator2` sürücüsünü kullanarak bir Android cihaz üzerinde aşağıdaki kullanıcı arayüzü (UI) etkileşimlerini otomatize eder:
- Belirtilen uygulamayı başlatma.
- Menüler arasında gezinme.
- Listelerde belirli bir öğeye kadar kaydırma (scroll).
- Metin kutularına yazı yazma.
- Onay kutularını (checkbox) işaretleme.
- Radyo düğmelerini (radio button) seçme.
- Açılır menülerden (spinner) seçim yapma.

## 🚀 Özellikler

- **Platform**: Android
- **Otomasyon Aracı**: Appium
- **Dil**: Python
- **Hedef Uygulama**: `io.appium.android.apis` (ApiDemos)

## ⚙️ Gereksinimler

Bu projeyi çalıştırabilmek için aşağıdaki araçların ve paketlerin sisteminizde kurulu olması gerekmektedir:

1.  **Python 3.x**: [Python Resmi Sitesi](https://www.python.org/downloads/)
2.  **Appium Server**: [Appium Resmi Sitesi](https://appium.io/)
3.  **Android SDK**: Android Studio ile birlikte gelir. (`adb` komutunun çalışır durumda olduğundan emin olun.)
4.  **Java JDK**: Appium için gereklidir.
5.  **Python Kütüphaneleri**:
    -   `Appium-Python-Client`

## 🛠️ Kurulum

1.  **Projeyi Klonlayın:**
    ```bash
    git clone https://github.com/soneryesilay/First-Automation
    cd First-Automation
    ```

2.  **Python Bağımlılıklarını Yükleyin:**
    Proje için bir `requirements.txt` dosyası oluşturup bağımlılıkları oradan yüklemek en iyi pratiktir.
    ```bash
    pip install Appium-Python-Client
    ```

3.  **Appium Server'ı Başlatın:**
    Terminal üzerinden veya Appium Desktop uygulaması ile Appium sunucusunu başlatın.
    ```bash
    appium
    ```

4.  **Android Cihazınızı Hazırlayın:**
    -   Gerçek bir Android cihazda "Geliştirici Seçenekleri" ve "USB Hata Ayıklama" modunu aktif edin ve bilgisayarınıza bağlayın.
    -   Veya bir Android Emulator (Sanal Cihaz) başlatın.
    -   `ApiDemos` uygulamasının cihazınızda kurulu olduğundan emin olun. Genellikle Appium ile birlikte gelen örnek uygulamalardandır.

## ▶️ Nasıl Çalıştırılır?

1.  **Script'i Yapılandırın:**
    `First_Automation.py` dosyasını açın ve `UiAutomator2Options` altındaki aşağıdaki ayarları kendi cihazınıza göre güncelleyin:
    ```python
    options.platform_version = "11"  # Kendi cihazınızın Android versiyonu
    options.device_name = "R6CX1017KCN" # `adb devices` komutu ile alacağınız cihaz ID'si
    options.udid = "R6CX1017KCN"      # `adb devices` komutu ile alacağınız cihaz ID'si
    ```

2.  **Script'i Çalıştırın:**
    Tüm kurulumlar tamamlandıktan ve Appium sunucusu çalışır durumdayken, aşağıdaki komut ile otomasyonu başlatabilirsiniz:
    ```bash
    python First_Automation.py
    ```

Script başarıyla çalıştığında, belirttiğiniz Android cihaz üzerinde adımların otomatik olarak gerçekleştirildiğini göreceksiniz.
