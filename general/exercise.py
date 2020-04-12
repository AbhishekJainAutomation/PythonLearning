default = 'XX'
h_line_count = 0
for v_len in range(5):
    if int(v_len % 2) == 0 and h_line_count < 2:
        print(default * 3)
        h_line_count += 1
    else:
        print(default)
        break

number = [3,400,5,2,4,90]
largest_number = int(number[0])
for num in number:
    if(num > largest_number):
        largest_number = num
print(largest_number)