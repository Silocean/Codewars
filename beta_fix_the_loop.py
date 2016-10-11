'''
Description:

Your collegue write an simple loop to list his favourite animals. But there seems to be a minor mistake. Fix it!:)

If You put list of Your favourite animals to the function, You should get list of the animals with ordering and newlines. For example:

animals = [ 'dog', 'cat', 'elephant' ]

Should return:

'1. dog\n2. cat\n3. elephant\n'
'''
def list_animals(animals):
    list = ''
    for i in range(len(animals)):
        list += str(i + 1) + '. ' + animals[i] + '\n'
    return list