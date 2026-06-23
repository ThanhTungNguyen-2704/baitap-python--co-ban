diem = [3, 7, 5, 9, 2, 8, 4, 6, 10, 1, 7, 5, 3, 8, 6]
result = []
for x in diem :
    if x >= 5 :
        result.append(x)


diem_tong = int(0) 
for x in diem :
    diem_tong += x 

diem_trung_binh = round(float(diem_tong / len(diem)),2)

so_hoc_sinh_tren_5 = len(result)
so_hoc_sinh_duoi_5 = len(diem) - len(result)

thong_ke = {
    "passed" : so_hoc_sinh_tren_5 ,
    "failed" : so_hoc_sinh_duoi_5 ,
    "avg"    : diem_trung_binh 
}
print("==============================")
print(f"  KẾT QUẢ THI — 15 HỌC SINH")
print(f"==============================")
print(f"  Điểm đậu (>=5) : {so_hoc_sinh_tren_5} học sinh")
print(f"  Điểm rớt (<5)  : {so_hoc_sinh_duoi_5} học sinh")
print(f"  Trung bình     : {diem_trung_binh}")
print(f"==============================")


