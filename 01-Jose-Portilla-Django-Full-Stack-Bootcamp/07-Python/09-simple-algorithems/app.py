def arrayCheck(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3:
            return  True
    return False


print(arrayCheck([1, 1, 2, 3, 1]))
print(arrayCheck([1, 1, 2, 4, 1]))
print(arrayCheck([1, 1, 2, 1, 2, 3]))


def string_bits(string):
    # return string[::2]
    result = ''
    for i in range(len(string)):
        if i % 2 == 0:
            result += string[i]
    return result


print(string_bits('Hello'))
print(string_bits('Hi'))
print(string_bits('Heeololeo'))


def end_other(a, b):
    a = a.lower()
    b = b.lower()
    return a[-(len(b)):] == b or b[-(len(a)):] == a


print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('abc', 'abXabc'))


def double_char(string):
    # return ''.join([s + s for s in list(string)])
    result = ''
    for char in string:
        result += char * 2
    return result


print(double_char('The'))
print(double_char('AAbb'))
print(double_char('Hi-There'))


def fix_teen(n):
    if n in [13, 14, 17, 18, 19]:
        return 0
    return n


def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)


print(no_teen_sum(1, 2, 3))
print(no_teen_sum(2, 13, 1))
print(no_teen_sum(2, 1, 14))


def count_evens(nums):
    # return len([i for i in nums if i % 2 == 0])
    result = 0
    for i in nums:
        if i % 2 == 0:
            result += 1
    return result


print(count_evens([2, 1, 2, 3, 4]))
print(count_evens([2, 2, 0]))
print(count_evens([1, 3, 5]))
