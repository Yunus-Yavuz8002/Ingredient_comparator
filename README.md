# Ingredient_comparator

How to install the library.

USAGE GUIDE: from Ingredient_comparator import Product

p=Product() 
p.create_and_send_message() 
CLI Simulation Input/Output:

What is the name of your product?:Lemonade

Type the ingredients you want to use.Type 'OKAY' when you are done.


Enter your ingredients:lemon 

How much/many lemon do you have?:40 

Enter the unit of lemon:pieces 

Enter your ingredients:orange

How much/many orange do you have?:4 

Enter the unit of orange:pieces 

Enter your ingredients:sugar 

How much/many sugar do you have?:7 

Enter the unit of sugar:glasses 

Enter your ingredients:hot water 

How much/many hot water do you have?:5 

Enter the unit of hot water:glasses 

Enter your ingredients:cold water

How much/many cold water do you have?:20 

Enter the unit of cold water :glasses 

Enter your ingredients:OKAY 

How many/much Lemonade is your recipe or instruction based on?:8 

How many/much Lemonade you want to make? :40 

How many/much pieces of lemon is needed for 8 Lemonade?:6 

How many/much pieces of orange is needed for 8 Lemonade?:1 

How many/much glasses of sugar is needed for 8 Lemonade?:1 

How many/much glasses of hot water is needed for 8 Lemonade?:1 

How many/much glasses of cold is needed for 8 Lemonade?:5 

lemon is more than enough by 10.0 pieces. 

orange is not enough.It needs 1.0 pieces more. 

sugar is more than enough by 2.0 glasses.

cold is not enough.It needs 5.0 glasses more.


DESIGN PATTERNS USED: Template method pattern is used in Hazirlik(preparation in Turkish) and Product in Ingredient_comparator.py
Strategy pattern is when Product class used is_ratio for calculation and results instead of doing those itself.

MEETING THE 6 LEARNING OUTCOMES:

Abstract Base Classes (ABCs): Hazirlik class inherits from abc.

Encapsulation & Mutability Protection:Inside the Hazirlik.init constructor, defensive copying (self.malzeme = malzeme.copy()) protects the internal dictionary structure.

Inheritance & Polymorphism:Product class inherits from abstract base Hazirlik class and uses super()init to initialize its attributes

Robust Error Handling:In malzeme_listesi_olusturma(self), a try-except loop captures ValueError for non-float(like strings) values.

Separation of Concerns (SoC):Ratio class calculates for Ingredient_comparator

Clean Type Annotation & Type Safety:Type hinting standarts are used for almost every function

ADVANCED CONCEPTS IMPLEMENTED:
Functional Programming: Inside the mesaj_gönderme function of the Product class, we utilized Python's functional tools: filter() combined with an anonymous lambda function. This avoids explicit and mutable state loops, dynamically streaming out balanced values ("tam") and isolating anomalous data tuples via declarative filtering, satisfying advanced programming paradigm requirements
