from random import choice

def coin_flip():
    flip = ['H', 'T']
    return choice(flip)


'''
Write a function called series_of_flips, that has one parameter, n, which represents the number of coin flips. Return a list of the random coin flips.
if n=4, then something like this: ['H', 'H', 'T', 'H']
'''
def series_of_flips(n):
    flips = []
    for _ in range(n):
        flips.append(coin_flip())
    return flips

print(series_of_flips(4))