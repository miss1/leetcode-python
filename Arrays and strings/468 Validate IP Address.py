class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        arr1 = queryIP.split('.')
        if len(arr1) == 4:
            for s in arr1:
                if not s.isdigit() or (len(s) > 1 and s[0] == '0') or int(s) > 255:
                    return 'Neither'
            return 'IPv4'
        arr2 = queryIP.split(':')
        pattern = r'^[0-9a-fA-F]+$'
        if len(arr2) == 8:
            for s in arr2:
                if len(s) < 1 or len(s) > 4 or not re.match(pattern, s):
                    return 'Neither'
            return 'IPv6'
        return 'Neither'
