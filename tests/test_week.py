from unittest import TestCase


class TestWeek(TestCase):
    def test_week(self):
        from package.subpackage.my_module2 import week

        self.assertEqual(week(1), 'понедельник')
        self.assertEqual(week(2), 'вторник')
        self.assertEqual(week(3), 'среда')
        self.assertEqual(week(4), 'четверг')
        self.assertEqual(week(5), 'пятница')
        self.assertEqual(week(6), 'суббота')
        self.assertEqual(week(7), 'воскресенье')
