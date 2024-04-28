from aiogram import Bot,types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,InputFile

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

    await message.answer("Здравствуйте!                                                                                                                               "
                         " Этот бот был создан, чтобы помочь вам узнать стоимость товара и предварительно ознакомиться с ним.                                                                                    "
                         " Это позволит упростить процесс покупки.                                                                                    "
                         " Чтобы помочь вам, нам нужно задать несколько вопросов.                                                                                    "
                         "Пожалуйста, ответьте на них, для появления вопросов нажмите кнопку: 'каталог'.                                                                                    "

                         ,reply_markup= main_menu)


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
async def okno_1(message: types.Message):
    ikb = InlineKeyboardMarkup(row_width=1)
    okno_1_1 = InlineKeyboardButton(text="я хочу одно окно", callback_data="okno_1_1")
    okno_3_1 = InlineKeyboardButton(text="я хочу 3 окна (пост охраны)", callback_data="okno_3_1")
    ikb.add(okno_1_1,okno_3_1 )
    await bot.send_message(message.from_user.id, "хорошо вы выбрыли площадь: 2.0 x 2.4 А теперь, пожалуйста, ответьте на несколько вопросов,сколько окон вы хотите в совоей бытовке?",reply_markup= ikb)

@dp.callback_query_handler(lambda c: c.data == 'razmer_2')
async def okno_2(message: types.Message):
    ikb = InlineKeyboardMarkup(row_width=1)
    okno_1_2 = InlineKeyboardButton(text="я хочу одно окно", callback_data="okno_1_2")
    okno_3_2 = InlineKeyboardButton(text="я хочу 3 окна", callback_data="okno_3_2")
    ikb.add(okno_1_2, okno_3_2)
    await bot.send_message(message.from_user.id,"хорошо вы выбрыли площадь: 3.0 x 2.4 А теперь, пожалуйста, ответьте на несколько вопросов,сколько окон вы хотите в совоей бытовке?",reply_markup=ikb)

@dp.callback_query_handler(lambda c: c.data == 'razmer_3')
async def okno_3(message: types.Message):
    ikb = InlineKeyboardMarkup(row_width=1)
    okno_1_3 = InlineKeyboardButton(text="я хочу одно окно", callback_data="okno_1_3")
    okno_3_3 = InlineKeyboardButton(text="я хочу 3 окна", callback_data="okno_3_3")
    ikb.add(okno_3_3, okno_1_3)
    await bot.send_message(message.from_user.id,"хорошо вы выбрыли площадь: 4.0 x 2.4 А теперь, пожалуйста, ответьте на несколько вопросов,сколько окон вы хотите в совоей бытовке?",reply_markup=ikb)

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









@dp.callback_query_handler(lambda c: c.data == 'okno_1_1')
async def electro_1(message: types.Message):
    pepsiKeyboard = InlineKeyboardMarkup(row_width=1)
    electro_net_1 = InlineKeyboardButton(text="бытовка без электроники", callback_data="electro_net_1")
    electro_da_1 = InlineKeyboardButton(text="бытовка с электроникой", callback_data="electro_da_1")
    pepsiKeyboard.add(electro_net_1, electro_da_1)
    await bot.send_message(message.from_user.id," вы выбрали 1 окно. А теперь ответьте пожайлуста окна Вам бы хотелось оборудовать свою бытовку электропроводкой?",reply_markup=pepsiKeyboard)

@dp.callback_query_handler(lambda c: c.data == 'okno_3_1')
async def electro_2(message: types.Message):
    pepsiKeyboard = InlineKeyboardMarkup(row_width=1)
    electro_net_2 = InlineKeyboardButton(text="бытовка без электроники", callback_data="electro_net_2")
    electro_da_2 = InlineKeyboardButton(text="бытовка с электроникой", callback_data="electro_da_2")
    pepsiKeyboard.add(electro_net_2, electro_da_2)
    await bot.send_message(message.from_user.id,"вы выбрали 3 окна. А теперь ответьте пожайлуста окна Вам бы хотелось оборудовать свою бытовку электропроводкой?",reply_markup=pepsiKeyboard)




@dp.callback_query_handler(lambda c: c.data == 'okno_1_2')
async def electro_3(message: types.Message):
    pepsiKeyboard = InlineKeyboardMarkup(row_width=1)
    electro_net_3 = InlineKeyboardButton(text="бытовка без электроники", callback_data="electro_net_3")
    electro_da_3 = InlineKeyboardButton(text="бытовка с электроникой", callback_data="electro_da_3")
    pepsiKeyboard.add(electro_net_3, electro_da_3)
    await bot.send_message(message.from_user.id," вы выбрали 1 окно. А теперь ответьте пожайлуста Вам бы хотелось оборудовать свою бытовку электропроводкой?",reply_markup=pepsiKeyboard)

@dp.callback_query_handler(lambda c: c.data == 'okno_3_2')
async def electro_4(message: types.Message):
    pepsiKeyboard = InlineKeyboardMarkup(row_width=1)
    electro_net_4 = InlineKeyboardButton(text="бытовка без электроники", callback_data="electro_net_4")
    electro_da_4 = InlineKeyboardButton(text="бытовка с электроникой", callback_data="electro_da_4")
    pepsiKeyboard.add(electro_net_4, electro_da_4)
    await bot.send_message(message.from_user.id,"вы выбрали 3 окна А теперь ответьте пожайлуста Вам бы хотелось оборудовать свою бытовку электропроводкой?",reply_markup=pepsiKeyboard)




@dp.callback_query_handler(lambda c: c.data == 'okno_1_3')
async def electro_5(message: types.Message):
    pepsiKeyboard = InlineKeyboardMarkup(row_width=1)
    electro_net_5 = InlineKeyboardButton(text="бытовка без электроники", callback_data="electro_net_5")
    electro_da_5 = InlineKeyboardButton(text="бытовка с электроникой", callback_data="electro_da_5")
    pepsiKeyboard.add(electro_net_5, electro_da_5)
    await bot.send_message(message.from_user.id," вы выбрали 1 окно. А теперь ответьте пожайлуста Вам бы хотелось оборудовать свою бытовку электропроводкой?",reply_markup=pepsiKeyboard)

@dp.callback_query_handler(lambda c: c.data == 'okno_3_3')
async def electro_6(message: types.Message):
    pepsiKeyboard = InlineKeyboardMarkup(row_width=1)
    electro_net_6 = InlineKeyboardButton(text="бытовка без электроники", callback_data="electro_net_6")
    electro_da_6 = InlineKeyboardButton(text="бытовка с электроникой", callback_data="electro_da_6")
    pepsiKeyboard.add(electro_net_6, electro_da_6)
    await bot.send_message(message.from_user.id,"вы выбрали 3 окна А теперь ответьте пожайлуста Вам бы хотелось оборудовать свою бытовку электропроводкой?",reply_markup=pepsiKeyboard)




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



#########################################################
#1размер
#########################################################

# БЕЗ ТАМБУРА 1 РАЗМЕР БЕЗ ЕЛЕКТРО

@dp.callback_query_handler(lambda c: c.data == 'electro_net_1')
async def otdelka_1(message: types.Message):
    colaKeyboard = InlineKeyboardMarkup(row_width=1)
    otdelka_1org = InlineKeyboardButton(text="оргалит", callback_data="otdelka_1org")
    colaKeyboard.add(otdelka_1org)
    await bot.send_message(message.from_user.id,"Вы выбрали вариант без проводки, и теперь у меня есть последний вопрос. Какую отделку вы выберете?",reply_markup=colaKeyboard)

# БЕЗ ТАМБУРА 1 РАЗМЕР С ЕЛЕКТРО

@dp.callback_query_handler(lambda c: c.data == 'electro_da_1')
async def otdelka_2(message: types.Message):
    colaKeyboard = InlineKeyboardMarkup(row_width=1)
    otdelka_2org = InlineKeyboardButton(text="оргалит", callback_data="otdelka_2org")
    colaKeyboard.add(otdelka_2org)
    await bot.send_message(message.from_user.id,"Вы выбрали вариант с проводки, и теперь у меня есть последний вопрос. Какую отделку вы выберете?",reply_markup=colaKeyboard)




# С ТАМБУРОМ  1 РАЗМЕР БЕЗ ЕЛЕКТРО
@dp.callback_query_handler(lambda c: c.data == 'electro_net_2')
async def otdelka_3(message: types.Message):
    colaKeyboard = InlineKeyboardMarkup(row_width=1)
    otdelka_3org = InlineKeyboardButton(text="оргалит", callback_data="otdelka_3org")

    colaKeyboard.add(otdelka_3org)
    await bot.send_message(message.from_user.id,"Вы выбрали вариант без проводки, и теперь у меня есть последний вопрос. Какую отделку вы выберете?",reply_markup=colaKeyboard)

# С ТАМБУРОМ  1 РАЗМЕР С ЕЛЕКТРО

@dp.callback_query_handler(lambda c: c.data == 'electro_da_2')
async def otdelka_4(message: types.Message):
    colaKeyboard = InlineKeyboardMarkup(row_width=1)
    otdelka_4org = InlineKeyboardButton(text="оргалит", callback_data="otdelka_4org")
    colaKeyboard.add(otdelka_4org)
    await bot.send_message(message.from_user.id,"Вы выбрали вариант с проводки, и теперь у меня есть последний вопрос. Какую отделку вы выберете?",reply_markup=colaKeyboard)


#########################################################
#2размер
########################################################
# БЕЗ ТАМБУРА 2 РАЗМЕР БЕЗ ЕЛЕКТРО

@dp.callback_query_handler(lambda c: c.data == 'electro_net_3')
async def otdelka_5(message: types.Message):
    colaKeyboard = InlineKeyboardMarkup(row_width=1)
    otdelka_5org = InlineKeyboardButton(text="оргалит", callback_data="otdelka_5org")
    otdelka_5pvh = InlineKeyboardButton(text="ПВХ", callback_data="otdelka_5pvh")
    otdelka_5tree = InlineKeyboardButton(text="дерево", callback_data="otdelka_5tree")
    colaKeyboard.add(otdelka_5org,otdelka_5pvh, otdelka_5tree)
    await bot.send_message(message.from_user.id,"Вы выбрали вариант без проводки, и теперь у меня есть последний вопрос. Какую отделку вы выберете?",reply_markup=colaKeyboard)

# БЕЗ ТАМБУРА 2 РАЗМЕР С ЕЛЕКТРО

@dp.callback_query_handler(lambda c: c.data == 'electro_da_3')
async def otdelka_6(message: types.Message):
    colaKeyboard = InlineKeyboardMarkup(row_width=1)
    otdelka_6org = InlineKeyboardButton(text="оргалит", callback_data="otdelka_6org")
    otdelka_6pvh = InlineKeyboardButton(text="ПВХ", callback_data="otdelka_6pvh")
    otdelka_6tree = InlineKeyboardButton(text="дерево", callback_data="otdelka_6tree")
    colaKeyboard.add(otdelka_6org, otdelka_6pvh, otdelka_6tree)
    await bot.send_message(message.from_user.id,"Вы выбрали вариант с проводки, и теперь у меня есть последний вопрос. Какую отделку вы выберете?",reply_markup=colaKeyboard)






# С ТАМБУРОМ  2 РАЗМЕР БЕЗ ЕЛЕКТРО
@dp.callback_query_handler(lambda c: c.data == 'electro_net_4')
async def otdelka_7(message: types.Message):
    colaKeyboard = InlineKeyboardMarkup(row_width=1)
    otdelka_7org = InlineKeyboardButton(text="оргалит", callback_data="otdelka_7org")
    otdelka_7pvh = InlineKeyboardButton(text="ПВХ", callback_data="otdelka_7pvh")
    otdelka_7tree = InlineKeyboardButton(text="дерево", callback_data="otdelka_7tree")
    colaKeyboard.add(otdelka_7org, otdelka_7pvh, otdelka_7tree)
    await bot.send_message(message.from_user.id,"Вы выбрали вариант без проводки, и теперь у меня есть последний вопрос. Какую отделку вы выберете?",reply_markup=colaKeyboard)

# С ТАМБУРОМ  2 РАЗМЕР С ЕЛЕКТРО

@dp.callback_query_handler(lambda c: c.data == 'electro_da_4')
async def otdelka_8(message: types.Message):
    colaKeyboard = InlineKeyboardMarkup(row_width=1)
    otdelka_8org = InlineKeyboardButton(text="оргалит", callback_data="otdelka_8org")
    otdelka_8pvh = InlineKeyboardButton(text="ПВХ", callback_data="otdelka_8pvh")
    otdelka_8tree = InlineKeyboardButton(text="дерево", callback_data="otdelka_8tree")
    colaKeyboard.add(otdelka_8org, otdelka_8pvh, otdelka_8tree)
    await bot.send_message(message.from_user.id,"Вы выбрали вариант с проводки, и теперь у меня есть последний вопрос. Какую отделку вы выберете?",reply_markup=colaKeyboard)

#########################################################
#3размер
#########################################################

# БЕЗ ТАМБУРА 3 РАЗМЕР БЕЗ ЕЛЕКТРО

@dp.callback_query_handler(lambda c: c.data == 'electro_net_5')
async def otdelka_9(message: types.Message):
    colaKeyboard = InlineKeyboardMarkup(row_width=1)
    otdelka_9org = InlineKeyboardButton(text="оргалит", callback_data="otdelka_9org")
    otdelka_9pvh = InlineKeyboardButton(text="ПВХ", callback_data="otdelka_9pvh")
    otdelka_9tree = InlineKeyboardButton(text="дерево", callback_data="otdelka_9tree")
    otdelka_9mdf = InlineKeyboardButton(text="МДФ", callback_data="otdelka_9mdf")
    colaKeyboard.add(otdelka_9org, otdelka_9pvh, otdelka_9tree, otdelka_9mdf)
    await bot.send_message(message.from_user.id,"Вы выбрали вариант без проводки, и теперь у меня есть последний вопрос. Какую отделку вы выберете?",reply_markup=colaKeyboard)

# БЕЗ ТАМБУРА 3 РАЗМЕР С ЕЛЕКТРО

@dp.callback_query_handler(lambda c: c.data == 'electro_da_5')
async def otdelka_10(message: types.Message):
    colaKeyboard = InlineKeyboardMarkup(row_width=1)
    otdelka_10org = InlineKeyboardButton(text="оргалит", callback_data="otdelka_10org")
    otdelka_10pvh = InlineKeyboardButton(text="ПВХ", callback_data="otdelka_10pvh")
    otdelka_10tree = InlineKeyboardButton(text="дерево", callback_data="otdelka_10tree")
    otdelka_10mdf = InlineKeyboardButton(text="МДФ", callback_data="otdelka_10mdf")
    colaKeyboard.add(otdelka_10org, otdelka_10pvh, otdelka_10tree, otdelka_10mdf)
    await bot.send_message(message.from_user.id,"Вы выбрали вариант с проводки, и теперь у меня есть последний вопрос. Какую отделку вы выберете?",reply_markup=colaKeyboard)






# С ТАМБУРОМ  3 РАЗМЕР БЕЗ ЕЛЕКТРО
@dp.callback_query_handler(lambda c: c.data == 'electro_net_6')
async def otdelka_11(message: types.Message):
    colaKeyboard = InlineKeyboardMarkup(row_width=1)
    otdelka_11org = InlineKeyboardButton(text="оргалит", callback_data="otdelka_11org")
    otdelka_11pvh = InlineKeyboardButton(text="ПВХ", callback_data="otdelka_11pvh")
    otdelka_11tree = InlineKeyboardButton(text="дерево", callback_data="otdelka_11tree")
    otdelka_11mdf = InlineKeyboardButton(text="МДФ", callback_data="otdelka_11mdf")
    colaKeyboard.add(otdelka_11org, otdelka_11pvh, otdelka_11tree, otdelka_11mdf)
    await bot.send_message(message.from_user.id,"Вы выбрали вариант без проводки, и теперь у меня есть последний вопрос. Какую отделку вы выберете?",reply_markup=colaKeyboard)

# С ТАМБУРОМ  3 РАЗМЕР С ЕЛЕКТРО

@dp.callback_query_handler(lambda c: c.data == 'electro_da_6')
async def otdelka_12(message: types.Message):
    colaKeyboard = InlineKeyboardMarkup(row_width=1)
    otdelka_12org = InlineKeyboardButton(text="оргалит", callback_data="otdelka_12org")
    otdelka_12pvh = InlineKeyboardButton(text="ПВХ", callback_data="otdelka_12pvh")
    otdelka_12tree = InlineKeyboardButton(text="дерево", callback_data="otdelka_12tree")
    otdelka_12mdf = InlineKeyboardButton(text="МДФ", callback_data="otdelka_12mdf")
    colaKeyboard.add(otdelka_12org, otdelka_12pvh, otdelka_12tree, otdelka_12mdf)
    await bot.send_message(message.from_user.id,"Вы выбрали вариант с проводки, и теперь у меня есть последний вопрос. Какую отделку вы выберете?",reply_markup=colaKeyboard)


#########################################################
#4размер
#########################################################

# БЕЗ ТАМБУРА 4 РАЗМЕР БЕЗ ЕЛЕКТРО

@dp.callback_query_handler(lambda c: c.data == 'electro_net_7')
async def otdelka_13(message: types.Message):
    colaKeyboard = InlineKeyboardMarkup(row_width=1)
    otdelka_13org = InlineKeyboardButton(text="оргалит", callback_data="otdelka_13org")
    otdelka_13pvh = InlineKeyboardButton(text="ПВХ", callback_data="otdelka_13pvh")
    otdelka_13tree = InlineKeyboardButton(text="дерево", callback_data="otdelka_13tree")
    otdelka_13mdf = InlineKeyboardButton(text="МДФ", callback_data="otdelka_13mdf")
    colaKeyboard.add(otdelka_13org, otdelka_13pvh, otdelka_13tree, otdelka_13mdf)
    await bot.send_message(message.from_user.id,"Вы выбрали вариант без проводки, и теперь у меня есть последний вопрос. Какую отделку вы выберете?",reply_markup=colaKeyboard)

# БЕЗ ТАМБУРА 4 РАЗМЕР С ЕЛЕКТРО

@dp.callback_query_handler(lambda c: c.data == 'electro_da_7')
async def otdelka_14(message: types.Message):
    colaKeyboard = InlineKeyboardMarkup(row_width=1)
    otdelka_14org = InlineKeyboardButton(text="оргалит", callback_data="otdelka_14org")
    otdelka_14pvh = InlineKeyboardButton(text="ПВХ", callback_data="otdelka_14pvh")
    otdelka_14tree = InlineKeyboardButton(text="дерево", callback_data="otdelka_14tree")
    otdelka_14mdf = InlineKeyboardButton(text="МДФ", callback_data="otdelka_14mdf")
    colaKeyboard.add(otdelka_14org, otdelka_14pvh, otdelka_14tree, otdelka_14mdf)
    await bot.send_message(message.from_user.id,"Вы выбрали вариант с проводки, и теперь у меня есть последний вопрос. Какую отделку вы выберете?",reply_markup=colaKeyboard)






# С ТАМБУРОМ  4 РАЗМЕР БЕЗ ЕЛЕКТРО
@dp.callback_query_handler(lambda c: c.data == 'electro_net_8')
async def otdelka_15(message: types.Message):
    colaKeyboard = InlineKeyboardMarkup(row_width=1)
    otdelka_15org = InlineKeyboardButton(text="оргалит", callback_data="otdelka_15org")
    otdelka_15pvh = InlineKeyboardButton(text="ПВХ", callback_data="otdelka_15pvh")
    otdelka_15tree = InlineKeyboardButton(text="дерево", callback_data="otdelka_15tree")
    otdelka_15mdf = InlineKeyboardButton(text="МДФ", callback_data="otdelka_15mdf")
    colaKeyboard.add(otdelka_15org, otdelka_15pvh, otdelka_15tree, otdelka_15mdf)
    await bot.send_message(message.from_user.id,"Вы выбрали вариант без проводки, и теперь у меня есть последний вопрос. Какую отделку вы выберете?",reply_markup=colaKeyboard)

# С ТАМБУРОМ  4 РАЗМЕР С ЕЛЕКТРО

@dp.callback_query_handler(lambda c: c.data == 'electro_da_8')
async def otdelka_16(message: types.Message):
    colaKeyboard = InlineKeyboardMarkup(row_width=1)
    otdelka_16org = InlineKeyboardButton(text="оргалит", callback_data="otdelka_16org")
    otdelka_16pvh = InlineKeyboardButton(text="ПВХ", callback_data="otdelka_16pvh")
    otdelka_16tree = InlineKeyboardButton(text="дерево", callback_data="otdelka_16tree")
    otdelka_16mdf = InlineKeyboardButton(text="МДФ", callback_data="otdelka_16mdf")
    colaKeyboard.add(otdelka_16org, otdelka_16pvh, otdelka_16tree, otdelka_16mdf)
    await bot.send_message(message.from_user.id,"Вы выбрали вариант с проводки, и теперь у меня есть последний вопрос. Какую отделку вы выберете?",reply_markup=colaKeyboard)



#########################################################
#5размер
#########################################################

# БЕЗ ТАМБУРА 5 РАЗМЕР БЕЗ ЕЛЕКТРО

@dp.callback_query_handler(lambda c: c.data == 'electro_net_9')
async def otdelka_17(message: types.Message):
    colaKeyboard = InlineKeyboardMarkup(row_width=1)
    otdelka_17org = InlineKeyboardButton(text="оргалит", callback_data="otdelka_17org")
    otdelka_17pvh = InlineKeyboardButton(text="ПВХ", callback_data="otdelka_17pvh")
    otdelka_17tree = InlineKeyboardButton(text="дерево", callback_data="otdelka_17tree")
    otdelka_17mdf = InlineKeyboardButton(text="МДФ", callback_data="otdelka_17mdf")
    colaKeyboard.add(otdelka_17org, otdelka_17pvh, otdelka_17tree, otdelka_17mdf)
    await bot.send_message(message.from_user.id,"Вы выбрали вариант без проводки, и теперь у меня есть последний вопрос. Какую отделку вы выберете?",reply_markup=colaKeyboard)

# БЕЗ ТАМБУРА 5 РАЗМЕР С ЕЛЕКТРО

@dp.callback_query_handler(lambda c: c.data == 'electro_da_9')
async def otdelka_18(message: types.Message):
    colaKeyboard = InlineKeyboardMarkup(row_width=1)
    otdelka_18org = InlineKeyboardButton(text="оргалит", callback_data="otdelka_18org")
    otdelka_18pvh = InlineKeyboardButton(text="ПВХ", callback_data="otdelka_18pvh")
    otdelka_18tree = InlineKeyboardButton(text="дерево", callback_data="otdelka_18tree")
    otdelka_18mdf = InlineKeyboardButton(text="МДФ", callback_data="otdelka_18mdf")
    colaKeyboard.add(otdelka_18org, otdelka_18pvh, otdelka_18tree, otdelka_18mdf)
    await bot.send_message(message.from_user.id,"Вы выбрали вариант с проводки, и теперь у меня есть последний вопрос. Какую отделку вы выберете?",reply_markup=colaKeyboard)






# С ТАМБУРОМ  5 РАЗМЕР БЕЗ ЕЛЕКТРО
@dp.callback_query_handler(lambda c: c.data == 'electro_net_10')
async def otdelka_19(message: types.Message):
    colaKeyboard = InlineKeyboardMarkup(row_width=1)
    otdelka_19org = InlineKeyboardButton(text="оргалит", callback_data="otdelka_19org")
    otdelka_19pvh = InlineKeyboardButton(text="ПВХ", callback_data="otdelka_19pvh")
    otdelka_19tree = InlineKeyboardButton(text="дерево", callback_data="otdelka_19tree")
    otdelka_19mdf = InlineKeyboardButton(text="МДФ", callback_data="otdelka_19mdf")
    colaKeyboard.add(otdelka_19org, otdelka_19pvh, otdelka_19tree, otdelka_19mdf)
    await bot.send_message(message.from_user.id,"Вы выбрали вариант без проводки, и теперь у меня есть последний вопрос. Какую отделку вы выберете?",reply_markup=colaKeyboard)

# С ТАМБУРОМ  5 РАЗМЕР С ЕЛЕКТРО

@dp.callback_query_handler(lambda c: c.data == 'electro_da_10')
async def otdelka_20(message: types.Message):
    colaKeyboard = InlineKeyboardMarkup(row_width=1)
    otdelka_20org = InlineKeyboardButton(text="оргалит", callback_data="otdelka_20org")
    otdelka_20pvh = InlineKeyboardButton(text="ПВХ", callback_data="otdelka_20pvh")
    otdelka_20tree = InlineKeyboardButton(text="дерево", callback_data="otdelka_20tree")
    otdelka_20mdf = InlineKeyboardButton(text="МДФ", callback_data="otdelka_20mdf")
    colaKeyboard.add(otdelka_20org, otdelka_20pvh, otdelka_20tree, otdelka_20mdf)
    await bot.send_message(message.from_user.id,"Вы выбрали вариант с проводки, и теперь у меня есть последний вопрос. Какую отделку вы выберете?",reply_markup=colaKeyboard)


#########################################################
#6размер
#########################################################

# БЕЗ ТАМБУРА 6 РАЗМЕР БЕЗ ЕЛЕКТРО

@dp.callback_query_handler(lambda c: c.data == 'electro_net_11')
async def otdelka_21(message: types.Message):
    colaKeyboard = InlineKeyboardMarkup(row_width=1)
    otdelka_21pvh = InlineKeyboardButton(text="ПВХ", callback_data="otdelka_21pvh")
    otdelka_21tree = InlineKeyboardButton(text="дерево", callback_data="otdelka_21tree")
    otdelka_21mdf = InlineKeyboardButton(text="МДФ", callback_data="otdelka_21mdf")
    colaKeyboard.add(otdelka_21pvh, otdelka_21tree, otdelka_21mdf)
    await bot.send_message(message.from_user.id,"Вы выбрали вариант без проводки, и теперь у меня есть последний вопрос. Какую отделку вы выберете?",reply_markup=colaKeyboard)

# БЕЗ ТАМБУРА 6 РАЗМЕР С ЕЛЕКТРО

@dp.callback_query_handler(lambda c: c.data == 'electro_da_11')
async def otdelka_22(message: types.Message):
    colaKeyboard = InlineKeyboardMarkup(row_width=1)
    otdelka_22pvh = InlineKeyboardButton(text="ПВХ", callback_data="otdelka_22pvh")
    otdelka_22tree = InlineKeyboardButton(text="дерево", callback_data="otdelka_22tree")
    otdelka_22mdf = InlineKeyboardButton(text="МДФ", callback_data="otdelka_22mdf")
    colaKeyboard.add(otdelka_22pvh, otdelka_22tree, otdelka_22mdf)
    await bot.send_message(message.from_user.id,"Вы выбрали вариант с проводки, и теперь у меня есть последний вопрос. Какую отделку вы выберете?",reply_markup=colaKeyboard)






# С ТАМБУРОМ  6 РАЗМЕР БЕЗ ЕЛЕКТРО
@dp.callback_query_handler(lambda c: c.data == 'electro_net_12')
async def otdelka_23(message: types.Message):
    colaKeyboard = InlineKeyboardMarkup(row_width=1)
    otdelka_23pvh = InlineKeyboardButton(text="ПВХ", callback_data="otdelka_23pvh")
    otdelka_23tree = InlineKeyboardButton(text="дерево", callback_data="otdelka_23tree")
    otdelka_23mdf = InlineKeyboardButton(text="МДФ", callback_data="otdelka_23mdf")
    colaKeyboard.add(otdelka_23pvh, otdelka_23tree, otdelka_23mdf)
    await bot.send_message(message.from_user.id,"Вы выбрали вариант без проводки, и теперь у меня есть последний вопрос. Какую отделку вы выберете?",reply_markup=colaKeyboard)

# С ТАМБУРОМ  6 РАЗМЕР С ЕЛЕКТРО

@dp.callback_query_handler(lambda c: c.data == 'electro_da_12')
async def otdelka_24(message: types.Message):
    colaKeyboard = InlineKeyboardMarkup(row_width=1)
    otdelka_24pvh = InlineKeyboardButton(text="ПВХ", callback_data="otdelka_24pvh")
    otdelka_24tree = InlineKeyboardButton(text="дерево", callback_data="otdelka_24tree")
    otdelka_24mdf = InlineKeyboardButton(text="МДФ", callback_data="otdelka_24mdf")
    colaKeyboard.add(otdelka_24pvh, otdelka_24tree, otdelka_24mdf)
    await bot.send_message(message.from_user.id,"Вы выбрали вариант с проводки, и теперь у меня есть последний вопрос. Какую отделку вы выберете?",reply_markup=colaKeyboard)




#########################################################
#7размер
#########################################################

# БЕЗ ТАМБУРА 7 РАЗМЕР БЕЗ ЕЛЕКТРО

@dp.callback_query_handler(lambda c: c.data == 'electro_net_13')
async def otdelka_25(message: types.Message):
    colaKeyboard = InlineKeyboardMarkup(row_width=1)
    otdelka_25pvh = InlineKeyboardButton(text="ПВХ", callback_data="otdelka_25pvh")
    otdelka_25tree = InlineKeyboardButton(text="дерево", callback_data="otdelka_25tree")
    otdelka_25mdf = InlineKeyboardButton(text="мдф", callback_data="otdelka_25mdf")
    colaKeyboard.add(otdelka_25pvh, otdelka_25tree,otdelka_25mdf)
    await bot.send_message(message.from_user.id,"Вы выбрали вариант без проводки, и теперь у меня есть последний вопрос. Какую отделку вы выберете?",reply_markup=colaKeyboard)

# БЕЗ ТАМБУРА 7 РАЗМЕР С ЕЛЕКТРО

@dp.callback_query_handler(lambda c: c.data == 'electro_da_13')
async def otdelka_26(message: types.Message):
    colaKeyboard = InlineKeyboardMarkup(row_width=1)
    otdelka_26pvh = InlineKeyboardButton(text="ПВХ", callback_data="otdelka_26pvh")
    otdelka_26tree = InlineKeyboardButton(text="дерево", callback_data="otdelka_26tree")
    otdelka_26mdf = InlineKeyboardButton(text="мдф", callback_data="otdelka_26mdf")
    colaKeyboard.add(otdelka_26pvh, otdelka_26tree,otdelka_26mdf)
    await bot.send_message(message.from_user.id,"Вы выбрали вариант с проводки, и теперь у меня есть последний вопрос. Какую отделку вы выберете?",reply_markup=colaKeyboard)






# С ТАМБУРОМ  7 РАЗМЕР БЕЗ ЕЛЕКТРО
@dp.callback_query_handler(lambda c: c.data == 'electro_net_14')
async def otdelka_27(message: types.Message):
    colaKeyboard = InlineKeyboardMarkup(row_width=1)
    otdelka_27pvh = InlineKeyboardButton(text="ПВХ", callback_data="otdelka_23pvh")
    otdelka_27tree = InlineKeyboardButton(text="дерево", callback_data="otdelka_23tree")
    otdelka_27mdf = InlineKeyboardButton(text="мдф", callback_data="otdelka_23mdf")
    colaKeyboard.add(otdelka_27pvh, otdelka_27tree,otdelka_27mdf)
    await bot.send_message(message.from_user.id,"Вы выбрали вариант без проводки, и теперь у меня есть последний вопрос. Какую отделку вы выберете?",reply_markup=colaKeyboard)

# С ТАМБУРОМ  7 РАЗМЕР С ЕЛЕКТРО

@dp.callback_query_handler(lambda c: c.data == 'electro_da_14')
async def otdelka_28(message: types.Message):
    colaKeyboard = InlineKeyboardMarkup(row_width=1)
    otdelka_28pvh = InlineKeyboardButton(text="ПВХ", callback_data="otdelka_28pvh")
    otdelka_28tree = InlineKeyboardButton(text="дерево", callback_data="otdelka_28tree")
    otdelka_28mdf = InlineKeyboardButton(text="мдф", callback_data="otdelka_28mdf")
    colaKeyboard.add( otdelka_28pvh, otdelka_28tree,otdelka_28mdf)
    await bot.send_message(message.from_user.id,"Вы выбрали вариант с проводки, и теперь у меня есть последний вопрос. Какую отделку вы выберете?",reply_markup=colaKeyboard)



#########################################################
#8размер
#########################################################

# БЕЗ ТАМБУРА 8 РАЗМЕР БЕЗ ЕЛЕКТРО

@dp.callback_query_handler(lambda c: c.data == 'electro_net_15')
async def otdelka_29(message: types.Message):
    colaKeyboard = InlineKeyboardMarkup(row_width=1)
    otdelka_29pvh = InlineKeyboardButton(text="ПВХ", callback_data="otdelka_29pvh")
    otdelka_29tree = InlineKeyboardButton(text="дерево", callback_data="otdelka_29tree")
    otdelka_29mdf = InlineKeyboardButton(text="МДФ", callback_data="otdelka_29mdf")
    colaKeyboard.add(otdelka_29pvh, otdelka_29tree, otdelka_29mdf)
    await bot.send_message(message.from_user.id,"Вы выбрали вариант без проводки, и теперь у меня есть последний вопрос. Какую отделку вы выберете?",reply_markup=colaKeyboard)

# БЕЗ ТАМБУРА 8 РАЗМЕР С ЕЛЕКТРО

@dp.callback_query_handler(lambda c: c.data == 'electro_da_15')
async def otdelka_30(message: types.Message):
    colaKeyboard = InlineKeyboardMarkup(row_width=1)
    otdelka_30pvh = InlineKeyboardButton(text="ПВХ", callback_data="otdelka_30pvh")
    otdelka_30tree = InlineKeyboardButton(text="дерево", callback_data="otdelka_30tree")
    otdelka_30mdf = InlineKeyboardButton(text="МДФ", callback_data="otdelka_30mdf")
    colaKeyboard.add(otdelka_30pvh, otdelka_30tree, otdelka_30mdf)
    await bot.send_message(message.from_user.id,"Вы выбрали вариант с проводки, и теперь у меня есть последний вопрос. Какую отделку вы выберете?",reply_markup=colaKeyboard)

# С ТАМБУРОМ  8 РАЗМЕР БЕЗ ЕЛЕКТРО
@dp.callback_query_handler(lambda c: c.data == 'electro_net_16')
async def otdelka_31(message: types.Message):
    colaKeyboard = InlineKeyboardMarkup(row_width=1)
    otdelka_31pvh = InlineKeyboardButton(text="ПВХ", callback_data="otdelka_31pvh")
    otdelka_31tree = InlineKeyboardButton(text="дерево", callback_data="otdelka_31tree")
    otdelka_31mdf = InlineKeyboardButton(text="МДФ", callback_data="otdelka_31mdf")
    colaKeyboard.add(otdelka_31pvh, otdelka_31tree, otdelka_31mdf)
    await bot.send_message(message.from_user.id,"Вы выбрали вариант без проводки, и теперь у меня есть последний вопрос. Какую отделку вы выберете?",reply_markup=colaKeyboard)

# С ТАМБУРОМ  8 РАЗМЕР С ЕЛЕКТРО

@dp.callback_query_handler(lambda c: c.data == 'electro_da_16')
async def otdelka_32(message: types.Message):
    colaKeyboard = InlineKeyboardMarkup(row_width=1)
    otdelka_32pvh = InlineKeyboardButton(text="ПВХ", callback_data="otdelka_32pvh")
    otdelka_32tree = InlineKeyboardButton(text="дерево", callback_data="otdelka_32tree")
    otdelka_32mdf = InlineKeyboardButton(text="МДФ", callback_data="otdelka_32mdf")
    colaKeyboard.add(otdelka_32pvh, otdelka_32tree, otdelka_32mdf)
    await bot.send_message(message.from_user.id,"Вы выбрали вариант с проводки, и теперь у меня есть последний вопрос. Какую отделку вы выберете?",reply_markup=colaKeyboard)

#########################################  наконец-то осталось ток фотки)) ###################################################################


#########################################  размер 1)) ###################################################################
# БЕЗ ТАМБУРА 1 РАЗМЕР БЕЗ ЕЛЕКТРО
@dp.callback_query_handler(lambda c: c.data == 'otdelka_1org')
async def finish_1(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_1/bytovka_024_cam001.jpg'),
                         caption='Размер: 2,4 х 2,4 м- пост охраны\n'
                                 'без тамбура,\n'
                                 'без электропроводки,\n'
                                 'отделка огралит,\n'
                                 '1 окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 83 000 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')


##################################################################################
# БЕЗ ТАМБУРА 1 РАЗМЕР С ЕЛЕКТРО
@dp.callback_query_handler(lambda c: c.data == 'otdelka_2org')
async def finish_2(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_1/bytovka_024_cam001.jpg'),
                         caption='Размер: 2.4 х 2,4 м- пост охраны\n'
                                 'с электропроводкой,\n'
                                 'отделка  оргалит,\n'
                                 '1 окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 92 500 руб . с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

##################################################################################
# С ТАМБУРОМ  1 РАЗМЕР БЕЗ ЕЛЕКТРО
@dp.callback_query_handler(lambda c: c.data == 'otdelka_3org')
async def finish_3(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_1/bytovka_024_cam001.jpg'),
                         caption='Размер: 2.4 х 2,4 м- пост охраны\n'
                                  'без электропроводки,\n'
                                 ' отделка оргалит,\n'
                                 '3 окна рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 92 000 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

# С ТАМБУРОМ  1 РАЗМЕР С ЕЛЕКТРО
##################################################################################
@dp.callback_query_handler(lambda c: c.data == 'otdelka_4org')
async def finish_4(message: types.Message):
   await bot.send_photo(message.from_user.id, InputFile('photos/razmer_1/bytovka_024_cam001.jpg'),
                        caption='Размер: 2.4 х 2,4 м- пост охраны\n'
                                 'с электропроводкой,\n'
                                 ' отделка оргалит,\n'
                                 '3 окна рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 101 500 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')


#########################################  размер 2)) ###################################################################
# БЕЗ ТАМБУРА 2 РАЗМЕР БЕЗ ЕЛЕКТРО

@dp.callback_query_handler(lambda c: c.data == 'otdelka_5org')
async def finish_5(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_2/bytovka_032_cam002.jpg'),
                         caption='Размер: 3,0х2,4 м,\n'
                                 'без электропроводки,\n'
                                 'отделка оргалит,\n'
                                 '1 окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 99 500 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

@dp.callback_query_handler(lambda c: c.data == 'otdelka_5pvh')
async def finish_6(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_2/bytovka_032_cam002.jpg'),
                         caption='Размер: 3,0х2,4 м,\n'
                                 'без тамбура,\n'
                                 'без электропроводки,\n'
                                 'отделка вагонка ПВХ,\n'
                                 '1 окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 121 000 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')
@dp.callback_query_handler(lambda c: c.data == 'otdelka_5tree')
async def finish_7(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_2/bytovka_032_cam002.jpg'),
                         caption='Размер: 3,0х2,4 м,\n'
                                 'без тамбура,\n'
                                 'без электропроводки,\n'
                                 ' отделка дерево,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 135 000 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

##################################################################################
# БЕЗ ТАМБУРА 2 РАЗМЕР С ЕЛЕКТРО
@dp.callback_query_handler(lambda c: c.data == 'otdelka_6org')
async def finish_8(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_2/bytovka_032_cam002.jpg'),
                         caption='Размер: 3,0х2,4 м,\n'
                                 'без тамбура,\n'
                                 'с электропроводкой,\n'
                                 'отделка оргалит,\n'
                                 '1 окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 109 000 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

@dp.callback_query_handler(lambda c: c.data == 'otdelka_6pvh')
async def finish_9(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_2/bytovka_032_cam002.jpg'),
                         caption='Размер: 3,0х2,4 м,\n'
                                 'без тамбура,\n'
                                 'с электропроводкой,\n'
                                 'отделка вагонка ПВХ,\n'
                                 '1 окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 130 500 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')
@dp.callback_query_handler(lambda c: c.data == 'otdelka_6tree')
async def finish_10(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_2/bytovka_032_cam002.jpg'),
                         caption='Размер: 3,0х2,4 м,\n'
                                 'без тамбура,\n'
                                 'с электропроводкой,\n'
                                 ' отделка дерево,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 144 500 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

##################################################################################
# С ТАМБУРОМ  2 РАЗМЕР БЕЗ ЕЛЕКТРО

@dp.callback_query_handler(lambda c: c.data == 'otdelka_7org')
async def finish_11(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_2/bytovka_032_cam002.jpg'),
                         caption='Размер: 3,0х2,4 м,\n'
                                 'без тамбура,\n'
                                 'без электропроводки,\n'
                                 'отделка оргалит,\n'
                                 '1 окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 99 500 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

@dp.callback_query_handler(lambda c: c.data == 'otdelka_7pvh')
async def finish_12(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_2/bytovka_032_cam002.jpg'),
                         caption='Размер: 3,0х2,4 м,\n'
                                 'без тамбура,\n'
                                 'без электропроводки,\n'
                                 'отделка вагонка ПВХ,\n'
                                 '1 окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 121 000 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')
@dp.callback_query_handler(lambda c: c.data == 'otdelka_7tree')
async def finish_13(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_2/bytovka_032_cam002.jpg'),
                         caption='Размер: 3,0х2,4 м,\n'
                                 'без тамбура,\n'
                                 'без электропроводки,\n'
                                 ' отделка дерево,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 135 000 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')
# С ТАМБУРОМ  2 РАЗМЕР С ЕЛЕКТРО
##################################################################################

@dp.callback_query_handler(lambda c: c.data == 'otdelka_8org')
async def finish_14(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_2/bytovka_032_cam002.jpg'),
                         caption='Размер: 3,0х2,4 м,\n'
                                 'без тамбура,\n'
                                 'без электропроводки,\n'
                                 ' отделка оргалит,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 118 000 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')
@dp.callback_query_handler(lambda c: c.data == 'otdelka_8pvh')
async def finish_15(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_2/bytovka_032_cam002.jpg'),
                         caption='Размер: 3,0х2,4 м,\n'
                                 'без тамбура,\n'
                                 'без электропроводки,\n'
                                 ' отделка вагонка ПВХ,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 140 000 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')
@dp.callback_query_handler(lambda c: c.data == 'otdelka_8tree')
async def finish_16(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_2/bytovka_032_cam002.jpg'),
                         caption='Размер: 3,0х2,4 м,\n'
                                 'без тамбура,\n'
                                 'без электропроводки,\n'
                                 ' отделка дерево,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 154 000 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')
#########################################################
#3размер
#########################################################
# БЕЗ ТАМБУРА 3 РАЗМЕР БЕЗ ЕЛЕКТРО

@dp.callback_query_handler(lambda c: c.data == 'otdelka_9org')
async def finish_17(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_3/bytovka_043_cam001.jpg'),
                         caption='Размер: 4,0х2,4 м,\n'                                 
                                 'без электропроводки,\n'
                                 ' отделка оргалит,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 117 500 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')
@dp.callback_query_handler(lambda c: c.data == 'otdelka_9pvh')
async def finish_18(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_3/bytovka_043_cam001.jpg'),
                         caption='Размер: 4,0х2,4 м,\n'
                                 'без электропроводки,\n'
                                 ' отделка вагонка ПВХ,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 140 000 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

@dp.callback_query_handler(lambda c: c.data == 'otdelka_9tree')
async def finish_19(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_3/bytovka_043_cam001.jpg'),
                         caption='Размер: 4,0х2,4 м,\n'
                                 'без электропроводки,\n'
                                 ' отделка дерево,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 147 500 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

@dp.callback_query_handler(lambda c: c.data == 'otdelka_9mdf')
async def finish_20(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_3/bytovka_043_cam001.jpg'),
                         caption='Размер: 4,0х2,4 м,\n'
                                 'без электропроводки,\n'
                                 'отделка МДФ,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 145 500 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

##################################################################################################################
# БЕЗ ТАМБУРА 3 РАЗМЕР С ЕЛЕКТРО

@dp.callback_query_handler(lambda c: c.data == 'otdelka_10org')
async def finish_21(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_3/bytovka_043_cam001.jpg'),
                         caption='Размер: 4,0х2,4 м,\n'
                                 'c электропроводкой,\n'
                                 ' отделка оргалит,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 127 000 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')


@dp.callback_query_handler(lambda c: c.data == 'otdelka_10pvh')
async def finish_22(message: types.Message):
     await bot.send_photo(message.from_user.id, InputFile('photos/razmer_3/bytovka_043_cam001.jpg'),
                          caption='Размер: 4,0х2,4 м,\n'
                                  'c электропроводкой,\n'
                                  ' отделка вагонка ПВХ,\n'
                                  'одно окно рама деревянная, утепление - 50 мм.\n'
                                  'Цена: 149 500 руб. с НДС\n'
                                  'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

@dp.callback_query_handler(lambda c: c.data == 'otdelka_10tree')
async def finish_23(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_3/bytovka_043_cam001.jpg'),
                         caption='Размер: 4,0х2,4 м,\n'
                                 'c электропроводкой,\n'
                                 ' отделка дерево,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 157 000 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

@dp.callback_query_handler(lambda c: c.data == 'otdelka_10mdf')
async def finish_24(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_3/bytovka_043_cam001.jpg'),
                         caption='Размер: 4,0х2,4 м,\n'
                                 'c электропроводкой,\n'
                                 ' отделка МДФ,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 155 000 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')
##################################################################################################################
# С ТАМБУРОМ  3 РАЗМЕР БЕЗ ЕЛЕКТРО

@dp.callback_query_handler(lambda c: c.data == 'otdelka_11org')
async def finish_25(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_3/bytovka_043_cam001.jpg'),
                         caption='Размер: 4,0х2,4 м,\n'
                                 'три окна рама деревянная, утепление - 50 мм.\n'
                                 'без электропроводки,\n'
                                 ' отделка оргалит,\n'
                                 'Цена: 126 500 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

@dp.callback_query_handler(lambda c: c.data == 'otdelka_11pvh')
async def finish_26(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_3/bytovka_043_cam001.jpg'),
                         caption='Размер: 4,0х2,4 м,\n'
                                 'три окна рама деревянная, утепление - 50 мм.\n'
                                 'без электропроводки,\n'
                                 ' отделка вагонка ПВХ,\n'
                                 'Цена: 149 000 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

@dp.callback_query_handler(lambda c: c.data == 'otdelka_11tree')
async def finish_27(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_3/bytovka_043_cam001.jpg'),
                         caption='Размер: 4,0х2,4 м,\n'
                                 'три окна рама деревянная, утепление - 50 мм.\n'
                                 'без электропроводки,\n'
                                 ' отделка дерево,\n'
                                 'Цена: 156 500 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')


@dp.callback_query_handler(lambda c: c.data == 'otdelka_11mdf')
async def finish_28(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_3/bytovka_043_cam001.jpg'),
                         caption='Размер: 4,0х2,4 м,\n'
                                 'три окна рама деревянная, утепление - 50 мм.\n'
                                 'без электропроводки,\n'
                                 ' отделка МДФ,\n'
                                 'Цена: 154 500 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

##################################################################################################################
# С ТАМБУРОМ  3 РАЗМЕР С ЕЛЕКТРО

@dp.callback_query_handler(lambda c: c.data == 'otdelka_12org')
async def finish_29(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_3/bytovka_043_cam001.jpgg'),
                         caption='Размер: 4,0х2,4 м,\n'
                                 'три окна рама деревянная, утепление - 50 мм.\n'
                                 'c электропроводкой,\n'
                                 'отделка оргалит,\n'
                                 'Цена: 136 000 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')



@dp.callback_query_handler(lambda c: c.data == 'otdelka_12pvh')
async def finish_30(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_3/bytovka_043_cam001.jpg'),
                         caption='Размер: 4,0х2,4 м,\n'
                                 'три окна рама деревянная, утепление - 50 мм.\n'
                                 'c электропроводкой,\n'
                                 'отделка вагонка ПВХ,\n'
                                 'Цена: 158 500 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

@dp.callback_query_handler(lambda c: c.data == 'otdelka_12tree')
async def finish_31(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_3/bytovka_043_cam001.jpg'),
                         caption='Размер: 4,0х2,4 м,\n'
                                 'три окна рама деревянная, утепление - 50 мм.\n'
                                 'c электропроводкой,\n'
                                 'отделка дерево,\n'
                                 'Цена: 166 000 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

@dp.callback_query_handler(lambda c: c.data == 'otdelka_12mdf')
async def finish_32(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_3/bytovka_043_cam001.jpg'),
                         caption='Размер: 4,0х2,4 м,\n'
                                 'три окна рама деревянная, утепление - 50 мм.\n'
                                 'c электропроводкой,\n'
                                 'отделка МДФ,\n'
                                 'Цена: 164 000 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

#########################################################
#4размер
#########################################################
# БЕЗ ТАМБУРА 4 РАЗМЕР БЕЗ ЕЛЕКТРО
@dp.callback_query_handler(lambda c: c.data == 'otdelka_13org')
async def finish_33(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_4/bytovka_062_cam001.jpg'),
                         caption='Размер: 6,0х2,4 м,\n'
                                 'без тамбура,\n'
                                 'без электропроводки,\n'
                                 ' отделка оргалит,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 145 000 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')



@dp.callback_query_handler(lambda c: c.data == 'otdelka_13pvh')
async def finish_34(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_4/bytovka_062_cam001.jpg'),
                         caption='Размер: 6,0х2,4 м,\n'
                                 'без тамбура,\n'
                                 'без электропроводки,\n'
                                 ' отделка вагонка ПВХ,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 175 000 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')



@dp.callback_query_handler(lambda c: c.data == 'otdelka_13tree')
async def finish_35(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_4/bytovka_062_cam001.jpg'),
                         caption='Размер: 6,0х2,4 м,\n'
                                 'без тамбура,\n'
                                 'без электропроводки,\n'
                                 ' отделка дерево,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 185 000 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

@dp.callback_query_handler(lambda c: c.data == 'otdelka_13mdf')
async def finish_36(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_4/bytovka_062_cam001.jpg'),
                         caption='Размер: 6,0х2,4 м,\n'
                                 'без тамбура,\n'
                                 'без электропроводки,\n'
                                 ' отделка МДФ,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 182 000 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')
##################################################################################################################
# БЕЗ ТАМБУРА 4 РАЗМЕР c ЕЛЕКТРО

@dp.callback_query_handler(lambda c: c.data == 'otdelka_14org')
async def finish_37(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_4/bytovka_062_cam001.jpg'),
                         caption='Размер: 6,0х2,4 м,\n'
                                 'без тамбура,\n'
                                 'с электропроводкой,\n'
                                 ' отделка оргалит,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 154 500 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')


@dp.callback_query_handler(lambda c: c.data == 'otdelka_14pvh')
async def finish_38(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_4/bytovka_062_cam001.jpg'),
                         caption='Размер: 6,0х2,4 м,\n'
                                 'без тамбура,\n'
                                 'с электропроводкой,\n'
                                 ' отделка вагонка ПВХ,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 184 000 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

@dp.callback_query_handler(lambda c: c.data == 'otdelka_14tree')
async def finish_39(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_4/bytovka_062_cam001.jpg'),
                         caption='Размер: 6,0х2,4 м,\n'
                                 'без тамбура,\n'
                                 'с электропроводкой,\n'
                                 ' отделка дерево,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 194 500 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

@dp.callback_query_handler(lambda c: c.data == 'otdelka_14mdf')
async def finish_40(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_4/bytovka_062_cam001.jpg'),
                         caption='Размер: 6,0х2,4 м,\n'
                                 'без тамбура,\n'
                                 'с электропроводкой,\n'
                                 ' отделка МДФ,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 191 500 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')
##################################################################################################################
# c ТАМБУРОМ 4 РАЗМЕР БЕЗ ЕЛЕКТРО


@dp.callback_query_handler(lambda c: c.data == 'otdelka_15org')
async def finish_41(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_4/bytovka_062_cam001.jpg'),
                         caption='Размер: 6,0х2,4 м,\n'
                                 'с тамбуром,\n'
                                 'без электропроводки,\n'
                                 'отделка оргалит,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 150 000 руб с НДС./160 000 руб с НДС-распашонка.\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')


@dp.callback_query_handler(lambda c: c.data == 'otdelka_15pvh')
async def finish_42(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_4/bytovka_062_cam001.jpg'),
                         caption='Размер: 6,0х2,4 м,\n'
                                 'с тамбуром,\n'
                                 'без электропроводки,\n'
                                 ' отделка вагонка ПВХ,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 180 000 руб с НДС./190 000 руб с НДС-распашонка.\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')


@dp.callback_query_handler(lambda c: c.data == 'otdelka_15tree')
async def finish_43(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_4/bytovka_062_cam001.jpg'),
                         caption='Размер: 6,0х2,4 м,\n'
                                 'с тамбуром,\n'
                                 'без электропроводки,\n'
                                 ' отделка дерево,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 190 000 руб с НДС./200 000 руб с НДС-распашонка.\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')


@dp.callback_query_handler(lambda c: c.data == 'otdelka_15mdf')
async def finish_44(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_4/bytovka_062_cam001.jpg'),
                         caption='Размер: 6,0х2,4 м,\n'
                                 'с тамбуром,\n'
                                 'без электропроводки,\n'
                                 ' отделка МДФ,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 187 000 руб с НДС./197 000 руб с НДС-распашонка.\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

##################################################################################################################
# с ТАМБУРА 4 РАЗМЕР с ЕЛЕКТРО


@dp.callback_query_handler(lambda c: c.data == 'otdelka_16org')
async def finish_45(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_4/bytovka_062_cam001.jpg'),
                         caption='Размер: 6,0х2,4 м,\n'
                                 'с тамбуром,\n'
                                 'с электропроводкой,\n'
                                 ' отделка оргалит  ,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 159 500 руб с НДС./169 500 руб с НДС-распашонка.\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')


@dp.callback_query_handler(lambda c: c.data == 'otdelka_16pvh')
async def finish_46(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_4/bytovka_062_cam001.jpg'),
                         caption='Размер: 6,0х2,4 м,\n'
                                 'с тамбуром,\n'
                                 'с электропроводкой,\n'
                                 ' отделка вагонка ПВХ,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 189 500 руб с НДС./199 500 000 руб с НДС-распашонка.\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')


@dp.callback_query_handler(lambda c: c.data == 'otdelka_16tree')
async def finish_47(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_4/bytovka_062_cam001.jpg'),
                         caption='Размер: 6,0х2,4 м,\n'
                                 'с тамбуром,\n'
                                'с электропроводкой,\n'
                                 ' отделка дерево,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 199 500 руб с НДС./209 500 руб с НДС-распашонка.\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

@dp.callback_query_handler(lambda c: c.data == 'otdelka_16mdf')
async def finish_48(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_4/bytovka_062_cam001.jpg'),
                         caption='Размер: 6,0х2,4 м,\n'
                                 'с тамбуром,\n'
                                 'с электропроводкой,\n'
                                 ' отделка МДФ,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 196 500 руб с НДС./206 500 руб с НДС-распашонка.\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

#########################################################
#5размер
#########################################################

# БЕЗ ТАМБУРА 5 РАЗМЕР БЕЗ ЕЛЕКТРО


@dp.callback_query_handler(lambda c: c.data == 'otdelka_17org')
async def finish_49(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_5/bytovka_064_cam002.jpg'),
                         caption='Размер: 6,0х4,8 м,\n'
                                 'без тамбура,\n'
                                 'без электропроводки,\n'
                                 ' отделка оргалит,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 290 000 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

@dp.callback_query_handler(lambda c: c.data == 'otdelka_17pvh')
async def finish_50(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_5/bytovka_064_cam002.jpg'),
                         caption='Размер: 6,0х4,8 м,\n'
                                 'без тамбура,\n'
                                 'без электропроводки,\n'
                                 ' отделка вагонка ПВХ,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 350 000 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

@dp.callback_query_handler(lambda c: c.data == 'otdelka_17tree')
async def finish_51(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_5/bytovka_064_cam002.jpg'),
                         caption='Размер: 6,0х4,8 м,\n'
                                 'без тамбура,\n'
                                 'без электропроводки,\n'
                                 ' отделка дерево,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 375 000 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

@dp.callback_query_handler(lambda c: c.data == 'otdelka_17mdf')
async def finish_52(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_5/bytovka_064_cam002.jpg'),
                         caption='Размер: 6,0х4,8 м,\n'
                                 'без тамбура,\n'
                                 'без электропроводки,\n'
                                 ' отделка МДФ,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 375 000 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')
# БЕЗ ТАМБУРА 5 РАЗМЕР c ЕЛЕКТРО
##################################################################################################################

@dp.callback_query_handler(lambda c: c.data == 'otdelka_18org')
async def finish_53(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_5/bytovka_064_cam002.jpg'),
                         caption='Размер: 6,0х4,8 м,\n'
                                 'без тамбура,\n'
                                 'без электропроводки,\n'
                                 ' отделка оргалит,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 299 500 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

@dp.callback_query_handler(lambda c: c.data == 'otdelka_18pvh')
async def finish_54(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_5/bytovka_064_cam002.jpg'),
                         caption='Размер: 6,0х4,8 м,\n'
                                 'без тамбура,\n'
                                 'без электропроводки,\n'
                                 ' отделка вагонка ПВХ,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 359 500 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

@dp.callback_query_handler(lambda c: c.data == 'otdelka_18tree')
async def finish_55(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_5/bytovka_064_cam002.jpg'),
                         caption='Размер: 6,0х4,8 м,\n'
                                 'без тамбура,\n'
                                 'без электропроводки,\n'
                                 ' отделка дерево,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 384 500 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')


@dp.callback_query_handler(lambda c: c.data == 'otdelka_18mdf')
async def finish_56(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_5/bytovka_064_cam002.jpg'),
                         caption='Размер: 6,0х4,8 м,\n'
                                 'без тамбура,\n'
                                 'без электропроводки,\n'
                                 ' отделка МДФ,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 384 500 руб с НДС.\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')
# С ТАМБУРА 5 РАЗМЕР БЕЗ ЕЛЕКТРО
##################################################################################################################

@dp.callback_query_handler(lambda c: c.data == 'otdelka_19org')
async def finish_57(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_5/bytovka_064_cam002.jpg'),
                         caption='Размер: 6,0х4,8 м,\n'
                                 'без тамбура,\n'
                                 'без электропроводки,\n'
                                 ' отделка оргалит,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 295 000 руб с НДС.\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

@dp.callback_query_handler(lambda c: c.data == 'otdelka_19pvh')
async def finish_58(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_5/bytovka_064_cam002.jpg'),
                         caption='Размер: 6,0х4,8 м,\n'
                                 'без тамбура,\n'
                                 'без электропроводки,\n'
                                 ' отделка вагонка ПВХ,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 355 000 руб с НДС.\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

@dp.callback_query_handler(lambda c: c.data == 'otdelka_19tree')
async def finish_59(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_5/bytovka_064_cam002.jpg'),
                         caption='Размер: 6,0х4,8 м,\n'
                                 'без тамбура,\n'
                                 'без электропроводки,\n'
                                 ' отделка дерево,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 380 000 руб с НДС.\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')



@dp.callback_query_handler(lambda c: c.data == 'otdelka_19mdf')
async def finish_60(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_5/bytovka_064_cam002.jpg'),
                         caption='Размер: 6,0х4,8 м,\n'
                                 'без тамбура,\n'
                                 'без электропроводки,\n'
                                 ' отделка МДФ,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 380 000 руб с НДС.\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')
# С ТАМБУРА 5 РАЗМЕР с ЕЛЕКТРО
##################################################################################################################
@dp.callback_query_handler(lambda c: c.data == 'otdelka_20org')
async def finish_57(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_5/bytovka_064_cam002.jpg'),
                         caption='Размер: 6,0х4,8 м,\n'
                                 'без тамбура,\n'
                                 'без электропроводки,\n'
                                 ' отделка оргалит,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 304 500 руб с НДС.\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

@dp.callback_query_handler(lambda c: c.data == 'otdelka_20pvh')
async def finish_58(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_5/bytovka_064_cam002.jpg'),
                         caption='Размер: 6,0х4,8 м,\n'
                                 'без тамбура,\n'
                                 'без электропроводки,\n'
                                 ' отделка вагонка ПВХ,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 364 500 руб с НДС.\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')
@dp.callback_query_handler(lambda c: c.data == 'otdelka_20tree')
async def finish_59(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_5/bytovka_064_cam002.jpg'),
                         caption='Размер: 6,0х4,8 м,\n'
                                 'без тамбура,\n'
                                 'без электропроводки,\n'
                                 ' отделка дерево,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 389 500 руб с НДС.\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

@dp.callback_query_handler(lambda c: c.data == 'otdelka_20mdf')
async def finish_60(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_5/bytovka_064_cam002.jpg'),
                         caption='Размер: 6,0х4,8 м,\n'
                                 'без тамбура,\n'
                                 'без электропроводки,\n'
                                 ' отделка МДФ,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 389 500 руб с НДС.\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')
#########################################################
#6размер
#########################################################
# БЕЗ ТАМБУРА 6 РАЗМЕР БЕЗ ЕЛЕКТРО


@dp.callback_query_handler(lambda c: c.data == 'otdelka_20pvh')
async def finish_61(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_6/bytovka_084_cam001.jpg'),
                         caption='Размер: 8,0х2,4 м,\n'
                                 'без тамбура,\n'
                                 'без электропроводки,\n'
                                 ' отделка вагонка ПВХ,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 245 000 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')
@dp.callback_query_handler(lambda c: c.data == 'otdelka_20tree')
async def finish_62(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_6/bytovka_084_cam001.jpg'),
                         caption='Размер: 8,0х2,4 м,\n'
                                 'без тамбура,\n'
                                 'без электропроводки,\n'
                                 ' отделка дерево,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 275 000 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

@dp.callback_query_handler(lambda c: c.data == 'otdelka_20mdf')
async def finish_63(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_6/bytovka_084_cam001.jpg'),
                         caption='Размер: 8,0х2,4 м,\n'
                                 'без тамбура,\n'
                                 'без электропроводки,\n'
                                 ' отделка МДФ,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 270 000 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')
#########################################################
# БЕЗ ТАМБУРА 6 РАЗМЕР с ЕЛЕКТРО

@dp.callback_query_handler(lambda c: c.data == 'otdelka_21pvh')
async def finish_64(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_6/bytovka_084_cam001.jpg'),
                         caption='Размер: 8,0х2,4 м,\n'
                                 'без тамбура,\n'
                                 'с электропроводкой,\n'
                                 ' отделка вагонка ПВХ,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 254 500 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')
@dp.callback_query_handler(lambda c: c.data == 'otdelka_21tree')
async def finish_65(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_6/bytovka_084_cam001.jpg'),
                         caption='Размер: 8,0х2,4 м,\n'
                                 'без тамбура,\n'
                                 'с электропроводкой,\n'
                                 ' отделка дерево,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 284 500 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

@dp.callback_query_handler(lambda c: c.data == 'otdelka_21mdf')
async def finish_66(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_6/bytovka_084_cam001.jpg'),
                         caption='Размер: 8,0х2,4 м,\n'
                                 'без тамбура,\n'
                                 'с электропроводкой,\n'
                                 ' отделка МДФ,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 279 500 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')
#########################################################
# с ТАМБУРА 6 РАЗМЕР без ЕЛЕКТРО

@dp.callback_query_handler(lambda c: c.data == 'otdelka_22pvh')
async def finish_67(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_6/bytovka_084_cam001.jpg'),
                         caption='Размер: 8,0х2,4 м,\n'
                                 'с тамбуром,\n'
                                 'без электропроводки,\n'
                                 ' отделка вагонка ПВХ,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 250 000 руб с НДС./260 000 руб с НДС-распашонка.\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')
@dp.callback_query_handler(lambda c: c.data == 'otdelka_22tree')
async def finish_68(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_6/bytovka_084_cam001.jpg'),
                         caption='Размер: 8,0х2,4 м,\n'
                                 'с тамбуром,\n'
                                 'без электропроводки,\n'
                                 ' отделка дерево,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 280 000 руб с НДС./295 000 руб с НДС-распашонка.\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

@dp.callback_query_handler(lambda c: c.data == 'otdelka_22mdf')
async def finish_69(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_6/bytovka_084_cam001.jpg'),
                         caption='Размер: 8,0х2,4 м,\n'
                                 'с тамбуром,\n'
                                 'без электропроводки,\n'
                                 ' отделка МДФ,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 275 000 руб с НДС./290 000 руб с НДС-распашонка.\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')
#########################################################
# с ТАМБУРА 6 РАЗМЕР с ЕЛЕКТРО

@dp.callback_query_handler(lambda c: c.data == 'otdelka_23pvh')
async def finish_70(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_6/bytovka_084_cam001.jpg'),
                         caption='Размер: 8,0х2,4 м,\n'
                                 'с тамбуром,\n'
                                 'с электропроводкой,\n'
                                 ' отделка вагонка ПВХ,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 259 500 руб с НДС./269 500 руб с НДС-распашонка.\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

@dp.callback_query_handler(lambda c: c.data == 'otdelka_23tree')
async def finish_71(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_6/bytovka_084_cam001.jpg'),
                         caption='Размер: 8,0х2,4 м,\n'
                                 'с тамбуром,\n'
                                 'с электропроводкой,\n'
                                 ' отделка дерево,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                'Цена: 289 500 руб с НДС./304 500 руб с НДС-распашонка.\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

@dp.callback_query_handler(lambda c: c.data == 'otdelka_23mdf')
async def finish_72(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_6/bytovka_084_cam001.jpg'),
                         caption='Размер: 8,0х2,4 м,\n'
                                 'с тамбуром,\n'
                                 'с электропроводкой,\n'
                                 ' отделка мдф,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 284 500 руб с НДС./299 500 руб с НДС-распашонка.\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')
#########################################################
#7размер
#########################################################
# БЕЗ ТАМБУРА 7 РАЗМЕР БЕЗ ЕЛЕКТРО
@dp.callback_query_handler(lambda c: c.data == 'otdelka_25pvh')
async def finish_73(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_7/bytovka_092_cam001.jpg'),
                         caption='Размер: 9,0х2,4 м,\n'
                                 'без тамбура,\n'
                                 'без электропроводки,\n'
                                 ' отделка вагонка ПВХ,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 270 000 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')
@dp.callback_query_handler(lambda c: c.data == 'otdelka_25tree')
async def finish_74(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_7/bytovka_092_cam001.jpg'),
                         caption='Размер: 9,0х2,4 м,\n'
                                 'без тамбура,\n'
                                 'без электропроводки,\n'
                                 ' отделка вагонка ПВХ,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 295 000 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

@dp.callback_query_handler(lambda c: c.data == 'otdelka_25mdf')
async def finish_75(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_7/bytovka_092_cam001.jpg'),
                         caption='Размер: 9,0х2,4 м,\n'
                                 'без тамбура,\n'
                                 'без электропроводки,\n'
                                 ' отделка вагонка ПВХ,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 290 000 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')
#########################################################
# БЕЗ ТАМБУРА 7 РАЗМЕР с ЕЛЕКТРО

@dp.callback_query_handler(lambda c: c.data == 'otdelka_26pvh')
async def finish_76(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_7/bytovka_092_cam001.jpg'),
                         caption='Размер: 9,0х2,4 м,\n'
                                 'без тамбура,\n'
                                 'без электропроводки,\n'
                                 ' отделка вагонка ПВХ,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 279 500 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')
@dp.callback_query_handler(lambda c: c.data == 'otdelka_26tree')
async def finish_77(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_7/bytovka_092_cam001.jpg'),
                         caption='Размер: 9,0х2,4 м,\n'
                                 'без тамбура,\n'
                                 'без электропроводки,\n'
                                 ' отделка вагонка ПВХ,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 304 500 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

@dp.callback_query_handler(lambda c: c.data == 'otdelka_26mdf')
async def finish_78(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_7/bytovka_092_cam001.jpg'),
                         caption='Размер: 9,0х2,4 м,\n'
                                 'без тамбура,\n'
                                 'без электропроводки,\n'
                                 ' отделка вагонка ПВХ,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 299 500 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')
#########################################################
# с ТАМБУРА 7 РАЗМЕР без ЕЛЕКТРО

@dp.callback_query_handler(lambda c: c.data == 'otdelka_27pvh')
async def finish_79(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_7/bytovka_092_cam001.jpg'),
                         caption='Размер: 9,0х2,4 м,\n'
                                 'c тамбуром,\n'
                                 'без электропроводки,\n'
                                 ' отделка вагонка ПВХ,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 275 000 руб с НДС./295 000 руб с НДС-распашонка.\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

@dp.callback_query_handler(lambda c: c.data == 'otdelka_27tree')
async def finish_80(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_7/bytovka_092_cam001.jpg'),
                         caption='Размер: 9,0х2,4 м,\n'
                                 'c тамбуром,\n'
                                 'без электропроводки,\n'
                                 ' отделка дерово,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 300 000 руб с НДС./320 000 руб с НДС-распашонка.\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')
@dp.callback_query_handler(lambda c: c.data == 'otdelka_27mdf')
async def finish_81(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_7/bytovka_092_cam001.jpg'),
                         caption='Размер: 9,0х2,4 м,\n'
                                 'c тамбуром,\n'
                                 'без электропроводки,\n'
                                 ' отделка МДФ,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 295 000 руб с НДС./315 000 руб с НДС-распашонка.\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

#########################################################
# с ТАМБУРА 7 РАЗМЕР с ЕЛЕКТРО

@dp.callback_query_handler(lambda c: c.data == 'otdelka_28pvh')
async def finish_82(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_7/bytovka_092_cam001.jpg'),
                         caption='Размер: 9,0х2,4 м,\n'
                                 'c тамбуром,\n'
                                 'c электропроводкой,\n'
                                 ' отделка вагонка ПВХ,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 284 500 руб с НДС./304 500 руб с НДС-распашонка.\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')
@dp.callback_query_handler(lambda c: c.data == 'otdelka_28tree')
async def finish_83(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_7/bytovka_092_cam001.jpg'),
                         caption='Размер: 9,0х2,4 м,\n'
                                 'c тамбуром,\n'
                                 'c электропроводкой,\n'
                                 ' отделка дерево,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена:  309 500 руб с НДС./329 500 руб с НДС-распашонка.\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')
@dp.callback_query_handler(lambda c: c.data == 'otdelka_28mdf')
async def finish_84(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_7/bytovka_092_cam001.jpg'),
                         caption='Размер: 9,0х2,4 м,\n'
                                 'без тамбура,\n'
                                 'c электропроводкой,\n'
                                 ' отделка МДФ,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена:  304 500 руб с НДС./ 324 500 руб с НДС-распашонка.\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

#########################################################
#8размер
#########################################################
# без ТАМБУРА 8 РАЗМЕР без ЕЛЕКТРО

@dp.callback_query_handler(lambda c: c.data == 'otdelka_29pvh')
async def finish_85(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_8/bytovka_125_cam001.jpg'),
                         caption='Размер: 12,0х2,4 м,\n'
                                 'без тамбура,\n'
                                 'без электропроводки,\n'
                                 ' отделка вагонка ПВХ,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 340 000 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

@dp.callback_query_handler(lambda c: c.data == 'otdelka_29tree')
async def finish_86(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_8/bytovka_125_cam001.jpg'),
                         caption='Размер: 12,0х2,4 м,\n'
                                 'без тамбура,\n'
                                 'без электропроводки,\n'
                                 ' отделка дерево,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 370 000 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

@dp.callback_query_handler(lambda c: c.data == 'otdelka_29mdf')
async def finish_87(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_8/bytovka_125_cam001.jpg'),
                         caption='Размер: 12,0х2,4 м,\n'
                                 'без тамбура,\n'
                                 'без электропроводки,\n'
                                 ' отделка мдф,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 365 000 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')
#########################################################
# без ТАМБУРА 8 РАЗМЕР с ЕЛЕКТРО

@dp.callback_query_handler(lambda c: c.data == 'otdelka_30pvh')
async def finish_88(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_8/bytovka_125_cam001.jpg'),
                         caption='Размер: 12,0х2,4 м,\n'
                                 'без тамбура,\n'
                                 'с электропроводкой,\n'
                                 ' отделка вагонка ПВХ,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 349 500  руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')
@dp.callback_query_handler(lambda c: c.data == 'otdelka_30tree')
async def finish_89(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_8/bytovka_125_cam001.jpg'),
                         caption='Размер: 12,0х2,4 м,\n'
                                 'без тамбура,\n'
                                 'с электропроводкой,\n'
                                 ' отделка дерево,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 379 500 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

@dp.callback_query_handler(lambda c: c.data == 'otdelka_30mdf')
async def finish_90(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_8/bytovka_125_cam001.jpg'),
                         caption='Размер: 12,0х2,4 м,\n'
                                 'без тамбура,\n'
                                 'с электропроводкой,\n'
                                 ' отделка МДФ,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 374 500 руб. с НДС\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

#########################################################
# с ТАМБУРА 8 РАЗМЕР без ЕЛЕКТРО

@dp.callback_query_handler(lambda c: c.data == 'otdelka_31pvh')
async def finish_88(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_8/bytovka_125_cam001.jpg'),
                         caption='Размер: 12,0х2,4 м,\n'
                                 'с тамбуромя,\n'
                                 'без электропроводки,\n'
                                 ' отделка вагонка ПВХ,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 345 000 руб с НДС./360 000 руб с НДС-распашонка.\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

@dp.callback_query_handler(lambda c: c.data == 'otdelka_31tree')
async def finish_89(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_8/bytovka_125_cam001.jpg'),
                         caption='Размер: 12,0х2,4 м,\n'
                                 'с тамбуром,\n'
                                 'без электропроводки,\n'
                                 'отделка дерево,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 375 000 руб с НДС./385 000 руб с НДС-распашонка.\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

@dp.callback_query_handler(lambda c: c.data == 'otdelka_31mdf')
async def finish_90(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_8/bytovka_125_cam001.jpg'),
                         caption='Размер: 12,0х2,4 м,\n'
                                 'с тамбуром,\n'
                                 'без электропроводки,\n'
                                 ' отделка МДФ,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 370 000 руб с НДС./380 000 руб с НДС-распашонка.\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

#########################################################
# с ТАМБУРА 8 РАЗМЕР с ЕЛЕКТРО

@dp.callback_query_handler(lambda c: c.data == 'otdelka_32pvh')
async def finish_91(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_8/bytovka_125_cam001.jpg'),
                         caption='Размер: 12,0х2,4 м,\n'
                                 'c тамбуром,\n'
                                 'c электропроводкой,\n'
                                 ' отделка вагонка ПВХ,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 354 500 руб с НДС./369 500 руб с НДС-распашонка.\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')
@dp.callback_query_handler(lambda c: c.data == 'otdelka_32tree')
async def finish_92(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_8/bytovka_125_cam001.jpg'),
                         caption='Размер: 12,0х2,4 м,\n'
                                 'с тамбуром,\n'
                                 'с электропроводкой,\n'
                                 ' отделка дерево,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 384 500 руб с НДС./394 500 руб с НДС-распашонка.\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')

@dp.callback_query_handler(lambda c: c.data == 'otdelka_32mdf')
async def finish_93(message: types.Message):
    await bot.send_photo(message.from_user.id, InputFile('photos/razmer_8/bytovka_125_cam001.jpg'),
                         caption='Размер: 12,0х2,4 м,\n'
                                 'с тамбуром,\n'
                                 'с электропроводкой,\n'
                                 ' отделка  мдф,\n'
                                 'одно окно рама деревянная, утепление - 50 мм.\n'
                                 'Цена: 379 500 руб с НДС./389 500 руб с НДС-распашонка.\n'
                                 'Доставка 1 блок-контейнера манипулятором: до 100 км. от площадки (п. Вешки) = 11 900 руб. свыше 100 км. = 11 900 руб. + 100 руб./км (свыше 100 км.)')











































# @dp.callback_query_handler(lambda c: c.data == 'otdelka_1org')
# async def callback_handler(callback_query: types.CallbackQuery):
#     data_art = "stroy/2/Новая папка (2)/bytovka_062_cam001.jpg"
#     spriteKeyboard = InlineKeyboardMarkup(row_width=1)
#     photka_org1 = InlineKeyboardButton(text="дальше➡️", callback_data="photka_org1")
#     caption = f"98 000р (с ндс)"
#     spriteKeyboard.add(photka_org1)
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
main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
@dp.message_handler(lambda message: message.text == "о нас 🔍")
async def catalog(message: types.Message):
    await bot.send_message(message.from_user.id,
                         "Производство, продажа и аренда бытовок c 1997г"
                         '                                                                          '
                         "🏠 Бытовки от производителя"
                         "                                                                          "
                         "🚛 Доставка завтра"
                         "                                                                                                    " 
                         "👩‍💼Аренда и продажа "
                         "                                                                                                   "
                         "🏪 Всегда в наличии "
                         "                                                                                                    "
                         "📍 Москва МО "
                         "                                                                                                    "
                         "💵 Скидка за наличный расчет "
                         "                                                                                                   "
                         "🏙 Оплата после получения "
                         "                                                                                                    "
                         "💯 Гарантия "                         
                         "                                                                                                                             "
                         "⛔️ Без посредников"                         
                         "                                                                                                    ",reply_markup= main_menu)


@dp.message_handler(lambda message: message.text == "контакты 📞")
async def catalog(message: types.Message):
    await bot.send_message(message.from_user.id,"  сайт bitovkin.ru,                                                                                               "
                                                " "
                                                "тел.: +7 (495) 780-61-60, +7 (495) 971-49-46, +7 (495) 741-46-63                                                       "
                                                
                                                "адрес нашей эл.почты: bitovkin@mail.ru                                                                      "
                                                
                                                "адрес: е"
                                                "МО,поселок Вешки, ул.Заводская, дом3Б                                                                                                                                       ")


try:
        # logger.info(f"\nSTATUS: Бот запущен.\n")
    executor.start_polling(dp,skip_updates = True)
except Exception as e:
    # logger.error(f"\nERROR: {e}\n")
    print(e)
