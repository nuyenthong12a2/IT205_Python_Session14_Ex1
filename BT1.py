# Phân tích lỗi 
# Câu 1 : Gán sai tham số 
# def calculate_final_price (price,discount,shipping_fee)
# Gọi hàm : calculate_final_price(100000,15000,0.1)
# Kết quả : 
# Price : nhận giá trị 1000 (Đúng)
# discount :Nhận giá trị 15000 (Sai, đúng ra phải là 0.1)
# shipping_fe : Nhận giá trị 0.1 (Sai , 0.1)

# Câu 2 : Công toán bị sai lệch 
# total = 100000 - (100000*15000) +0.1
# total =  = 100000 - 1500000000 + 0.1 = -1499999999.9
# Thực tế tiền không được tính ra số âm 

# Câu 3 & Câu 4 
# Lỗi TypeError và giá trị của order_total 
# Dòng lệnh final_payment = order_total + 5000 bị lỗi Vì biến order_total đang mang giá trị None 
# Không thể cộng dữ liệu NoneType với một kiểu dữ liệu int 
# Order_total bằng None : Hàm calculate_final_price ở legacy code chỉ sử dụng lệnh print() để hiển thị kết quả ra màn hình chứ không có lệnh return . Khi có một hàm kết thúc mà không có return , Python sẽ mặc định trả về giá trị None 

# Câu 5 : Sự khác biệt giữa print () và return 
# print (total) :Nhiệm vụ "Hiển thị " giá trị của biến total lên màn hình console cho người dùng nhìn thấy . Máy tính không thể giữ lại giá trị này để làm toán hay thực hiện các logic khác tiếp theo 
# return total : Có nhiệm vụ "trả kết quả " từ trong hàm ra ngoài . Nó cho phép gán kết quả của hàm vào một biến 

# Câu 6 : Sửa đồi hàm 
# đổi calculate_final_price , đổi dòng lệnh print ("đã tính xong tổng tiền :".total) (hoặc bỏ hẳn nó đi để đáp ứng yêu cầu output duy nhất ) và thêm vào lệnh return total 

def calculate_final_price(price,discount,shipping_fee):
    total = price - (price * discount) + shipping_fee
    return total 

order_total = calculate_final_price(100000,0.1,15000)

final_payment = order_total + 5000

print ("Khách hàng cần thanh toán :", final_payment)
