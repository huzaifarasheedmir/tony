"""
~~~~~~~~~~~~~~~~~
models.products_models.py

Park products related models
~~~~~~~~~~~~~~~~~
"""

from datetime import datetime

from mongoengine import (
    CASCADE,
    DateTimeField,
    DynamicDocument,
    ListField,
    ReferenceField,
    StringField,
    FloatField,
    IntField,
)


class Categories(DynamicDocument):
    """
    Purposed model for Categories
    # todo research
    """

    name = StringField()
    sub_categories = ListField(StringField(), default=[])


class Product(DynamicDocument):
    """
    Model for product details

    source_product_id would be the id comming from the source
    rating_score is the prediction socre provided by classifier
    """

    meta = {
        # 'shard_key': ('added_at', 'category'),
        "indexes": [
            # 'added_at',  #indexed for sharding purposes for clustered environment
            # 'category', #indexed for sharding purposes for clustered environment
            {"fields": ("source", "source_product_id"), "unique": True},
            {
                "fields": ["$name", "$sub_categories"],
                "default_language": "english",
                "weights": {"name": 10, "sub_categories": 5},
            },
        ]
    }
    name = StringField()
    asin = StringField()
    category = StringField(required=True)
    sub_categories = StringField()
    source_product_id = StringField(required=True)
    brand = StringField()
    rating_score = FloatField()
    manufacturer = StringField()
    added_at = DateTimeField(required=True, default=datetime.utcnow())
    reviews = ListField(ReferenceField("Review"))
    source = StringField(required="Amazon")


class Review(DynamicDocument):
    """
    Model for Review stats

    If source doesnt provide review id calculate sha from review text
    Sha can also be used for change detection
    """

    meta = {"indexes": [{"fields": ("source", "source_review_id"), "unique": True},]}

    source_review_id = StringField(unique=True, required=True)
    rating = IntField()
    score = FloatField(required=True)
    sha = (
        StringField()
    )  # calculate sha by combining review text, rating and source in case id is provided
    date = DateTimeField(required=True, default=datetime.utcnow())
    source = StringField(required="Amazon")
    product = ReferenceField(Product, reverse_delete_rule=CASCADE, required=True)

    def save(self, **kwargs):
        super(Review, self).save(**kwargs)
        self.product.reviews.append(self)
        self.product.save()
