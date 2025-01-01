DEATH NOTE Dizisinin Sosyal Ağ Analizi
Bu proje, Death Note anime serisindeki karakterler arasındaki sosyal ilişkilerin analizini yapmak amacıyla geliştirilmiştir. Çizge tabanlı bir ağ modeli oluşturularak, karakterlerin rolü ve etkisi merkeziyet ölçümleri, derecelendirme analizleri ve topluluk tespiti gibi yöntemlerle incelenmiştir. Bu analiz, sosyal etkileşimlerin derinlemesine anlaşılmasını sağlamaktadır.

Kullanılan Verinin Açıklaması
Death Note un veri seti olmadığı için veri setini kendimiz oluşturduk.

Death Note Fan ve Wiki sayfalarından bildiğimiz sosyal ilişkilerden emin olarak oluşturduk.

Oluşturulan Çizgenin Açıklaması
Karakterler: Light, L, Misa, Near, Mello, vb.
Kenarlar: Düşman, sevgili-yandaş, mentor-öğrenci gibi ilişkiler.
Yönsüz: Death Note evrenindeki ilişkiler genelde karşılıklıdır. Örneğin, bir karakter düşmansa, bu iki taraf için de geçerlidir.
Homojen: Çizge yalnızca karakterleri modellemek için tasarlandı, bu yüzden düğümler aynı türdedir.
Ağırlıksız: İlişkilerin yalnızca varlığı önemlidir; ilişkinin gücü veya yoğunluğu bu modelde dikkate alınmamıştır. 
 
![image](https://github.com/user-attachments/assets/9ba88f3a-6d07-4eb0-9a9c-945bcbf1841b)

Çizge Üzerinde Ağ Ölçülerinin Alınması

Temel Ölçümler:
Düğüm Sayısı: 19 Kaç karakter olduğunu temsil eder.
Kenar Sayısı: 42 karakterler arasında kaç bağ olsuğunu temsil eder 
Ortalama Yol Uzunluğu: 2.03 Ağdaki herhangi iki düğüm arasındaki ortalama en kısa yol uzunluğudur.
Kümeleme Katsayısı: 0.617 (Topluluk yapılarının varlığını gösterir). Bir düğümün komşularının birbirleriyle ne kadar bağlantılı olduğunu ölçer.


Merkeziyet Ölçüleri: Derece Merkeziyeti: Bir düğümün kaç kenara bağlı olduğunu ölçer. 
![image](https://github.com/user-attachments/assets/56ca7c64-7350-4487-a8ba-8922e0074685)

Yakınlık Merkeziyeti: Bir düğümün diğer düğümlere ne kadar kısa yollarla ulaşabileceğini gösterir.
![image](https://github.com/user-attachments/assets/27f82b45-c7e9-427a-8d45-62e741734074)

Arasındalık Merkeziyeti: Bir düğümün diğer düğümler arasındaki en kısa yollar üzerinde ne sıklıkla bulunduğunu ölçer.
![image](https://github.com/user-attachments/assets/9779107b-0151-4f5c-acd1-f9a0be43174f)


K-Core Analizi: Bu analiz, ağın en yoğun ve etkili bölgelerini belirler ve hangi düğümlerin ağdaki en kritik geçiş noktaları olduğunu gösterir. Örneğin, ağda k=2 core değerinde iken karaterler aşağıdaki gibidir.
![image](https://github.com/user-attachments/assets/21241312-8671-4ce1-a921-966bf60f5fa9)


Link Analizi

PageRank: Pagerank, bir ağdaki düğümlerin önemi veya popülaritesini ölçmek için kullanılan bir algoritmadır. Google’ın arama motoru algoritmasından esinlenerek geliştirilmiştir. Pagerank, bir düğümün, bir ağdaki diğer düğümlere ne kadar “önemli” olduğuna bağlı olarak ağırlıklandırılmış bir değer atar. Light (0.1656) ve L (0.1053) en merkezi karakterlerdir. Bu durum onların ağdaki kritik rolünü göstermektedir.
![image](https://github.com/user-attachments/assets/33345f3b-6676-46f8-87bd-4aef85952224)

SimRank: SimRank, düğümler arasındaki yapısal benzerliği ölçer. Bu, ağdaki iki düğümün, ortak komşuları ne kadar benzerse o kadar benzer olduğuna dayalı bir ölçümdür. Light, Near ve Mello  benzer bağlantı yapılarına sahiptir. Yani ağdaki rolleri veya pozisyonları birbirine benzerdir. 
![image](https://github.com/user-attachments/assets/f6aa4e53-1d65-4da9-bb9a-8f9c52add46a)
![image](https://github.com/user-attachments/assets/743ec95e-bb25-48b4-ae4d-50ccaf601dad)
![image](https://github.com/user-attachments/assets/82cb3e32-2302-4090-ade7-d8bbbb012c36)

Topluluk Yapısının Ortaya Çıkarılması
Louvain Algoritması ile ağda yoğun bağlantılı 3 büyük topluluk ortaya çıkmıştır. Bu topluluklar polis teşkilatı, L ve ekibi ve Light ın çevresi olarak çok güzel bir şekilde bölünmüştür.
 
Sonuçların Değerlendirilmesi
Yaptığım ölçümler sonucunda, ağın belirli özelliklerini ve yapısal düzenini daha net bir şekilde gözlemledik. Öncelikle, ağımız Death Note evrenindeki karakterlerin ilişkilerini modelleyen bir yapı olduğu için gerçek dünya ağı sayılmaz, ancak sosyal ağ analizinde kullanılan yöntemlerle incelendiği için gerçek dünyadaki sosyal ağlara benzer özellikler taşıyor.
Ağın küçük dünya olup olmadığını değerlendirdiğimizde, ortalama yol uzunluğunun 2.03 ve kümeleme katsayısının 0.617 olması, ağın küçük dünya özellikleri gösterdiğini ortaya koyuyor. Düğümler arasındaki kısa mesafeler ve yoğun yerel bağlantılar, bilgilerin veya etkileşimlerin ağ içinde hızlı bir şekilde yayılabileceğini gösteriyor.
Derece dağılımına baktığımızda, ağın tamamen güç kuralına uymadığını gördük. Bu kural genellikle bazı düğümlerin çok fazla, çoğu düğümün ise çok az bağlantıya sahip olduğu ölçeklenebilir ağlarda görülür. Burada ise derece dağılımı daha dengeli ve homojen bir yapı sergiliyor. Bu durum, düğümler arasındaki ilişkilerin nispeten eşit dağıldığını ve belirli düğümlerin aşırı baskın olmadığını gösteriyor.
Başlangıçta ağın tamamen güç kuralına uyacağını düşünüyordum L ve Light hariç diğer karakterlerin daha düşük kalacağını sanıyordum ama polis teşkilatının kendi arasındaki bağlar durumu değiştirdi ve nerdeyse bu networkünün yarısının güçlü olduğunu göseriyor. Aynı zamanda Light ve L in en çok birbirine benzer diye düşnürken Light ın L in öğrencileriyle daha çok benzerlik oranı göstermesi beni şaşırttı. Geri kala şeyler ise beklediğimiz gibiydi.

Sonuç
Proje de Death Note evrenindeki karakterler arasındaki ilişkilerin sosyal ağ analizi yöntemleriyle incelenmesidir. Bu amaçla, düğümler olarak karakterleri ve kenarlar olarak düşmanlık, dostluk, mentor-öğrenci gibi ilişkileri kullanarak yönsüz, homojen ve statik bir ağ oluşturdum.
Ölçümler sonucunda önemli bulgular elde ettik. Light, derece, yakınlık ve arasındalık merkeziyetinde en yüksek değerlere sahip düğüm olarak ağın merkezi ve en etkili karakteri olarak belirlendi. Ortalama yol uzunluğunun 2.03 olması, ağın küçük dünya özellikleri taşıdığını; kümeleme katsayısının 0.617 olması ise ağda güçlü topluluk yapılarına işaret etti. Ancak derece dağılımı, güç kuralına tam olarak uymayarak daha homojen bir yapı sergiledi.
Bu çalışmayı yaparken, hazır bir veri seti bulamadığımız için veriyi kendimiz oluşturmak zorunda kaldım. Bu durum, projemizi daha fazla emek gerektiren bir hale getirse de, oluşturduğumuz veri seti sayesinde gelecekte benzer ağ analizleri yapmak isteyenler için bir temel oluşturmuş olduk. Bu yönüyle çalışmam, eksiklikten çok alana bir katkı sağlayarak, ağ analizinde kullanılabilecek özgün bir veri sunmaktadır. Gelecekte, bu veriler üzerine farklı analiz yöntemleri uygulanarak çalışmalar daha da geliştirilebilir.
