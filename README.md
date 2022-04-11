# AfvalwijzerArnhem

Usage:
```python
afval = Afvalwijzer('0000AA', 1)
print('{} - {}'.format('GFT     ', afval.get_volgende_groen()))
print('{} - {}'.format('Plastic ', afval.get_volgende_plastic()))
print('{} - {}'.format('Papier  ', afval.get_volgende_papier()))
```
