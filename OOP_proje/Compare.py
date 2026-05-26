#ratio


class Ratio:
    def __init__(self,malzemelerimiz:dict[str,float] ,ratio_constant :float,ratio_rates):
        self.malzemelerimiz=malzemelerimiz#elimizdeki malzemelerin ismi ve sayısı bunun ögeleri
        self.ratio_constant=ratio_constant# kaç tane ürün olması lazım
        self.ratio_rates=ratio_rates#bir ürünün içinde bundan kaç tane olmalı   


    def is_ratio(self):
        """elimizdeki malzemelerle gereken malzemelerin arasındaki farkı buluyor.sonra list of tuples döndürüyor.tupleler (durum,malzeme ismi,aradaki fark) formatında"""
        malzeme_isimleri: list[str]=list(self.malzemelerimiz.keys())
        el_malz_say=list(self.malzemelerimiz.values())#elimizdeki malzeme sayısı
        sonuc=[]
        if len(el_malz_say)!=len(self.ratio_rates):
            return "Liste ve oran uzunlukları eşit olmalı"
        for i in range(len(el_malz_say)):
            gereken=self.ratio_constant*self.ratio_rates[i]
            if el_malz_say[i]<gereken:
                sonuc.append(("yetersiz",malzeme_isimleri[i],abs(el_malz_say[i]-gereken)))#sonuç listesine tuple koydum
            elif el_malz_say[i]>gereken:
                sonuc.append(("fazla",malzeme_isimleri[i],abs(el_malz_say[i]-gereken)))#1. parametre durumu,2.'si malzeme ismini,3.'sü de farkı veriyor
            else:
                sonuc.append(("tam",malzeme_isimleri[i],abs(el_malz_say[i]-gereken)))
        if sonuc:
            return sonuc
        else:
            return True




