from flask import Flask
import random


app = Flask(__name__)

@app.route('/rastgele_gercek')
def rastgele_gercek():  
    
    facts_list = [
        "2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor.",
        "Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir.",
        "Teknolojik bağımlılıkla mücadele etmenin bir yolu, zevk veren ve ruh halini iyileştiren faaliyetler aramaktır.",
        "Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor..",
        "Elon Musk ayrıca sosyal ağların düzenlenmesini ve kullanıcıların kişisel verilerinin korunmasını savunmaktadır. Sosyal ağların hakkımızda büyük miktarda bilgi topladığını ve bu bilgilerin daha sonra düşüncelerimizi ve davranışlarımızı manipüle etmek için kullanılabileceğini iddia ediyor."
        "Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar."
        "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor."
        "Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir."
    ]
    return f'<p>{random.choice(facts_list)}</p>'
    
@app.route('/')
def anasayfa():
    return '<h1>Hoşgeldşiniz! Rastgele Gerçekler için linke tıklayın.</h1><a href="/rastgele_gercek">Rastgele Gerçekler</a>'

@app.route("/rastgele_gercek/secret")
def secret():
    sonuc = random.choice(["Yazı", "Tura"])
    return f"<h1>Gizli sayfayı buldun! al sana yazı tura</h1><p>Yazı Tura Sonucu: {sonuc}</p>"



app.run(debug=True, port=6453)
