class Parent:
    def phone(self):
        print("nokia")
    def bike(self):
        print("passion pro")
class Child(Parent):
    def phone(self):
        print("iphone 12")
    def bike(self):
        print("duke")
ch=Child()
ch.phone()
ch.bike()