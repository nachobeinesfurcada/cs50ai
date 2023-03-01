

page = "1.html"

corpus = {"1.html": {"2.html", "3.html"}, "2.html": {"3.html"}, "3.html": {"2.html"}}

for key in corpus:
     if key == page:
          linked_pages = len(corpus[key])
          print(linked_pages)

          key_dict = corpus[key]
          print(key_dict)
          key_dict[key] = 1




"""
for key in corpus:
     if key == page:
          linked_pages = len(corpus[key])
          key_dict = corpus[key]
          print(key_dict)
          
          for value in (key_dict):
            curr_value = value
            if curr_value == value:
                  count =+1
                  key_dict["1.html"] = count
            print(key_dict)
"""
              


     # key_dict = {}        
     # key_dict[key] = value