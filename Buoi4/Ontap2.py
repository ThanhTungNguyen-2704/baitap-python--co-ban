#bài 1
price = 149000 
print(f"Giá sản phẩm: {price:,} VNĐ")
score = 8.6789 
print(f"Điểm trung bình: {score:.2f}")
def bao_cao(ten,diem):
	return f"{ten} đạt {diem} điểm"

for i in range(3):
	ten = input()
	diem = int(input())
	print(bao_cao(ten,diem)) 

#Bài 2
tuoi = int(input())
print(f"Bạn sinh ra khoảng năm {2026-tuoi}")
strings = ["10", "25", "3", "8"]
tong = 0
for i in strings:
	so = int(i)
	tong += so
print(f"Tổng các số trong list string là : {tong}")
#câu 3 bool(False) chưa biết 

#bài 3
def chia(a,b):
	try :
		x = int(a)
		y = int(b)
		ket_qua = x/y
	except ValueError:
		print("bạn phải nhập số")
	except ZeroDivisionError:
		print("không thể chia cho 0")
	else:
		print(f"kết quả: {ket_qua}")
	finally:
		print("đã xử lý xong")
chia(10,2)
chia(5,0)
chia(10,"abc")
chia("xyz",20)


du_lieu = ["10", "abc", "5", "0", "20"]

for x in du_lieu:
	try :
		so2 = 100/int(x)
	except ValueError:
		continue
	except ZeroDivisionError:
		continue 
	else:
		print(so2)
	finally:
		print("đã hoàn thành")
#bài 4
diem = [4, 8, 6.5, 9, 3, 7.5]
diem_tren_tb = [x for x in diem if x >= 5]
danh_sach= ["Ha Noi", "Sai Gon", "Da Nang"]
danh_sach_moi = [len(x) for x in danh_sach  ]

sinh_vien = {"Tung": 8.5, "Lan": 6.2, "Minh": 9.1, "Hoa": 4.8}
sinh_vien_moi = { k : v for k,v in sinh_vien.items() if v >= 5}

#có ý tưởng nhưng chưa biết cách triển khai
def loc_va_tinh_tong(danh_sach_str):
    so_hop_le = []
    for x in danh_sach_str:
        try:
            a = int(x)
            so_hop_le.append(a)
        except ValueError:
            continue
    tong = sum(so_hop_le)
    print(f"Các số hợp lệ: {so_hop_le}, tổng = {tong}")



