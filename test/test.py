

page = "1.html"

corpus = {"1.html": {"2.html", "3.html"}, "2.html": {"3.html"}, "3.html": {"2.html"}}

for key in corpus:
     if key == page:
          linked_pages = len(corpus[key])
          key_dict = {page}
          key_dict["page"]="0.2"
          for value in corpus[key]:
              
              print(key_dict)
              
     