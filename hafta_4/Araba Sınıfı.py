class araba:
    def __init__ (self,marka,model,yil):
        self.marka=marka
        self.model=model
        self.yil=yil
    def bilgi_ver(self):
        print(self.marka,",",self.model,",",self.yil)    
araba1=araba("Audi","A3","2020")
araba2=araba("Honda","Civic","2025")
araba1.bilgi_ver()
araba2.bilgi_ver()
