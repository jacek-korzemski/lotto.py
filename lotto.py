import random
import sys

'''
Zrobimy sobie sztuczne losowanie, na zasadzie:
losuj tak długo, aż losowanie się powtórzy. Jeśli się powtórzy:
Wyświetl wynik losowania.
Ot taka magia - komputer będzie losował wciąż i wciąż, aż trafi się powtórka
Ta powtórka będzie magiczna i będzie liczbami które chce obstawić w EuroJackpot
'''

allDraws = []
smallRandom = [0, 0, 0, 0, 0]
goldenDraws = []


def checkDuplicates(arr):
    for elem in arr:
        if arr.count(elem) > 1:
            return True
    return False


while len(goldenDraws) < 5:
    while checkDuplicates(allDraws) == False:
        smallRandom = random.sample(range(1, 50), 5)
        smallRandom.sort()

        allDraws.append(str(smallRandom))
        sys.stdout.write("\r{draw}".format(draw=str(smallRandom)))

    print(
        f"\rAnd the winner is {allDraws[len(allDraws) - 1]} after {len(allDraws)} draws!")
    goldenDraws.append(allDraws[len(allDraws) - 1])
    allDraws = []

counter = 0
while counter < len(goldenDraws):
    print(goldenDraws[counter])
    counter += 1
