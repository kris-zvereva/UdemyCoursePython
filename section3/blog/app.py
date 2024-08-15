from section3 import blog
from section3.blog.blog import Blog

MENU_PROMPT = 'Enter "c" to create a blog, "l" to list blogs, "r" to read one, "p" to create a post, or "q" to quit: '
# normally means a constant, but upper case doesnt make it unchangeable
POST_TEMPLATE = '''
    == {} ==
    
    {}
    
'''

blogs = dict()  # blog_name : blog object

def menu():
    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)


def print_blogs():
    for key, blog in blogs.items():  # key = title
        print('- {}'.format(blog))


def ask_create_blog():  # ask user for blog title, user name, create a blog, store in blogs dict
    title = input('enter a blog title: ')
    author = input('enter your name: ')
    blogs[title] = Blog(title, author)


def ask_read_blog():  # ask for a blog title, print posts
    title = input('enter a blog title you want to read: ')
    print_posts(blogs[title])


def print_posts(blog):
    for post in blog.posts:
        print_post(post)


def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))  # multiline string


def ask_create_post():  # ask for blog title post title post content
    blog_name = input('enter a blog title you want to post in: ')
    title = input('enter your post title: ')
    content = input('enter your post content: ')

    blogs[blog_name].create_post(title, content)

