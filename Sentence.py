sentence = input("Sentence: ")

screen_width = 80
text_width = len(sentence)
box_width = text_width + 4
##left_margin = (screen_width - box_width) // 2

print()
print( '+'  + '-' * (box_width-2) +  '+')
print( '| ' + ' ' * text_width    + ' |')
print( '| ' + sentence            + ' |')
print('| ' + ' ' * text_width    + ' |')
print('+'  + '-' * (box_width-2) +  '+')
print()
