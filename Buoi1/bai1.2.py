# Viết chương trình nhận vào 2 số từ bàn phím,
# tính tổng, hiệu, tích, thương (chia lấy phần nguyên).
# Lưu ý: input() trả về str, phải ép kiểu trước khi tính.

# Output mẫu:
# Nhập số 1: 10
# Nhập số 2: 3
# Tổng: 13
# Hiệu: 7
# Tích: 30
# Thương nguyên: 3

print("Nhập số 1 :")
so1 = input(str())
print("Nhap so 2: ")
so2 = input(str())
tong = int(so1) + int(so2) 
hieu = int(so1) - int(so2)
tich = int(so1) * int(so2)
thuongNguyen = int(float(so1)/ float(so2))
print(f"Tổng {tong} Hiệu {hieu} Tích {tich} Thương Nguyên {thuongNguyen}"  )