from unittest import TestCase
from unittest.mock import patch
from section3.blog import app
from section3.blog.blog import Blog


class AppTest(TestCase):
    def test_print_blog(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- <Blog(Test, Test Author, posts: 0)>')
