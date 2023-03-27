# stock-app-backend-django

It is the backend part of the https://github.com/ihsan24-24/stock-app-24 application that I made the front-end. It is a back-end application where we can see the total amounts of the materials remaining in stock by creating a user record and making purchase and sale transactions. The stock status of each product to be purchased is checked in SalesView in views.py in the stock folder. In signals.py in the Stock folder, the total sales amounts are recalculated after each trading transaction.

# Turkish

Front-end'ini yaptığım https://github.com/ihsan24-24/stock-app-24 uygulamasının backend kısmıdır. Kullanıcı kaydı oluşturup alış-satış işlemleri yaparak stokta kalan malzemeleri toplam tutarları görebileceğimiz bir back-end uygulamasıdır. stock klasöründeki views.py da ki SalesView da satın alınmak istenilen her ürünün stok durumu kontrol ediliyor eğer stok yetersizse müşteriye yeterli stok yoktur mesajı dönülüyor. Stock klasöründeki signals.py da her alım-satım işleminden sonra toplam satış miktarları yeniden hesaplanıyor. 
