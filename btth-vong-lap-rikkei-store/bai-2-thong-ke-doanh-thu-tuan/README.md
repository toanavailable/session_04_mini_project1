# Bài 2 - [BTTH] Thống kê doanh thu cố định trong tuần

## Đề bài

Quản lý Rikkei Store cần công cụ thống kê hiệu quả kinh doanh theo chu kỳ **một tuần (cố định 7 ngày, Thứ 2 → Chủ Nhật)** để báo cáo ban giám đốc, thay vì cộng tay doanh thu từng ngày. Chương trình nhận doanh thu 7 ngày, tính **tổng doanh thu**, **doanh thu trung bình** và **đếm số ngày đạt mục tiêu** doanh thu cao (từ 5,000,000 VND trở lên).

- **Chức năng 1:** Dùng vòng lặp chạy **đúng 7 lần** để nhập doanh thu từng ngày (in rõ "Ngày 1" đến "Ngày 7").
- **Chức năng 2:** Dùng các **biến tích lũy** để tính tổng doanh thu cả tuần và doanh thu trung bình mỗi ngày.
- **Chức năng 3:** Đếm số ngày có doanh thu đạt từ 5,000,000 VND trở lên.

## Phân tích

| Dữ liệu | Biến | Kiểu | Vai trò |
|---|---|---|---|
| Doanh thu từng ngày (input) | `daily_revenue` | `int` | Giá trị của lượt lặp hiện tại |
| Tổng doanh thu | `total_revenue` | `int` | **Biến tích lũy** (cộng dồn) |
| Số ngày đạt mục tiêu | `target_days` | `int` | **Biến đếm** |
| Doanh thu trung bình | `average_revenue` | `float` | Tính **sau** vòng lặp |

Các điểm mấu chốt:
- **Biết trước đúng 7 lần** nên dùng `for day in range(1, 8)`. Bắt đầu từ 1 để in đúng "Ngày 1" → "Ngày 7".
- Biến tích lũy `total_revenue` và biến đếm `target_days` phải **khởi tạo bằng 0 TRƯỚC vòng lặp**. Nếu đặt bên trong, chúng bị reset về 0 mỗi lượt, giống lỗi ở bài "Sự cố tính toán quỹ lương".
- Trung bình = tổng / 7, tính **một lần sau khi** vòng lặp kết thúc. In bằng `:.0f` để làm tròn, không hiện phần thập phân.

## Lời giải

File: [`thong_ke_doanh_thu.py`](thong_ke_doanh_thu.py)

```python
days_in_week = 7
target_revenue = 5000000   # mục tiêu doanh thu cao: từ 5,000,000 VND trở lên

# Biến tích lũy: khởi tạo TRƯỚC vòng lặp
total_revenue = 0
target_days = 0

# Chức năng 1: lặp đúng 7 lần, nhập doanh thu từng ngày
for day in range(1, days_in_week + 1):
    daily_revenue = int(input(f"Nhập doanh thu Ngày {day}: "))

    # Chức năng 2: cộng dồn tổng doanh thu
    total_revenue += daily_revenue

    # Chức năng 3: đếm số ngày đạt mục tiêu
    if daily_revenue >= target_revenue:
        target_days += 1

# Tính trung bình SAU vòng lặp (khi đã có đủ 7 ngày)
average_revenue = total_revenue / days_in_week

print("--- BÁO CÁO DOANH THU TUẦN RIKKEI STORE ---")
print(f"Tổng doanh thu cả tuần: {total_revenue} VND")
print(f"Doanh thu trung bình mỗi ngày: {average_revenue:.0f} VND")
print(f"Số ngày đạt doanh thu mục tiêu (>= {target_revenue:,} VND): {target_days} ngày")
```

## Kết quả

```
Nhập doanh thu Ngày 1: 4000000
Nhập doanh thu Ngày 2: 6000000
Nhập doanh thu Ngày 3: 4900000
Nhập doanh thu Ngày 4: 4900000
Nhập doanh thu Ngày 5: 4900000
Nhập doanh thu Ngày 6: 4800000
Nhập doanh thu Ngày 7: 5500000
--- BÁO CÁO DOANH THU TUẦN RIKKEI STORE ---
Tổng doanh thu cả tuần: 35000000 VND
Doanh thu trung bình mỗi ngày: 5000000 VND
Số ngày đạt doanh thu mục tiêu (>= 5,000,000 VND): 2 ngày
```

Kết quả khớp output mẫu của đề (tổng 35,000,000; trung bình 5,000,000; 2 ngày đạt mục tiêu là Ngày 2 và Ngày 7).
