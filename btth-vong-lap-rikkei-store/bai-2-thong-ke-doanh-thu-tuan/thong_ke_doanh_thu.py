"""[BTTH] 2. Thống kê doanh thu cố định trong tuần - Rikkei Store."""

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
