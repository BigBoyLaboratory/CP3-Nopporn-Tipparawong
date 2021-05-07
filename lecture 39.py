#ถ้าเกิดคะแนน
#มากกว่าหรือเท่ากับ 80 จะได้เกรด A
#มากกว่าหรือเท่ากับ 75 จะได้เกรด B+
#มากกว่าหรือเท่ากับ 70 จะได้เกรด B
#มากกว่าหรือเท่ากับ 65 จะได้เกรด C+
#มากกว่าหรือเท่ากับ 60 จะได้เกรด C
#มากกว่าหรือเท่ากับ 55 จะได้เกรด D+
#มากกว่าหรือเท่ากับ 50 จะได้เกรด D
#น้อยกว่า      50 จะได้เกรด F

score = int(input("Your Score: "))
if score >= 80:
    print("Grade: A")
elif score >=75:
    print ("Grade: B+")
elif score >= 65:
    print ("Grade: B")
elif score >= 60:
    print ("Grade: C+")
elif score >= 55:
    print ("Grade: D+")
elif score >= 50:
    print ("Grade: D")
else:
    print ("Grade: F")