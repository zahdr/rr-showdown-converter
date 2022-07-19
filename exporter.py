def fixBerryName(itemName):
    slackyBerryName = ('Aguav', 'Apicot', 'Aspear', 'Babiri', 'Belue', 'Bitter', 'Bluk', 'Burnt', 'Charti', 'Cheri', 'Chesto', 'Chilan', 'Chople', 'Coba', 'Colbur', 'Cornn', 'Custap', 'Durin', 'Enigma', 'Figy', 'Ganlon', 'Gold', 'Grepa', 'Haban', 'Hondew', 'Iapapa', 'Ice', 'Jaboca', 'Kasib', 'Kebia', 'Kee', 'Kelpsy', 'Lansat', 'Leppa', 'Liechi', 'Lum', 'Mago', 'Magost', 'Maranga', 'Micle', 'Mint', 'Miracle', 'Mystery', 'Nanab', 'Nomel', 'Occa', 'Oran', 'Pamtre', 'Passho', 'Payapa', 'Pecha', 'Persim', 'Petaya', 'Pinap', 'Pomeg', 'PRZ', 'PSN', 'Qualot', 'Rabuta', 'Rawst', 'Razz', 'Rindo', 'Roseli', 'Rowap', 'Salac', 'Shuca', 'Sitrus', 'Spelon', 'Starf', 'Tamato', 'Tanga', 'Wacan', 'Watmel', 'Wepear', 'Wiki', 'Yache')
    if itemName in slackyBerryName:
        return itemName + " Berry"
    else:
        return itemName


if __name__ == '__main__':
    trainerName = ""
    pokemonName = ""
    pokemonItem = ""
    pokemonLevel = ""
    pokemonNature = ""
    pokemonAbility = ""
    pokemonMoves = []
    pokemonAmount = 0

    with open('fight-input.txt', 'r') as f:
       trainerName = f.readline()
       pokemonName = f.readline().split("\t")
       pokemonAmount = len(pokemonName)
       pokemonLevel = f.readline().split("\t")
       pokemonItem = f.readline().split("\t")
       pokemonAbility = f.readline().split("\t")
       pokemonNature = f.readline().split("\t")
       pokemonMoveOne = f.readline().split("\t")
       pokemonMoveTwo = f.readline().split("\t")
       pokemonMoveThree = f.readline().split("\t")
       pokemonMoveFour = f.readline().split("\t")
       for i in range(pokemonAmount):
        pokemonMoves.append([
            pokemonMoveOne[i].strip('\n'), 
            pokemonMoveTwo[i].strip('\n'), 
            pokemonMoveThree[i].strip('\n'), 
            pokemonMoveFour[i].strip('\n')
            ])
        
    # Final Output
    print(trainerName)
    for i in range(pokemonAmount):
        print(pokemonName[i].strip('\n'), "@", fixBerryName(pokemonItem[i].strip('\n')) )
        print("Level:", pokemonLevel[i].strip('\n'))
        print(pokemonNature[i].strip('\n'), "Nature")
        print("Ability:", pokemonAbility[i].strip('\n'))
        for move in pokemonMoves[i]:
            print("-", move)
        print("")
