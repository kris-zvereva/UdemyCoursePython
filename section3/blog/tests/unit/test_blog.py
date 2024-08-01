from unittest import TestCase
from section3.blog.blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test Author')

        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([], b.posts)
        self.assertEqual(0, len(b.posts))  # same as line 11

    def test_repr(self):
        b = Blog('Test', 'Test Author')

        self.assertEqual(
            b.__repr__(),
            "<Blog(Test, Test Author, posts: 0)>"
        )

    def test_repr_multiple(self):
        b = Blog('Test', 'Test Author')
        b.posts = ['test post']

        self.assertEqual(
            b.__repr__(),
            "<Blog(Test, Test Author, posts: 1)>"
        )
