# -*- coding: utf-8 -*-
class Solution:
    def decodeString(self, s: str) -> str:
        s = list(s)
        struct_stack = []
        alpha_stack = []
        num_stack = []
        ans = ""
        while s:
            tmp = s.pop(0)
            if tmp == "[":
                struct_stack.append(tmp)
                alpha_stack.append("")
            elif tmp.isdigit():
                if num_stack and len(num_stack) > len(struct_stack):
                    num_stack[-1] += tmp
                else:
                    num_stack.append(tmp)
            elif tmp.isalpha():
                if struct_stack:
                    alpha_stack[-1] += tmp
                else:
                    ans += tmp
            else:
                struct_stack.pop(-1)
                res = alpha_stack.pop(-1)
                res *= int(num_stack.pop(-1))
                if struct_stack:
                    if alpha_stack:
                        alpha_stack[-1] += res
                    else:
                        alpha_stack.append(res)
                else:
                    ans += res
        return ans