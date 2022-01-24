# Author: Frank Shang
# Date: 06/30/2021
# Description: This program simulates a lemonade stand.

class InvalidSalesItemError(Exception):
    pass

class MenuItem:
    '''A MenuItem object represents a menu item to be offered for sale at the lemonade stand.'''
    def __init__(self, name, wholesale, sPrice):
        '''
        init method
        takes as parameters three values with which to initialize the MenuItem
        name, wholesale cost, selling price
        '''
        self._name = name
        self._wholesale = wholesale
        self._sellingPrice = sPrice

    def get_name(self):
        '''
        get method that retrieves the Menu Item's name
        '''
        return self._name

    def get_wholesale_cost(self):
        '''
        get method that retrieves the Menu Item's wholesale cost
        '''
        return self._wholesale

    def get_selling_price(self):
        '''
        get method that retrieves the Menu Item's selling price
        '''
        return self._sellingPrice

class SalesForDay:
    '''
    A SalesForDay object represents the sales for a particular day.
    '''

    def __init__(self, day, items_sold):
        '''
        Init method
        takes as parameters two values with which to initialize the SalesForDay
        1. the day (as an integer for the number of days the stand has been open so far)
        2. dictionary (names of items sold as the key, numbers of items sold as the value)
        '''
        self._day = day
        self._items_sold = items_sold

    def get_day(self):
        '''
        get method that retrieves the SalesForDay object's day
        '''
        return self._day

    def get_sales_dict(self):
        '''
        get method that retrieves the SalesForDay object's dictionary
        '''
        return self._items_sold

class LemonadeStand:
    '''
    A LemonadeStand object represents a lemonade stand, which has four data members:
    1. string - name of the stand
    2. integer - represents the current day
    3. dictionary of MenuItem objects (names of the items as keys, MenuItem objects as values)
    4. list of SalesForDay objects
    '''

    def __init__(self, storeName):
        '''
        init method
        takes one parameter which is the name of the stand
        initializes the name to the parameter value
        initializes current day to 0
        initializes the menu to an empty dictionary
        initializes the sales record to an empty list
        '''
        self._store_name = storeName
        self._current_day = 0
        self._menu = {}
        self._sales_record = []

    def get_name(self):
        '''
        get method that retrieves the LemonadeStand object's name
        '''
        return self._store_name

    def add_menu_item(self, menu_item_obj):
        '''
        Takes as a parameter a MenuItem object and adds it to the menu dictionary
        (names of the items as keys, MenuItem objects as values)
        '''
        self._menu[menu_item_obj.get_name()] = menu_item_obj

    def enter_sales_for_today(self, dict):
        '''
        Takes in one parameter: a dictionary where the names of items sold are the keys
        and the number of units sold are the values

        If the name of any item sold does not match the name of any MenuItem in the menu, it raises an
        InvalidSalesItemError

        Otherwise, it creates a new SalesForDay object, adds it to the sales record list, and increments the current
        day by 1.
        '''
        for item in dict:
            if item not in self._menu:
                raise InvalidSalesItemError

        newSalesObj = SalesForDay(self._current_day, dict)
        self._sales_record.append(newSalesObj)
        self._current_day += 1

    def get_sales_dict_for_day(self, day):
        '''
        takes in one parameter: an integer that represents a particular day
        returns the dictionary of sales for that day (not a SalesForDay object)
        '''
        return self._sales_record[day].get_sales_dict()

    def total_sales_for_menu_item(self, menu_name):
        '''
        takes in one parameter: the name of a menu item
        returns the total number of that item sold over the history of the stand
        '''
        total_sales = 0
        for sale_obj in self._sales_record:
            sales_dict = sale_obj.get_sales_dict()
            if menu_name in sales_dict:
                total_sales += sales_dict[menu_name]
        return total_sales

    def total_profit_for_menu_item(self, menu_name):
        '''
        takes as a parameter the name of a menu item
        returns the total profit on that item over the history of the stand
        '''
        total_items_sold = self.total_sales_for_menu_item(menu_name)
        wholesale_cost = self._menu[menu_name].get_wholesale_cost()
        selling_price = self._menu[menu_name].get_selling_price()
        # for sale_obj in self._sales_record:
        #     sales_dict = sale_obj.get_sales_dict()
        #     if menu_name in sales_dict:
        #         total_items_sold += sales_dict[menu_name]
        total_profits = (total_items_sold * selling_price) - (total_items_sold * wholesale_cost)
        return total_profits

    def total_profit_for_stand(self):
        '''
        takes in no parameters
        returns the total profit on all items sold over the history of the stand
        '''
        total_profits = 0
        for menu_name in self._menu:
            total_profits += self.total_profit_for_menu_item(menu_name)

        return total_profits

stand = LemonadeStand('Lemons R Us')
item1 = MenuItem('lemonade', .5, 1.5)
stand.add_menu_item(item1)
item2 = MenuItem('cookie', .2, 1)
stand.add_menu_item(item2)
day0 = {
    'lemonade' : 5,
    'cookie'   : 2
}
day1 = {
    'lemonade' : 15,
    'cookie'   : 2
}
day2 = {
    'cookie'   : 2
}
stand.enter_sales_for_today(day0)
stand.enter_sales_for_today(day1)
stand.enter_sales_for_today(day2)
print(stand.get_sales_dict_for_day(0))

print(f"lemonade sales = {stand.total_sales_for_menu_item('lemonade')}")
print(f"cookie sales = {stand.total_sales_for_menu_item('cookie')}")

print(f"lemonade profit = {stand.total_profit_for_menu_item('lemonade')}")
print(f"cookie profit = {stand.total_profit_for_menu_item('cookie')}")

print(f"total profits = {stand.total_profit_for_stand()}")
