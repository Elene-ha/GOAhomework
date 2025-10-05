# for ციკლის მეშვეობით დაბეჭდეთ ყველა კენტი რიცხვის ჯამი 1-დან 99 ის ჩათვლით

sum = 0

for i in range(1, 100, 2):
    sum += i

print(sum)  

# while ციკლის მეშვეობით დაბეჭდეთ ყველა კენტი რიცხვის ჯამი 1-დან 99 ის ჩათვლით

sum = 0
i = 1  

while i <= 99:
    sum += i
    i += 2  

print(sum)


# მომხმარებელს შემოატანინეთ რიცხვი მანამ სანამ ესრიცხვი არ იქნება ლუწი, ხოლო როდესაც
# მომხმარებელი შეიყვანს ლუწ რიცხვს , ტერმინალში დაიპრინტოს "You enter an even number and the loop is over"

num = 1 
while num % 2 != 0:
    num = int(input("გთხოვთ შეიყვანოთ რიცხვი: "))

print("You enter an even number and the loop is over")

# *if/else Statements**
# მომხმარებელს შემოატანინეთ რიცხვი , თქვენი მიზანია გაიგოთ ეს რიცხვი დადებითია , უარყოფითია თუ ნულის ტოლია

num = float(input("Enter num: "))

if num == 0:
    print("The number is zero")
else:
    if num > 0:
        print("The number is positive")
    else:
        print("The number is negative")



# მომხმარებელს შემოატანინეთ რიცხვი , თქვენი მიზანია გაიგოთ ეს რიცხვი კენტია თუ ლუწი

num = int(input("შეიყვანეთ რიცხვი: "))

if num % 2 == 0:
    print("რიცხვი ლუწია")
else:
    print("რიცხვი კენტია")




