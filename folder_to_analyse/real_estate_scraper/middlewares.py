```python
"""
Module contenant les classes de middleware pour le scraper de biens immobiliers.

Cette classe de middleware s'assure que les données sont traitées correctement et qu'il ne
y a pas d'erreurs lors du traitement des requêtes et des réponses.
"""

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class RealEstateScraperSpiderMiddleware:
    """
    Cette classe de middleware s'assure que les données sont traitées correctement pour
    le scraper de biens immobiliers.
    """

    @classmethod
    def from_crawler(cls, crawler):
        """
        Methode utilisée par Scrapy pour créer la classe de middleware.

        :param crawler: objet de Scrapy
        :type crawler: scrapy.crawler.Crawler
        :return: l'objet de la classe de middleware
        :rtype: RealEstateScraperSpiderMiddleware
        """
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        """
        Appelle lorsque le Spider reçoit une réponse à traiter.

        :param response: la réponse à traiter
        :type response: scrapy.http.Response
        :param spider: l'objet Spider
        :type spider: scrapy.spiders.Spider
        :return: None ou exception
        """
        return None

    def process_spider_output(self, response, result, spider):
        """
        Appelle lorsque le Spider a traité une réponse.

        :param response: la réponse traitée
        :type response: scrapy.http.Response
        :param result: les données de sortie du Spider
        :type result: list
        :param spider: l'objet Spider
        :type spider: scrapy.spiders.Spider
        :return: une liste d'objets Request ou de données
        """
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        """
        Appelle lorsque le Spider ou un autre middleware a émis une exception.

        :param response: la réponse
        :type response: scrapy.http.Response
        :param exception: l'exception émise
        :type exception: Exception
        :param spider: l'objet Spider
        :type spider: scrapy.spiders.Spider
        """
        pass

    def spider_opened(self, response, spider):
        """
        Appelle lorsque le spider est ouvert.

        :param response: la réponse
        :type response: scrapy.http.Response
        :param spider: l'objet Spider
        :type spider: scrapy.spiders.Spider
        """
        pass


class RealEstateScraperDownloaderMiddleware:
    """
    Cette classe de middleware s'assure que les données sont traitées correctement pour
    le scraper de biens immobiliers.
    """

    def process_request(self, request):
        """
        Appelle lorsque une requête est en cours de traitement.

        :param request: la requête à traiter
        :type request: scrapy.Request
        :return: None ou objet Request
        """
        return None

    def process_response(self, request, response, spider):
        """
        Appelle lorsque une réponse est reçue.

        :param request: la requête envoyée
        :type request: scrapy.Request
        :param response: la réponse reçue
        :type response: scrapy.Response
        :param spider: l'objet Spider
        :type spider: scrapy.Spiders.Spider
        :return: None ou objet Response
        """
        pass

    def process_exception(self, request, exception, spider):
        """
        Appelle lorsque une exception est émise.

        :param request: la requête
        :type request: scrapy.Request
        :param exception: l'exception émise
        :type exception: Exception
        :param spider: l'objet Spider
        :type spider: scrapy.spiders.Spider
        """
        pass

    def spider_opened(self, response, spider):
        """
        Appelle lorsque le spider est ouvert.

        :param response: la réponse
        :type response: scrapy.http.Response
        :param spider: l'objet Spider
        :type spider: scrapy.spiders.Spider
        """
        pass
```