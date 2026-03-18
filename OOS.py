class make_up():
    tax_amt=1.18
    def __init__(self,first,last,product,price):
        self.first = first
        self.last = last
        self.product = product
        self.price = price
        self.email = first+'.'+ last +"@gmail.com"

    def full_name(self):
        return '{} {}'.format(self.first,self.last) 
    
    def final_price(self):
        return self.price* self.tax_amt
    


lady1= make_up('manjari','Awasthi','blush',200)
lady2= make_up('madhu','Yadav','contour',300)

print(f"price of product{lady1.product}-{lady1.final_price()}")

print(f"class value-{make_up.tax_amt}")
print(f"class value of obj1-{lady1.tax_amt}")

lady1.="manjari"
lady1.product="lipstick"

lady2.name="madhu"
lady2.product="foundation"


print(lady1.full_name())
print(lady2.full_name()) 




# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
         
#      def result(self):
#            if self.marks>=60:
#               return"pass"
#            else:
#               return"fail"
#     s= Student("manjari",70)
#     print(s.result())