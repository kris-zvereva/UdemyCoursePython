from unittest import TestCase
from unittest.mock import patch
from section3.blog import app
from section3.blog.blog import Blog
from section3.blog.post import Post


class AppTest(TestCase):
    def test_menu_calls_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('c', 'Test Create Blog', 'Test Author', 'q')

            app.menu()
            self.assertIsNotNone(app.blogs['Test Create Blog'])

    def test_menu_calls_print_blogs(self):
        with patch('builtins.input') as mocked_input:
            with patch('section3.blog.app.print_blogs') as mocked_print_blogs:
                mocked_input.side_effect = ('l', 'q')
                app.menu()

                mocked_print_blogs.assert_called()

    def test_menu_calls_ask_read_blog(self):
        with patch('builtins.input') as mocked_input:
            with patch('section3.blog.app.ask_read_blog') as mocked_read_blog:
                mocked_input.side_effect = ('r', 'q')
                app.menu()

                mocked_read_blog.assert_called()

    def test_menu_calls_ask_create_post(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('p', 'Test', 'Test Title', 'Test Content', 'q')
            app.menu()

            self.assertEqual(blog.posts[0].title, 'Test Title')
            self.assertEqual(blog.posts[0].content, 'Test Content')

    def test_menu_prints_prompt(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('q')
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)


    def test_print_blogs(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- <Blog(Test, Test Author, posts: 0)>')

    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test Author')  # returns for each input
            app.ask_create_blog()
            self.assertIsNotNone(app.blogs.get("Test"))

    def test_ask_read_blog(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}
        with patch('builtins.input', return_value='Test'):
            with patch('section3.blog.app.print_posts') as mocked_print_posts:
                app.ask_read_blog()
                mocked_print_posts.assert_called_with(blog)


    def test_print_post(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}
        blog.create_post('Test Post', 'Test Content')
        with patch('section3.blog.app.print_post') as mocked_print_post:
            app.print_posts(blog)
            mocked_print_post.assert_called_with(blog.posts[0])

    def test_print_post(self):
        post = Post('Post Title', 'Post Content')
        expected_print = '''
    == Post Title ==
    
    Post Content
    
'''
        with patch('builtins.print') as mocked_print:
            app.print_post(post)

            mocked_print.assert_called_with(expected_print)


    def test_ask_create_post(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test Title', 'Test Content')

            app.ask_create_post()

            self.assertEqual(blog.posts[0].title, 'Test Title')
            self.assertEqual(blog.posts[0].content, 'Test Content')

