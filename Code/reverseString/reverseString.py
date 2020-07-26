from typing import List

class Solution:
    def twoPoint(self, s: List[str]):
        left, right = 0, len(s) -1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s

    def pyFunction(self, s:List[str]):
        s.reverse()
        return s

def main():
    reverseString = Solution()

    print("======twoPoint을 사용한 방법========")
    print(reverseString.twoPoint(["h","e","l","l","o"]))

    print("======reverse 함수를 사용한 방법========")
    print(reverseString.pyFunction(["h","e","l","l","o"]))

if __name__ == '__main__':
    main()