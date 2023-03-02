import random



corpus = {"1.html": {"2.html", "3.html"}, "2.html": {"3.html"}, "3.html": {"2.html"}} 

damping_factor = 0.85

SAMPLES = 100000

def transition_model(corpus, page, damping_factor):
    # related pages to page in transition model
    related_pages = corpus[page]

    # number of pages in corpus
    total_pages = len(corpus)

    # total damping over all pages in corpus
    damping_over_total_corpus = round((1 - damping_factor)/total_pages,10)

    # dictionary definition for the return of the function
    new_dict = {}

    for key in corpus:

        # condition for checking if there are related pages
        if key in related_pages and related_pages:
            
            linked_probability = damping_factor * (1/len(related_pages)) + damping_over_total_corpus
            new_dict[key] = linked_probability

        else: 
            new_dict[key] = damping_over_total_corpus

    return new_dict





# number of pages in corpus
pages_in_corpus = len(corpus)

# create new dict to change for every sample
dict_of_probab = {}

# create new dict to store page counts. key=page:value=count
page_rank = {}

for i in range(SAMPLES):
    if i == 0:
        # pick a pseudorandom number from the corpus´ keys
        first_random_number = random.randrange(0, pages_in_corpus, 1)
        # look for the page on that key
        first_random_page = list(corpus)[first_random_number]

        # + 1 because it starts in 0
        pages_visited = i + 1

        # initialize this page's count to 0
        count = 0

        # add count to that page's page_count and calculate probabilities directly
        page_rank[first_random_page] = (count + 1) #/ pages_visited


        # get probabilities for the first page 
        dict_of_probab = transition_model(corpus, first_random_page, damping_factor)

        
    elif i > 0:
        # + 1 because it starts in 0
        pages_visited = i + 1
        
        # define lists to store previous dict_of_probab info. to be able to 
        # pass it through random.choice function
        prob_population = list(dict_of_probab.keys())
        prob_weights = list(dict_of_probab.values())

        # make a random choice from last dict_of_probab
        random_choice = random.choices(prob_population,prob_weights)
        random_choice_string = random_choice[0]

        # increment page count and calculate probability
        if random_choice_string not in page_rank :
            page_rank[random_choice_string] = 1
        else:
            past_value = page_rank[random_choice_string]
            page_rank[random_choice_string] = past_value + 1

    
        # get probability dict for next SAMPLE
        dict_of_probab = transition_model(corpus, random_choice[0], damping_factor)

print(page_rank)


for i in page_rank:
    past_value = page_rank[i]
    page_rank[i] = past_value/SAMPLES

print(page_rank)



"""
        # initialize this page's count to 1
        page_rank.update(curr_page_dict)
        print(page_rank)

        # if it is the first time visiting this page, put 1. else, increment by 1
        if page_rank[random_choice[0]] == 0:
            page_rank[random_choice[0]] = 1 #/ pages_visited
        else:
            page_rank[random_choice[0]] =+ 1



        # get probabilities for this page
        dict_of_probab = transition_model(corpus, random_choice[0], damping_factor)






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
                #new_dict[page] = round((1 - damping_factor)/(linked_pages + 1),10)
                
                probability = (count/linked_pages) - (1-damping_factor)/(linked_pages) + round((1 - damping_factor)/(linked_pages + 1),10)
                new_dict[i] = round(probability,10)
                
                #if key not in key_set:
                    
                
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

            
        








# def sample_pagerank(corpus, damping_factor, n):


        





        
"""