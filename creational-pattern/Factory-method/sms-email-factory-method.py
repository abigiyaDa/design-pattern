# create a common interface 

from abc import ABC, abstractmethod
class Notification(ABC):
    @abstractmethod
    def send(self):
        pass

# concrete products
class SMSNotification(Notification):
    def send(self):
        return "Sending SMS notification."  
    
class EmailNotification(Notification):
    def send(self):
        return "Sending Email notification."
    
# adding another product to show the flexibility of the factory method pattern
class PushNotification(Notification):
    def send(self):
        return "Sending Push notification."
    
# creator class
class NotificationFactory(ABC):
    @abstractmethod
    def create_notification(self) -> Notification:
        pass
# concrete creators
class SMSNotificationFactory(NotificationFactory):
    def create_notification(self) -> Notification:
        return SMSNotification()
    
class EmailNotificationFactory(NotificationFactory):
    def create_notification(self) -> Notification:
        return EmailNotification()

class PushNotificationFactory(NotificationFactory):
    def create_notification(self) -> Notification:
        return PushNotification()

# client code
def client_code(factory: NotificationFactory):
    notification = factory.create_notification()
    print(notification.send())

# testing the code
if __name__ == "__main__":
    print("Client: Testing SMS Notification Factory:")
    client_code(SMSNotificationFactory())
    
    print("\nClient: Testing Email Notification Factory:")
    client_code(EmailNotificationFactory())

    print("\nClient: Testing Push Notification Factory:")
    client_code(PushNotificationFactory())

# output:
# Client: Testing SMS Notification Factory:
# Sending SMS notification. 

# Client: Testing Email Notification Factory:
# Sending Email notification.

# Client: Testing Push Notification Factory:
# Sending Push notification.