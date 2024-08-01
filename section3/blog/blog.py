class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self):
        return (
            f"<Blog({self.title}, {self.author}, posts: {len(self.posts)})>"
        )

    def create_post(self, title, content):
        post = {'title': self.title, 'content': self.content}
        self.posts.append(post)

    def json(self):
        pass

