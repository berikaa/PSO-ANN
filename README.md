# PSO-ANN
PSO-ANN modeli ile deprem hasar tahmin modelinin oluşturulmuştur. Veri seti ön işlemden geçirilmelidir. 
Veri setinden yapılması gereken temel ön işlem adımları:
  1. Eksik değerler bulunmaktadır bunlar tamamlanmalıdır.
  2. Veri setinde label encoder yönremi ile country region ve location name özellikleri etiketlenmelidir.
  3. Özellik seçimi sırasında aşağıdaki gibi korelasyon matrisi oluşturularak yüksek ilişkili özellikler veri setinden çıkartılabilir. 
Bu sayede modelin performans başarısı arttırılabilir.

![image](https://user-images.githubusercontent.com/9701895/224981855-e03e9887-1fa6-4ea7-b5b1-f8e00cf5e5ba.png)


