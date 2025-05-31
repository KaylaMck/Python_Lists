planet_list = ["Mercury", "Mars"]

planet_list.append("Jupiter")
planet_list.append("Saturn")


last_two_planets = ["Uranus", "Neptune"]

planet_list.extend(last_two_planets)

planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")

planet_list.append("Pluto")


rocky_planets = planet_list[:4]

print(rocky_planets)

del planet_list[-1]

print(planet_list)


spacecraft = [
    ("Mariner 10", "Mercury"),
    ("MESSENGER", "Mercury"),
    ("Venera 1-16", "Venus"),
    ("Mariner 2", "Venus"),
    ("Mariner 5", "Venus"),
    ("Mariner 10", "Venus"),
    ("Pioneer Venus 1", "Venus"),
    ("Pioneer Venus 2", "Venus"),
    ("Vega 1", "Venus"),
    ("Vega 2", "Venus"),
    ("Galileo", "Venus"),
    ("Magellan", "Venus"),
    ("Cassini", "Venus"),
    ("MESSENGER", "Venus"),
    ("Venus Express", "Venus"),
    ("Parker Solar Probe", "Venus"),
    ("Mariner 4", "Mars"),
    ("Mariner 6", "Mars"),
    ("Mariner 7", "Mars"),
    ("Mariner 9", "Mars"),
    ("Viking 1", "Mars"),
    ("Viking 2", "Mars"),
    ("Mars Pathfinder", "Mars"),
    ("Mars Odyssey", "Mars"),
    ("Spirit", "Mars"),
    ("Opportunity", "Mars"),
    ("Phoenix", "Mars"),
    ("Dawn", "Mars"),
    ("Curiosity", "Mars"),
    ("InSight", "Mars"),
    ("Perseverance", "Mars"),
    ("Pioneer 10", "Jupiter"),
    ("Pioneer 11", "Jupiter"),
    ("Voyager 1", "Jupiter"),
    ("Voyager 2", "Jupiter"),
    ("Ulysses", "Jupiter"),
    ("Galileo", "Jupiter"),
    ("Cassini", "Jupiter"),
    ("New Horizons", "Jupiter"),
    ("Juno", "Jupiter"),
    ("Pioneer 11", "Saturn"),
    ("Voyager 1", "Saturn"),
    ("Voyager 2", "Saturn"),
    ("Cassini", "Saturn"),
    ("Voyager 2", "Uranus"),
    ("Voyager 2", "Neptune"),
    ("New Horizons", "Pluto")
]

for planet in planet_list:
    print(f"\nSpacecrafts that have visited {planet}:")
    print("-" * 20)

    for spacecraft_name, planet_name in spacecraft:
        if planet == planet_name:
            print(spacecraft_name)