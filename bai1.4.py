# Đoạn code dưới có LỖI. Tìm và sửa tất cả lỗi:

name = input("Tên: ")
age = input("Tuổi: ")
gpa = input("GPA: ")

birth_year = 2026 - int(age)          # Lỗi 1
print("Năm sinh: " + str(birth_year)) # Lỗi 2

if float(gpa) >= 3.5:                   # Lỗi 3
    print(name + " học giỏi!")