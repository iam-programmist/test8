# КТУ
# def test(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a
# a = int(input())
# b = int(input())
# print(test(a,b))

# Ракамхои рими
# def test(a):
#     res = {
#         1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 
#         100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 
#         10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
#     }
#     cnt = ""    
#     for i in res:
#         while a >= i:
#             cnt += res[i]
#             a -= i
#     return cnt
# a = int(input())
# print(test(a))