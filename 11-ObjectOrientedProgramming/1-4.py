class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")

    def display_timeline(self):
        return






def main():
    posts = []
    john_doe = SocialMediaProfile("John Doe")
    john_doe.add_post()