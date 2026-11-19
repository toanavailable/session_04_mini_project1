"""[BTTH] 1. Tính số tiền hóa đơn cho khách hàng - Rikkei Store."""

discount_threshold = 500000   # hóa đơn từ 500,000 VND trở lên được giảm giá
discount_percent = 10         # mức giảm 10%

# Chức năng 1: nhập tổng tiền ban đầu của hóa đơn (số nguyên)
original_total = int(input("Nhập tổng tiền hóa đơn ban đầu: "))

# Chức năng 2: tính số tiền giảm giá
if original_total >= discount_threshold:
    discount_amount = original_total * discount_percent // 100
else:
    discount_amount = 0

# Chức năng 3: tính số tiền thực tế khách phải trả
final_total = original_total - discount_amount

print("--- HÓA ĐƠN THANH TOÁN RIKKEI STORE ---")
print(f"Số tiền được giảm giá: {discount_amount} VND")
print(f"Tổng tiền khách phải trả: {final_total} VND")
