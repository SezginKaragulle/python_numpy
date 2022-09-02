import numpy as np

yeniDizim = np.random.randint(1,100,20)
print("YENİ DİZİM: ",yeniDizim)

yeniKareKokDizim = np.sqrt(yeniDizim)
print("KAREKOK SONUC: ",yeniKareKokDizim)

enYuksekDeger = yeniDizim.max()
enDusukDeger = yeniDizim.min()

print("EN YÜKSEK DEĞER: ",enYuksekDeger)
print("EN DÜŞÜK DEĞER: ",enDusukDeger)

enYuksekIndex = yeniDizim.argmax()
enDusukIndex = yeniDizim.argmin()

print("EN YÜKSEK INDEX YERİ: ",enYuksekIndex)
print("EN DÜŞÜK INDEX YERİ: ",enDusukIndex)