import asyncio
import os
import pandas as pd
import json
from datetime import datetime
from playwright.async_api import async_playwright

class ExcelToJsonConverter:
    def __init__(self, url, download_button_selector):
        self.url = url
        self.download_button_selector = download_button_selector
        self.file_path = "Mahalle_Listesi.xls"  # Manuel olarak belirlenmiş dosya, adı otomatik atayınca hata aldım
        self.json_file = "veriler.json"  # Asıl kullanılan JSON
        self.backup_folder = "json_yedekleri"  # Yedeklerin saklanacağı klasör

        # Eğer yedek klasörü yoksa oluştur
        os.makedirs(self.backup_folder, exist_ok=True)

    async def download_excel(self):
        """Web sitesinden Excel dosyasını indirir."""
        async with async_playwright() as p:
            print("🌐 Tarayıcı başlatılıyor...")
            browser = await p.chromium.launch(headless=False)
            context = await browser.new_context(accept_downloads=True)
            page = await context.new_page()

            print(f"📡 {self.url} adresine gidiliyor...")
            await page.goto(self.url)
            await page.wait_for_load_state("networkidle")

            print("📥 Excel indirme butonu tespit ediliyor ve tıklanıyor...")
            await page.wait_for_selector(self.download_button_selector, timeout=10000)
            download_task = page.wait_for_event("download", timeout=60000)  # 60 saniye bekle
            await page.locator(self.download_button_selector).click()
            download = await download_task

            # Dosyanın içeriğini okuyarak manuel olarak kaydet
            file_stream = await download.path()
            with open(self.file_path, "wb") as f:
                f.write(file_stream.read_bytes())

            print(f"✅ Excel dosyası başarıyla indirildi: {self.file_path}")
            await browser.close()

    def backup_old_json(self):
        """Mevcut JSON dosyasını tarih damgası ile yedekler."""
        if os.path.exists(self.json_file):
            timestamp = datetime.now().strftime("%Y-%m-%d")
            backup_path = os.path.join(self.backup_folder, f"veriler_{timestamp}.json")
            os.rename(self.json_file, backup_path)
            print(f"📂 Eski JSON yedeklendi: {backup_path}")

    def process_excel(self):
        """İndirilen Excel dosyasını JSON formatına çevirir ve değişiklikleri günceller."""
        if not os.path.exists(self.file_path):
            print("❌ Hata: Excel dosyası bulunamadı!")
            return

        print("📊 Excel dosyası işleniyor...")
        df = pd.read_excel(self.file_path, usecols=["Unnamed: 0", "Unnamed: 3", "Unnamed: 5"], engine="xlrd")

        # Sütun isimlerini düzenle
        df = df.rename(columns={"Unnamed: 0": "ID", "Unnamed: 3": "Mahalle", "Unnamed: 5": "Güzergah"})

        # Null (boş) değerleri kaldır
        df = df.dropna(how="any")

        # Yeni JSON'u oluştur
        new_data = df.to_dict(orient="records")

        # Eğer eski JSON varsa değişiklik kontrolü yap
        if os.path.exists(self.json_file):
            with open(self.json_file, "r", encoding="utf-8") as f:
                old_data = json.load(f)
        else:
            old_data = []

        # Değişiklikleri kontrol et
        if new_data != old_data:
            print("🔄 Değişiklik tespit edildi, güncelleniyor...")
            self.backup_old_json()  # Eski JSON'u yedekle

            # Yeni JSON'u kaydet
            with open(self.json_file, "w", encoding="utf-8") as f:
                json.dump(new_data, f, ensure_ascii=False, indent=4)
            print(f"✅ JSON dosyası güncellendi: {self.json_file}")
        else:
            print("✔️ Veriler aynı, güncellemeye gerek yok.")

async def main():
    """Tüm işlemleri yöneten ana fonksiyon."""
    url = "https://www.e-icisleri.gov.tr/Anasayfa/MulkiIdariBolumleri.aspx"
    download_button_selector = "#ctl00_cph1_CografiBirimControl_imgButtonMahalleSayisiExcel"

    converter = ExcelToJsonConverter(url, download_button_selector)
    
    await converter.download_excel()  # Excel dosyasını indir
    converter.process_excel()         # JSON'a dönüştür ve güncelle

# Asenkron işlemi başlat
asyncio.run(main())