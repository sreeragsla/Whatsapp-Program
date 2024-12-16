'''
In the early days we don't have these properties at the starting stage of whatsapp. It is introduced in new versions.They 
have introduced new properties along with the existing properties.We can achieve it by using Inheritance and polymorphism.
'''
class Whatsapp_V1:
    def __init__(self,n,mn,dp):
        self.name=n
        self.mobilenumber=mn
        self.profilepicture=dp
        
    def details(self):
        print('Name - ',self.name)
        print('Mobile Number - ',self.mobilenumber)
        print('Profile Picture - ',self.profilepicture)

class Whatsapp_V2(Whatsapp_V1):            #inheritance
    def __init__(self,n,mn,dp,ac,amsg,vc):
        Whatsapp_V1.__init__(self,n,mn,dp)             #constructor chaining by using class name
        self.audiocall=ac
        self.audiomessage=amsg
        self.videocall=vc

    def details(self):             #polymorphism (method overriding)
        Whatsapp_V1.details(self)          #method chaining by using class name
        print('Audio Call - ',self.audiocall)
        print('Audio Message - ',self.audiomessage)
        print('Video Call - ',self.videocall)

class Whatsapp_V3(Whatsapp_V2):          #inheritance
    def __init__(self,n,mn,dp,ac,amsg,vc,sta,sti,vmsg,p):
        super().__init__(n,mn,dp,ac,amsg,vc)               #constructor chaining by using super method
        self.whatsappstatus=sta
        self.whatsappsticker=sti
        self.videomessage=vmsg
        self.payment=p

    def details(self):               #polymorphism  (method overriding)
        super().details()              #method chaining by using super method
        print('Whatsapp Status - ',self.whatsappstatus)
        print('Whatsapp Sticker - ',self.whatsappsticker)
        print('Whatsapp Video Message - ',self.videomessage)
        print('Whatsapp Payment - ',self.payment)

srg=Whatsapp_V3('Sreerag',1234,'Yes','Yes','Yes','Yes','Yes','Yes','Yes','Yes')
srg.details()




        
        
