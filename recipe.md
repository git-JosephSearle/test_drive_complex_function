# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So I don't forget the details
I want to keep a record of friends' names and birthdates

list_of_friends = [ 
    {name : Tom Smith, birthday : 01/01/1995}
    {name : Harry Potter, birthday : 01/02/1995}
]



As a user
So I can make edits when I've got dates wrong
I want to be able to update a record by passing in a name and new date

As a user
So I can make edits when people change their name
I want to be able to update a record by passing in an old and a new name

As a user
So I can remember to send birthday cards at the right time
I want to be able to list friends whose birthdays are coming up soon and to whom I need to send a card

As a user
So I can buy age-appropriate birthday cards
I want to calculate the upcoming ages for friends with birthdays


## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class BirthdayTracker():

    def __init__(self):
        list_of_friends = []

        pass 

    def add_friend(self, name, birthday):

        pass 

    def edit_friend_name(self, old_name, new_name):

        pass 


    def edit_friend_birthday(self, name, new_birthday):

        pass 
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

def test_list_starts_empty():
    instance = BirthdayTracker()
    assert instance.list_of_friends == []

def test_add_friend_info_to_list():    
    instance = BirthdayTracker()
    instance.add_friend("Harry Potter", "01/01/1990")
    assert instance.list_of_friends == [{'name' : 'Harry Potter', 'birthday' : '01/01/1990'}]

def test_edit_friend_name():
    instance = BirthdayTracker()
    instance.add_friend("Harry Potter", "01/01/1990")
    instance.edit_friend_name("Harry Potter", "Ron Weasley")
    assert instance.list_of_friends == [{'name' : 'Ron Weasley', 'birthday' : '01/01/1990'}]

def test_edit_friend_birthday():
    instance = BirthdayTracker()
    instance.add_friend("Harry Potter", "01/01/1990")
    instance.edit_friend_birthday("Harry Potter", "01/01/1980")
    assert instance.list_of_friends == [{'name' : "Harry Potter", 'birthday' : '01/01/1980'}]

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
