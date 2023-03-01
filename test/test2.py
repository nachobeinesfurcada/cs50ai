import random

page = "1.html"

corpus = {"1.html": {"2.html", "3.html"}, "2.html": {"3.html"}, "3.html": {"2.html"}, "4.html": {"2.html", "3.html", "5.html", "6.html"}, "5.html":{}, "6.html":{}}

damping_factor = 0.85

SAMPLES = 10

def transition_model(corpus, page, damping_factor):
    for key in corpus:
        if key == page and len(corpus[key])>0:
            linked_pages = len(corpus[key])

            # defining a set for the page we want to know
            key_set = corpus[key]
            
            # define a new dict for this page 
            # and calculate the probability of each linked page
            new_dict = {}
            for i in key_set:
                count =+ 1
                
                #assign (1-damping) to current page (as it cannot be linked to itself)
                new_dict[page] = round((1 - damping_factor)/(linked_pages + 1),10)
                
                probability = (count/linked_pages) - (1-damping_factor)/(linked_pages) + round((1 - damping_factor)/(linked_pages + 1),10)

                new_dict[i] = round(probability,10)

            return new_dict
        elif key == page:
            
            #number of pages in corpus
            pages_in_corpus = len(corpus)

            # define a new dict for this page 
            new_dict = {}

            # iterate over all pages names in corpus and add them to the new dict
            # with it´s probability (equal for each page, and all adding to 1)

            for i in corpus:
                new_dict[i] = round(1/pages_in_corpus, 10)
            return new_dict
            


transition_model(corpus, page, damping_factor)


# number of pages in corpus
pages_in_corpus = len(corpus)

first = random.randrange(0, pages_in_corpus, 1)

print(first)

for i in range(SAMPLES):
    if i == 0:
        first_page = random.randrange(0, pages_in_corpus, 1)
        #TO DOOOOOOO
    else: #TO DOOOOOOO
        





# def sample_pagerank(corpus, damping_factor, n):


        





        
    