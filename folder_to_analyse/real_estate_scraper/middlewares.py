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
        # This method is used by Scrapy to create your spiders.
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
        # Called for each response that goes through the spider
        # middleware and into the spider.
        # Should return None or raise an exception.
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
        # Called with the results returned from the Spider, after
        # it has processed the response.
        # Must return an iterable of Request, or item objects.
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
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.
        pass

    def spider_opened(self, response, spider):
        """
        Appelle lorsque le spider est ouvert.

        :param response: la réponse
        :type response: scrapy.http.Response
        :param spider: l'objet Spider
        :type spider: scrapy.spiders.Spider
        """
        # This hook function will be called for every response that is opened by
        # the Spider.
        pass


class RealEstateScraperDownloaderMiddleware:
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
        :rtype: RealEstateScraperDownloaderMiddleware
        """
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        """
        Appelle lorsque une requête est envoyée.

        :param request: la requête à envoyer
        :type request: scrapy.http.Request
        :param spider: l'objet Spider
        :type spider: scrapy.spiders.Spider
        :return: None ou objet Request
        """
        # Called for each request that goes through the downloader
        # middleware.
        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        """
        Appelle lorsque une réponse est reçue.

        :param request: la requête envoyée
        :type request: scrapy.http.Request
        :param response: la réponse reçue
        :type response: scrapy.http.Response
        :param spider: l'objet Spider
        :type spider: scrapy.spiders.Spider
        :return: None ou objet Response
        """
        # Called with the results returned from the Spider, after
        # it has processed the response.
        # Must return an iterable of Request, or item objects.
        pass

    def process_exception(self, request, exception, spider):
        """
        Appelle lorsque une exception est émise.

        :param request: la requête
        :type request: scrapy.http.Request
        :param exception: l'exception émise
        :type exception: Exception
        :param spider: l'objet Spider
        :type spider: scrapy.spiders.Spider
        """
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.
        pass

    def spider_opened(self, response, spider):
        """
        Appelle lorsque le spider est ouvert.

        :param response: la réponse
        :type response: scrapy.http.Response
        :param spider: l'objet Spider
        :type spider: scrapy.spiders.Spider
        """
        # This hook function will be called for every response that is opened by
        # the Spider.
        pass
```