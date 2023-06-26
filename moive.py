import telebot
from telebot import types
import random
from tmdbv3api import TMDb, Movie, Discover  # Database with movies
tmdb = TMDb()
bot = telebot.TeleBot('5840163914:AAGIB0uWOo6FZvFdNFJcJwHa_Sms__sIzQ4')

b = random.randint(1, 195)

tmdb.api_key = '3d47413eb828a8d573e11f130f37f299'
tmdb.language = 'uk'  # choose your language


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    film = types.KeyboardButton('Вибрати фільм')
    end = types.KeyboardButton('Стоп')
    markup.add(film, end)
    mess = f'Бот запущено, <b>{message.from_user.first_name}</b>\nЯ  допоможу тобі з вибором фільму!'
    bot.send_message(message.chat.id, mess,
                     parse_mode='html', reply_markup=markup)
    # bot.send_message(message.chat.id, message, parse_mode='html')


@bot.message_handler(content_types='text')
def reply_button(message):
    if message.text == 'Вибрати фільм':
        markup_2 = types.InlineKeyboardMarkup()
        markup_2.add(types.InlineKeyboardButton('Жахи', callback_data='btn1'),
                     types.InlineKeyboardButton(
                         'Комедія', callback_data='btn2'),
                     types.InlineKeyboardButton(
                         'Пригодницький', callback_data='btn3'),
                     types.InlineKeyboardButton(
                         'Триллер', callback_data='btn4'),
                     types.InlineKeyboardButton(
                         'Мультфільм', callback_data='btn5'),
                     types.InlineKeyboardButton(
                         'Драма', callback_data='btn6'),
                     types.InlineKeyboardButton('Фентезі', callback_data='btn7'))
        bot.send_message(
            message.chat.id, f'Виберіть жанр, {message.from_user.first_name}', reply_markup=markup_2)
    elif message.text == 'Стоп':
        bot.send_message(
            message.chat.id, f'До побачення, {message.from_user.username}.\nГарного перегляду ;)')
        bot.polling(none_stop=False)


@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data(callback):
    if callback.data == 'btn1':
        discover = Discover()
        horror = discover.discover_movies({
            'with_genres': 27
        })
        hr_choice = random.choice(horror)
        # img = open(a.poster_path, 'rb')
        # bot.send_photo(callback.message.chat.id, img)
        bot.send_message(callback.message.chat.id,
                         f'{hr_choice.title}\nДата прем\'єри: {hr_choice.release_date}\nСередня оцінка: {hr_choice.vote_average}\nСюжет: {hr_choice.overview}')

    if callback.data == 'btn2':
        discover = Discover()
        comedy = discover.discover_movies({
            'with_genres': 35
        })
        cmd_choice = random.choice(comedy)
        # img = open(a.poster_path, 'rb')
        # bot.send_photo(callback.message.chat.id, img)
        bot.send_message(callback.message.chat.id,
                         f'{cmd_choice.title}\nДата прем\'єри: {cmd_choice.release_date}\nСередня оцінка: {cmd_choice.vote_average}\nСюжет: {cmd_choice.overview}')

    if callback.data == 'btn3':
        discover = Discover()
        advent = discover.discover_movies({
            'with_genres': 12
        })
        ad_choice = random.choice(advent)
        # img = open(a.poster_path, 'rb')
        # bot.send_photo(callback.message.chat.id, img)
        bot.send_message(callback.message.chat.id,
                         f'{ad_choice.title}\nДата прем\'єри: {ad_choice.release_date}\nСередня оцінка: {ad_choice.vote_average}\nСюжет: {ad_choice.overview}')

    if callback.data == 'btn4':
        discover = Discover()
        thriller = discover.discover_movies({
            'with_genres': 53
        })
        thr_choice = random.choice(thriller)
        # img = open(a.poster_path, 'rb')
        # bot.send_photo(callback.message.chat.id, img)
        bot.send_message(callback.message.chat.id,
                         f'{thr_choice.title}\nДата прем\'єри: {thr_choice.release_date}\nСередня оцінка: {thr_choice.vote_average}\nСюжет: {thr_choice.overview}')

    if callback.data == 'btn5':
        discover = Discover()
        cartoon = discover.discover_movies({
            'with_genres': 16
        })
        crtn_choice = random.choice(cartoon)
        # img = open(a.poster_path, 'rb')
        # bot.send_photo(callback.message.chat.id, img)
        bot.send_message(callback.message.chat.id,
                         f'{crtn_choice.title}\nДата прем\'єри: {crtn_choice.release_date}\nСередня оцінка: {crtn_choice.vote_average}\nСюжет: {crtn_choice.overview}')

    if callback.data == 'btn6':
        discover = Discover()
        drama = discover.discover_movies({
            'with_genres': 18
        })
        drm_choice = random.choice(drama)
        # img = open(a.poster_path, 'rb')
        # bot.send_photo(callback.message.chat.id, img)
        bot.send_message(callback.message.chat.id,
                         f'{drm_choice.title}\nДата прем\'єри: {drm_choice.release_date}\nСередня оцінка: {drm_choice.vote_average}\nСюжет: {drm_choice.overview}')

    if callback.data == 'btn7':
        discover = Discover()
        fantasy = discover.discover_movies({
            'with_genres': 14
        })
        fnts_choice = random.choice(fantasy)
        # img = open(a.poster_path, 'rb')
        # bot.send_photo(callback.message.chat.id, img)
        bot.send_message(callback.message.chat.id,
                         f'{fnts_choice.title}\nДата прем\'єри: {fnts_choice.release_date}\nСередня оцінка: {fnts_choice.vote_average}\nСюжет: {fnts_choice.overview}')


bot.polling(none_stop=True)
