# -*- coding: utf-8 -*-
some_dict = {}
some_dict[5.5] = "Ruby"
some_dict[5.0] = "JavaScript"
some_dict[5] = "Python"
print(some_dict[5.5],some_dict[5.0],some_dict[5])
# 这时候5和5.0打印出来都是python，这就是哈希冲突
# 对于字典来说值相同，所以5会覆盖掉5.0
# 拉链法就是用链表存取发生冲突的关键字
# 开放定址法就是再寻址，直到找到个为空的地址为止
# 再散列法就是每次冲突都重新散列