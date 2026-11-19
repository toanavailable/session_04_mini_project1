"""[BTTH] 3. Tìm hóa đơn cao nhất trong ca làm việc - Rikkei Store."""

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
