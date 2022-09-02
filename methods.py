import numpy as np

#arange => belirtilen iki sayı arasında dizi oluşturmak için kullanılır.

benimArrangeListem = np.arange(0,10)
print("Benim Arrange Listem: ",benimArrangeListem)

benimArrangeListem2 = np.arange(0,10,2)
print("Benim Arrange Listem2: ",benimArrangeListem2)

#zero => 0 olan bir dizi oluşturmak için kullanılır.

benimZeroListem = np.zeros(5)
print("Benim Zero Listem: ",benimZeroListem)

#ones => 1 olan bir dizi oluşturmak için kullanılır.

benimOnesListem = np.ones(5)
print("Benim Ones Listem: ",benimOnesListem)

#linspace => Belirtilen sayılar arasında eşit şekilde bir dizi oluşturmaya yarıyor.

benimLinspaceListem = np.linspace(0,20,5)
print("Benim Linspace Listem: ",benimLinspaceListem)

#eye => identity bir matris oluşturmak için kullanılır.
benimEyesListem = np.eye(5)
print("Benim Eye Listem: ",benimEyesListem)


