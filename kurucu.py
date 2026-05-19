import subprocess
import sys

PAKETLER = [
    "rich",
    "requests",
    "aiohttp",
    "dnspython",
    "python-whois",
    "beautifulsoup4",
    "colorama",
    "pyfiglet",
    "exifread",
    "PyPDF2",
    "python-docx",
    "geoip2",
    "fake-useragent",
    "lxml"
]

def paketleri_kur():

    for paket in PAKETLER:

        try:
            __import__(paket.replace("-", "_"))

        except ImportError:

            print(f"[+] Kuruluyor: {paket}")

            subprocess.check_call([
                sys.executable,
                "-m",
                "pip",
                "install",
                paket
            ])

if __name__ == "__main__":
    paketleri_kur()