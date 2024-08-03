blogs = dict()  # blog_name : blog object

def menu():
# show the user available blogs
# let the user make a choice
# do smt with that choice
# exit
    print_blogs()


def print_blogs():
    for key, blog in blogs.items():  # key = title
        print('- {}'.format(blog))

        