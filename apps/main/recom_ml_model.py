import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

from apps.cart.models import *

def join_tuple_string(strings_tuple) -> str:
   return ' '.join(strings_tuple)

def get_feature_products():
    product_list = list(Product.objects.values_list('title','description','gender_cat'))
    result = list(map(join_tuple_string, product_list))
    return result

def get_products_with_id():
    feature_product = get_feature_products()
    all_products_id = list(Product.objects.values_list('id',flat=True))
    products_with_id = {}
    for index,id in enumerate(all_products_id):
        products_with_id[id] = feature_product[index]
    return products_with_id


def similar_products(product_id,no_similar_prod):
    all_products = get_feature_products()
    all_products_id = list(Product.objects.values_list('id',flat=True))
    cm = CountVectorizer().fit_transform(all_products)
    cs = cosine_similarity(cm)
    product_index = all_products_id.index(product_id)
    unsorted_similar_product = list(enumerate(cs[product_index]))
    sorted_similar_product = sorted(unsorted_similar_product, key=lambda x:x[1], reverse=True)
    similar_products_query_set = []
    temp=0
    for product in sorted_similar_product:
        similar_products_query_set.append(Product.objects.get(id=all_products_id[product[0]]))
        temp=temp+1
        if temp>no_similar_prod:
            break
    
    return similar_products_query_set[1:]


    