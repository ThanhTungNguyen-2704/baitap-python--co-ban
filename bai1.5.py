# Viết chương trình tính BMI:
# - Nhập cân nặng (kg) và chiều cao (cm)
# - Tính BMI = weight / (height_m ** 2)
# - In kết quả và phân loại:
#   BMI < 18.5  → "Thiếu cân"
#   18.5 – 24.9 → "Bình thường"  
#   25.0 – 29.9 → "Thừa cân"
#   >= 30       → "Béo phì"

weight = input("Nhập cân nặng: ")
height = input("Nhập chiều cao: ")

bmi = float(float(weight) / (float(height) ** 2) )
if(bmi < 18.5) :
	print("Thiếu cân")
elif(18.5 <= bmi <= 24.9) :
	print("Bình Thường")
elif (25.0 <= bmi <= 29.9 ) :
	print("Thừa cân")
else :
	print("Béo phì")