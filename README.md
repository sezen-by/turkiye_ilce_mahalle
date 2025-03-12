# 📊 Web'den Otomatik Excel İndirme ve JSON Dönüştürme Sistemi

Bu Python projesi, belirli bir web sitesinden **Excel dosyasını otomatik olarak indirir, JSON formatına çevirir ve değişiklikleri yönetir**.  

## 🚀 Nasıl Çalışır?
Bu sistem, **Playwright** kütüphanesi kullanarak web sitesine bağlanır, Excel indirme butonuna tıklar ve dosyayı kaydeder. Ardından **Pandas** ile verileri işler ve JSON formatına çevirir.  

## 🔧 Bileşenler

### **📌 `ExcelToJsonConverter` Sınıfı**
- **Web sitesine bağlanır** ve Excel dosyasını otomatik olarak indirir.
- **Sütun isimlerini düzenler** ve gereksiz verileri temizler.
- **Eski JSON ile karşılaştırma yapar**, değişiklik varsa yedekleme ve güncelleme yapar.


## 🔄 Çalışma Mantığı
1. **Excel dosyası indirilir** 📥  
2. **Sütunlar temizlenir ve JSON formatına dönüştürülür** 🔄  
3. **Eski JSON ile kıyas yapılır** 🔍  
4. **Veri değiştiyse eski JSON yedeklenir ve güncellenir** 🛠

## 🔥 Kurulum & Çalıştırma

### **1️⃣ Gerekli Bağımlılıkları Yükle**
Python 3.8+ yüklü olduğundan emin ol.

```bash
pip install pandas playwright xlrd
playwright install
