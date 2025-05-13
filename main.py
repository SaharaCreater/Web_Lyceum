import json
import csv
import logging
from random import sample
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from bot_token import TOKEN

# Загрузка данных тестов
with open('geography_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Структуры для хранения состояния пользователя
user_sessions = {}

# Запускаем логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)
reply_keyboard = [['/start'], ['/test', '/level', '/stats'], ['/help'], ['/stop']]
first = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
level = [['лёгкий', 'средний', 'сложный']]
second = ReplyKeyboardMarkup(level, one_time_keyboard=True)
LEVEL = 1
point = 1


# Стартовая команда
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global point
    point = 0
    await update.message.reply_text(
        "Привет! Я бот c географическими тестами.\n"
        "Используйте /test, чтобы начать тест.\n"
        "Используйте /stats для просмотра статистики.", reply_markup=first
    )


async def test_level(update, context):
    global point
    await update.message.reply_text(
        'Выбери сложность', reply_markup=second
    )


# Старт теста
async def test_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global point
    point = 1
    user_id = update.message.from_user.id
    # Выбор теста (по умолчанию первый)
    name = ['лёгкий', 'средний', 'сложный'][LEVEL - 1]
    test = data['tests'][LEVEL - 1]
    await update.message.reply_text(f"Уровень: {name}")
    # Инициализация сессии
    user_sessions[user_id] = {
        'test': test,
        'questions': sample(test['items'], len(test['items'])),
        'current_index': 0,
        'correct': 0,
        'incorrect': 0,
        'awaiting_answer': False,
        'current_item': None
    }
    await send_question(update, user_id)


# Отправка вопроса
async def send_question(update: Update, user_id: int):
    global point
    if point == 0:
        return
    session = user_sessions[user_id]
    idx = session['current_index']
    if idx >= len(session['questions']):
        # Тест завершён
        point = 0
        await update.message.reply_text(
            f"Тест завершен!\nПравильных ответов: {session['correct']}\n"
            f"Неправильных: {session['incorrect']}"
            )
        name = update.message.from_user.first_name
        # Запись данных в csv-файл
        with open("test_stats.csv", 'r', newline='', encoding='utf-8') as csvfile:
            reader = list(csv.reader(csvfile))
            reader[0] = ['Пользователь', name]
            reader[1] = ['Правильных ответов', session['correct']]
            reader[2] = ['Неправильных ответов', session['incorrect']]
        with open("test_stats.csv", 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(reader)
        return
    item = session['questions'][idx]
    session['current_item'] = item
    session['awaiting_answer'] = True
    # Отправка изображения
    await update.message.reply_photo(photo=item['image_url'], caption="Какой город изображен на снимке?")


# Обработка ответов
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global point
    global LEVEL
    if point == 0:
        return
    name = update.message.text
    if name in ['лёгкий', 'средний', 'сложный']:
        point = 0
        if 'средний' in name:
            LEVEL = 2
        elif 'сложный' in name:
            LEVEL = 3
        else:
            LEVEL = 1
        await update.message.reply_text(f"Уровень: {name}\nТеперь вы можете начать тест командой /test", reply_markup=first)
        return
    user_id = update.message.from_user.id
    if user_id not in user_sessions:
        await update.message.reply_text("Пожалуйста, начните тест командой /test")
        return
    session = user_sessions[user_id]
    if not session['awaiting_answer']:
        await update.message.reply_text("Пожалуйста, дождитесь следующего вопроса.")
        return
    user_answer = update.message.text.strip()
    correct_answer = session['current_item']['label']
    if user_answer.lower() == correct_answer.lower():
        session['correct'] += 1
        reply = "Верно!"
    else:
        session['incorrect'] += 1
        reply = f"Неверно! Правильный ответ: {correct_answer}"
    session['current_index'] += 1
    await update.message.reply_text(reply)
    # Следующий вопрос
    await send_question(update, user_id)


# Статистика
async def stats_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global point
    point = 0
    stats_text = "Ваша статистика:\n"
    name = update.message.from_user.first_name
    for user_id, session in user_sessions.items():
        stats_text += (
            f"Пользователь {name}:\n"
            f"Правильных: {session['correct']}\n"
            f"Неправильных: {session['incorrect']}\n\n"
        )
    await update.message.reply_text(stats_text)


# Основная функция
def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('level', test_level))
    application.add_handler(CommandHandler('test', test_command))
    application.add_handler(CommandHandler('stats', stats_command))
    application.add_handler(CommandHandler('help', start))
    application.add_handler(CommandHandler('stop', stats_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.run_polling()


if __name__ == '__main__':
    main()
