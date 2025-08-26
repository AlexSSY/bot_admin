from sqlalchemy import inspect

import config


models = {}
models_names = []


def register_model(sa_model_class):
    model_name = sa_model_class.__name__
    models[model_name] = sa_model_class
    models_names.append(model_name)


def get_sa_model_by_name(sa_model_name):
    return models.get(sa_model_name)


def get_readable_model_columns(sa_model_class):
    mapper = inspect(sa_model_class)
    return [column.key for column in mapper.columns]


def get_editable_model_columns(sa_model_class):
    mapper = inspect(sa_model_class)
    return [
        column.key for column
        in mapper.columns
        if column.key not in config.ADMIN.get('READONLY_FIELDS')
    ]
