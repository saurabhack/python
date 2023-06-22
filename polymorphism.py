class man:
    def name(self):
        self.red=str(input("enter your name"))
        print("your name is=",self.red)

class rend:
    def name(self):
        self.mans=str(input("enter your name="))
        print("your name =",self.mans)

    
dj=man()
ld=rend()

for natu in (dj,ld):
    natu.name()
    natu.name()