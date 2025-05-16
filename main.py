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
level = [['/easy', '/normal', '/hard']]
second = ReplyKeyboardMarkup(level, one_time_keyboard=True)


# Стартовая команда
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["point"] = 0
    context.user_data["level"] = 1
    await update.message.reply_text(
        "Привет! Я бот c географическими тестами.\n"
        "Используйте /test, чтобы начать тест.\n"
        "Используйте /stats для просмотра статистики.\n"
        "Используйте /level для смены уровня сложности.\n"
        "Уровень по умолчанию: легкий", reply_markup=first
    )


async def level(update, context):
    await update.message.reply_text(
        'Выбери сложность', reply_markup=second
    )

async def test_level(update, context):
    text = update.message.text
    if text == '/easy':
        context.user_data["level"] = 1
    elif text == '/normal':
        context.user_data["level"] = 2
    else:
        context.user_data["level"] = 3
    context.user_data["point"] = 0
    await update.message.reply_text(f"Уровень: {text}\nТеперь вы можете начать тест командой /test", reply_markup=first)
    return


# Старт теста
async def test_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["point"] = 1
    user_id = update.message.from_user.id
    # Выбор теста (по умолчанию первый)
    name = ['лёгкий', 'средний', 'сложный'][context.user_data["level"] - 1]
    test = data['tests'][context.user_data["level"] - 1]
    await update.message.reply_text(f"Уровень: {name}")
    # Инициализация сессии
    user_sessions[user_id] = {
        'test': test,
        'questions': sample(test['items'], 10),
        'current_index': 0,
        'correct': 0,
        'incorrect': 0,
        'awaiting_answer': False,
        'current_item': None
    }
    await send_question(update, user_id, context)


# Отправка вопроса
async def send_question(update: Update, user_id: int, context: ContextTypes.DEFAULT_TYPE):
    if context.user_data["point"] == 0:
        return
    session = user_sessions[user_id]
    idx = session['current_index']
    if idx >= len(session['questions']):
        context.user_data["point"] = 0
        # Тест завершён
        await update.message.reply_text(
            f"Тест завершен!\nПравильных ответов: {session['correct']}\n"
            f"Неправильных: {session['incorrect']}"
            )
        name = update.message.from_user.first_name
        with open('test_stats.csv', "r+", newline="", encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            lines = list(reader)
            if name in [a[0] for a in lines]:
                n = 0
                for i in lines:
                    if i[0] == name:
                        if int(i[context.user_data["level"]]) < int(session['correct']):
                            lines[n][int(context.user_data["level"])] = str(session['correct'])
                            with open('test_stats.csv', 'w', newline='', encoding='utf-8') as file:
                                writer = csv.writer(file)
                                writer.writerows(lines)
                        break
                    n += 1
            else:
                writer = csv.writer(
                    csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                if context.user_data["level"] == 1:
                    writer.writerow([name, session['correct'], 0, 0])
                elif context.user_data["level"] == 2:
                    writer.writerow([name, 0, session['correct'], 0])
                elif context.user_data["level"] == 3:
                    writer.writerow([name, 0, 0, session['correct']])
        return
    item = session['questions'][idx]
    session['current_item'] = item
    session['awaiting_answer'] = True
    # Отправка изображения
    await update.message.reply_photo(photo=item['image_url'], caption="Какой город изображен на снимке?")


# Обработка ответов
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.user_data["point"] == 0:
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
    await send_question(update, user_id, context)


# Статистика
async def stats_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["point"] = 0
    stats_text = "Ваша статистика:\n"
    name = update.message.from_user.first_name
    with open('test_stats.csv', "r+", newline="", encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        lines = list(reader)
        is_user = False
        for i in lines:
            if i[0] == name:
                is_user = True
                easy = i[1]
                normal = i[2]
                hard = i[3]
                break

    if is_user:
        stats_text += (
            f"Пользователь {name}:\n"
            f"Лучший результат в лёгком тесте: {easy} из 10\n"
            f"Лучший результат в среднем тесте: {normal} из 10\n"
            f"Лучший результат в сложном тесте: {hard} из 10\n"
            )
    else:
        stats_text += "Не пройден ни один тест\n"

    await update.message.reply_text(stats_text)


# Основная функция
def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('level', level))
    application.add_handler(CommandHandler('easy', test_level))
    application.add_handler(CommandHandler('normal', test_level))
    application.add_handler(CommandHandler('hard', test_level))
    application.add_handler(CommandHandler('test', test_command))
    application.add_handler(CommandHandler('stats', stats_command))
    application.add_handler(CommandHandler('help', start))
    application.add_handler(CommandHandler('stop', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.run_polling()


if __name__ == '__main__':
    main()
