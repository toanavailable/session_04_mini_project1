# Bài 3 - [BTTH] Tìm hóa đơn cao nhất trong ca làm việc

## Đề bài

Rikkei Store khen thưởng cuối ca cho nhân viên thu ngân bán được đơn hàng có giá trị cao nhất. Số lượng hóa đơn mỗi ca **không cố định** (tùy hôm đông hay vắng khách). Vì vậy chương trình cho quản lý **nhập số lượng hóa đơn thực tế của ca trước**, sau đó nhập giá trị từng hóa đơn và tìm ra hóa đơn **cao nhất (Max)** và **thấp nhất (Min)**.

- **Chức năng 1:** Nhập tổng số lượng hóa đơn đã xuất trong ca.
- **Chức năng 2:** Lặp và nhập giá trị cho từng hóa đơn.
- **Chức năng 3:** Tìm giá trị hóa đơn lớn nhất (Max) và nhỏ nhất (Min) sau khi kết thúc việc nhập.

## Phân tích

| Dữ liệu | Biến | Kiểu |
|---|---|---|
| Số lượng hóa đơn (input) | `invoice_count` | `int` |
| Giá trị từng hóa đơn (input) | `invoice_value` | `int` |
| Hóa đơn lớn nhất / nhỏ nhất | `max_invoice` / `min_invoice` | `int` |

**Thuật toán tìm Max / Min trong lúc nhập** (không cần lưu lại toàn bộ hóa đơn):
1. Hóa đơn **đầu tiên** được lấy làm **mốc**: vừa là Max vừa là Min.
2. Từ hóa đơn thứ 2 trở đi, so sánh với mốc hiện tại:
   - Lớn hơn `max_invoice` → cập nhật Max.
   - Nhỏ hơn `min_invoice` → cập nhật Min.

Vì sao không khởi tạo `max_invoice = 0`? Cách đó vẫn đúng cho Max (tiền luôn dương), nhưng `min_invoice = 0` sẽ **sai**: không hóa đơn nào nhỏ hơn 0, nên Min luôn bằng 0. Lấy hóa đơn đầu tiên làm mốc thì đúng với mọi dữ liệu.

Số lượng hóa đơn đã biết sau khi nhập ở Chức năng 1, nên dùng `for ... in range(1, invoice_count + 1)`. Nếu nhập số lượng `<= 0` thì báo "ca không có hóa đơn". Nếu không xử lý, chương trình sẽ cố in biến `max_invoice` chưa từng được tạo và gặp lỗi `NameError`.

## Lời giải

File: [`tim_hoa_don_max_min.py`](tim_hoa_don_max_min.py)

```python
# Chức năng 1: nhập số lượng hóa đơn đã xuất trong ca
invoice_count = int(input("Nhập số lượng hóa đơn trong ca: "))

if invoice_count <= 0:
    print("--- KẾT QUẢ KIỂM TOÁN CA RIKKEI STORE ---")
    print("Ca làm việc không có hóa đơn nào.")
else:
    # Chức năng 2: lặp và nhập giá trị từng hóa đơn
    for invoice_number in range(1, invoice_count + 1):
        invoice_value = int(input(f"Nhập giá trị hóa đơn thứ {invoice_number}: "))

        # Chức năng 3: cập nhật Max / Min ngay trong lúc nhập
        if invoice_number == 1:
            # Hóa đơn đầu tiên vừa là lớn nhất vừa là nhỏ nhất (mốc so sánh ban đầu)
            max_invoice = invoice_value
            min_invoice = invoice_value
        else:
            if invoice_value > max_invoice:
                max_invoice = invoice_value
            if invoice_value < min_invoice:
                min_invoice = invoice_value

    print("--- KẾT QUẢ KIỂM TOÁN CA RIKKEI STORE ---")
    print(f"Hóa đơn có giá trị cao nhất: {max_invoice} VND")
    print(f"Hóa đơn có giá trị thấp nhất: {min_invoice} VND")
```

## Kết quả

```
Nhập số lượng hóa đơn trong ca: 3
Nhập giá trị hóa đơn thứ 1: 150000
Nhập giá trị hóa đơn thứ 2: 1200000
Nhập giá trị hóa đơn thứ 3: 500000
--- KẾT QUẢ KIỂM TOÁN CA RIKKEI STORE ---
Hóa đơn có giá trị cao nhất: 1200000 VND
Hóa đơn có giá trị thấp nhất: 150000 VND
```

| Số hóa đơn | Giá trị | Max | Min |
|---|---|---|---|
| 3 | 150000, 1200000, 500000 | 1200000 | 150000 (dữ liệu mẫu) |
| 1 | 70000 | 70000 | 70000 (chỉ 1 hóa đơn) |
| 0 | | `Ca làm việc không có hóa đơn nào.` | |
