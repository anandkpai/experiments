#
# @lc app=leetcode id=482 lang=python3
#
# [482] License Key Formatting
#

# @lc code=start
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        sclean = s.replace('-','').upper()
        stub = len(sclean)%k        
        pieces = [sclean[:stub:]] if stub else []        
        for start_p in range(stub, len(sclean),k):
            pieces.append(sclean[start_p:start_p+k:])
        return '-'.join(pieces)
        
# @lc code=end

print(Solution().licenseKeyFormatting("5F3Z-2e-9-w",4))