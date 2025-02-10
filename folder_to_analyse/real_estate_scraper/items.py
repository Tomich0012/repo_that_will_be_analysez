```python
"""
Module définissant les modèles pour vos items scrapés.

Voir la documentation de Scrapy pour plus d'informations :
https://docs.scrapy.org/en/latest/topics/items.html

Cette classe définit un modèle pour stocker les informations extraites à partir des sources.
"""

import scrapy


class RealEstateScraperItem(scrapy.Item):
    """
    Modèle pour stocker les informations scrapecées.

    Ce modèle définit les champs disponibles pour stocker les données extraites.
    
    Attributes:
        name (str): Nom de l'item.
        description (str): Description de l'item.
        price (float): Prix du bien immobilier.
        location (str): Emplacement du bien immobilier.
        
    Raises:
        None
    
    Examples:
        item = RealEstateScraperItem(name='Bien 1', description='Description 1', price=1000.00, location='Paris')
    """

    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
```