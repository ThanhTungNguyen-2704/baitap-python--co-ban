
students = []

def appendStudents(id,name,grades):
	result = {"id" : id , "name" : name , "grades" : grades}
	students.append(result)
	pass 

def tinh_diem_tb(id):
	for x in students:
		if x.get("id") == id :
			return sum(x.get("grades")) / len(x.get("grades")) 
	return -1 

def danh_sach_tb_lon_hon_8(students):
	result = [x for x in students if tinh_diem_tb(x.get("id")) > 8 ]
	return result

while True :
	print("Nhập id:")
	id = input() 
	print("Nhập họ và tên: ")
	name = input()
	print("Nhập lần lượt điểm toán, văn, anh : ")
	grades = [float(input()),float(input()),float(input())]
	appendStudents(id,name,grades)
	print("tổng số học sinh là: " + str(len(students)) )
	print("Bạn có muốn nhập thêm học sinh chứ :" )
	b = input()
	if (b == "không"):
		break
for hs in students:
    dtb = tinh_diem_tb(hs["id"])
    print(f"- Học viên: {hs['name']} (ID: {hs['id']}) có điểm TB là: {dtb:.2f}")

hoc_vien_gioi = danh_sach_tb_lon_hon_8(students)
print(f"\nDanh sách học viên xuất sắc (Điểm TB > 8.0):")
if hoc_vien_gioi:
    for hs in hoc_vien_gioi:
        dtb = tinh_diem_tb(hs["id"])
        print(f"[XUẤT SẮC] {hs['name']} (ID: {hs['id']}) - Điểm TB: {dtb:.2f}")
else:
    print("Không có học viên nào đạt điểm trung bình trên 8.0.")



