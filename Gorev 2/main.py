# Kullanıcı tarafından girilecek bir cümleyi kelimelerine göre tersten yazan bir program yazınız? Eğer
# cümlede (ama, ve, veya, göre, ile, yalnız, ise, ne, nasıl, ancak, çünkü, neden, oysa, için) bağlaçları
# geçiyorsa bu bağlaçları tersten yazın ve cümlede geçen boşluk hariç karakterlerin (küçük büyük
# harf duyarsız) tekrar sayılarını ekrana örnekteki gibi yazın.

def ters_cumle():
    bağlaçları = ["ama", "ve", "veya", "göre", "ile", "yalnız", "ise", "ne", "nasıl", "ancak", "çünkü",
                  "neden", "oysa", "için"]
    sentence = input("Lütfen çümleniz giriniz:\n")
    sentence_cy = sentence.split() # split the sentence into words
    tersten_yazma = ''
    while len(sentence_cy):
        temp = ''
        temp += sentence_cy.pop()
        if temp.lower() in bağlaçları:
            reverse = ''.join(reversed(temp))
            tersten_yazma += (reverse) + ' '
        else:
            tersten_yazma += temp + ' '
    print(tersten_yazma)

    words_freq = {'.': 0, 'A': 0, 'B': 0, 'C': 0, 'Ç': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'Ğ': 0, 'H': 0, 'I': 0,
                  'İ': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'Ö': 0, 'P': 0,  'R': 0,
                  'S': 0,  'Ş': 0, 'T': 0, 'U': 0, 'Ü': 0, 'V': 0, 'Y':0, 'Z': 0}

    sentence = sentence.replace('i', 'İ')   # i'yi 'I'ye çeviriliyor ö yüzden bunu yapmak gerekir
    sentence = sentence.upper()
    for ch in sentence:
        if ch == ' ':
            continue
        elif ch not in words_freq.keys():  # skip special characters. (example ':', '@', '%', etc.)
            continue
        else:
            words_freq[ch] += 1
    print("\nCümlede Geçen Karakterlerin Tekrar Sayısı:")
    for k, v in words_freq.items():
        print(f"{k} => {v} adet")


if __name__ == "__main__":
    ters_cumle()

