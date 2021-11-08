# function observed which makes a set
def observed():

    observations = {'Flying Car','Sky Scraper','Laser','Dome'}
    # returns a value to where it has been called
    return observations

def run():
    # seen is set to the return values of observed
    seen = observed()
    # prints set
    print(seen)

# calls initial run function
run()


