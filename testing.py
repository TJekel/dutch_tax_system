"""inhoud bekijken"""

#from openfisca_core.entities import build_entity
from openfisca_core import entities as entiteit

pensioengerechtigde = entiteit.build_entity(
    key = "pensioengerechtigde",
    plural = "pensioengerechtigden",
    label = "Persoon die recht heeft op ouderdomspensioen op grond van de AOW",
    doc = """
    Hier kan extra informatie komen over de pensioengerechtigde. Context meegeven? verder uitzoeken.
    """,
    roles = [
        {
            "key": "partner",
            "plural": "partners",
            "label": "Parents",
            "max": 1,
            "subroles": ["eerste_partner", "tweede_partner"],
            "doc": "partner of gehuwde op grond van artikel 1 lid 2 AOW. http://wetten.overheid.nl/jci1.3:c:BWBR0002221&hoofdstuk=I&artikel=1&lid=2",
            },
        {
            "key": "gehuwde",
            "plural": "gehuwden",
            "label": "Getrwoud",
            "doc": "Getrouwd volgens de wet",
            },
        ],
    is_person = True,
    
    )

print(pensioengerechtigde.is_person)
print(pensioengerechtigde.key)