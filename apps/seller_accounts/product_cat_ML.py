from django.shortcuts import render
import joblib
import os

gender_list = ['Men', 'Women', 'Boys', 'Girls', 'Unisex' ]
subCat_list = ['Topwear', 'Bottomwear', 'Dress', 'Saree', 'Shoes', 'Innerwear', 'Headwear', 'Socks', 'Flip Flops']
all_articel_type_list = ['Belts', 'Blazers', 'Booties', 'Boxers', 'Bra', 'Briefs', 'Camisoles', 'Capris', 'Caps', 'Casual Shoes', 'Churidar', 'Dresses', 'Dupatta', 'Flats', 'Flip Flops', 'Formal Shoes', 'Hat', 'Headband', 'Heels', 'Innerwear Vests', 'Jackets', 'Jeans', 'Jeggings', 'Jumpsuit', 'Kurtas', 'Kurtis', 'Leggings', 'Lehenga Choli', 'Nehru Jackets', 'Patiala', 'Rain Jacket', 'Rain Trousers', 'Rompers', 'Salwar', 'Salwar and Dupatta', 'Sandals', 'Sarees', 'Shapewear', 'Shirts', 'Shorts', 'Shrug', 'Skirts', 'Socks', 'Sports Shoes', 'Stockings', 'Suits', 'Suspenders', 'Sweaters', 'Sweatshirts', 'Swimwear', 'Tights', 'Tops', 'Track Pants', 'Tracksuits', 'Trousers', 'Trunk', 'Tshirts', 'Tunics', 'Waistcoat']

top_men_articel_type_list = ['Belts', 'Blazers', 'Dresses', 'Dupatta', 'Jackets', 'Kurtas', 'Kurtis', 'Lehenga Choli', 'Nehru Jackets', 'Rain Jacket', 'Rompers', 'Shirts', 'Shrug', 'Suits', 'Suspenders', 'Sweaters', 'Sweatshirts', 'Tops', 'Tshirts', 'Tunics', 'Waistcoat']
bottom_men_articel_type_list = ['Capris', 'Churidar', 'Jeans', 'Leggings', 'Rain Trousers', 'Shorts', 'Swimwear', 'Tights', 'Track Pants', 'Tracksuits', 'Trousers']
top_women_articel_type_list = ['Blazers', 'Dresses', 'Dupatta', 'Jackets', 'Kurtas', 'Kurtis', 'Lehenga Choli', 'Rain Jacket', 'Rompers', 'Shirts', 'Shrug', 'Sweaters', 'Sweatshirts', 'Tops', 'Tshirts', 'Tunics', 'Waistcoat']
bottom_women_articel_type_list = ['Capris', 'Churidar', 'Jeans', 'Jeggings', 'Leggings', 'Patiala', 'Salwar', 'Salwar and Dupatta', 'Shorts', 'Skirts', 'Stockings', 'Swimwear', 'Tights', 'Track Pants', 'Tracksuits', 'Trousers']

extra_articel_type_list = ['Booties', 'Boxers', 'Bra', 'Briefs', 'Camisoles', 'Caps', 'Casual Shoes', 'Dresses', 'Flats', 'Flip Flops', 'Formal Shoes', 'Hat', 'Headband', 'Heels', 'Innerwear Vests', 'Jumpsuit', 'Sandals', 'Sarees', 'Shapewear', 'Socks', 'Sports Shoes', 'Trunk']

mlModelsFiles = {"gender_model":"lvl1_gender_cat.sav","sub_cat":"lvl2_sub_cat.sav","articel_type":"lvl3_articelType_cat.sav","top_men":"lvl3_men_top_cat_new.sav","top_women":"lvl3_top_women_cat.sav","bottom_men":"lvl3_bottom_men_cat.sav","bottom_women":"lvl3_bottom_women_cat.sav","extra_articel_type":"lvl3_extra_articel_type.sav"}

def get_ml_model_file_path(filename):
    module_dir = os.path.dirname(__file__)   #get current directory
    file_path = os.path.join(module_dir,'ml_models', filename)   #full path to text.
    return file_path

def get_product_cat(product_name):
    product_name_list = []
    product_name_list.append(product_name)

    lvl1_gender_cat_model = joblib.load(get_ml_model_file_path(mlModelsFiles['gender_model']))
    lvl2_sub_cat_model = joblib.load(get_ml_model_file_path(mlModelsFiles['sub_cat']))
    # lvl3_articelType_cat_model = joblib.load(get_ml_model_file_path(mlModelsFiles['articel_type']))

    lvl3_top_men_cat_model = joblib.load(get_ml_model_file_path(mlModelsFiles['top_men']))
    lvl3_top_women_cat_model = joblib.load(get_ml_model_file_path(mlModelsFiles['top_women']))
    lvl3_bottom_men_cat_model = joblib.load(get_ml_model_file_path(mlModelsFiles['bottom_men']))
    lvl3_bottom_women_cat_model = joblib.load(get_ml_model_file_path(mlModelsFiles['bottom_women']))

    lvl3_extra_articel_type_model = joblib.load(get_ml_model_file_path(mlModelsFiles['extra_articel_type']))

    lvl1_gender_cat = lvl1_gender_cat_model.predict(product_name_list)
    lvl2_sub_cat = lvl2_sub_cat_model.predict(product_name_list)

    lvl3_articel_cat = ""
    if gender_list[lvl1_gender_cat[0]] == ("Men" or "Boys" or "Unisex") :
        if subCat_list[lvl2_sub_cat[0]] == "Topwear":
            lvl3_men_top_cat = lvl3_top_men_cat_model.predict(product_name_list)
            lvl3_articel_cat = top_men_articel_type_list[lvl3_men_top_cat[0]]
        elif subCat_list[lvl2_sub_cat[0]] == "Bottomwear":
            lvl3_men_bottom_cat = lvl3_bottom_men_cat_model.predict(product_name_list)
            lvl3_articel_cat = bottom_men_articel_type_list[lvl3_men_bottom_cat[0]]
        else:
            lvl3_articelType_cat = lvl3_extra_articel_type_model.predict(product_name_list)
            lvl3_articel_cat = extra_articel_type_list[lvl3_articelType_cat[0]]
    elif gender_list[lvl1_gender_cat[0]] == ("Women" or "Girls" or "Unisex"):
        if subCat_list[lvl2_sub_cat[0]] == "Topwear":
            lvl3_women_top_cat = lvl3_top_women_cat_model.predict(product_name_list)
            lvl3_articel_cat = top_women_articel_type_list[lvl3_women_top_cat[0]]
        elif subCat_list[lvl2_sub_cat[0]] == "Bottomwear":
            lvl3_women_bottom_cat = lvl3_bottom_women_cat_model.predict(product_name_list)
            lvl3_articel_cat = bottom_women_articel_type_list[lvl3_women_bottom_cat[0]]
        else:
            lvl3_articelType_cat = lvl3_extra_articel_type_model.predict(product_name_list)
            lvl3_articel_cat = extra_articel_type_list[lvl3_articelType_cat[0]]

    product_cat = {'gender':gender_list[lvl1_gender_cat[0]],'sub_cat':subCat_list[lvl2_sub_cat[0]],'articel_type':lvl3_articel_cat}

    return product_cat
