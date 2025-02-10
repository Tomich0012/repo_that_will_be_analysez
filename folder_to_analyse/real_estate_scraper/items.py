```python
"""
Module définissant les modèles pour vos items scrapés.

Voir la documentation de Scrapy pour plus d'informations :
https://docs.scrapy.org/en/latest/topics/items.html

Cette classe définit un modèle pour stocker les informations extraits à partir des sources.
"""

import scrapy


class RealEstateScraperItem(scrapy.Item):
    """
    Modèle pour stocker les informations scrapecées.

    Ce modèle définit les champs disponibles pour stocker les données extraites.
    """

    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
```