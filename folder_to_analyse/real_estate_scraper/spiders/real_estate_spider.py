import scrapy


class RealEstateSpiderSpider(scrapy.Spider):
    name = "real_estate_spider"
    allowed_domains = ["www.huurwoningen.nl"]
    start_urls = ["https://www.huurwoningen.nl/in/leiden/"]

    def parse(self, response):
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