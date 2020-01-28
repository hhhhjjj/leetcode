# -*- coding: utf-8 -*-
class Solution:
    def filterRestaurants(self, restaurants, veganFriendly, maxPrice, maxDistance):
        length = len(restaurants)
        if length == 0:
            return []
        # 其实不用那么多for循环
        rating_list = []
        if veganFriendly == 1:
            for i in range(length):
                if restaurants[i][2] == 1 and restaurants[i][3] <= maxPrice and restaurants[i][4] <= maxDistance:
                    # 三个一起判断比三个分开判断速度还慢。。。
                    rating_list.append(restaurants[i])
        else:
            for i in range(length):
                if restaurants[i][3] <= maxPrice and restaurants[i][4] <= maxDistance:
                    rating_list.append(restaurants[i])
        # rating相同按照id大小排序
        res = []
        # 这个sorted可以这样子用，先按照rating排序，再按照id来排序就行了
        for i in sorted(rating_list, key=lambda x: [x[1], x[0]], reverse=True):
            res.append(i[0])
        return res


print(Solution().filterRestaurants([[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]],0,50,10))