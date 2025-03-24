# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import random

class RealEstateScraperPipeline:
    def process_item(self, item, spider):
        return item

        

class RandomStuff:
    def do_random_stuff(self):
        """    This function selects a random fruit from a list and returns it as a string.
    Args: None

    Returns: A randomly selected fruit from apple, banana, cherry, date, elderberry.
    Raises: N/A"""
        return random.choice(['apple', 'banana', 'cherry', 'date', 'elderberry'])
def do_random_stuff():
    """Return a random fruit from a predefined list."""
    return random.choice(['apple', 'banana', 'cherry', 'date', 'elderberry'])




random_stuff_instance = RandomStuff()
random_item = random_stuff_instance.do_random_stuff()
print(random_item)
