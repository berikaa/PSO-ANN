# PSO-ANN
PSO-ANN modeli ile deprem hasar tahmin modelinin oluşturulmuştur. Veri seti aşağıdaki gibidir fakat bazı eksiklikler mevcuttur bu sebepten veri seti ön işlemden geçirilmelidir. 
![image](https://user-images.githubusercontent.com/9701895/224983617-43616b35-3749-4b1a-81a2-f9dd0fd725b5.png)

Veri setinden yapılması gereken temel ön işlem adımları:
  1. Eksik değerler bulunmaktadır bunlar tamamlanmalıdır.
  
  ![image](https://user-images.githubusercontent.com/9701895/225011095-c8ffdf30-6ac0-4b64-bb5c-5e883e106c23.png)
  
  ![image](https://user-images.githubusercontent.com/9701895/225011134-ab8b2bb6-77a4-4f13-9e3b-0d54457c3a9e.png)

  2. Enterolasyon yöntemi ile verilerin tamamlanması gerçekleştirilebilir.
  
  ![image](https://user-images.githubusercontent.com/9701895/225011447-7da5331b-0c73-4816-afd9-4a9a5c51c46a.png)

  ![image](https://user-images.githubusercontent.com/9701895/225011398-9e8b0727-ee57-45f1-b57f-645d2e21a9bc.png)
  
  3.Veri setinde label encoder yönremi ile country region ve location name özellikleri etiketlenmelidir.
  
  ![image](https://user-images.githubusercontent.com/9701895/225011571-bf7dd1a5-3b8b-4d10-b827-8fd95a34020f.png)

  ![image](https://user-images.githubusercontent.com/9701895/225011684-eb106010-4afb-4eca-a1a0-5d3b4ae5187b.png)

  4. Özellik seçimi sırasında aşağıdaki gibi korelasyon matrisi oluşturularak yüksek ilişkili özellikler veri setinden çıkartılabilir. 
  ![image](https://user-images.githubusercontent.com/9701895/225011896-09ebbfc9-d03d-471d-95b1-e836b02b2fed.png)

  ![image](https://user-images.githubusercontent.com/9701895/224981855-e03e9887-1fa6-4ea7-b5b1-f8e00cf5e5ba.png)


Bu adımlar sayesinde modelin performans başarısı arttırılabilir.
