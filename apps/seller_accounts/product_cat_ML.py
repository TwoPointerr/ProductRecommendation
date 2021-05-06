from django.shortcuts import render
import joblib
import os

gender_list = ['Men', 'Women', 'Boys', 'Girls', 'Unisex' ]
subCat_list = ['Topwear', 'Bottomwear', 'Dress', 'Saree', 'Shoes', 'Innerwear', 'Headwear', 'Socks', 'Flip Flops']
all_articel_type_list = ['Belts', 'Blazers', 'Booties', 'Boxers', 'Bra', 'Briefs', 'Camisoles', 'Capris', 'Caps', 'Casual Shoes', 'Churidar', 'Dresses', 'Dupatta', 'Flats', 'Flip Flops', 'Formal Shoes', 'Hat', 'Headband', 'Heels', 'Innerwear Vests', 'Jackets', 'Jeans', 'Jeggings', 'Jumpsuit', 'Kurtas', 'Kurtis', 'Leggings', 'Lehenga Choli', 'Nehru Jackets', 'Patiala', 'Rain Jacket', 'Rain Trousers', 'Rompers', 'Salwar', 'Salwar and Dupatta', 'Sandals', 'Sarees', 'Shapewear', 'Shirts', 'Shorts', 'Shrug', 'Skirts', 'Socks', 'Sports Shoes', 'Stockings', 'Suits', 'Suspenders', 'Sweaters', 'Sweatshirts', 'Swimwear', 'Tights', 'Tops', 'Track Pants', 'Tracksuits', 'Trousers', 'Trunk', 'Tshirts', 'Tunics', 'Waistcoat']

mlModelsFiles = {"gender_model":"lvl1_gender_cat.sav","sub_cat":"lvl2_sub_cat.sav","articel_type":"lvl3_articelType_cat.sav"}

def get_ml_model_file_path(filename):
    module_dir = os.path.dirname(__file__)   #get current directory
    file_path = os.path.join(module_dir, filename)   #full path to text.
    return file_path

def get_product_cat(product_name):
    product_name_list = []
    product_name_list.append(product_name)

    lvl1_gender_cat_model = joblib.load(get_ml_model_file_path(mlModelsFiles['gender_model']))
    lvl2_sub_cat_model = joblib.load(get_ml_model_file_path(mlModelsFiles['sub_cat']))
    lvl3_articelType_cat_model = joblib.load(get_ml_model_file_path(mlModelsFiles['articel_type']))

    lvl1_gender_cat = lvl1_gender_cat_model.predict(product_name_list)
    lvl2_sub_cat = lvl2_sub_cat_model.predict(product_name_list)
    lvl3_articelType_cat = lvl3_articelType_cat_model.predict(product_name_list)
    product_cat = {'gender':gender_list[lvl1_gender_cat[0]],'sub_cat':subCat_list[lvl2_sub_cat[0]],'articel_type':all_articel_type_list[lvl3_articelType_cat[0]]}

    return product_cat
