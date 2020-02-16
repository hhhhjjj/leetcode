# -*- coding: utf-8 -*-
class Solution:
    def maxEvents(self, events: [[int]]) -> int:
        length = len(events)
        if length < 2:
            return length
