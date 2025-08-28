
class Smartphone:
    def __init__(self, brand, model, storage):
        # Attributes
        self.brand = brand
        self.model = model
        self.storage = storage
    
    # Method
    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB")


# Child class 
class SmartPhonePro(Smartphone):
    def __init__(self, brand, model, storage, camera_quality):
        # Inherit attributes from Smartphone
        super().__init__(brand, model, storage)
        # Extra attribute for Pro version
        self.camera_quality = camera_quality

    # Overriding method
    def info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB, Camera: {self.camera_quality}MP")

    # private attribute
    def __secret_feature(self):
        print("This phone has a secret AI chip 🤖")

    def reveal_secret(self):
        self.__secret_feature()


# Creating objects
phone1 = Smartphone("Samsung", "Galaxy S21", 128)
phone2 = SmartPhonePro("Apple", "iPhone 15 Pro", 256, 48)

# Using methods
phone1.info()
phone1.call("+256700000001")

phone2.info()
phone2.call("+256700000002")
phone2.reveal_secret()
