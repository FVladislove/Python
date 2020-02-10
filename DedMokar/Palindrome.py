def is_palindrome_num(num):
    if num == 0:
        return True
    elif num < 0:
        i = num * (-1)
    else:
        i = num
    num_list = []
    while i / 10 != 0:
        num_list.append(i % 10)
        i = i // 10
    is_palindrome = True
    l_idx = 0
    r_idx = len(num_list) - 1
    while r_idx > l_idx:
        if num_list[l_idx] != num_list[r_idx]:
            is_palindrome = False
            break
        r_idx -= 1
        l_idx += 1
    return is_palindrome


print(is_palindrome_num(0))
max_palindrome = -1
s_cycle = False
for i in range(100, 1000):
    for j in range(100, 1000):
        mult = i * j
        is_pal = is_palindrome_num(mult)
        if is_pal and mult > max_palindrome:
            max_palindrome = mult

print(max_palindrome)