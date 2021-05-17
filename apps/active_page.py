from django.conf import settings # import the settings file

active_page = settings.ACTIVE_PAGE

def admin_media(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return active_page

def set_page_active(page_name):
    if active_page[page_name] != "active":
        active_page[page_name] = "active"
        for page, status in active_page.items():
            if page != page_name:
                active_page[page] = ""
        settings.ACTIVE_PAGE = active_page
    


