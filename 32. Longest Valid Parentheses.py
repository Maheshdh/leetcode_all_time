def longestValidParentheses(self, s: str) -> int:
        left_count, right_count, max_length = 0,0,0

        # count left count and right count, if they are equal, maintain max length found
        # if right count exceeds left count, reset counts to 0
        for i in range(len(s)):
            if(s[i] == '('):
                left_count += 1
            else:
                right_count += 1
            if left_count == right_count:
                max_length = max(max_length, 2*right_count)
            if right_count > left_count:
                right_count = 0
                left_count = 0
        left_count, right_count = 0,0

        # iterate in reverse to handle cases like (()
        for i in range(len(s)-1,-1,-1):
            if s[i] == '(':
                left_count += 1
            else:
                right_count += 1
            if left_count == right_count:
                max_length = max(max_length, 2 * left_count)
            if left_count > right_count:
                left_count = 0
                right_count = 0
        return max_length
