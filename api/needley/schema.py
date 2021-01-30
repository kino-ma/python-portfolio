from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

import graphene

from .models import User, Article


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        filter_fields = ['name', 'nickname', 'avator',
                         'created_at', 'updated_at', 'articles']
        interfaces = (relay.Node, )


class ArticleNode(DjangoObjectType):
    class Meta:
        model = Article
        filter_fields = {
            'author': ['exact'],
            'title': ['exact', 'icontains'],
            'content': ['exact', 'icontains'],
            'created_at': ['exact', 'lt', 'gt'],
            'updated_at': ['exact', 'lt', 'gt'],
        }
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")




schema = graphene.Schema(query=Query)