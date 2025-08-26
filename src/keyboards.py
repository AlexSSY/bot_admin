import pagination
import config
import admin
import crud


from telebot.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)


def gen_kb_for_models():
    per_page = config.ADMIN.get('MODELS_PER_PAGE')
    total = len(admin.models) 
    offset, limit = pagination.paginate(total, per_page, 1)
    models_to_display = admin.models_names[offset:offset + limit]
    
    buttons = [
        [InlineKeyboardButton(m, callback_data=f'admin:{m}')]
        for m in models_to_display
    ]

    return InlineKeyboardMarkup(buttons)


def gen_kb_for_records(sa_model_name, back_callback_data):
    sa_model_class = admin.models[sa_model_name]
    per_page = config.ADMIN.get('RECORDS_PER_PAGE')
    total = crud.count(sa_model_class)
    offset, limit = pagination.paginate(total, per_page, 1)
    records_to_display = crud.rows(sa_model_class, limit, offset)

    buttons = [
        [InlineKeyboardButton(str(m), callback_data=f'amd={sa_model_name}={m.id}')]
        for m in records_to_display
    ]

    buttons.append(
        [InlineKeyboardButton('<- Back --<', callback_data=back_callback_data)]
    )

    return InlineKeyboardMarkup(buttons)


def gen_kb_for_record_detail(sa_model_name, id):
    buttons = [
        [InlineKeyboardButton('Edit', callback_data=f'ame={sa_model_name}={id}')],
        [InlineKeyboardButton('<- Back --<', callback_data=f'am={sa_model_name}')]
    ]

    return InlineKeyboardMarkup(buttons)
