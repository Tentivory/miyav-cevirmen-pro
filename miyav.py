#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Miyav Çevirmen Pro v1.0
Dünyanın en ciddi miyav çeviri motoru.
"""

import random
import sys

def miyav_cevir(metin):
    """Her kelimeyi uzunluğuna göre özel miyava çevirir."""
    miyavlar = []
    for kelime in metin.split():
        uzunluk = max(1, len(kelime))
        miyav = "Miyav" + "ı" * (uzunluk % 4) + "!" * random.randint(1, 4)
        miyavlar.append(miyav)
    return " ".join(miyavlar)

def kedi_cevabi():
    """Kedi felsefesi üretir."""
    cevaplar = [
        "Miyav... senin de çayın var mı?",
        "Hımm, o lafı duymuştum. Ama fare daha lezzetli.",
        "Tamam abi, anladım. Şimdi uyuyorum.",
        "Bu iş bitmez, form doldur, imza at, sonra tekrar gel.",  # Gizli bürokrasi eleştirisi
        "Özgürlük miyavla gelir, formla değil."  # Saklı siyasi mesaj
    ]
    return random.choice(cevaplar)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        giris = " ".join(sys.argv[1:])
    else:
        giris = input("Bir şey söyle, miyava çevireyim (veya Ctrl+C ile kaç): ")
    print("\n=== RESMİ ÇEVİRİ RAPORU ===")
    print("Orijinal:", giris)
    print("Miyav Çevirisi:", miyav_cevir(giris))
    print("Kedi Yorumu:", kedi_cevabi())
    print("===========================")
    print("\nDamga: 🐾")
    print("İmza: Grok Kayyum")
    print("Tarih: 15 Ekim 2026")
    print("İsim: Absürt Kod Üstadı")
    print("(Ciddi: Evet. Ciddi değil: Kesinlikle.)")
