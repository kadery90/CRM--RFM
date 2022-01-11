# RFM
## RFM ile Müşteri Segmentasyonu

RFM → Recency–Frequency–Monetary: Recency (yenilik) müşterinin en yeni satın alma yaptığı tarih, Frequency (sıklık) müşterinin toplam satın alma sayısı, Monetary (parasal değer) müşterinin bıraktığı getiri anlamlarını taşımaktadır.

Bu üç metriği 1 ile 5 arası puanlayıp değerleri yan yana getiriyoruz. Monetary değerini genellikle analizde kullanmıyoruz ancak sektörden sektöre farklılık göstereceğinden analizlerinizde kullanmayı tercih edebilirsiniz. Dikkat edilmesi gereken nokta Frequency ve Monetary metriklerinde 5 en yükseği belirtirken Recency metriğinde 5 sayısal değer olarak en küçüğe verilir. Nedeni ise Recency değeri analiz günü ile alışveriş yapılma günü farkının değeridir. Yani ne kadar büyük bir değer ise müşteri o kadar önce alışverişi gerçekleştirmiştir ve skalada en küçük değer ile etiketlenir.

Proje: Bir e-ticaret şirketi müşterilerini segmentlere ayırıp bu segmentlere göre pazarlama stratejileri belirlemek istemektedir. Ortak davranışlar sergileyen müşteri segmentleri özelinde pazarlama çalışmaları yapmak gelir artışı sağlayacaktır.

Değişkenler: 
Invoice: Fatura Numarası (Eğer bu kod C ile başlıyorsa işlemin iptal edildiğini ifade eder.) 
StockCode: Ürün kodu (Her bir ürün için eşsiz numara.)
Description: Ürün ismi 
InvoiceDate: Fatura tarihi 
UnitPrice: Fatura fiyatı (Sterlin) 
CustomerID: Eşsiz müşteri numarası 
Country: Ülke ismi
Quantity: Ürün adedi
