from unittest import TestCase
from datetime import date


class TestDateRepr(TestCase):
    def test_package_header(self):
        import package
        from package.my_module1 import date_repr
        self.assertIs(package.date_repr, date_repr)

    def test_date_repr(self):
        from package.my_module1 import date_repr

        d1 = date(2022, 9, 1)
        self.assertIn(date_repr(d1), 'четверг 1 сентября 2022 года')

        d2 = date(2020, 2, 29)
        self.assertEqual(date_repr(d2), 'суббота 29 февраля 2020 года')
