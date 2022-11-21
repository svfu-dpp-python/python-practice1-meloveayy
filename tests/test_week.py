from unittest import TestCase


class TestWeekday(TestCase):
    def test_week(self):
        from package.subpackage.my_module2 import weekday

        self.assertEqual(weekday(1), 'понедельник')
        self.assertEqual(weekday(2), 'вторник')
        self.assertEqual(weekday(3), 'среда')
        self.assertEqual(weekday(4), 'четверг')
        self.assertEqual(weekday(5), 'пятница')
        self.assertEqual(weekday(6), 'суббота')
        self.assertEqual(weekday(7), 'воскресенье')
