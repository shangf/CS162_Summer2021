# Assignment 3
# Name : Frank Shang
# Date: 07/04/2021
# Description: This program simulates a Library.

class LibraryItem:
    '''class that makes library item objects'''

    def __init__(self, library_item_id, title):
        '''init method that takes in parameters id and title'''
        self._library_item_id = library_item_id
        self._title = title
        self._checked_out_by = None
        self._requested_by = None
        self._location = "ON_SHELF"
        self._date_checked_out = 0

    def get_date_checked_out(self):
        '''method that returns the date checked out'''
        return self._date_checked_out

    def get_requested_by(self):
        '''method that returns requested by attribute'''
        return self._requested_by

    def get_location(self):
        '''method that returns the location'''
        return self._location

    def get_library_item_id(self):
        '''method that returns the library item'''
        return self._library_item_id

    def get_checked_out_by(self):
        '''method that returns the checked out attribute'''
        return self._checked_out_by

    def get_title(self):
        '''method that returns the title'''
        return self._title

    def set_title(self, title):
        '''method that sets the title'''
        self._title = title

    def set_location(self, location):
        '''method that sets the location'''
        self._location = location

    def set_requested_by(self, requested_by):
        '''method that sets the requested by attribute'''
        self._requested_by = requested_by

    def set_checked_out_by(self, checked_out_by):
        '''method that sets the checked out by attribute'''
        self._checked_out_by = checked_out_by

    def set_date_checked_out(self, date_checked_out):
        '''method that sets the date checked out attribute'''
        self._date_checked_out = date_checked_out
        print("Date checked out is", date_checked_out)


class Patron:
    '''class that makes Patron objects'''

    def __init__(self, patron_id, name):
        '''init method that takes in parameters id and name'''
        self._patron_id = patron_id

        self._name = name
        self._checked_out_items = []
        self._fine_amount = 0

    def get_fine_amount(self):
        '''method that returns the fine amount'''
        return self._fine_amount

    def get_patron_name(self):
        '''returns the patron object's name'''
        return self._name

    def add_library_item(self, lib_item_object):
        '''adds library item object to the list of checked out items'''
        self._checked_out_items.append(lib_item_object)

    def remove_library_item(self, lib_item_object):
        '''removes library item object from the list of checked out items'''
        self._checked_out_items.remove(lib_item_object)

    def amend_fine(self, amount):
        '''adds or decreases fine amount by the amount parameter'''
        # if amount != .10:
        #  amount = amount * -1
        self._fine_amount += amount
        print("Fine amount is now", self._fine_amount)

    def get_patron_id(self):
        '''method that returns the patron id'''
        return self._patron_id

    def set_patron_name(self, name):
        self._name = name


class Library:
    '''class that creates Library objects'''

    def __init__(self):
        '''init method that initializes current date, holdings, and members'''
        self._current_date = 0
        self._holdings = []
        self._members = []

    def add_library_item(self, lib_item_object):
        '''method that adds LibraryItem object to the list of holdings'''
        for lib_item in self._holdings:
            while lib_item.get_title() == lib_item_object.get_title():
                print("Item #", lib_item.get_library_item_id(), "has the title:", lib_item.get_title())
                print("Item #", lib_item_object.get_library_item_id(), "has the title:", lib_item_object.get_title())
                print("Titles can not be the same.")
                print("Please enter in a new title for item #", lib_item_object.get_library_item_id())
                new_title = input()
                lib_item_object.set_title(new_title)
        self._holdings.append(lib_item_object)

    def add_patron(self, patron_object):
        '''method that adds Patron object to the list of members'''
        for patron_obj in self._members:
            while patron_obj.get_patron_name() == patron_object.get_patron_name():
                print("Patron ID:", patron_obj.get_patron_id(), "has the name", patron_obj.get_patron_name())
                print("Pratron ID:", patron_object.get_patron_id(), "has the name", patron_object.get_patron_name())
                print("Names can not be the same.")
                print("Please enter in a new name for Patron", patron_obj.get_patron_id())
                new_name = input()
                patron_obj.set_patron_name(new_name)
        self._members.append(patron_object)

    def lookup_library_item_from_id(self, lib_item_id):
        '''method that looks up the library item from the holdings list'''
        print("Searching for", lib_item_id, "in our database.")
        for lib_item_obj in self._holdings:
            if lib_item_id == lib_item_obj.get_library_item_id():
                print(lib_item_id, "found!")
                return lib_item_obj
        print(lib_item_id, "not found.")
        return None

    def lookup_patron_from_id(self, patron_id):
        '''method that looks up the patron from the memeber list'''
        print("Searching for", patron_id, "in our database.")
        for patron_obj in self._members:
            if patron_id == patron_obj.get_patron_id():
                print(patron_id, "found!")
                return patron_obj
        print(patron_id, "not found.")
        return None

    def check_out_library_item(self, patron_id, library_item_ID):
        '''method that checks out a library item'''
        for patron_obj in self._members:
            if patron_id == patron_obj.get_patron_id():
                print(patron_id, "found!")
                print("Continuing the checkout process.")
                for lib_item_obj in self._holdings:
                    if library_item_ID == lib_item_obj.get_library_item_id():
                        print(library_item_ID, "found!")
                        if lib_item_obj.get_location() == "CHECKED_OUT":
                            print(library_item_ID, "has been checked out already.")
                            return "Item already checked out."
                        elif lib_item_obj.get_location() == "ON_HOLD_SHELF" and patron_obj != lib_item_obj.get_requested_by():
                            print(library_item_ID, "is on hold by another patron.")
                            return "Item on hold by other patron."
                        else:
                            lib_item_obj.set_checked_out_by(patron_obj)
                            lib_item_obj.set_date_checked_out(self._current_date)
                            if lib_item_obj.get_location() == "ON_HOLD_SHELF":
                                lib_item_obj.set_requested_by(patron_obj)
                            lib_item_obj.set_location("CHECKED_OUT")
                            patron_obj.add_library_item(lib_item_obj)
                            print(patron_obj.get_patron_id(), "checked out", lib_item_obj.get_library_item_id())
                            return "Check out successful."

                print(library_item_ID, "not found.")
                return "Item not found."

        print(patron_id, "not found.")
        return "Patron not found."

    def return_library_item(self, library_item_ID):
        '''method that returns a library item'''
        for lib_item_obj in self._holdings:
            while (library_item_ID == lib_item_obj.get_library_item_id()):
                if lib_item_obj.get_location() == "ON_SHELF":
                    print(library_item_ID, "is available.")
                    return "Item already in library."
                else:
                    patron_object = lib_item_obj.get_checked_out_by()
                    patron_object.remove_library_item(lib_item_obj)
                    if lib_item_obj.get_requested_by() == None:
                        lib_item_obj.set_location("ON_SHELF")
                        lib_item_obj.set_checked_out_by(None)
                    else:
                        lib_item_obj.set_location("ON_HOLD_SHELF")
                        lib_item_obj.set_checked_out_by(None)
                print(library_item_ID, "was successfully returned.")
                return "Return successful."

        print(library_item_ID, "not found.")
        return "Item not found."

    def request_library_item(self, patron_ID, library_item_ID):
        '''method that makes a request for the library item'''
        for patron_obj in self._members:
            while patron_ID == patron_obj.get_patron_id():
                for lib_item_obj in self._holdings:
                    if library_item_ID == lib_item_obj.get_library_item_id():
                        print(library_item_ID, "found!")
                        if lib_item_obj.get_requested_by() != None:
                            print(library_item_ID, "is already on hold.")
                            return "Item already on hold."
                        else:
                            lib_item_obj.set_requested_by(patron_obj)
                            if lib_item_obj.get_location() == "ON_SHELF":
                                lib_item_obj.set_location("ON_HOLD_SHELF")
                            print(patron_ID, "is now holding", library_item_ID)
                            return "Request successful."

                print(library_item_ID, "not found.")
                return "Item not found."

        print(patron_ID, "not found.")
        return "Patron not found."

    def pay_fine(self, patron_ID, dollar_amount):
        '''method that pays the fine'''
        for patron_obj in self._members:
            if patron_ID == patron_obj.get_patron_id():
                dollar_amount = dollar_amount * -1
                patron_obj.amend_fine(dollar_amount)
                print("You paid", dollar_amount)
                return "Payment successful."
        return "Patron not found."

    def increment_current_date(self):
        '''method that increments the date and increments fine'''
        self._current_date += 1
        print("Now it is day", self._current_date)
        for patron_obj in self._members:
            for item_obj in patron_obj._checked_out_items:
                if ((self._current_date - item_obj.get_date_checked_out()) - item_obj.get_check_out_length()) > 0:
                    patron_obj.amend_fine(.10)


class Book(LibraryItem):
    '''class that makes Book objects'''

    def __init__(self, library_item_id, title, author):
        '''init method that initializes book object by inheriting LibraryItem class'''
        super().__init__(library_item_id, title)
        self._author = author

    def get_author(self):
        '''method that returns the author'''
        return self._author

    def get_check_out_length(self):
        '''method that returns the check out length'''
        return 21

    def set_author(self, author):
        '''method that sets the author'''
        self._author = author

    def __str__(self):
        '''method that prints the object's description'''
        return "A book by the author " + self._author + "."


class Album(LibraryItem):
    '''class that makes Album objects'''

    def __init__(self, library_item_id, title, artist):
        '''init method that initializes the Album object by inheriting LibraryItem class'''
        super().__init__(library_item_id, title)
        self._artist = artist

    def get_artist(self):
        '''method that returns the artist'''
        return self._artist

    def get_check_out_length(self):
        '''method that returns check out length'''
        return 14

    def set_artist(self, artist):
        '''method that sets the artist'''
        return self._artist

    def __str__(self):
        '''method that prints the object's description'''
        return "An album by the artist " + self._artist + "."


class Movie(LibraryItem):
    '''class that creates Movie objects'''

    def __init__(self, library_item_id, title, director):
        '''init method that initalizes Movie object by inheriting LibrayItem class'''
        super().__init__(library_item_id, title)
        self._director = director

    def get_director(self):
        '''method that returns the director'''
        return self._director

    def get_check_out_length(self):
        '''method that returns the check out length'''
        return 7

    def set_director(self, director):
        '''method that sets the director'''
        self._director = director

    def __str__(self):
        '''method that prints the object's description'''
        return "A movie by the director " + self._director + "."
