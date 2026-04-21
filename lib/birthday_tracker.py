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
        