import random

web_list = ["http://ecosia.org/",
            "http://nasa.gov/",
            "http://usda.gov/",
            "http://nationalgeographic.com/",
            "http://epa.gov/",
            "http://scielo.org.mx/",
            "http://weatherspark.com/",
            "http://inaturalist.org/",
            "http://earth.com/",
            "http://ebird.org/",
            "http://ecologiaverde.com/",
            "http://cnrs.fr/",
            "http://treehugger.com/",
            "http://usherbrooke.ca/",
            "http://greenpeace.org/"
            ]

def get_random_link():
    return random.choice(web_list)