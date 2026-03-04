# step 1 create subject interface
from abc import ABC, abstractmethod
class Image(ABC):
    @abstractmethod
    def display(self):
        pass

# step 2 create real subject
class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.load_from_disk()

    def load_from_disk(self):
        print(f"Loading {self.filename} from disk...")

    def display(self):
        print(f"Displaying {self.filename}")

# step 3 create proxy
class ProxyImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None

    def display(self):
        if self.real_image is None:
            self.real_image = RealImage(self.filename)
        self.real_image.display()
# step 4 client code
if __name__ == "__main__":
    image1 = ProxyImage("photo1.jpg")
    image2 = ProxyImage("photo2.jpg")

    # Image will be loaded from disk only when display is called
    image1.display()  # Loading photo1.jpg from disk... Displaying photo1.jpg
    image1.display()  # Displaying photo1.jpg (no loading this time)

    image2.display()  # Loading photo2.jpg from disk... Displaying photo2.jpg
    image2.display()  # Displaying photo2.jpg (no loading this time)