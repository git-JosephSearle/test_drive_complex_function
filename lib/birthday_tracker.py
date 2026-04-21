from datetime import datetime

class BirthdayTracker():
    def __init__(self):
        self.list_of_friends = []

    def add_friend(self, name, birthday):
        info = dict(Name = name, Birthday = birthday)
        self.list_of_friends.append(info)
        
    def edit_friend_name(self, old_name, new_name):
        for friend in self.list_of_friends:
            if friend['Name'] == old_name:
                friend['Name'] = new_name         

    def edit_friend_birthday(self, name, new_birthday):
        for friend in self.list_of_friends:
            if friend['Name'] == name:
                friend['Birthday'] = new_birthday  
    
    def view_upcoming_birthdays(self):
        for friend in self.list_of_friends:
            birthday = friend['Birthday']
            bday = datetime.strptime(birthday, '%d/%m/%Y')
            print(bday)
            # today = datetime.now()
            # diff = bday - today
            # diff

instance = BirthdayTracker()
instance.add_friend("Harry Potter", "01/01/1990")
instance.add_friend("Ron Weasley", "01/02/1990")
instance.add_friend("Hermione Granger", "01/03/1990")
instance.view_upcoming_birthdays()
        