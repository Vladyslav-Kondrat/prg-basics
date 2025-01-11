class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")

    def display_timeline(self):
        print(self.username)
        print()
        #print(self.posts)
        for item in self.posts:
            print(item)


def main():
    john_doe = SocialMediaProfile("John Doe")
    john_doe.add_post("Hello, world!")
    john_doe.add_post("Had a great day at the park!")
    john_doe.add_post("What's up, Natalie? How are you?")
    john_doe.display_timeline()

if __name__ == "__main__":
    main()