class Restuarent:
    name=''
    owner=''


    def resturant_details(self):
        print(self.name, self.owner)

    def details_address(self, address):
        print(self.name,self.owner)
        print(address)

# instantiate

restuarent1=Restuarent() # object creation
restuarent1.name='muslim sweets'
restuarent1.owner='abir'
restuarent1.resturant_details()
restuarent1.details_address('bogra')
