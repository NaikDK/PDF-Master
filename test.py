# def romanToInt(s):
#     """
#     :type s: str
#     :rtype: int
#     """
#     d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
#     c=0
#     i = 0
#     ls = len(s)
#     while i<ls:
#         if i == ls-1:
#             c = c + d[s[i]]
#             return c
#         else:
#             if s[i] == 'I' and s[i+1] in 'VX':
#                 c = c + d[s[i+1]] - 1
#                 i = i+2
#                 continue
#             elif s[i] == 'X' and s[i+1] in 'LC':
#                 c = c + d[s[i+1]] - 10
#                 i = i+2
#                 continue
#             elif s[i] == 'C' and s[i+1] in 'DM':
#                 c = c + d[s[i+1]] - 100
#                 i = i+2
#                 continue
#             else:
#                 c = c + d[s[i]]
#                 i = i+1
#     return c
    
# print(romanToInt("III"))

import pandas as pd
data = pd.read_csv("otnunit_aat_datacenter_attributes_8a94_cefd_f8a3.csv")

df = data.dropna(axis=1, how='all')
df.to_csv("new.csv")