class Grand_Father:
    HOD="Nadipanna"
    def __init__(self,gm,s1,s2,d1,d2,d3):
        self.grande_mother=gm
        self.Elder_son=s1
        self.young_son=s2
        self.yelder_daughter=d1
        self.middle_dauther=d2
        self.young_daughter=d3
class Father(Grand_Father):
    HOD='Sampth'
    def __init__(self,gm,s1,s2,d1,d2,d3,m,s11,s22,s33,d11):
        super().__init__(gm,s1,s2,d1,d2,d3)  
        self.mother=m
        self.Elder_son=s11
        self.middle_son=s22
        self.young_son=s33
        self.daughter=d11
class Current:
    HOD='ANIL'
    def __init__(self,gm,s1,s2,d1,d2,d3,m,s11,s22,s33,d11,mw):
        super().__init__(gm,s1,s2,d1,d2,d3,m,s11,s22,s33,d11)
        self.head=mw
obj=Current("Lakshumamma",'govindu','sampath','Yellamma','nagamma','lakshmi','Syam','mani','sathosh','anil','jhansi','searching')
        

