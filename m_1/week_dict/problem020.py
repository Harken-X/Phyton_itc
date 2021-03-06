
set1 = {'.add("*")', '.remove("*")', '.clear()', '.update("*")', '.difference("*")', '.discard("*")', '.intersection("*")', '.intersection_update(*)', '.pop()'}
set2 = {'.clear()', '.get("*")', '.values()', '.items()', '.update("*")', '.pop()'}
set2.intersection_update(set1)
print(set2)
