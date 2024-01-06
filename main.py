türbilans=int(input("türbilans var mı varsa 1 e bas yoksa 0 a bas"))#radar verisinden türbilans olup olmadığı alınır bizim elimizde radar olmadığı için pilottan istiyoruz#
if türbilans==1:
    konum=input("nerede türbilans var")#normalde gps verisinden direkt koordinat almalıyız ama elimizde gps verisi olmadığı için pilottan istiyoruz#
    from datetime import datetime#zaman eklemek için datetime kütüphanesini kullanıyoruz#
    import geopandas as calistir#adresten koordinat alabilmek için geopandas kütüphanesini kullanıyoruz#
    adres = calistir.tools.geocode(konum)#geopandas kütüphanesini çalıştıran kod#
    koordinat=(adres.geometry.y[0], adres.geometry.x[0])#koordinatlar#
    y=adres.geometry.y[0]#boylamı y ye tanımladık#
    x=adres.geometry.x[0]#enlemi x e tanımladık#
    import folium#haritada türbilans olan yeri işaretlemek için folium kütüphanesini çağırdık#
    harita = folium.Map(location=[37.872895,32.492190], zoom_start=11,width=550, height=550,)#konya merkezli boş bir harita oluşturur#
    folium.Marker(location=[y, x],popup=datetime.now(),tooltip='<strong>TÜRBİLANS Detaylar için tıklayın</strong>',icon=folium.Icon(color='blue',prefix='fa',icon='tornado')).add_to(harita)#türbilans olan yeri haritada işaretleriz ve üstüne tıkladığımız zaman hangi tarih ve saatte işaretlendiğini görürüz#
    harita.save('sample_map.html')#haritayı html dosyasına kaydederiz#
    print("harita url:file:///c%3A/Users/yusuf/Desktop/projeb/sample_map.html")#kodu kullananlar urlyi açabilmeleri için ekrana yazdırır#
elif türbilans==0:#türbilans yoksa iyi uçuşlar diler#
    print("iyi uçuşlar")#ekrana iyi uçuşlar yazar#
else:#1 veya 0 dan başka bir sayıya basılırsa yanlış tuşlama yapıldığını söyler#
    print("yanlış bir tuşa bastınız lütfen kodu tekrar çalıştırıp sizden istenen tuşlamaları yapınız")#ekrana yanlış tuşlama yapıldığı yazar#