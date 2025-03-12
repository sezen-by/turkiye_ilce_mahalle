# 📊 Web'den Otomatik Excel İndirme ve JSON Dönüştürme Sistemi

Bu Python projesi, belirli bir web sitesinden **Excel dosyasını otomatik olarak indirir, JSON formatına çevirir ve değişiklikleri yönetir**.  

---

## 🚀 Nasıl Çalışır?
Bu sistem, **Playwright** kütüphanesi kullanarak web sitesine bağlanır, Excel indirme butonuna tıklar ve dosyayı kaydeder. Ardından **Pandas** ile verileri işler ve JSON formatına çevirir.  
- **Eski JSON dosyalarını yedekler** 📂  
- **Yeni verileri mevcut JSON ile kıyaslar** 🔍  
- **Değişiklik varsa günceller, yoksa işlem yapmaz** 🔄  

---

## 🔧 Bileşenler

### **📌 `ExcelToJsonConverter` Sınıfı**
- **Web sitesine bağlanır** ve Excel dosyasını otomatik olarak indirir.
- **Sütun isimlerini düzenler** ve gereksiz verileri temizler.
- **Eski JSON ile karşılaştırma yapar**, değişiklik varsa yedekleme ve güncelleme yapar.

---

## 🛠 Kullanılan Fonksiyonlar

### **🔹 `download_excel()`**
- **Playwright** kullanarak web sayfasına gider.
- **İndirme butonunu tespit eder** ve otomatik olarak tıklar.
- **Excel dosyasını indirir ve kaydeder**.

### **🔹 `process_excel()`**
- **İndirilen Excel dosyasını Pandas ile işler**.
- **Sütun isimlerini düzenler** ve boş satırları kaldırır.
- **Mevcut JSON ile kıyaslama yaparak değişiklikleri kontrol eder**.

### **🔹 `backup_old_json()`**
- **Eğer veriler değişmişse, eski JSON'u tarih damgalı olarak yedekler**.

### **🔹 `main()`**
- **Tüm işlemleri sırayla çalıştırır**.
- **Önce Excel dosyasını indirir, sonra JSON'a dönüştürür**.

---

## 🔄 Çalışma Mantığı
1. **Excel dosyası indirilir** 📥  
2. **Sütunlar temizlenir ve JSON formatına dönüştürülür** 🔄  
3. **Eski JSON ile kıyas yapılır** 🔍  
4. **Veri değiştiyse eski JSON yedeklenir ve güncellenir** 🛠  

---

## 📅 Periyodik Çalıştırma
Bu sistem **otomatik çalıştırılabilir**:
- **Windows'ta "Görev Zamanlayıcı" ile** 📅
- **Linux'ta "cron job" ile** ⏳


---

## 🔥 Kurulum & Çalıştırma

### **1️⃣ Gerekli Bağımlılıkları Yükle**
Python 3.8+ yüklü olduğundan emin ol.

```bash
pip install pandas playwright xlrd
playwright install
python -m install playwright



