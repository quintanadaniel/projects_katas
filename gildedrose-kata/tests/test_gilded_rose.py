# -*- coding: utf-8 -*-
"""
Averiguar como hacer un test que la Clase del python principal devuelva una representacion
"""
import unittest

from gilded_rose import Item, GildedRose, AgedBrie, Backstage, Sulfura


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    
    def test_gilder_rose(self):
        items = [AgedBrie(name='Aged Brie', sell_in=2, quality=0)]
        items_result = GildedRose(items).update_quality()
        items_expected = [AgedBrie(name='Aged Brie', sell_in=1, quality=1)]
        self.assertEqual(items_result[0].name,items_expected[0].name)

        
if __name__ == '__main__':
    unittest.main()
