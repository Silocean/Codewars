'''
Description:

Santa is coming to town and he needs your help finding out who's been Naughty or Nice. You will be given an entire year of JSON data following this format:

{
    January: {
        '1': ‘Naughty’,
        '31': 'Nice'
    },
    February: {
        '1': 'Nice’,
        '28': 'Nice'
    },
    November: {
        '1': 'Naughty',
        '30': 'Naughty'
    },
    December: {
        '1': 'Naughty',
        '31': 'Naughty'
    }
}
Your function should return "Naughty!" or "Nice!" depending on the total number of occurrences in a given year (whichever one is greater). If both are equal, return "Nice!"
'''
def naughty_or_nice(data):
    nice = 0
    for month in data:
        for day in data[month]:
            nice += 1 if data[month][day] == "Nice" else -1
    return "Nice!" if nice >= 0 else "Naughty!"