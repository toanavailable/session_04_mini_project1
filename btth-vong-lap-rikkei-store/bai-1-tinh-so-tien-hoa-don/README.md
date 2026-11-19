# Bài 1 - [BTTH] Tính số tiền hóa đơn cho khách hàng

## Đề bài

Rikkei Store áp dụng chính sách giảm giá tại quầy thu ngân để tri ân khách hàng thân thiết. Chi nhánh mới cần một module Console bằng Python: nhân viên thu ngân **nhập số tiền**, máy **tự động tính số tiền giảm giá** và **số tiền cuối cùng khách phải trả**.

- **Chức năng 1:** Nhập tổng số tiền ban đầu của hóa đơn (số nguyên).
- **Chức năng 2:** Tính số tiền giảm giá:
  - Hóa đơn từ **500,000 VND trở lên**: giảm **10%** trên tổng số tiền.
  - Hóa đơn **dưới 500,000 VND**: không được giảm giá (giảm 0%).
- **Chức năng 3:** Tính số tiền thực tế khách phải trả (tổng tiền ban đầu trừ số tiền giảm giá) và in ra màn hình.

## Phân tích

| Dữ liệu | Biến | Kiểu |
|---|---|---|
| Tổng tiền ban đầu (input) | `original_total` | `int` |
| Số tiền giảm giá | `discount_amount` | `int` |
| Tiền khách phải trả | `final_total` | `int` |

- Điều kiện giảm giá dùng `>=` vì "từ 500,000 trở lên" **bao gồm** đúng 500,000.
- Tính 10% bằng `original_total * 10 // 100`: nhân trước, **chia lấy phần nguyên** sau, để kết quả vẫn là số nguyên (`60000` thay vì `60000.0`), đúng với output mẫu. Tiền VND không có phần lẻ.
- Ngưỡng `500000` và mức `10` được đặt thành biến ở đầu file để dễ đổi khi chính sách thay đổi.

## Lời giải

File: [`tinh_hoa_don.py`](tinh_hoa_don.py)

```python
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
```

## Kết quả

```
Nhập tổng tiền hóa đơn ban đầu: 600000
--- HÓA ĐƠN THANH TOÁN RIKKEI STORE ---
Số tiền được giảm giá: 60000 VND
Tổng tiền khách phải trả: 540000 VND
```

| Tổng tiền ban đầu | Giảm giá | Khách phải trả | Ghi chú |
|---|---|---|---|
| 600000 | 60000 | 540000 | Dữ liệu mẫu của đề |
| 500000 | 50000 | 450000 | Biên: đúng 500,000 vẫn được giảm |
| 499999 | 0 | 499999 | Dưới ngưỡng, không giảm |
