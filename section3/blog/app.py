MENU_PROMPT = 'Enter "c" to create a blog, "l" to list blogs, "r" to read one, "p" to create a post, or "q" to quit: '
# normally means a constant, but upper case doesnt make it unchangeable
blogs = dict()  # blog_name : blog object

def menu():
# show the user available blogs
# let the user make a choice
# do smt with that choice
# exit
    print_blogs()
    selection = input(MENU_PROMPT)


def print_blogs():
    for key, blog in blogs.items():  # key = title
        print('- {}'.format(blog))

