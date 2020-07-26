class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        # 팰린드롬 여부 판별
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False

        return True


def main():
    palindrome = Solution()
    print(palindrome.isPalindrome("기러기"))
    print(palindrome.isPalindrome("참새"))
    print(palindrome.isPalindrome("race car"))


if __name__ == '__main__':
    main()