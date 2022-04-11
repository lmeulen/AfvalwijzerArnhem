# AfvalwijzerArnhem

Usage:
afval = Afvalwijzer('6846LJ', 5)
print('{} - {}'.format('GFT     ', afval.get_volgende_groen()))
print('{} - {}'.format('Plastic ', afval.get_volgende_plastic()))
print('{} - {}'.format('Papier  ', afval.get_volgende_papier()))
