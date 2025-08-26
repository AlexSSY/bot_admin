from sqlalchemy import inspect


models = {}
models_names = []


def register_model(sa_model_class):
    model_name = sa_model_class.__name__
    models[model_name] = sa_model_class
    models_names.append(model_name)


def get_readable_model_columns(sa_model_class):
    mapper = inspect(sa_model_class)
    return [column.key for column in mapper.columns]
