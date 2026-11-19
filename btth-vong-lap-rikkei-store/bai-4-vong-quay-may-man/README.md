# Bài 4 - [BTTH] Vòng quay may mắn trúng thưởng cho khách VIP

## Đề bài

Trong ngày hội tri ân, khách hàng có hóa đơn VIP được chơi minigame **"Đoán số may mắn"** tại quầy thu ngân. Hệ thống có một **"Mã số bí ẩn" cố định (VD: 79)**; khách đoán số và hệ thống đưa ra phản hồi để điều hướng người chơi.

- **Quy tắc 1 (Giới hạn lượt chơi):** mỗi khách có **tối đa 5 lần** đoán.
- **Quy tắc 2 (Gợi ý thông minh):** đoán sai thì báo số vừa nhập **lớn hơn** hay **nhỏ hơn** mã số may mắn.
- **Quy tắc 3 (Điểm dừng trò chơi):** kết thúc **lập tức** khi khách đoán đúng, **hoặc** khi đã dùng hết 5 lượt.
- **Quy tắc 4 (Thông báo kết quả):** dựa vào kết quả để chúc mừng trúng thưởng, hoặc báo hết lượt và chúc may mắn lần sau.

## Phân tích

| Dữ liệu | Biến | Kiểu |
|---|---|---|
| Mã số bí ẩn | `secret_number` | `int` (cố định = 79) |
| Số lượt tối đa | `max_attempts` | `int` (= 5) |
| Số khách đoán (input) | `guess` | `int` |
| Cờ trúng thưởng | `is_winner` | `bool` |

Thiết kế:
- Số lượt **tối đa đã biết (5)** nên dùng `for attempt in range(1, 6)`. Vòng lặp tự dừng khi hết 5 lượt, thỏa vế thứ hai của Quy tắc 3.
- Đoán đúng thì dùng **`break`** để thoát vòng lặp **ngay lập tức**, không hỏi thêm lượt nào. Đây là vế thứ nhất của Quy tắc 3.
- Vòng lặp có **hai cách kết thúc** (đúng → `break`, hoặc hết lượt), nên cần **biến cờ** `is_winner` để sau vòng lặp biết đã kết thúc theo cách nào và in thông báo phù hợp (Quy tắc 4).
- Gợi ý dùng `if - elif - else`: bằng / nhỏ hơn / lớn hơn.

## Lời giải

File: [`doan_so_may_man.py`](doan_so_may_man.py)

```python
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
```

## Kết quả

**Đoán đúng ở lượt 2** (khớp output mẫu):

```
Lượt đoán 1 - Nhập số của bạn: 50
=> Gợi ý: Số của bạn nhỏ hơn mã số may mắn!
Lượt đoán 2 - Nhập số của bạn: 79
=> Chúc mừng! Bạn đã đoán chính xác mã số may mắn!
--- TRÒ CHƠI KẾT THÚC ---
```

**Hết 5 lượt mà không đoán đúng:**

```
Lượt đoán 1 - Nhập số của bạn: 50
=> Gợi ý: Số của bạn nhỏ hơn mã số may mắn!
Lượt đoán 2 - Nhập số của bạn: 90
=> Gợi ý: Số của bạn lớn hơn mã số may mắn!
Lượt đoán 3 - Nhập số của bạn: 80
=> Gợi ý: Số của bạn lớn hơn mã số may mắn!
Lượt đoán 4 - Nhập số của bạn: 78
=> Gợi ý: Số của bạn nhỏ hơn mã số may mắn!
Lượt đoán 5 - Nhập số của bạn: 1
=> Gợi ý: Số của bạn nhỏ hơn mã số may mắn!
=> Rất tiếc! Bạn đã hết 5 lượt đoán. Mã số may mắn là 79.
=> Chúc bạn may mắn lần sau!
--- TRÒ CHƠI KẾT THÚC ---
```

**Đoán đúng ngay lượt 1:** chỉ hỏi 1 lần rồi chúc mừng và kết thúc.
