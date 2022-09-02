import numpy as np

#reshape => yeniden var olan bir diziden dizi oluşturmak için kullanılır.

benimNumpyDizim = np.arange(30)

yeniDizi = benimNumpyDizim.reshape(5,6)


print("BENİM NUMPY DİZİM: ",yeniDizi)

#max => dizi içerisindeki en yüksek sayıyısı. min=> dizi içerisindeki en düşük sayıyı gösterir

enYuksekSayi = yeniDizi.max()
print("EN YÜKSEK SAYI : ",enYuksekSayi)

enDusukSayi = yeniDizi.min()
print("EN DÜŞÜK SAYI: ",enDusukSayi)

# argmax => en yüksek sayının kaçıncı index de olduğunu öğreniyoruz.

enYuksekIndex = yeniDizi.argmax()
print("EN YUKSEK SAYİ INDEX: ",enYuksekIndex)

# argmin => en küçük sayının kaçıncı index de olduğunu öğreniyoruz.

enDusukIndex = yeniDizi.argmin()
print("EN DUSUK SAYİ INDEX: ",enDusukIndex)
