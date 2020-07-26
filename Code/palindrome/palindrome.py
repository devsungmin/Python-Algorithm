import collections
from typing import Deque

# isSlicing에서 정규 표현식을 사용하기 위해 선언
import re

class Solution:
    # =======List형식======
    def isList(self, s: str) -> bool:
        strs = []
        for char in s:
            # isalnum()은 영문자, 숫자 여부를 판별하는 함수
            if char.isalnum():
                # 대소문자를 구분하지 않기 때문에 lower()함수를 사용하여 소문자로 변환
                strs.append(char.lower())

        # 팰린드롬 여부 판별
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False

        return True

    # =======Deque 형식======
    def isDeque(self, s: str) -> bool:
        strs: Deque=collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs)>1:
            if strs.popleft() != strs.pop():
                return False
        return True

    # =======slicing형식======
    def isSlicing(self, s: str) -> bool:
        s=s.lower()
        # 정규식 선언 -> 영어 한글 숫자
        s = re.sub('[^a-z0-9ㄱ-ㅎ|ㅏ-ㅣ|가-힣]', '', s)

        return s == s[::-1]
        



def main():
    palindrome = Solution()

    print("======List형식으로 구현======")
    print(palindrome.isList("기러기"))
    print(palindrome.isList("참새"))
    print(palindrome.isList("race car"))

    print("======Deque형식으로 구현======")
    print(palindrome.isDeque("기러기"))
    print(palindrome.isDeque("참새"))
    print(palindrome.isDeque("race car"))


    print("======slicing형식으로 구현======")
    print(palindrome.isSlicing("기러기"))
    print(palindrome.isSlicing("참새"))
    print(palindrome.isSlicing("race car"))

if __name__ == '__main__':
    main()