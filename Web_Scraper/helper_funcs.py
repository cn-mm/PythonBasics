import sys

# GETTING QUERY FROM COMMAND LINE OR THE USER
def get_query():
    if len(sys.argv) > 1:
        # Get address from command line.
        query = ' '.join(sys.argv[1:])
    else:
        #Get query from user 
        option = input("Type 1 to input query ")
        if option == '1':
            query = str(input("Enter your query: "))
            print("Searching Google Images for", query)
            query= query.split()
            query='+'.join(query)
        else:
            # Use default query 
            query = "drums"
            print("Using default query \" Drums\"")

    return query


# GET URL 
def get_url(query):
    return 'https://www.google.co.in/search?q='+query+'&source=lnms&tbm=isch'

