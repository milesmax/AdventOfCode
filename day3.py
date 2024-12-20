import re
test_string = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
myinput_string = ''


f=open('myinput', "r")

myinput = []
for line in f:
    myinput.append(line)

myinput_string = str(myinput)



first_index = test_string.find('mul(')
print(first_index)

# define the pattern for regex
pattern = 'mul\((-?\d+),\s*(-?\d+)\)'

result = re.findall(pattern, myinput_string)
print(result)


sum = 0
for item in result:
    print(f"{item[0]}, {item[1]}")
    mul_result = int(item[0]) * int(item[1])
    sum += mul_result


print(sum)