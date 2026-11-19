"""[BTTH] 5. Hệ thống tính toán tổng doanh thu ca liên tục - Rikkei Store."""

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
