"""
~~~~~~~~~~~~~~~~~
dao.product_service.py

Park Product model related db interactions here
~~~~~~~~~~~~~~~~~
"""

import logging
from models.product_models import Product, Review
from models.utils import catch_mongo_exceptions

logger = logging.getLogger("dao.product_service")


class ProductService:
    def __init__(self):
        self.products = Product
        self.review = Review

    @catch_mongo_exceptions
    def add_product(self, product_dict):
        """Add product using provided dict"""

        return Product(**product_dict).save()

    def get_review_by_id(self, source, source_id):
        """Get a review by id amd source"""

        review = Review.objects(source=source, source_review_id=source_id).get()
        if review:
            return review

    @catch_mongo_exceptions
    def add_from_template(self, template):
        """Add product and reviews using provided template"""

        reviews = template["reviews"]
        del template["reviews"]
        product = self.add_product(template)
        Review.objects.insert([Review(**review, product=product) for review in reviews])

    def aggregate_product_rating_score(self, source_id):
        """Aggregate and update product rating score"""

        product = Product.objects(source_product_id=source_id).get()
        if not product:
            return
        score = Review.objects(product=product).average("score")
        product.score = score
        product.save()
