letter = '''Dear  <|Name|>,
You are selected !
<|date|>'''

print(letter.replace("  ", ""))
print(letter.replace("<|Name|>", "Harry").replace("<|date|>", "21 July 2025"))
#s