import datetime
from random import randint, choice

from factory import LazyAttribute, LazyFunction, Sequence, SubFactory
from factory.django import DjangoModelFactory, ImageField
from faker import Faker

from blog.models import Post, Comment, RateOfComment
from core.settings import AUTH_USER_MODEL

delta = datetime.timedelta
now = datetime.datetime.now

fake = Faker('ru')


class UserFactory(DjangoModelFactory):
    class Meta:
        model = AUTH_USER_MODEL

    email = LazyAttribute(lambda o: '{username}@123.com'.format(username=o.username))
    first_name = LazyFunction(fake.first_name)
    last_name = LazyFunction(fake.last_name)
    username = Sequence(lambda n: '{}{}'.format(fake.user_name(), n))


class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post

    author = SubFactory(UserFactory)
    title = LazyFunction(lambda: fake.text(randint(5, 20)))
    picture = ImageField(color=choice(['blue', 'yellow', 'green', 'orange']),
                         height=randint(250, 1000),
                         width=randint(250, 1000),
                         )
    text = LazyFunction(lambda: fake.text(randint(20, 500)))
    created_at = LazyFunction(lambda: now() - delta(days=365))


class CommentFactory(DjangoModelFactory):
    class Meta:
        model = Comment

    author = SubFactory(UserFactory)
    post = SubFactory(PostFactory)
    text = LazyFunction(lambda: fake.text(randint(20, 500)))
    created_at = LazyFunction(lambda: now() - delta(days=365))


class RateOfCommentFactory(DjangoModelFactory):
    class Meta:
        model = RateOfComment

    author = SubFactory(UserFactory)
    comment = SubFactory(CommentFactory)
    opinion = LazyFunction(lambda: choice(['P', 'N']))
    created_at = LazyFunction(lambda: now() - delta(days=365))


# class ShopFactory(DjangoModelFactory):
#     class Meta:
#         model = Shop
#
#     user = SubFactory(UserFactory)
#
#     name = LazyFunction(lambda: fake.text(randint(5, 20)))
#     content = LazyFunction(lambda: fake.text(randint(20, 500)))
#     created = LazyFunction(lambda: now() - delta(days=365))
#     updated = LazyAttribute(lambda o: o.created + delta(days=randint(0, 365)))