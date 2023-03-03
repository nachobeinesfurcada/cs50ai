import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    #ranks = iterate_pagerank(corpus, DAMPING)
    #print(f"PageRank Results from Iteration")
    #for page in sorted(ranks):
    #    print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages



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
                


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

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

    # iterate to update page's count into a percentage
    for i in page_rank:
        past_value = page_rank[i]
        page_rank[i] = past_value/SAMPLES

    return page_rank




def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    




if __name__ == "__main__":
    main()
