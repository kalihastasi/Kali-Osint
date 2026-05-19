import asyncio
import os

from rich.console import Console
from rich.table import Table

from kurucu import paketleri_kur

from utils.banner import banner
from utils.exporter import disa_aktar
from utils.logger import log

from modules import whois_sorgu
from modules import dns_sorgu
from modules import ip_sorgu
from modules import kullanici_adi
from modules import metadata
from modules import web_kaziyici

console = Console()

paketleri_kur()

os.makedirs("cikti", exist_ok=True)

class KaliOsint:

    def menu(self):

        while True:

            os.system("cls" if os.name == "nt" else "clear")

            banner()

            tablo = Table(title="KALI OSINT MODULLERI")

            tablo.add_column("ID")
            tablo.add_column("MODUL")

            tablo.add_row("1", "Whois Sorgu")
            tablo.add_row("2", "DNS Sorgu")
            tablo.add_row("3", "IP Istihbarati")
            tablo.add_row("4", "Kullanici Adi Tarama")
            tablo.add_row("5", "Metadata Analizi")
            tablo.add_row("6", "Web Kaziyici")
            tablo.add_row("0", "Cikis")

            console.print(tablo)

            secim = input("Secim > ")

            if secim == "1":
                self.whois_modul()

            elif secim == "2":
                self.dns_modul()

            elif secim == "3":
                self.ip_modul()

            elif secim == "4":
                asyncio.run(self.kullanici_modul())

            elif secim == "5":
                self.metadata_modul()

            elif secim == "6":
                self.web_modul()

            elif secim == "0":
                break

            input("\nDevam etmek icin Enter...")

    def whois_modul(self):

        domain = input("Domain > ")

        sonuc = whois_sorgu.calistir(domain)

        console.print(sonuc)

        disa_aktar(sonuc, "whois")

        log(f"Whois sorgu -> {domain}")

    def dns_modul(self):

        domain = input("Domain > ")

        sonuc = dns_sorgu.calistir(domain)

        console.print(sonuc)

        disa_aktar(sonuc, "dns")

        log(f"DNS sorgu -> {domain}")

    def ip_modul(self):

        ip = input("IP > ")

        sonuc = ip_sorgu.calistir(ip)

        console.print(sonuc)

        disa_aktar(sonuc, "ip")

        log(f"IP sorgu -> {ip}")

    async def kullanici_modul(self):

        kullanici = input("Kullanici Adi > ")

        sonuc = await kullanici_adi.calistir(kullanici)

        console.print(sonuc)

        disa_aktar(sonuc, "kullanici")

        log(f"Kullanici tarama -> {kullanici}")

    def metadata_modul(self):

        dosya = input("Dosya Yolu > ")

        sonuc = metadata.calistir(dosya)

        console.print(sonuc)

        disa_aktar(sonuc, "metadata")

        log(f"Metadata -> {dosya}")

    def web_modul(self):

        url = input("URL > ")

        sonuc = web_kaziyici.calistir(url)

        console.print(sonuc)

        disa_aktar(sonuc, "web")

        log(f"Web kaziyici -> {url}")

if __name__ == "__main__":

    uygulama = KaliOsint()

    uygulama.menu()