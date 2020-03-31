from Postapp.settings import DATABASE_APPS_MAPPING

class MyRouter(object):
    def db_for_read(self, model, **hints):
        return DATABASE_APPS_MAPPING.get(model._meta.app_label, 'default')

    def db_for_write(self, model, **hints):
        return DATABASE_APPS_MAPPING.get(model._meta.app_label, 'default')

    