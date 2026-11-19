"""[BTTH] 4. Vòng quay may mắn trúng thưởng cho khách VIP - Rikkei Store."""

secret_number = 79   # Mã số bí ẩn cố định
max_attempts = 5     # Quy tắc 1: tối đa 5 lượt đoán
is_winner = False    # cờ ghi nhận khách đã đoán đúng hay chưa

for attempt in range(1, max_attempts + 1):
    guess = int(input(f"Lượt đoán {attempt} - Nhập số của bạn: "))

    if guess == secret_number:
        is_winner = True
        break   # Quy tắc 3: đoán đúng -> kết thúc ngay, không dùng hết lượt
    elif guess < secret_number:
        print("=> Gợi ý: Số của bạn nhỏ hơn mã số may mắn!")   # Quy tắc 2
    else:
        print("=> Gợi ý: Số của bạn lớn hơn mã số may mắn!")   # Quy tắc 2

# Quy tắc 4: thông báo kết quả dựa vào cờ is_winner
if is_winner:
    print("=> Chúc mừng! Bạn đã đoán chính xác mã số may mắn!")
else:
    print(f"=> Rất tiếc! Bạn đã hết {max_attempts} lượt đoán. Mã số may mắn là {secret_number}.")
    print("=> Chúc bạn may mắn lần sau!")

print("--- TRÒ CHƠI KẾT THÚC ---")
