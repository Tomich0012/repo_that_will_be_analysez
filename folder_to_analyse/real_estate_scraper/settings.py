```python
"""
Scrapy settings for real_estate_scraper project.

This file contains common Scrapy project settings. For simplicity, this file contains
only settings considered important or commonly used. You can find more settings
consulting the documentation:

    https://docs.scrapy.org/en/latest/topics/settings.html
    https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
    https://docs.scrapy.org/en/latest/topics/spider-middleware.html

For a complete list of available settings and their values, see:
https://docs.scrapy.org/en/latest/topics/settings.html
"""

BOT_NAME = "real_estate_scraper"
"""
The name of the bot that will be used in all generated data.

This is useful for debugging purposes or for identifying your scraper in
the logs produced by Scrapy.
"""

SPIDER_MODULES = ["real_estate_scraper.spiders"]
"""
List of Spider module names. This is usually only needed when you're building a new
Scrapy project from scratch.

If you're using an existing project, this should be left empty.
"""

NEWSPIDER_MODULE = "real_estate_scraper.spiders"
"""
Module name for NewSpider modules. This is usually empty for existing projects.
"""

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "real_estate_scraper (+http://www.yourdomain.com)"
"""
The User-Agent header used in HTTP requests made by Scrapy.

This is useful for debugging purposes or for identifying your scraper in the logs
produced by Scrapy.
"""

# Obey robots.txt rules
ROBOTSTXT_OBEY = True
"""
Whether to obey robots.txt rules when crawling.

If you want to crawl a website that specifies robots.txt, this should be set to `True`.
Otherwise, it will be ignored.
"""

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32
"""
The number of concurrent requests Scrapy should make at the same time.

Increasing this value can speed up your crawling process, but it may also increase
the load on the websites you're scraping and potentially cause them to block or
ban your IP address.
"""

# Configure a delay for requests for the same website (default: 0)
DOWNLOAD_DELAY = 3
"""
The number of seconds Scrapy should wait before sending another request to the
same website.

This can help prevent overwhelming the websites you're scraping and reduce the
load on their servers.
"""

# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 16
"""
The number of concurrent requests Scrapy should make to a domain or IP address.

Increasing these values can speed up your crawling process, but it may also increase
the load on the websites you're scraping and potentially cause them to block or
ban your IP address.
"""

# Disable cookies (enabled by default)
COOKIES_ENABLED = False
"""
Whether Scrapy should include or exclude cookies in its requests.

Setting this to `True` can help prevent websites from recognizing and blocking
your scraper, but it may also reduce the effectiveness of certain types of scraping.
"""

# Disable Telnet Console (enabled by default)
TELNETCONSOLE_ENABLED = False
"""
Whether the Telnet console should be enabled or disabled.

The Telnet console is a debugging tool that allows you to interact with Scrapy's
internal reactor. It's usually not needed for most users, but can be useful for
debugging purposes.
"""

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en",
}
"""
Custom request headers that should be sent with every request.

This can help prevent websites from recognizing and blocking your scraper, but it
may also reduce the effectiveness of certain types of scraping.
"""

# Enable or disable spider middlewares
SPIDER_MIDDLEWARES = {
    # "real_estate_scraper.middlewares.RealEstateScraperSpiderMiddleware": 543,
}
"""
Custom spider middlewares that should be enabled or disabled.

Spiders use middleware to customize their behavior and interact with other parts of
Scrapy. You can add your own custom middlewares here.
"""

# Enable or disable downloader middlewares
DOWNLOADER_MIDDLEWARES = {
    # "real_estate_scraper.middlewares.RealEstateScraperDownloaderMiddleware": 543,
}
"""
Custom downloader middlewares that should be enabled or disabled.

Downloader middleware is responsible for interacting with the Scrapy reactor and
downloading content from websites. You can add your own custom middlewares here.
"""

# Enable or disable extensions
EXTENSIONS = {
    # "scrapy.extensions.telnet.TelnetConsole": None,
}
"""
Custom extensions that should be enabled or disabled.

Extensions are reusable pieces of code that can enhance the behavior and functionality
of Scrapy. You can add your own custom extensions here.
"""

# Configure item pipelines
ITEM_PIPELINES = {
    # "real_estate_scraper.pipelines.RealEstateScraperPipeline": 300,
}
"""
Custom pipelines that should be enabled or disabled.

Pipelines are responsible for processing and transforming the data that Scrapy has
collected. You can add your own custom pipelines here.
"""

# The item pipeline will honor only one of:
CONCURRENT_ITEM_PIPELINES = {
    # "real_estate_scraper.pipelines.RealEstateScraperPipeline": 300,
}
"""
The number of concurrent items that the pipeline should process at the same time.

Increasing this value can speed up your processing, but it may also increase
the load on Scrapy and potentially cause it to become unresponsive.
"""

# The pipeline will honor only one of:
CONCURRENT_ITEM_PIPELINES = {
    # "real_estate_scraper.pipelines.RealEstateScraperPipeline": 300,
}

# The error handler will honor only one of:
CONCURRENT_ERROR_HANDLE = {
    # "real_estate_scraper.pipelines.ErrorHandler": 500,
}
"""
The number of concurrent errors that the pipeline should handle at the same time.

Increasing this value can speed up your processing, but it may also increase
the load on Scrapy and potentially cause it to become unresponsive.
"""

# The error handler will honor only one of:
CONCURRENT_ERROR_HANDLE = {
    # "real_estate_scraper.pipelines.ErrorHandler": 500,
}

# Whether the pipeline should be enabled or disabled.
ENABLED = True
"""
Whether the pipeline should be enabled or disabled.

Setting this to `True` can help you test and debug your pipeline, but it may also
reduce its effectiveness when used in production.
"""

# The number of concurrent errors that the pipeline will handle at the same time.
MAX_ERROR_HANDLE = 500
"""
The maximum number of concurrent errors that the pipeline should handle.

Increasing this value can speed up your processing, but it may also increase
the load on Scrapy and potentially cause it to become unresponsive.
"""

# Whether the pipeline should be enabled or disabled.
PIPELINE_ENABLED = True
"""
Whether the pipeline should be enabled or disabled.

Setting this to `True` can help you test and debug your pipeline, but it may also
reduce its effectiveness when used in production.
"""

# The number of concurrent errors that the pipeline will handle at the same time.
CONCURRENT_ERROR_HANDLE = 500
"""
The maximum number of concurrent errors that the pipeline should handle.

Increasing this value can speed up your processing, but it may also increase
the load on Scrapy and potentially cause it to become unresponsive.
"""

# Whether the pipeline should be enabled or disabled.
ENABLED = True
"""
Whether the pipeline should be enabled or disabled.

Setting this to `True` can help you test and debug your pipeline, but it may also
reduce its effectiveness when used in production.
"""