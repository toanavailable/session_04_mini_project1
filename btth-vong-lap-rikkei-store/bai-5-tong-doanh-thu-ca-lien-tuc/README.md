# Bài 5 - [BTTH] Hệ thống tính toán tổng doanh thu ca liên tục

## Đề bài

Đây là module cuối ngày của Rikkei Store: kiểm toán tổng kết doanh thu trước khi đóng cửa. Lượng khách mỗi ngày khác nhau và **không thể biết trước**, nên phần mềm không thể đặt số lượt nhập cố định. Thu ngân phải nhập dữ liệu **liên tục cho đến khi không còn hóa đơn nào** thì mới dừng và xuất báo cáo.

- **Quy tắc 1 (Luồng nhập linh hoạt):** nhập giá trị hóa đơn (số nguyên) của từng khách liên tục. Sau mỗi hóa đơn, hỏi thu ngân muốn **tiếp tục** hay **dừng** để xuất báo cáo (gõ `K` hoặc `k`). Lặp lại cho đến khi chủ động chọn dừng.
- **Quy tắc 2 (Xử lý thời gian thực):** ngay trong lúc nhập, đồng thời cộng dồn tổng doanh thu, đếm tổng số hóa đơn, và đếm riêng số **"hóa đơn lớn"** (từ 1,000,000 VND trở lên).
- **Quy tắc 3 (Báo cáo tổng kết):** khi dừng, in ngay báo cáo gồm Tổng doanh thu, Tổng số hóa đơn, và **Tỷ lệ phần trăm (%)** hóa đơn lớn trên tổng số hóa đơn.
- **Quy tắc 4 (An toàn hệ thống):** nếu quản lý vừa mở phần mềm đã chọn dừng ngay (**chưa có hóa đơn nào**), hệ thống vẫn hoạt động an toàn, **không sập** hay phát sinh lỗi tính toán.

## Phân tích

| Dữ liệu | Biến | Kiểu | Vai trò |
|---|---|---|---|
| Giá trị hóa đơn (input) | `value_text` → `invoice_value` | `str` → `int` | Kiểm tra rồi mới ép kiểu |
| Tổng doanh thu | `total_revenue` | `int` | Biến tích lũy |
| Tổng số hóa đơn | `invoice_count` | `int` | Biến đếm |
| Số hóa đơn lớn | `large_invoice_count` | `int` | Biến đếm có điều kiện |
| Tỷ lệ hóa đơn lớn | `large_invoice_ratio` | `float` | Tính sau vòng lặp |
| Lựa chọn tiếp tục | `answer` | `str` (`C` / `K`) | Điều khiển vòng lặp |

Thiết kế:
- **Không biết trước số lần lặp** nên dùng `while True` + `break` (dừng khi thu ngân chọn `K`).
- Ba biến tích lũy/đếm **khởi tạo bằng 0 trước vòng lặp** và được cập nhật **ngay sau mỗi hóa đơn** (Quy tắc 2).
- **Quy tắc 4: tránh lỗi chia cho 0.** Tỷ lệ = `large_invoice_count / invoice_count * 100`. Nếu `invoice_count = 0`, Python báo `ZeroDivisionError` và chương trình sập. Vì vậy phải kiểm tra `if invoice_count > 0` trước khi chia, ngược lại gán tỷ lệ = `0.0`.
- Để quản lý **dừng được ngay khi chưa có hóa đơn nào**, ô nhập giá trị hóa đơn cũng chấp nhận `K`.
- **Chống nhập sai:** giá trị hóa đơn không phải số nguyên dương (`abc`, `-5`, `0`) thì báo lỗi và hỏi lại (`continue`). Câu hỏi C/K gõ sai thì hỏi lại. `.upper()` để chấp nhận cả `c`/`k` viết thường.

### Pseudocode

```
total_revenue ← 0; invoice_count ← 0; large_invoice_count ← 0
LẶP MÃI:
    NHẬP value_text ("Khách hàng <invoice_count + 1> - Nhập giá trị hóa đơn")
    NẾU value_text là "K" THÌ THOÁT
    NẾU value_text không phải số nguyên > 0 THÌ báo lỗi, QUAY LẠI đầu vòng lặp
    invoice_value ← int(value_text)
    total_revenue += invoice_value; invoice_count += 1
    NẾU invoice_value >= 1,000,000 THÌ large_invoice_count += 1
    HỎI "Có muốn nhập tiếp không? (C/K)" (hỏi lại đến khi là C hoặc K)
    NẾU "K" THÌ THOÁT
NẾU invoice_count > 0 THÌ ratio ← large_invoice_count / invoice_count * 100
NGƯỢC LẠI ratio ← 0.0
IN báo cáo
```

## Lời giải

File: [`doanh_thu_ca_lien_tuc.py`](doanh_thu_ca_lien_tuc.py)

```python
large_invoice_limit = 1000000   # hóa đơn lớn: từ 1,000,000 VND trở lên

# Biến tích lũy - khởi tạo TRƯỚC vòng lặp
total_revenue = 0
invoice_count = 0
large_invoice_count = 0

# Quy tắc 1: luồng nhập linh hoạt - lặp cho đến khi thu ngân chọn dừng
while True:
    value_text = input(f"Khách hàng {invoice_count + 1} - Nhập giá trị hóa đơn: ").strip()

    # Cho phép gõ K ngay tại đây để dừng (kể cả khi chưa nhập hóa đơn nào)
    if value_text.upper() == "K":
        break

    # Chặn dữ liệu không phải số nguyên dương -> hỏi lại, không crash
    if not value_text.isdigit() or int(value_text) == 0:
        print("[!] Giá trị hóa đơn phải là số nguyên lớn hơn 0. Vui lòng nhập lại (hoặc gõ K để dừng).")
        continue

    invoice_value = int(value_text)

    # Quy tắc 2: xử lý dữ liệu thời gian thực
    total_revenue += invoice_value
    invoice_count += 1
    if invoice_value >= large_invoice_limit:
        large_invoice_count += 1

    # Hỏi tiếp tục hay dừng (chỉ chấp nhận C hoặc K)
    answer = input("Có muốn nhập tiếp không? (C/K): ").strip().upper()
    while answer != "C" and answer != "K":
        answer = input("Vui lòng chỉ gõ C (tiếp tục) hoặc K (dừng): ").strip().upper()
    print()

    if answer == "K":
        break

# Quy tắc 4: an toàn hệ thống - tránh chia cho 0 khi chưa có hóa đơn nào
if invoice_count > 0:
    large_invoice_ratio = large_invoice_count / invoice_count * 100
else:
    large_invoice_ratio = 0.0

# Quy tắc 3: báo cáo tổng kết
print("--- BÁO CÁO DOANH THU CUỐI NGÀY RIKKEI STORE ---")
if invoice_count == 0:
    print("Chưa có hóa đơn nào được nhập trong ca.")
print(f"Tổng số hóa đơn đã xử lý: {invoice_count} hóa đơn.")
print(f"Tổng doanh thu ngày hôm nay: {total_revenue:,} VND.")
print(f"Số hóa đơn lớn (>= {large_invoice_limit:,} VND): {large_invoice_count} hóa đơn.")
print(f"Tỷ lệ hóa đơn lớn đạt: {large_invoice_ratio:.1f}% trên tổng số đơn hàng.")
```

## Kết quả

**Dữ liệu mẫu của đề:**

```
Khách hàng 1 - Nhập giá trị hóa đơn: 500000
Có muốn nhập tiếp không? (C/K): C

Khách hàng 2 - Nhập giá trị hóa đơn: 1200000
Có muốn nhập tiếp không? (C/K): K

--- BÁO CÁO DOANH THU CUỐI NGÀY RIKKEI STORE ---
Tổng số hóa đơn đã xử lý: 2 hóa đơn.
Tổng doanh thu ngày hôm nay: 1,700,000 VND.
Số hóa đơn lớn (>= 1,000,000 VND): 1 hóa đơn.
Tỷ lệ hóa đơn lớn đạt: 50.0% trên tổng số đơn hàng.
```

**Quy tắc 4: dừng ngay khi chưa có hóa đơn nào** (không bị `ZeroDivisionError`):

```
Khách hàng 1 - Nhập giá trị hóa đơn: K
--- BÁO CÁO DOANH THU CUỐI NGÀY RIKKEI STORE ---
Chưa có hóa đơn nào được nhập trong ca.
Tổng số hóa đơn đã xử lý: 0 hóa đơn.
Tổng doanh thu ngày hôm nay: 0 VND.
Số hóa đơn lớn (>= 1,000,000 VND): 0 hóa đơn.
Tỷ lệ hóa đơn lớn đạt: 0.0% trên tổng số đơn hàng.
```

**Nhập sai dữ liệu** (`abc`, `-5`, câu trả lời `x`) → báo lỗi và hỏi lại, chương trình không sập:

```
Khách hàng 1 - Nhập giá trị hóa đơn: abc
[!] Giá trị hóa đơn phải là số nguyên lớn hơn 0. Vui lòng nhập lại (hoặc gõ K để dừng).
Khách hàng 1 - Nhập giá trị hóa đơn: -5
[!] Giá trị hóa đơn phải là số nguyên lớn hơn 0. Vui lòng nhập lại (hoặc gõ K để dừng).
Khách hàng 1 - Nhập giá trị hóa đơn: 2000000
Có muốn nhập tiếp không? (C/K): x
Vui lòng chỉ gõ C (tiếp tục) hoặc K (dừng): c

Khách hàng 2 - Nhập giá trị hóa đơn: 300000
Có muốn nhập tiếp không? (C/K): k

--- BÁO CÁO DOANH THU CUỐI NGÀY RIKKEI STORE ---
Tổng số hóa đơn đã xử lý: 2 hóa đơn.
Tổng doanh thu ngày hôm nay: 2,300,000 VND.
Số hóa đơn lớn (>= 1,000,000 VND): 1 hóa đơn.
Tỷ lệ hóa đơn lớn đạt: 50.0% trên tổng số đơn hàng.
```
