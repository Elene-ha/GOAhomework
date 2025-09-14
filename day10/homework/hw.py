# დავალება - 1

# მონაცემების ტიპის შეცვლა (Data Conversion) 

# int()	გარდაქმნის მონაცემს მთელ რიცხვად
# float()	გარდაქმნის მონაცემს ათწილად რიცხვად
# str()	გარდაქმნის მონაცემს სტრიქონად
# bool()	გარდაქმნის მონაცემს ლოგიკურ ტიპად (True/False)

# დავალება - 2

 # Implicit Type Conversion
# ხდება ავტომატურად, პროგრამის მიერ.

# მაგ: int გადაიქცევა float-ად საჭიროების შემთხვევაში.

# მაგალითი:

x = 5 + 3.0   # x ხდება 8.0 (float)

# ✅ Explicit Type Conversion

# ხდება ხელით.

# გამოიყენება გარდაქმნის ფუნქციები: int(), float(), str() და სხვა.

# მაგალითი:

x = int("5") + 2   # x = 7

# დავალება - 3

# მაგალითი 1 :⬇️

x = 10      # int
y = 2.5     # float
result = x + y   # x ავტომატურად გადაიქცევა float-ად
print(result)    # 12.5

# მაგალითი 2 :⬇️

x = True     # bool
y = 4        # int
result = x + y  # True ავტომატურად გადაიქცევა 1-ად
print(result)   # 5


# მაგალით 3 :

x = 5        # int
y = 2        # int
z = x / y    # ავტომატურად ხდება float-ად გარდაქმნა
print(z)     # 2.5


# მაგალითი 4 : 

a = 7      # int
b = 1.0    # float
c = a * b  # a ავტომატურად გარდაიქმნება float-ად
print(c)   # 7.0


# დავალება - 4

#მაგალითი 1: str ➝ int

x = "10"        # სტრინგი
y = int(x) + 5  # ვაქცევთ int-ად
print(y)        # 15

# მაგალითი 2: float ➝ int
x = 3.9
y = int(x)      # მოჭრის ათწილად ნაწილს
print(y)        # 3
# მაგალითი 3: int ➝ float

x = 8
y = float(x)    # გადარი"

# მაგალითი 5: list ➝ tuple

x = [1, 2, 3]
y = tuple(x)    
print(y)        # (1, 2, 3)
# გადავაქციეთ float-ად
print(y)        # 8.0

# მაგალითი 4: int ➝ str
x = 100
y = str(x) + " ლარი"
print(y)        # "100 ლარი 
# დავალება - 5 

# Concatenation ნიშნავს მონაცემების შეერთებას ერთმანეთთან

# მაგალითები : ⬇️

a = "Hello"
b = "World"
print(a + " " + b)  

age = 9999
print("I am " + str(age) + " years old") 

# დავალება - 6

birth_year = int(input("შეიყვანეთ თქვენი დაბადების წელი: "))

# მიმდინარე წლის მიღება
current_year = int(input("შეიყვანეთ თქვენი მიმდინარე წელი: "))


# ასაკის გამოთვლა
age = current_year - birth_year

# შედეგის დაბეჭდვა
print("თქვენ ხართ", age, "წლის")

# დავალება - 7
 
name ="snake"
surname ="....."
age = 999
height = 1.99  
address = "საქართველო"
address2 = address + "ში"
sentence = "მე ვარ " + name + " " + surname + ", ასაკი მაქვს " + str(age) + " წელი, სიმაღლე " + str(height) + " მეტრი და ვცხოვრობ " + address2 + "."
           
print(sentence) 



