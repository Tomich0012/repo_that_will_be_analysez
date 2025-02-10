```python
import scrapy


class RealEstateSpiderSpider(scrapy.Spider):
    """
    Spider pour extraire les annonces de logements à louer sur huurwoningen.nl.

    Cette classe implémente le modèle de spider standard de Scrapy, où la méthode parse est appelée pour traiter chaque page web.
    Elle suit un processus de pagination dynamique pour collecter toutes les annonces disponibles.

    Attributes:
        name (str): Le nom du spider.
        allowed_domains (list): La liste des domaines autorisés pour les requêtes HTTP.
        start_urls (list): La liste des pages de départ à partir desquelles le spider démarrera.

    Methods:
        parse(response): Traitement de chaque page web pour extraire les annonces et les données de pagination suivantes.
    """

    name = "real_estate_spider"
    allowed_domains = ["www.huurwoningen.nl"]
    start_urls = ["https://www.huurwoningen.nl/in/leiden/"]

    def parse(self, response):
        """
        Traitement de chaque page web pour extraire les annonces et les données de pagination suivantes.

        Args:
            response (Response): La réponse HTTP reçue depuis la page web.
        Returns:
            Response: L'URL de la page suivante à traiter.
        Yields:
            dict: Les données extraites de chaque annonce, contenant le nom et l'URL de l'annonce.
        """
        # Sélection des annonces sur la page
        listings = response.css("li.search-list__item--listing")

        # Extraction des données pour chaque annonce
        for listing in listings:
            # Récupération du titre (nom de l'annonce)
            name = listing.css("h2.listing-search-item__title a::text").get()

            # Récupération de l'URL (lien vers l'annonce)
            url = listing.css("h2.listing-search-item__title a::attr(href)").get()

            # Construction de l'URL complète si elle est relative
            if url and not url.startswith("http"):
                url = response.urljoin(url)

            # Vérification et envoi des données extraites
            if name and url:
                yield {
                    "name": name.strip(),
                    "url": url,
                }

        # Gestion de la pagination
        next_page = response.css("a.pagination__link--next::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
```