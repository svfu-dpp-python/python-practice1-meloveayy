from unittest import TestCase


class TestStart(TestCase):
    filename = 'start.py'

    def test_imports(self):
        from datetime import date
        import start
        from package import date_repr

        self.assertIs(start.date_repr, date_repr)
        self.assertIs(start.date, date)
