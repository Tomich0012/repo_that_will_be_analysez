```python
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class RealEstateScraperPipeline:
    """
    Pipeline pour traiter les données de réal estate.

    Cette classe implémente une interface commune pour différents types d'items.
    Elle permettrait de gérer des données avec un seul interface.

    Les méthodes suivantes sont disponibles dans cette classe :
    - process_item(item, spider) : Traitement du item en question.
    """

    def __init__(self):
        """
        Constructeur par défaut pour la classe RealEstateScraperPipeline.
        """
        pass

    def process_item(self, item, spider):
        """
        Traitement d'un item spécifique.

        Args:
            item (object) : L'item à traiter.
            spider (Spider) : Le spider associé à l'item.

        Returns:
            object : L'item traité avec succès.

        """
        return item
```