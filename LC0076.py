class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1
        
        window = {}
        have = 0
        need_count = len(need)

        result = ""
        result_len = float("inf")

        i = 0

        for j in range(len(s)):
            ch = s[j]
            window[ch] = window.get(ch, 0) + 1

            if ch in need and window[ch] == need[ch]:
                have += 1

            while have == need_count:
                window_len = j - i + 1

                if window_len < result_len:
                    result = s[i : j + 1]
                    result_len = window_len

                left_ch = s[i]
                window[left_ch] -= 1

                if left_ch in need and window[left_ch] < need[left_ch]:
                    have -= 1
                
                i += 1
            
        return result