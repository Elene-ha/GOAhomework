# 3) შექმენი სია სადაც შეინახავ ადამიანების სახელებს, რომლებიც გინდა ,რომ დაპატიჟო წვეულებაზე ,
#  შენი მიზანია გაფილტრო ეს ადამიანები, ზოგი ამოშალო ზოგი დაამატო(append , pop , insert) , ბოლოს უნდა დაბეჭდო ყველანაირი ინფორმაცია ,
#  1)თავდფაპირველი სია 2)ამოკლებული ადამიანები 3)დამატებული ადამიანები , 4)რამდენი ადამიანი დარჩა სულ , 5)საბოლოო სია

guests = ["წითელი პანდა", "დათვი", "გველი", "ლომი", "პანდა", "ვეფხვი", "პეპელა"]


original_guests = guests.copy()


removed_Animal = []
added_Animal = []


removed_Animal.append(guests.pop(2))   
removed_Animal.append(guests.pop(3))   


removed_Animal.append(guests.pop())    

guests.append("კატა")
added_Animal.append("კატა")


guests.insert(1, "ლეოპარდი")
added_Animal.append("ლეოპარდი")


guests.append("მგელი")
added_Animal.append("მგელი")


total_remaining = len(guests)


final_guests = guests  


print("1) თავდაპირველი სია:", original_guests)
print("2) ამოკლებული 🐾:", removed_Animal)
print("3) დამატებული 🌸🐾:", added_Animal)
print("4) სულ დარჩა 🐾:", total_remaining)
print("5) საბოლოო სია:", final_guests)
