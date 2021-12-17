# -*- coding: utf-8 -*-
class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_quality()
        return self.items


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def update_quality(self):
        if self.quality > 0:
            self.quality = self.quality - 1
        
        if self.sell_in < 0:
            if self.quality > 0:
                self.quality = self.quality - 1


class AgedBrie(Item):

    def update_quality(self):
        self.sell_in -= 1
        if self.quality < 50:
            self.quality += 1
        if self.sell_in < 0:
            if self.quality > 0:
                self.quality = self.quality - 1
        

class Backstage(Item):

    def update_quality(self):
        self.sell_in -= 1
        
        if self.quality < 50:
            self.quality = self.quality + 1
        if (self.sell_in < 11 and self.quality < 50) or (self.sell_in < 6 and self.quality < 50):
                self.quality = self.quality + 1
        if self.sell_in < 0:
            self.quality = self.quality - self.quality


class Sulfura(Item):

    def update_quality(self):
        if self.sell_in < 0:
            self.quality = self.quality - 1
        if self.sell_in < 0:
            if self.quality > 0:
                self.quality = self.quality - 1
        if self.sell_in < 0:
            self.quality = self.quality - self.quality
            if self.quality < 50:
                self.quality = self.quality + 1