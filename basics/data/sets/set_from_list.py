
def observed():
    observations = ["Neon Sign","Neon Sign","Skyscraper"]

    return observations

def run():

    print("Counting observations...")

    sightList = observed()

    sightSet = set()

    for sight in sightList:
        neon_amount = sight.count("Neon Sign")
        skyscraper_amount = sight.count("Skyscraper")

    print(neon_amount)
    print(skyscraper_amount)

    print(sightSet)

run()