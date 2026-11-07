"""Regression checks for safe, navigable handbook output."""
import unittest
import build


class HandbookTests(unittest.TestCase):
    def test_semantic_blocks(self):
        result = build.markdown('## Topic\n\n- One\n- Two\n\n| A | B |\n| --- | --- |\n| 1 | 2 |', 'sample')
        self.assertIn('id="sample-1"', result)
        self.assertIn('<ul>', result)
        self.assertIn('<th scope="col">A</th>', result)
        self.assertEqual(result.count('<td>'), 2)

    def test_hostile_input(self):
        self.assertNotIn('<img', build.inline('<img src=x onerror=alert(1)>'))
        for target in ['javascript:alert', '//evil.example', '#x" onclick="x', 'http://example.org']:
            with self.assertRaises(ValueError):
                build.inline('[unsafe](' + target + ')')
        self.assertIn('href="#seeds"', build.inline('[Seeds](#seeds)'))

    def test_scope_and_navigation(self):
        for language in ['zh', 'en']:
            page = build.render(language)
            self.assertNotIn('0.5.5', page)
            for chapter in ['ranked', 'seeds', 'scoring', 'rng', 'draft', 'modes']:
                self.assertIn('id="' + chapter + '"', page)
            self.assertIn('type="search"', page)
            self.assertIn('/assets/js/wiki.js', page)


if __name__ == '__main__':
    unittest.main()
