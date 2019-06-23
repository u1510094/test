class TransferRouter:

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'old_myjob':
            return 'old_myjob'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'old_myjob':
            return 'old_myjob'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if not obj1._meta.app_label == 'old_myjob' and not obj2._meta.app_label == 'old_myjob':
            return True
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label != 'old_myjob':
            return True
        return False
