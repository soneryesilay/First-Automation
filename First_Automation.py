from appium.webdriver.webdriver import WebDriver as Remote
from appium.options.android.uiautomator2.base import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

# 1 - Appium bağlantı ayarları
options = UiAutomator2Options()
options.platform_name = "Android"
options.platform_version = "11" # Kendi cihazınızın Android versiyonunu girin
options.device_name = "" # `adb devices` komutu ile alacağınız cihaz ID'sini buraya girin
options.app_package = "io.appium.android.apis"
options.app_activity = ".ApiDemos"
options.no_reset = True
options.udid = "" # `adb devices` komutu ile alacağınız cihaz ID'sini buraya girin

# 2 - Appium server'a bağlan
driver = Remote("http://localhost:4723/wd/hub", options=options)
time.sleep(3)

# 3 - Views menüsüne tıkla
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Views").click()

# 4 - "Controls" öğesine kadar scroll yap ve tıkla
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
    'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Controls"))'
).click()

# 5 - "1. Light Theme" öğesini seç
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1. Light Theme").click()

# 6 - Metin kutusuna yazı yaz
edit_text = driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/edit")
edit_text.send_keys("Appium Test Başarılı!")

# 7 - Checkbox’ı işaretle
driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/check1").click()

# 8 - RadioButton seç
driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/radio1").click()

# 9 - Spinner'ı aç
spinner = driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/spinner1")
spinner.click()
time.sleep(1)

# 10 - "Venus" seçeneğini seç
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
    'new UiSelector().text("Venus")'
).click()
time.sleep(1)

# 11 - Bekle ve çık
time.sleep(2)
driver.quit()
