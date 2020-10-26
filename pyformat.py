#Basic formatting
print('{} {}'.format('Sebatian', 'Krzynówek'))
#Padding and aligning strings
#Align right
print(('{:>5}'.format('Projektowanie')))
#Align left
print(('{:10}'.format('Projektowanie')))
#paddingCharacter
print('{:_<10}'.format('Projektowanie'))
#Combinning truncating and padding
print('{:10.7}'.format('Projektowanie'))
