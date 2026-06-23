#Bài tập về Tuple
sales_data = [
    ("DH001", "Anh", "iPhone 15", 1, 1000, "Hà Nội"),
    ("DH002", "Bình", "iPad Air", 2, 600, "TP.HCM"),
    ("DH003", "Chi", "iPhone 15", 2, 1000, "Hà Nội"),
    ("DH004", "Dương", "MacBook Pro", 1, 2000, "Đà Nẵng"),
    ("DH005", "Anh", "AirPods", 3, 200, "Hà Nội"),
    ("DH006", "Giang", "iPad Air", 1, 600, "TP.HCM"),
    ("DH007", "Hương", "iPhone 15", 1, 1000, "Đà Nẵng")
]

tong_doanh_thu =  int(0)
for x in sales_data :
	(ma_don, ten_kh, san_pham, so_luong, gia, thanh_pho) = x 
	tong_doanh_thu += (so_luong * gia)

print(f"Tổng doanh thu là :{tong_doanh_thu}")

tong_tien_HN = int(0)
tong_tien_TPHCM = int(0)
for x in sales_data :
	if x[-1] == "Hà Nội" :
		tong_tien_HN += (x[-3] * x[-2])
	if x[-1] == "TP.HCM" :
		tong_tien_TPHCM += (x[-3] * x[-2])
thong_ke_theo_tp={
	"Hà Nội" : tong_tien_HN ,
	"TP.HCM" : tong_tien_TPHCM
}
print (thong_ke_theo_tp)
danh_sach_Vip={}
for x in sales_data : 
	danh_sach_Vip[x[1]] = (x[-2] * x[-3])
max = 0
nguoi_tieu_nhieu_nhat = ""
for x in danh_sach_Vip:
	if(danh_sach_Vip[x] > max):
		max = danh_sach_Vip[x]
		nguoi_tieu_nhieu_nhat = x
print(f"người tiêu nhiều tiền nhất : {nguoi_tieu_nhieu_nhat} với số tiền là : {max}")





