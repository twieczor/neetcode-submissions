class Solution:
    def isPalindrome(self, s: str) -> bool:

        n = len(s)

        if n == 0:
            return False
        elif n == 1:
            return True

        def is_digit(c):
            return (c >= '0' and c <= '9')

        def is_letter(c):
            return (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z')

        def is_valid(c):
            return is_letter(c) or is_digit(c)
                

        def is_equal(a, b, case_diff):

            if is_digit(a) and is_digit(b):
                return a == b
            elif is_letter(a) and is_letter(b):
                diff = ord(a) - ord(b)

                if diff == 0 or diff == case_diff or diff == -1 * case_diff:
                    return True
                else: 
                    return False
            else:
                return False


        l,r = 0, n-1

        diff = ord('A') - ord('a')

        while l < r:
            if is_equal(s[l], s[r], diff):
                l += 1
                r -= 1
            elif not is_valid(s[l]):
                l += 1
            elif not is_valid(s[r]):
                r -= 1
            else:
                return False
        return True
        


        