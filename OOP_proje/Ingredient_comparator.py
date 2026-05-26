from abc import ABC,abstractmethod
from Compare import Ratio
from typing import Any
"""Bu 2 fonksiyon mesaj gödermede oldukça işimize yarayacak"""
def az_mesaj(isim:str,fark:float,mesaj:list,birim:str)->None:
    return mesaj.append(f"{isim} is not enough.It needs {fark} {birim} more.\n")
def fazla_mesaj(isim:str,fark:float,mesaj:list,birim:str)->None:
    return mesaj.append(f"{isim} is more than enough by {fark} {birim}.\n")



class Hazirlik(ABC):
    """Abstract altyapı"""
    def __init__(self,malzeme=None)->None:
        if malzeme is None:
                malzeme={}
        self.malzeme=malzeme.copy()#orijinal listeye dokunulmaması için
        self.oran_katlari=[]
        self.oran_sabiti=1
    @abstractmethod
    def malzeme_listesi_olusturma(self)->None:#bununla malzeme listesi oluşturulacak
        pass
    @abstractmethod
    def oran_yapma(self,ratio_engine_class:Any):#hanngi malzemeden kaç tane katmamızı girmek için.Ayrıca burdaki ratio_engine_class sayesinde DI sorunu ortadan kalkıyor 
        pass

class Product(Hazirlik):#Ürün
    def __init__(self,malzeme=None):
        super().__init__(malzeme)
        self.urun_ismi=None
    def malzeme_listesi_olusturma(self):
        """elimizdeki malzemeler hakkında listeli sözlük yaratır.{malzeme ismi:[elimizdeki miktarı,birim]}"""
        self.urun_ismi=input("What is the name of your product?:")
        print("Type the ingredients you want to use.Type 'OKAY' when you are done.\n")
        while True:
            yeni_malzeme=input("Enter your ingredients:")
            """OKAY yazılınca malzeme ismi almayı bırakıyor"""
            if yeni_malzeme=="OKAY":break

            while True:
                try:
                    yeni_malzemeden_elimizde_ne_kadar_var=float(input(f"How much/many {yeni_malzeme} do you have?:"))
                    break
                except ValueError:
                    print("Error,enter a number")
            malzeme_birimi=input(f"Enter the unit of {yeni_malzeme}:")
            miktar_ve_birim=[yeni_malzemeden_elimizde_ne_kadar_var,malzeme_birimi]
            
            self.malzeme.update({yeni_malzeme:miktar_ve_birim})
    def oran_yapma(self,ratio_engine_class: Any):
        """tarifte gereken malzemeleri uygun bir şekilde istediğimiz ürün sayısına göre ayarlayıp hesabi Ratio ya yaptırıyoruz"""
        talimatta_oran_sabiti=int(input(f"How many/much {self.urun_ismi} is your recipe or instruction based on?:"))
        self.oran_sabiti=int(input(f"How many/much {self.urun_ismi} you want to make? :"))  
        self.oran_katlari=[]
        self.oran_sabiti=self.oran_sabiti/talimatta_oran_sabiti
        for isim,[miktar,birim] in self.malzeme.items():#oran katlarını yazmak için
            sayi=float(input(f"How many/much {birim} of {isim} is needed for {talimatta_oran_sabiti} {self.urun_ismi}?:"))
            self.oran_katlari.append(sayi)
        elimizdekiler={isim:miktar[0] for isim,miktar in self.malzeme.items()}
        r=ratio_engine_class(elimizdekiler,self.oran_sabiti,self.oran_katlari)
        return r.is_ratio()
    def mesaj_gönderme(self,ratio_engine_class: Any):
        """Kullanıcıya eksik veya fazla malzemeler hakkında mesaj gönderiyor"""
        sonuc=self.oran_yapma(ratio_engine_class)#burda Ratio koyduğumuzda list of tuple alır.tupleler;durum,malzeme ismi ve farktan oluşuyor
        birimler=[miktar[1] for miktar in self.malzeme.values()]#elimizdeki malzemelerin birimlerini döndüren liste
        mesaj:list[str]=[]
        tam_olmayanlar=list(filter(lambda x:x[1][0]!="tam",enumerate(sonuc)))#burda filter sayesinde arada fark bulunanları başka listeye alıp,enumerate yaptık.yani(0,(durum,isim,fark)) vs oldu

        for i,(durum,isim,fark) in tam_olmayanlar:
            if durum=="yetersiz":
                az_mesaj(isim,fark,mesaj,birimler[i])#dosyanın en başındaki fonksiyonlar
            elif durum=="fazla":
                fazla_mesaj(isim,fark,mesaj,birimler[i])
        return mesaj
    def create_and_send_message(self,ratio_engine_class: Any):#ayrı ayrı fonk yazmak yerine hepsini birden yapan fonksiyon
        self.malzeme_listesi_olusturma()
        tum_mesajlar = "".join(self.mesaj_gönderme(ratio_engine_class))
        print(tum_mesajlar)
            
if __name__ == "__main__":
    p= Product()
    p.create_and_send_message(ratio_engine_class=Ratio)


