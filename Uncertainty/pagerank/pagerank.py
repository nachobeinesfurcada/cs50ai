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
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


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

    for i in SAMPLES:
        if i == 1:
            first_page = random.randrange(0, pages_in_corpus, 1)



    return new_dict




def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    raise NotImplementedError


if __name__ == "__main__":
    main()
