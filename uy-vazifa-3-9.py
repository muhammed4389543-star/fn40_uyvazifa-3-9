# 1
sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
kop_sonlar = list(map(lambda x: x*3, sonlar))
print(kop_sonlar)


# 2
sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
kvad_sonlar = list(map(lambda x: x*x, sonlar))
print(kvad_sonlar)



# 3
sozlar = ["python", "it", "salom"]
katta_sozl = list(map(lambda s: s.upper(), sozlar))
print(katta_sozl)



# 4
ismlar = ["Muhammad", "Muhammadsodiq", "Muhammadqodir"]
count_isml = list(map(lambda i: len(i), ismlar))
print(count_isml)



# 5
sonlar_aralash = [1, 2, -3, 4, 5, -6, -9]
musbatga = list(map(lambda x: -x if x < 0 else x, sonlar_aralash))
print(musbatga)



# 6
narxlar = [120, 239, 566, 977]
foiz_qoshilgan = list(map(lambda x: x+x*0.15,narxlar))
print(foiz_qoshilgan)



# 7
sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
juft_0_ga = list(map(lambda x: 0 if x % 2 == 0 else x, sonlar))
print(juft_0_ga)



# 8
sozlar = ["python", "it", "salom"]
sozlarga_qoshimcha = list(map(lambda s: s+"!", sozlar))
print(sozlarga_qoshimcha)



# 9
sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
faqat_juft = list(filter(lambda x: x%2==0, sonlar))
print(faqat_juft)


# 10
sonlar_aralash = [1, 2, -3, 4, 5, -6, -9, 0]
katta_0dan = list(filter(lambda x: x>0, sonlar_aralash))
print(katta_0dan)



# 11
sozlar = ["python", "it", "salom"]
kop_harf_5dan = list(filter(lambda x: 5 < len(x), sozlar))
print(kop_harf_5dan)


# 12
sonlar = [34, 45, 12, 55, 12, 32]
bolinadi_5ga = list(filter(lambda x: x%5==0, sonlar))
print(bolinadi_5ga)


# 13
ismlar = ["Aziz", "Molik", "Sobir", "Akmal"]
faqat_A_bilan = list(filter(lambda s: s.upper()[0] == "A", ismlar))
print(faqat_A_bilan)


# 14
sonlar_aralash = [1, 2, -3, 4, 5, -6, -9, 0]
faqat_musbat = list(filter(lambda x: x>= 0, sonlar_aralash))
print(faqat_musbat)


# 15
sozlar = ["   python salom", "it", "pythonlar",  "salom"]
python_bormi = list(filter(lambda x: "python" in x.strip(), sozlar))
print(python_bormi)


print("github ga oddiy push qilish")