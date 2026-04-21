from lib.birthday_tracker import BirthdayTracker


def test_list_starts_empty():
    instance = BirthdayTracker()
    assert instance.list_of_friends == []

def test_add_friend_info_to_list():    
    instance = BirthdayTracker()
    instance.add_friend("Harry Potter", "01/01/1990")
    assert instance.list_of_friends == [{'Name' : 'Harry Potter', 'Birthday' : '01/01/1990'}]

def test_edit_friend_name():
    instance = BirthdayTracker()
    instance.add_friend("Harry Potter", "01/01/1990")
    instance.edit_friend_name("Harry Potter", "Ron Weasley")
    assert instance.list_of_friends == [{'Name' : 'Ron Weasley', 'Birthday' : '01/01/1990'}]

def test_edit_friend_birthday():
    instance = BirthdayTracker()
    instance.add_friend("Harry Potter", "01/01/1990")
    instance.edit_friend_birthday("Harry Potter", "01/01/1980")
    assert instance.list_of_friends == [{'Name' : "Harry Potter", 'Birthday' : '01/01/1980'}]