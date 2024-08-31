from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

# Функция для команды /start
def start(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("Play", callback_data='play')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Absolutely Nothing. You could click "Play" button, but Nothing here...' reply_markup=reply_markup)

# Функция для обработки нажатий кнопок
def button(update: Update, context):
    query = update.callback_query
    query.answer()

    if query.data == 'play':
        query.message.reply_text('Открываем игру...', reply_markup=InlineKeyboardMarkup([]))
        # Используйте ссылку на ваше веб-приложение
        query.message.reply_text('[Открыть игру](https://honeyfxckers.github.io/)', parse_mode='Markdown')

# Основная функция для запуска бота
def main():
    updater = Updater("6926943403:AAEXHHWGc-u_TcyjGN6OKX_UOkhqp9W-lRM", use_context=True)
    dp = updater.dispatcher

    # Команда /start
    dp.add_handler(CommandHandler("start", start))

    # Обработка нажатий кнопок
    dp.add_handler(CallbackQueryHandler(button))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
