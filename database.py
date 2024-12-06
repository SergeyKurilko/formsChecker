from tinydb import TinyDB, Query

db = TinyDB('form_templates.json')
Template = Query()

def get_templates():
    """
    Возвращает все шаблоны форм из form_templates.json
    """
    return db.all()



