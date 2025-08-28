import telebot
from telebot.types import Message, CallbackQuery

import config
import keyboards
from models import Employee, Slut
import admin
import crud
import session


admin.register_model(Employee)
admin.register_model(Slut)


bot = telebot.TeleBot(config.BOT_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")
	

@bot.message_handler(commands=['admin'])
def admin_command_handler(message):
	bot.reply_to(
		message,
		'Welcome to admin toolkit.',
		reply_markup=keyboards.gen_kb_for_models()
	)
	

@bot.callback_query_handler(lambda call: call.data == 'amodels')
def admin_models_handler(call):
	bot.edit_message_text(
		'Welcome to admin toolkit.',
		call.message.chat.id,
		call.message.id,
        reply_markup=keyboards.gen_kb_for_models()
    )
	

@bot.callback_query_handler(lambda call: call.data.startswith('am='))
def admin_model_handler(call):
	_, sa_model_name = call.data.split('=', 2)
	bot.edit_message_text(
		f'Records for model: {sa_model_name}',
		call.message.chat.id,
		call.message.id,
		reply_markup=keyboards.gen_kb_for_records(sa_model_name, 'amodels')
	)
	

@bot.callback_query_handler(lambda call: call.data.startswith('amd='))
def admin_model_detail_handler(call):
	_, sa_model_name, id = call.data.split('=', 3)
	sa_model_class = admin.get_sa_model_by_name(sa_model_name)
	sa_model_instance = crud.detail(sa_model_class, id)
	column_names = admin.get_readable_model_columns(sa_model_class)
	text = ''
	for column_name in column_names:
		text += f"{column_name}: {getattr(sa_model_instance, column_name)}\n"
	bot.edit_message_text(
		text,
		call.message.chat.id,
		call.message.id,
		reply_markup=keyboards.gen_kb_for_record_detail(sa_model_name, id)
    )


@bot.callback_query_handler(lambda call: call.data.startswith('ame='))
def admin_model_edit_handler(call):
	_, sa_model_name, id = call.data.split('=', 3)
	sa_model_class = admin.get_sa_model_by_name(sa_model_name)
	editable_field_names = admin.get_editable_model_columns(sa_model_class)
	editable_fields_length = len(editable_field_names)

	if editable_fields_length == 0:
		bot.reply_to(call.message, 'Nothing to edit.')
		return
	
	user_id = call.message.from_user.id
	session.store(user_id)
	bot.reply_to(call.message, f'Enter: {editable_field_names[0]}')


@bot.message_handler(func=lambda m: True)
def any_message_handler(message: Message):
	user_id = message.from_user.id
	stack = session.get_user_stack(user_id)

	while not stack.is_empty():
		stack.pop()


if __name__ == '__main__':
    bot.infinity_polling()
