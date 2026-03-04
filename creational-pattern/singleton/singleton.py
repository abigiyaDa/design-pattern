#  using __new__ method to create singleton class
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating new instance ...")  
            cls._instance = super().__new__(cls)
        return cls._instance
# useage 
if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()
    print(s1 is s2)  # Output: True