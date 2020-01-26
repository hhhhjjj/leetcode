# -*- coding: utf-8 -*-
class Solution:
    def filterRestaurants(self, restaurants, veganFriendly, maxPrice, maxDistance):
        length = len(restaurants)
        if length == 0:
            return []
        res = []
        if veganFriendly == 1:
            for i in range(length):
                if restaurants[i][2] != 1:
                    restaurants[i][2] = 2
        for i in range(length):
            if restaurants[i][3] > maxPrice:
                restaurants[i][2] = 2
        rating_dict = {}
        for i in range(length):
            if restaurants[i][4] <= maxDistance and restaurants[i][2] != 2:
                rating_dict[restaurants[i][0]] = restaurants[i][1]
        print(rating_dict)
        for i in sorted(rating_dict, key=rating_dict.__getitem__,reverse=True):
            res.append(i)
        return res


print(Solution().filterRestaurants([[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]],0,50,10))
