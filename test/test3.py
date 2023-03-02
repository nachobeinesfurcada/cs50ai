

SAMPLES = 10





dict  = {"1.html":2, "2.html":0}

page = "2.html"


print(dict[page])





past_value = dict[page]

if past_value == 0:
    dict[page] = 1
else:
    dict[page] = past_value + 1
