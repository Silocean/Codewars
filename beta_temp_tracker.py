'''
Description:

You've started a heating company with an oddly-mathematical All-Time Max, Min, Mean and Mode Temperature Guarantee™.

Write a class TempTracker with these methods:

insert()    # records a new temperature
get_max()   # returns the highest temp we've seen so far
get_min()   # returns the lowest temp we've seen so far
get_mean()  # returns the mean of all temps we've seen so far
get_mode()  # returns the temp we've seen the most times so far
Do not store every single temperature inserted. You expect to get so much input that you won't be able to store all the temperatures in memory. Optimize for space and time. The time and space costs of your functions should all be O(1)!

The function to get the mean should return a float, but the rest of the get functions can return integers. If no temperatures have been inserted yet, the get functions should return null objects. Temperatures will all be inserted as integers. You'll record your temperatures in Fahrenheit, so you can assume they'll all be in the range 0 to 110.

If there is more than one mode, return any of the modes.

Note: this challenge was contributed by Interview Cake. If you get stuck, check it out for hints and gotchas that guide you to the solution by prompting you to have your own insights.
'''
class TempTracker:

    def __init__(self):
        self.num = 0
        self.temps = {}

    def insert(self, temperature):
        if self.num == 0:
            self.max, self.min  = temperature, temperature
            self.mean = float(temperature)
        else:
            if temperature > self.max: self.max = temperature
            if temperature < self.min: self.min = temperature
            self.mean = float(self.mean*self.num + temperature)/(self.num+1)
        self.temps[temperature] = self.temps.get(temperature, 0)+1
        self.mode = self.temps.keys()[self.temps.values().index(max(self.temps.values()))]
        self.num += 1    
  
    def get_max(self):
        return self.max if self.num else None
  
    def get_min(self):
        return self.min if self.num else None
  
    def get_mean(self):
        return self.mean if self.num else None
  
    def get_mode(self):
        return self.mode if self.num else None