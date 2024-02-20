from aiogram import Bot,types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

tg_bot_token = "6522757967:AAH0pF4mkSTJ4HtRg1PUFGBEgffieVOgzGk"

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):

    main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
    catalog = KeyboardButton("каталог 🛒")
    about = KeyboardButton("о нас 🔍")
    contacts = KeyboardButton("контакты 📞")
    main_menu.add(catalog, about, contacts)

    await message.answer("тут будет инструкция к боту",reply_markup= main_menu)

@dp.message_handler(lambda message: message.text == "каталог 🛒")
async def catalog(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=1)
    razmer_1 = InlineKeyboardButton(text="2.4 x 2.4", callback_data="razmer_1")
    razmer_2 = InlineKeyboardButton(text="3.0 x 2.4", callback_data="razmer_2")
    razmer_3 = InlineKeyboardButton(text="4.0 x 2.4", callback_data="razmer_3")
    razmer_4 = InlineKeyboardButton(text="6.0 x 2.4", callback_data="razmer_4")
    razmer_5 = InlineKeyboardButton(text="6.0 x 4.8(модульная)", callback_data="razmer_5")
    razmer_6 = InlineKeyboardButton(text="8.0 x 2.4", callback_data="razmer_6")
    razmer_7 = InlineKeyboardButton(text="9.0 x 2.4", callback_data="razmer_7")
    razmer_8 = InlineKeyboardButton(text="12.0 x 2.4", callback_data="razmer_8")

    keyboard.add(razmer_1, razmer_2, razmer_3, razmer_4, razmer_5, razmer_6, razmer_7, razmer_8)
    await message.answer("пожайлуста выбирите габариты бытовки📐", reply_markup=keyboard)
#######################################################################
@dp.callback_query_handler(lambda c: c.data == 'razmer_1')
async def tambur_1(message: types.Message):
    ikb = InlineKeyboardMarkup(row_width=1)
    tambur_net_1 = InlineKeyboardButton(text="бытовка без тамбура", callback_data="tambur_net_1")
    tambur_da_1 = InlineKeyboardButton(text="бытовка с тамбуром", callback_data="tambur_da_1")
    ikb.add(tambur_net_1,tambur_da_1 )
    await bot.send_message(message.from_user.id, "хорошо вы выбрыли площадь: 2.0 x 2.4 А теперь, пожалуйста, ответьте на несколько вопросов, Вам бы хотелось, чтобы в бытовке был тамбур?",reply_markup= ikb)

@dp.callback_query_handler(lambda c: c.data == 'razmer_2')
async def tambur_2(message: types.Message):
    ikb = InlineKeyboardMarkup(row_width=1)
    tambur_net_2 = InlineKeyboardButton(text="бытовка без тамбура", callback_data="tambur_net_2")
    tambur_da_2= InlineKeyboardButton(text="бытовка с тамбуром", callback_data="tambur_da_2")
    ikb.add(tambur_net_2, tambur_da_2)
    await bot.send_message(message.from_user.id,"хорошо вы выбрыли площадь: 3.0 x 2.4 А теперь, пожалуйста, ответьте на несколько вопросов, Вам бы хотелось, чтобы в бытовке был тамбур?",reply_markup=ikb)

@dp.callback_query_handler(lambda c: c.data == 'razmer_3')
async def tambur_3(message: types.Message):
    ikb = InlineKeyboardMarkup(row_width=1)
    tambur_net_3 = InlineKeyboardButton(text="бытовка без тамбура", callback_data="tambur_net_3")
    tambur_da_3 = InlineKeyboardButton(text="бытовка с тамбуром", callback_data="tambur_da_3")
    ikb.add(tambur_net_3, tambur_da_3)
    await bot.send_message(message.from_user.id,"хорошо вы выбрыли площадь: 4.0 x 2.4 А теперь, пожалуйста, ответьте на несколько вопросов, Вам бы хотелось, чтобы в бытовке был тамбур?",reply_markup=ikb)

@dp.callback_query_handler(lambda c: c.data == 'razmer_4')
async def tambur_4(message: types.Message):
    ikb = InlineKeyboardMarkup(row_width=1)
    tambur_net_4 = InlineKeyboardButton(text="бытовка без тамбура", callback_data="tambur_net_4")
    tambur_da_4 = InlineKeyboardButton(text="бытовка с тамбуром", callback_data="tambur_da_4")
    ikb.add(tambur_net_4, tambur_da_4)
    await bot.send_message(message.from_user.id,"хорошо вы выбрыли площадь: 6.0 x 2.4 А теперь, пожалуйста, ответьте на несколько вопросов, Вам бы хотелось, чтобы в бытовке был тамбур?",reply_markup=ikb)

@dp.callback_query_handler(lambda c: c.data == 'razmer_5')
async def tambur_5(message: types.Message):
    ikb = InlineKeyboardMarkup(row_width=1)
    tambur_net_5 = InlineKeyboardButton(text="бытовка без тамбура", callback_data="tambur_net_5")
    tambur_da_5 = InlineKeyboardButton(text="бытовка с тамбуром", callback_data="tambur_da_5")
    ikb.add(tambur_net_5, tambur_da_5)
    await bot.send_message(message.from_user.id,"хорошо вы выбрыли площадь: 6.0 x 4.8 А теперь, пожалуйста, ответьте на несколько вопросов, Вам бы хотелось, чтобы в бытовке был тамбур?",reply_markup=ikb)

@dp.callback_query_handler(lambda c: c.data == 'razmer_6')
async def tambur_6(message: types.Message):
    ikb = InlineKeyboardMarkup(row_width=1)
    tambur_net_6 = InlineKeyboardButton(text="бытовка без тамбура", callback_data="tambur_net_6")
    tambur_da_6 = InlineKeyboardButton(text="бытовка с тамбуром", callback_data="tambur_da_6")
    ikb.add(tambur_net_6, tambur_da_6)
    await bot.send_message(message.from_user.id,"хорошо вы выбрыли площадь: 8.0 x 2.4 А теперь, пожалуйста, ответьте на несколько вопросов, Вам бы хотелось, чтобы в бытовке был тамбур?",reply_markup=ikb)

@dp.callback_query_handler(lambda c: c.data == 'razmer_7')
async def tambur_7(message: types.Message):
    ikb = InlineKeyboardMarkup(row_width=1)
    tambur_net_7 = InlineKeyboardButton(text="бытовка без тамбура", callback_data="tambur_net_7")
    tambur_da_7 = InlineKeyboardButton(text="бытовка с тамбуром", callback_data="tambur_da_7")
    ikb.add(tambur_net_7, tambur_da_7)
    await bot.send_message(message.from_user.id,"хорошо вы выбрыли площадь: 9.0 x 2.4 А теперь, пожалуйста, ответьте на несколько вопросов, Вам бы хотелось, чтобы в бытовке был тамбур?.",reply_markup=ikb)

@dp.callback_query_handler(lambda c: c.data == 'razmer_8')
async def tambur_8(message: types.Message):
    ikb = InlineKeyboardMarkup(row_width=1)
    tambur_net_8 = InlineKeyboardButton(text="бытовка без тамбура", callback_data="tambur_net_8")
    tambur_da_8 = InlineKeyboardButton(text="бытовка с тамбуром", callback_data="tambur_da_8")
    ikb.add(tambur_net_8, tambur_da_8)
    await bot.send_message(message.from_user.id,"хорошо вы выбрыли площадь: 12.0 x 2.4 А теперь, пожалуйста, ответьте на несколько вопросов, Вам бы хотелось, чтобы в бытовке был тамбур?.",reply_markup=ikb)









@dp.callback_query_handler(lambda c: c.data == 'tambur_net_1')
async def electro_1(message: types.Message):
    pepsiKeyboard = InlineKeyboardMarkup(row_width=1)
    electro_net_1 = InlineKeyboardButton(text="бытовка без электроники", callback_data="electro_net_1")
    electro_da_1 = InlineKeyboardButton(text="бытовка с электроникой", callback_data="electro_da_1")
    pepsiKeyboard.add(electro_net_1, electro_da_1)
    await bot.send_message(message.from_user.id," Ладно, обойдемся без тамбура. А теперь ответьте пожайлуста Вам бы хотелось оборудовать свою бытовку электропроводкой?",reply_markup=pepsiKeyboard)

@dp.callback_query_handler(lambda c: c.data == 'tambur_da_1')
async def electro_2(message: types.Message):
    pepsiKeyboard = InlineKeyboardMarkup(row_width=1)
    electro_net_2 = InlineKeyboardButton(text="бытовка без электроники", callback_data="electro_net_2")
    electro_da_2 = InlineKeyboardButton(text="бытовка с электроникой", callback_data="electro_da_2")
    pepsiKeyboard.add(electro_net_2, electro_da_2)
    await bot.send_message(message.from_user.id," Вам бы хотелось оборудовать свою бытовку электропроводкой?",reply_markup=pepsiKeyboard)




@dp.callback_query_handler(lambda c: c.data == 'tambur_net_2')
async def electro_3(message: types.Message):
    pepsiKeyboard = InlineKeyboardMarkup(row_width=1)
    electro_net_3 = InlineKeyboardButton(text="бытовка без электроники", callback_data="electro_net_3")
    electro_da_3 = InlineKeyboardButton(text="бытовка с электроникой", callback_data="electro_da_3")
    pepsiKeyboard.add(electro_net_3, electro_da_3)
    await bot.send_message(message.from_user.id," Ладно, обойдемся без тамбура. А теперь ответьте пожайлуста Вам бы хотелось оборудовать свою бытовку электропроводкой?",reply_markup=pepsiKeyboard)

@dp.callback_query_handler(lambda c: c.data == 'tambur_da_2')
async def electro_4(message: types.Message):
    pepsiKeyboard = InlineKeyboardMarkup(row_width=1)
    electro_net_4 = InlineKeyboardButton(text="бытовка без электроники", callback_data="electro_net_4")
    electro_da_4 = InlineKeyboardButton(text="бытовка с электроникой", callback_data="electro_da_4")
    pepsiKeyboard.add(electro_net_4, electro_da_4)
    await bot.send_message(message.from_user.id," Вам бы хотелось оборудовать свою бытовку электропроводкой?",reply_markup=pepsiKeyboard)




@dp.callback_query_handler(lambda c: c.data == 'tambur_net_3')
async def electro_5(message: types.Message):
    pepsiKeyboard = InlineKeyboardMarkup(row_width=1)
    electro_net_5 = InlineKeyboardButton(text="бытовка без электроники", callback_data="electro_net_5")
    electro_da_5 = InlineKeyboardButton(text="бытовка с электроникой", callback_data="electro_da_5")
    pepsiKeyboard.add(electro_net_5, electro_da_5)
    await bot.send_message(message.from_user.id,"Ладно, обойдемся без тамбура. А теперь ответьте пожайлуста Вам бы хотелось оборудовать свою бытовку электропроводкой?",reply_markup=pepsiKeyboard)

@dp.callback_query_handler(lambda c: c.data == 'tambur_da_3')
async def electro_6(message: types.Message):
    pepsiKeyboard = InlineKeyboardMarkup(row_width=1)
    electro_net_6 = InlineKeyboardButton(text="бытовка без электроники", callback_data="electro_net_6")
    electro_da_6 = InlineKeyboardButton(text="бытовка с электроникой", callback_data="electro_da_6")
    pepsiKeyboard.add(electro_net_6, electro_da_6)
    await bot.send_message(message.from_user.id,"Вам бы хотелось оборудовать свою бытовку электропроводкой?",reply_markup=pepsiKeyboard)




@dp.callback_query_handler(lambda c: c.data == 'tambur_net_4')
async def electro_7(message: types.Message):
    pepsiKeyboard = InlineKeyboardMarkup(row_width=1)
    electro_net_7 = InlineKeyboardButton(text="бытовка без электроники", callback_data="electro_net_7")
    electro_da_7 = InlineKeyboardButton(text="бытовка с электроникой", callback_data="electro_da_7")
    pepsiKeyboard.add(electro_net_7, electro_da_7)
    await bot.send_message(message.from_user.id,"Ладно, обойдемся без тамбура. А теперь ответьте пожайлуста Вам бы хотелось оборудовать свою бытовку электропроводкой?",reply_markup=pepsiKeyboard)

@dp.callback_query_handler(lambda c: c.data == 'tambur_da_4')
async def electro_8(message: types.Message):
    pepsiKeyboard = InlineKeyboardMarkup(row_width=1)
    electro_net_8 = InlineKeyboardButton(text="бытовка без электроники", callback_data="electro_net_8")
    electro_da_8 = InlineKeyboardButton(text="бытовка с электроникой", callback_data="electro_da_8")
    pepsiKeyboard.add(electro_net_8, electro_da_8)
    await bot.send_message(message.from_user.id," Вам бы хотелось оборудовать свою бытовку электропроводкой?",reply_markup=pepsiKeyboard)




@dp.callback_query_handler(lambda c: c.data == 'tambur_net_5')
async def electro_9(message: types.Message):
    pepsiKeyboard = InlineKeyboardMarkup(row_width=1)
    electro_net_9 = InlineKeyboardButton(text="бытовка без электроники", callback_data="electro_net_9")
    electro_da_9 = InlineKeyboardButton(text="бытовка с электроникой", callback_data="electro_da_9")
    pepsiKeyboard.add(electro_net_9, electro_da_9)
    await bot.send_message(message.from_user.id,"Ладно, обойдемся без тамбура. А теперь ответьте пожайлуста Вам бы хотелось оборудовать свою бытовку электропроводкой?",reply_markup=pepsiKeyboard)

@dp.callback_query_handler(lambda c: c.data == 'tambur_da_5')
async def electro_10(message: types.Message):
    pepsiKeyboard = InlineKeyboardMarkup(row_width=1)
    electro_net_10 = InlineKeyboardButton(text="бытовка без электроники", callback_data="electro_net_10")
    electro_da_10 = InlineKeyboardButton(text="бытовка с электроникой", callback_data="electro_da_10")
    pepsiKeyboard.add(electro_net_10, electro_da_10)
    await bot.send_message(message.from_user.id," Вам бы хотелось оборудовать свою бытовку электропроводкой?",reply_markup=pepsiKeyboard)




@dp.callback_query_handler(lambda c: c.data == 'tambur_net_6')
async def electro_11(message: types.Message):
    pepsiKeyboard = InlineKeyboardMarkup(row_width=1)
    electro_net_11 = InlineKeyboardButton(text="бытовка без электроники", callback_data="electro_net_11")
    electro_da_11 = InlineKeyboardButton(text="бытовка с электроникой", callback_data="electro_da_11")
    pepsiKeyboard.add(electro_net_11, electro_da_11)
    await bot.send_message(message.from_user.id,"Ладно, обойдемся без тамбура. А теперь ответьте пожайлуста Вам бы хотелось оборудовать свою бытовку электропроводкой?",reply_markup=pepsiKeyboard)

@dp.callback_query_handler(lambda c: c.data == 'tambur_da_6')
async def electro_12(message: types.Message):
    pepsiKeyboard = InlineKeyboardMarkup(row_width=1)
    electro_net_12 = InlineKeyboardButton(text="бытовка без электроники", callback_data="electro_net_12")
    electro_da_12 = InlineKeyboardButton(text="бытовка с электроникой", callback_data="electro_da_12")
    pepsiKeyboard.add(electro_net_12, electro_da_12)
    await bot.send_message(message.from_user.id," Вам бы хотелось оборудовать свою бытовку электропроводкой?",reply_markup=pepsiKeyboard)




@dp.callback_query_handler(lambda c: c.data == 'tambur_net_7')
async def electro_13(message: types.Message):
    pepsiKeyboard = InlineKeyboardMarkup(row_width=1)
    electro_net_13 = InlineKeyboardButton(text="бытовка без электроники", callback_data="electro_net_13")
    electro_da_13 = InlineKeyboardButton(text="бытовка с электроникой", callback_data="electro_da_13")
    pepsiKeyboard.add(electro_net_13, electro_da_13)
    await bot.send_message(message.from_user.id,"Ладно, обойдемся без тамбура. А теперь ответьте пожайлуста Вам бы хотелось оборудовать свою бытовку электропроводкой?",reply_markup=pepsiKeyboard)

@dp.callback_query_handler(lambda c: c.data == 'tambur_da_7')
async def electro_14(message: types.Message):
    pepsiKeyboard = InlineKeyboardMarkup(row_width=1)
    electro_net_14 = InlineKeyboardButton(text="бытовка без электроники", callback_data="electro_net_14")
    electro_da_14 = InlineKeyboardButton(text="бытовка с электроникой", callback_data="electro_da_14")
    pepsiKeyboard.add(electro_net_14, electro_da_14)
    await bot.send_message(message.from_user.id," Вам бы хотелось оборудовать свою бытовку электропроводкой?",reply_markup=pepsiKeyboard)




@dp.callback_query_handler(lambda c: c.data == 'tambur_net_8')
async def electro_15(message: types.Message):
    pepsiKeyboard = InlineKeyboardMarkup(row_width=1)
    electro_net_15 = InlineKeyboardButton(text="бытовка без электроники", callback_data="electro_net_15")
    electro_da_15 = InlineKeyboardButton(text="бытовка с электроникой", callback_data="electro_da_15")
    pepsiKeyboard.add(electro_net_15, electro_da_15)
    await bot.send_message(message.from_user.id," Ладно, обойдемся без тамбура. А теперь ответьте пожайлуста Вам бы хотелось оборудовать свою бытовку электропроводкой?",reply_markup=pepsiKeyboard)

@dp.callback_query_handler(lambda c: c.data == 'tambur_da_8')
async def electro_16(message: types.Message):
    pepsiKeyboard = InlineKeyboardMarkup(row_width=1)
    electro_net_16 = InlineKeyboardButton(text="бытовка без электроники", callback_data="electro_net_16")
    electro_da_16 = InlineKeyboardButton(text="бытовка с электроникой", callback_data="electro_da_16")
    pepsiKeyboard.add(electro_net_16, electro_da_16)
    await bot.send_message(message.from_user.id," вы выбрали с тамбуром, Вам бы хотелось оборудовать свою бытовку электропроводкой?",reply_markup=pepsiKeyboard)





# БЕЗ ТАМБУРА 1 РАЗМЕР БЕЗ ЕЛЕКТРО

@dp.callback_query_handler(lambda c: c.data == 'electro_net_1')
async def otdelka_1(message: types.Message):
    colaKeyboard = InlineKeyboardMarkup(row_width=1)
    otdelka_1org = InlineKeyboardButton(text="оргалит", callback_data="eletro_net_1")
    otdelka_1osb = InlineKeyboardButton(text="OSB", callback_data="eletro_net_1")
    otdelka_1steal = InlineKeyboardButton(text="сталь", callback_data="eletro_net_1")
    otdelka_1pvh = InlineKeyboardButton(text="ПВХ", callback_data="eletro_net_1")
    otdelka_1tree = InlineKeyboardButton(text="дерево", callback_data="eletro_net_1")
    otdelka_1mdf = InlineKeyboardButton(text="МДФ", callback_data="eletro_net_1")
    otdelka_1no = InlineKeyboardButton(text="хочу без отделки", callback_data="eletro_net_1")
    colaKeyboard.add(otdelka_1org, otdelka_1osb, otdelka_1steal, otdelka_1pvh, otdelka_1tree, otdelka_1mdf, otdelka_1no)
    await bot.send_message(message.from_user.id,"Вы выбрали вариант без проводки, и теперь у меня есть последний вопрос. Какую отделку вы выберете?",reply_markup=colaKeyboard)

# БЕЗ ТАМБУРА 1 РАЗМЕР С ЕЛЕКТРО

@dp.callback_query_handler(lambda c: c.data == 'electro_da_1')
async def otdelka_2(message: types.Message):
    colaKeyboard = InlineKeyboardMarkup(row_width=1)
    otdelka_2org = InlineKeyboardButton(text="оргалит", callback_data="eletro_da_2")
    otdelka_2osb = InlineKeyboardButton(text="OSB", callback_data="eletro_da_2")
    otdelka_2steal = InlineKeyboardButton(text="сталь", callback_data="eletro_da_2")
    otdelka_2pvh = InlineKeyboardButton(text="ПВХ", callback_data="eletro_da_2")
    otdelka_2tree = InlineKeyboardButton(text="дерево", callback_data="eletro_da_2")
    otdelka_2mdf = InlineKeyboardButton(text="МДФ", callback_data="eletro_da_2")
    otdelka_2no = InlineKeyboardButton(text="хочу без отделки", callback_data="eletro_da_2")
    colaKeyboard.add(otdelka_2org, otdelka_2osb, otdelka_2steal, otdelka_2pvh, otdelka_2tree, otdelka_2mdf, otdelka_2no)
    await bot.send_message(message.from_user.id,"Вы выбрали вариант с проводки, и теперь у меня есть последний вопрос. Какую отделку вы выберете?",reply_markup=colaKeyboard)






# С ТАМБУРОМ  1 РАЗМЕР БЕЗ ЕЛЕКТРО
@dp.callback_query_handler(lambda c: c.data == 'electro_net_2')
async def otdelka_3(message: types.Message):
    colaKeyboard = InlineKeyboardMarkup(row_width=1)
    otdelka_3org = InlineKeyboardButton(text="оргалит", callback_data="eletro_net_3")
    otdelka_3osb = InlineKeyboardButton(text="OSB", callback_data="eletro_net_3")
    otdelka_3steal = InlineKeyboardButton(text="сталь", callback_data="eletro_net_3")
    otdelka_3pvh = InlineKeyboardButton(text="ПВХ", callback_data="eletro_net_3")
    otdelka_3tree = InlineKeyboardButton(text="дерево", callback_data="eletro_net_3")
    otdelka_3mdf = InlineKeyboardButton(text="МДФ", callback_data="eletro_net_3")
    otdelka_3no = InlineKeyboardButton(text="хочу без отделки", callback_data="eletro_net_3")
    colaKeyboard.add(otdelka_3org, otdelka_3osb, otdelka_3steal, otdelka_3pvh, otdelka_3tree, otdelka_3mdf, otdelka_3no)
    await bot.send_message(message.from_user.id,"Вы выбрали вариант без проводки, и теперь у меня есть последний вопрос. Какую отделку вы выберете?",reply_markup=colaKeyboard)

# С ТАМБУРОМ  1 РАЗМЕР С ЕЛЕКТРО

@dp.callback_query_handler(lambda c: c.data == 'electro_da_2')
async def otdelka_4(message: types.Message):
    colaKeyboard = InlineKeyboardMarkup(row_width=1)
    otdelka_4org = InlineKeyboardButton(text="оргалит", callback_data="eletro_da_4")
    otdelka_4osb = InlineKeyboardButton(text="OSB", callback_data="eletro_da_4")
    otdelka_4steal = InlineKeyboardButton(text="сталь", callback_data="eletro_da_4")
    otdelka_4pvh = InlineKeyboardButton(text="ПВХ", callback_data="eletro_da_4")
    otdelka_4tree = InlineKeyboardButton(text="дерево", callback_data="eletro_da_4")
    otdelka_4mdf = InlineKeyboardButton(text="МДФ", callback_data="eletro_da_4")
    otdelka_4no = InlineKeyboardButton(text="хочу без отделки", callback_data="eletro_da_4")
    colaKeyboard.add(otdelka_4org, otdelka_4osb, otdelka_4steal, otdelka_4pvh, otdelka_4tree, otdelka_4mdf, otdelka_4no)
    await bot.send_message(message.from_user.id,"Вы выбрали вариант с проводки, и теперь у меня есть последний вопрос. Какую отделку вы выберете?",reply_markup=colaKeyboard)



#2



# БЕЗ ТАМБУРА 2 РАЗМЕР БЕЗ ЕЛЕКТРО

@dp.callback_query_handler(lambda c: c.data == 'electro_net_3')
async def otdelka_5(message: types.Message):
    colaKeyboard = InlineKeyboardMarkup(row_width=1)
    otdelka_5org = InlineKeyboardButton(text="оргалит", callback_data="eletro_net_5")
    otdelka_5osb = InlineKeyboardButton(text="OSB", callback_data="eletro_net_5")
    otdelka_5steal = InlineKeyboardButton(text="сталь", callback_data="eletro_net_5")
    otdelka_5pvh = InlineKeyboardButton(text="ПВХ", callback_data="eletro_net_5")
    otdelka_5tree = InlineKeyboardButton(text="дерево", callback_data="eletro_net_5")
    otdelka_5mdf = InlineKeyboardButton(text="МДФ", callback_data="eletro_net_5")
    otdelka_5no = InlineKeyboardButton(text="хочу без отделки", callback_data="eletro_da_5")
    colaKeyboard.add(otdelka_5org, otdelka_5osb, otdelka_5steal, otdelka_5pvh, otdelka_5tree, otdelka_5mdf, otdelka_5no)
    await bot.send_message(message.from_user.id,"Вы выбрали вариант без проводки, и теперь у меня есть последний вопрос. Какую отделку вы выберете?",reply_markup=colaKeyboard)

# БЕЗ ТАМБУРА 2 РАЗМЕР С ЕЛЕКТРО

@dp.callback_query_handler(lambda c: c.data == 'eletro_da_3')
async def otdelka_6(message: types.Message):
    colaKeyboard = InlineKeyboardMarkup(row_width=1)
    otdelka_6org = InlineKeyboardButton(text="оргалит", callback_data="eletro_da_6")
    otdelka_6osb = InlineKeyboardButton(text="OSB", callback_data="eletro_da_6")
    otdelka_6steal = InlineKeyboardButton(text="сталь", callback_data="eletro_da_6")
    otdelka_6pvh = InlineKeyboardButton(text="ПВХ", callback_data="eletro_da_6")
    otdelka_6tree = InlineKeyboardButton(text="дерево", callback_data="eletro_da_6")
    otdelka_6mdf = InlineKeyboardButton(text="МДФ", callback_data="eletro_da_6")
    otdelka_6no = InlineKeyboardButton(text="хочу без отделки", callback_data="eletro_da_6")
    colaKeyboard.add(otdelka_6org, otdelka_6osb, otdelka_6steal, otdelka_6pvh, otdelka_6tree, otdelka_6mdf, otdelka_6no)
    await bot.send_message(message.from_user.id,"Вы выбрали вариант с проводки, и теперь у меня есть последний вопрос. Какую отделку вы выберете?",reply_markup=colaKeyboard)






# С ТАМБУРОМ  2 РАЗМЕР БЕЗ ЕЛЕКТРО
@dp.callback_query_handler(lambda c: c.data == 'eletro_net_4')
async def otdelka_7(message: types.Message):
    colaKeyboard = InlineKeyboardMarkup(row_width=1)
    otdelka_7org = InlineKeyboardButton(text="оргалит", callback_data="eletro_net_7")
    otdelka_7osb = InlineKeyboardButton(text="OSB", callback_data="eletro_net_7")
    otdelka_7steal = InlineKeyboardButton(text="сталь", callback_data="eletro_net_7")
    otdelka_7pvh = InlineKeyboardButton(text="ПВХ", callback_data="eletro_net_7")
    otdelka_7tree = InlineKeyboardButton(text="дерево", callback_data="eletro_net_7")
    otdelka_7mdf = InlineKeyboardButton(text="МДФ", callback_data="eletro_net_7")
    otdelka_7no = InlineKeyboardButton(text="хочу без отделки", callback_data="eletro_net_7")
    colaKeyboard.add(otdelka_7org, otdelka_7osb, otdelka_7steal, otdelka_7pvh, otdelka_7tree, otdelka_7mdf, otdelka_7no)
    await bot.send_message(message.from_user.id,"Вы выбрали вариант без проводки, и теперь у меня есть последний вопрос. Какую отделку вы выберете?",reply_markup=colaKeyboard)

# С ТАМБУРОМ  2 РАЗМЕР С ЕЛЕКТРО

@dp.callback_query_handler(lambda c: c.data == 'electro_da_4')
async def otdelka_8(message: types.Message):
    colaKeyboard = InlineKeyboardMarkup(row_width=1)
    otdelka_8org = InlineKeyboardButton(text="оргалит", callback_data="electro_da_8")
    otdelka_8osb = InlineKeyboardButton(text="OSB", callback_data="electro_da_8")
    otdelka_8steal = InlineKeyboardButton(text="сталь", callback_data="electro_da_8")
    otdelka_8pvh = InlineKeyboardButton(text="ПВХ", callback_data="electro_da_8")
    otdelka_8tree = InlineKeyboardButton(text="дерево", callback_data="electro_da_8")
    otdelka_8mdf = InlineKeyboardButton(text="МДФ", callback_data="electro_da_8")
    otdelka_8no = InlineKeyboardButton(text="хочу без отделки", callback_data="electro_da_8")
    colaKeyboard.add(otdelka_8org, otdelka_8osb, otdelka_8steal, otdelka_8pvh, otdelka_8tree, otdelka_8mdf, otdelka_8no)
    await bot.send_message(message.from_user.id,"Вы выбрали вариант с проводки, и теперь у меня есть последний вопрос. Какую отделку вы выберете?",reply_markup=colaKeyboard)

# async def callback_handler(callback_query: types.CallbackQuery):
#     data_art = "stroy/2/1/bytovka_024_cam001.jpg"
#     caption = f"82 000р (с ндс)"
#     await bot.send_photo(callback_query.from_user.id, photo=types.InputFile(data_art), caption=caption,
#                          parse_mode="Markdown")

# @dp.callback_query_handler(lambda c: c.data == 'tambur_da')
# async def callback_handler(callback_query: types.CallbackQuery):
#     data_art = "stroy/2/Новая папка (2)/bytovka_062_cam001.jpg"
#     caption = f"98 000р (с ндс)"
#     await bot.send_photo(callback_query.from_user.id, photo=types.InputFile(data_art), caption=caption,
#                          parse_mode="Markdown")



# @dp.callback_query_handler(lambda c: c.data == 'metal_bitovka')
# async def vse_stroy(message: types.Message):
#     ikb = InlineKeyboardMarkup(row_width=1)
#     bitovka_1 = InlineKeyboardButton(text="Бытовка для строителей 2,40 х 2,40 БК-02 (охр.) Пост охраны  ", callback_data="bitovka_1")
#     bitovka_2 = InlineKeyboardButton(text="Бытовка строительная БК-03 (3 м.) 3,0 х 2,40", callback_data="bitovka_2")
#     bitovka_3 = InlineKeyboardButton(text="Бытовка для строителей 3,0 х 2,40 БК03 (3м)", callback_data="bitovka_3")
#     bitovka_4 = InlineKeyboardButton(text="Бытовка для строителей 4,0 х 2,40 БК-03 (4 м.)", callback_data="bitovka_4")
#     ikb.add(bitovka_1, bitovka_2,bitovka_3 , bitovka_4 )
#     await bot.send_message(message.from_user.id, "тут будет текст",reply_markup= ikb)
# @dp.callback_query_handler(lambda c: c.data == 'bitovka_1')
# async def callback_handler(callback_query: types.CallbackQuery):
#     data_art = "stroy/2/1/bytovka_024_cam001.jpg"
#     caption = f"82 000р (с ндс)"
#     await bot.send_photo(callback_query.from_user.id, photo=types.InputFile(data_art), caption=caption,
#                          parse_mode="Markdown")

@dp.message_handler(lambda message: message.text == "о нас 🔍")
async def catalog(message: types.Message):
    await bot.send_message(message.from_user.id,"тут будет текст")

@dp.message_handler(lambda message: message.text == "контакты 📞")
async def catalog(message: types.Message):
    await bot.send_message(message.from_user.id,"тут будет текст")

try:
        # logger.info(f"\nSTATUS: Бот запущен.\n")
    executor.start_polling(dp,skip_updates = True)
except Exception as e:
    # logger.error(f"\nERROR: {e}\n")
    print(e)
