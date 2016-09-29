#!/usr/bin/python
import difflib

text1 = """text1:
This module provides classes and functions for comparing sequences.
including HTML and context and unified diffs.
difflib document v7.4
add string
"""

text1_lines = text1.splitlines() #对于以上格式的字符串，需要以行进行分割

text2 = """text2:
This module provides classes and functions for Comparing sequences.
including HTML and context and unified diffs.
difflib document v7.5"""

text2_lines = text2.splitlines()

d = difflib.Differ()  #创建Differ对象
diff = d.compare(text1_lines, text2_lines)  #采用compare方法对字符串进行比较
print '\n'.join(list(diff)) #在每个列表元素后加上换行符进行格式化输出


输出示例：
shiyanlou:pythontest/ $ python diFF.py                                                                                    [16:24:35]
- text1:
?     ^

+ text2:
?     ^

- This module provides classes and functions for comparing sequences.
?                                                ^

+ This module provides classes and functions for Comparing sequences.
?                                                ^

  including HTML and context and unified diffs.
- difflib document v7.4
?                     ^

+ difflib document v7.5
?                     ^

- add string

符号含义说明
'-'     包含在第一个序列行中，但不包含在第二行序列中
'+'     包含在第二个序列行中，但不包含在第一行序列中
''      两个序列行一致
'?'     标志两个序列行存在增量差异
'^'     标志两个序列行存在的差异字符
