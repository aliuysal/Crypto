ilk olarak programın ne yaptığı hakkında kısa bir bilgi vermek istiyorum 

program BENIOKU.txt dosyasından aldığı düz metni simetrik algoritma ile şifreleyerek cypher.txt dosyasına kaydetmektedir 
program kendi içerisinde keys.txt adında bir dosya oluşturmakta bu dosyanın içerisinde kullanıcının seçebileceği keyler bulunmakta bu keylerden birini seçerek şifrelemeyi gerçekleştirebilir 
aynı şekilde decrypt ederkende aynı keyi kullanmamız gerekmektedir 
decrypt işleminde keyi kullanarak çözme işlemi gerçekleştirilir çıkan sonuc plain.txt içerisine kaydedilir.

eklenenler:
hashnen fonksiyonu içerisinde BENIOKU.txt dosyasını sha256 ile hashleyip tekrar CypherText fonksiyonu içerisinde hashlenmiş dosyayı şifreliyor 

kry.py dosyasının en altında hashmd fonksiyonu yer almaktadır bu fonksiyon keys.txt dosyasını 100 defa sha256 ile hashliyor .

	
