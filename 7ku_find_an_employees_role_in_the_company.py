'''
Description:

You get a new job working for Eggman Movers. Your first task is to write a method that will allow the admin staff to enter a person’s name and return what that person's role is in the company.

You will be given an array of object literals holding the current employees of the company. You code must find the employee with the matching firstName and lastName and then return the role for that employee or if no employee is not found it should return "Does not work here!"

The array is preloaded and can be referenced using the variable employees ($employees in Ruby). It uses the following structure.

employees = [ {'first_name': "Dipper", 'last_name': "Pines", 'role': "Boss"}, ...... ]
There are no duplicate names in the array and the name passed in will be a single string with a space between the first and last name i.e. Jane Doe or just a name.
'''
def find_employees_role(name):
    #your code here
    if len(name.split(' ')) != 2:
        return 'Does not work here!'
    first = name.split(' ')[0]
    last = name.split(' ')[1]
    for d in employees:
        if d.get('first_name') == first and d.get('last_name') == last:
            return d.get('role')
    return 'Does not work here!'