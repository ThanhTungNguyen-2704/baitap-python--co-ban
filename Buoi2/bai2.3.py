clb_bóng_đá = {"An", "Bình", "Chi", "An", "Dương", "Bình"}
clb_cờ_vua = {"Chi", "Đạt", "Gia", "An", "Hùng"}

# 1. Loại bỏ trùng lặp 
print("1. CLB Bóng đá sau lọc trùng:", clb_bóng_đá) 
# Kết quả: {'Bình', 'Dương', 'An', 'Chi'} (Thứ tự có thể ngẫu nhiên)

# 2. Học sinh tham gia cả 2 câu lạc bộ 
danh_sach_hoc_sinh_2_CLB = clb_bóng_đá.intersection(clb_cờ_vua)
print("2. Học sinh tham gia cả 2 CLB:", danh_sach_hoc_sinh_2_CLB)
# Kết quả: {'An', 'Chi'}

# 3. Học sinh CHỈ tham gia bóng đá 
print("3. Học sinh chỉ đá bóng:", clb_bóng_đá.difference(clb_cờ_vua))
# Kết quả: {'Bình', 'Dương'}

# 4. Tổng số học sinh độc nhất tham gia phong trào
tat_ca_hoc_sinh = clb_bóng_đá.union(clb_cờ_vua)
print("4. Danh sách tổng hợp:", tat_ca_hoc_sinh)
print(f"==> Tổng số học sinh độc nhất là: {len(tat_ca_hoc_sinh)} người.")
# Kết quả: 6 người