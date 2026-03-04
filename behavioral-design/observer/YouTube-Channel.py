# Subject → YouTube Channel
# Observers → Subscribers
# When the channel uploads a video → all subscribers get notified automatically


# Observer Interface

class Subscriber:
    def update(self, channel_name, video_title):
        pass

# Subject(YouTube Channel)
class YouTubeChannel:
    def __init__(self, name):
        self._name = name
        self._subscribers = []

    def register_subscriber(self, subscriber):
        self._subscribers.append(subscriber)

    def remove_subscriber(self, subscriber):
        self._subscribers.remove(subscriber)

    def _notify_subscribers(self, video_title):
        for subscriber in self._subscribers:
            subscriber.update(self._name, video_title)

    def upload_video(self, video_title):
        print(f"{self._name} uploaded a new video: {video_title}")
        self._notify_subscribers(video_title)

# Concrete Observers (Subscribers)
class User(Subscriber):
    def __init__(self, name):
        self._name = name
    def update(self, channel_name, video_title):
        print(f"User {self._name} notified: {channel_name} uploaded '{video_title}'")

#  use the YouTubeChannel and Subscribers
if __name__ == "__main__":
    channel = YouTubeChannel("Tech Guru")

    user1 = User("Alice")
    user2 = User("Bob") 

    # user subscribe to the channel
    channel.register_subscriber(user1)
    channel.register_subscriber(user2)

    # channel uploads videos
    channel.upload_video("How to use the Observer Pattern in Python")
    channel.upload_video("10 Tips for Python Developers")

# output:
# Tech Guru uploaded a new video: How to use the Observer Pattern in Python
# User Alice notified: Tech Guru uploaded 'How to use the Observer Pattern in Python'
# User Bob notified: Tech Guru uploaded 'How to use the Observer Pattern in Python'
# Tech Guru uploaded a new video: 10 Tips for Python Developers
# User Alice notified: Tech Guru uploaded '10 Tips for Python Developers'
# User Bob notified: Tech Guru uploaded '10 Tips for Python Developers'
