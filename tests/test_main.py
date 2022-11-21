from unittest import TestCase


class TestMain(TestCase):
    filename = 'main.py'

    def test_imports(self):
        from datetime import date
        import main
        from package import date_repr

        self.assertIs(main.date_repr, date_repr)
        self.assertIs(main.date, date)
