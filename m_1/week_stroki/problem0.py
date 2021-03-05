text = ("в который ранее входили лишь")

l = len(text)
part_1 = text[0:l//2]
part_2 = text[l//2:]
print (part_1.upper()+part_2.lower())
