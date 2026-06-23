# Bước 1: import thư viện cần thiết (nếu dùng regex)
import re

def clean_name(s):
    """
    Input : chuỗi tên bẩn

    Output: chuỗi tên sạch, capitalize
    """
    # TODO 1: loại ký tự đặc biệt
    s = re.sub('[^a-zA-ZÀ-ỹ]', ' ' , s) 
    

    
    # TODO 2: xóa khoảng trắng thừa
    s = ' '.join(s.split())
    
    # TODO 3: capitalize từng từ
    
    return s.title() 
dirty_names = [
    "  nguyễn văn  an  ", "TRẦN  THỊ   BÌNH",
    "lê@#minh!cường",    "  pHạM   tHị  dUnG  ",
    "hoàng***văn***em",  "VŨ THỊ   PHƯƠNG",
    "đặng!!minh!!giàu", "  bùi   thị   hằng  ",
    "ngô$văn$inh",       "  LÝ   THỊ   KIM  ",
    "đinh%minh%lâm",     "  tRươnG  tHị  mAi  ",
    "võ...văn...nam...", "  HỒ   THỊ   OANH  ",
    "lương#văn#phúc",    "   mai   thị  quyên   ",
    "dương^minh^rạng",  "  NGUyễN  tHị  sAo  ",
    "trịnh&văn&tài",    "  phan   thị   uyên  "
]

# Áp dụng map() — viết 1 dòng duy nhất
clean_names = list(map(clean_name, dirty_names))

# In kết quả
for name in clean_names:
    print(name)
