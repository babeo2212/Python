def square_numbers(nums):
    '''
    Return a list of square numbers
    '''
    for i in nums:
        yield(i*i)

my_nums = square_numbers([1, 2, 3, 4, 5])

# # comprehensive way:
# my_nums = (x*x for x in [1, 2, 3, 4, 5])

# print ((my_nums)) # <generator object square_numbers at 0x00000240A3E44DC8>
print(next(my_nums)) # 1
for num in my_nums:
    print(num)

print(list(my_nums))