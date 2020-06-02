def solution(n):
    roman_numerals = {1000:'M',
                      900: 'CM',
                      500: 'D',
                      400: 'CD',
                      100: 'C',
                      90: 'XC',
                      50: 'L',
                      40: 'XL',
                      10: 'X',
                      9: 'IX',
                      5: 'V',
                      4: 'IV',
                      1: 'I'
    }
    roman_string = ''
    for key in sorted(roman_numerals.keys(),reverse=True):
        while n >= key:
            roman_string += roman_numerals[key]
            n -= key
    return roman_string

print(solution(1989))


# my attempt
# def solution(n):
#     """
#     Purpose: Convert an integer into its roman numeral equivalent
#     pre: n - must a positive integer
#     :return: Roman Numeral string
#     """
#     # base case
#     if n == 0:
#         return ""
#
#     # general cases with 1000
#     elif n >= 1000:
#         return "M" + solution(n-1000)
#     # special cases with post 1000
#     elif n == 1001:
#         return "MI" + solution(n - 1001)
#     elif n == 1005:
#         return "MV" + solution(n - 1005)
#     elif n == 1010:
#         return "MX" + solution(n - 1010)
#     elif n == 1050:
#         return "ML" + solution(n - 1050)
#     elif n == 1100:
#         return "MC" + solution(n - 1100)
#     # special cases with pre 1000
#     elif n == 999:
#         return "IM" + solution(n-999)
#     elif n == 995:
#         return "VM" + solution(n-995)
#     elif n == 990:
#         return "XM" + solution(n-990)
#     elif n == 950:
#         return "LM" + solution(n-950)
#     elif n == 900:
#         return "CM" + solution(n-900)
#
#     # general cases with 500-1000
#     elif n in range(500, 1000):
#         return "D" + solution(n-500)
#     # special cases with post 500
#     elif n == 501:
#         return "DI" + solution(n-501)
#     elif n == 505:
#         return "DV" + solution(n-505)
#     elif n == 510:
#         return "DX" + solution(n-510)
#     elif n == 550:
#         return "DL" + solution(n-550)
#     elif n == 600:
#         return "DC" + solution(n-600)
#     # special cases with pre 500
#     elif n == 499:
#         return "ID" + solution(n-499)
#     elif n == 495:
#         return "VD" + solution(n-495)
#     elif n == 490:
#         return "XD" + solution(n-490)
#     elif n == 450:
#         return "LD" + solution(n-450)
#     elif n == 400:
#         return "CD" + solution(n-400)
#
#     # general case for 100-500
#     elif n in range(100, 500):
#         return "C" + solution(n-100)
#     # special cases with post 100
#     elif n == 101:
#         return "CI" + solution(n-101)
#     elif n == 105:
#         return "CV" + solution(n-105)
#     elif n == 110:
#         return "CX" + solution(n-110)
#     # special cases with pre 100
#     elif n == 99:
#         return "IC" + solution(n-99)
#     elif n == 95:
#         return "VC" + solution(n-95)
#     elif n == 90:
#         return "XC" + solution(n-90)
#
#     # general case for 50-100
#     elif n in range(50, 100):
#         return "L" + solution(n-50)
#     # special cases with post 50
#     elif n == 51:
#         return "LI" + solution(n-51)
#     elif n == 55:
#         return "LV" + solution(n-55)
#     elif n == 60:
#         return "LX" + solution(n-60)
#     # special cases with pre 50
#     elif n == 49:
#         return "IL" + solution(n-49)
#     elif n == 45:
#         return "VL" + solution(n-45)
#     elif n == 40:
#         return "XC" + solution(n-95)
#
#     # general case for 10-50
#     elif n in range(10, 50):
#         return "X" + solution(n-10)
#     # special case with post 10
#     elif n == 11:
#         return "XI" + solution(n-11)
#     # special case with pre 10
#     elif n == 9:
#         return "IX" + solution(n-9)
#
#     # general case for 5-10
#     elif n in range(5, 10):
#         return "V" + solution(n-5)
#     # special case with pre 5
#     elif n == 4:
#         return "IV" + solution(n-4)
#
#     # general case for 1-5
#     elif n in range(1, 5):
#         return "I" + solution(n - 1)
#
# print(solution(1989))
