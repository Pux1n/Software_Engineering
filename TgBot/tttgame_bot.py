import telebot
from telebot import types

bot = telebot.TeleBot('6797479769:AAGy-waoaZX04kyPpZuYjdDbHEuQOXN5N6U')

size = 5
board = [['⏹️' for r in range(size)] for c in range(size)]
players = ('❌', '⭕', '❓', '❗')
c_p = 0
current_player = players[c_p]


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Начать новую игру")
    markup.add(item1)

    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!".format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mdg_handler(message):
    if message.chat.type == 'private':
        if message.text == 'Начать новую игру':
            global board
            global current_player
            global size
            global players
            global c_p

            board = [['⏹️' for _ in range(size)] for _ in range(size)]
            c_p = 0
            current_player = players[c_p]

            markup = types.InlineKeyboardMarkup()

            for r in range(size):
                row = []
                c = 0
                while c <= size - 1:
                    item = types.InlineKeyboardButton(board[r][c], callback_data=str(r) + " " + str(c))
                    row.append(item)
                    c += 1
                markup.row(*row)

            bot.send_message(message.chat.id, "Ход ❌:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            global board
            global current_player
            global players
            global c_p
            row = int(call.data.split()[0])
            col = int(call.data.split()[1])
            if board[row][col] == '⏹️':
                board[row][col] = current_player

            else:
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                          text="Выберите незанятую ячейку!")

            if check_winner():
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text=f"{current_player} выиграл 🎉\n\n" + '\n'.join([''.join(map(str, row))
                                                                                          for row in board]),
                                      reply_markup=None)

            elif is_board_full():
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text=f"Hичья!\n\n" + '\n'.join([''.join(map(str, row)) for row in board]),
                                      reply_markup=None)

            else:
                if c_p == 3:
                    c_p = 0
                    current_player = players[c_p]

                else:
                    c_p += 1
                    current_player = players[c_p]

                markup = types.InlineKeyboardMarkup()
                for r in range(size):
                    row = []
                    c = 0
                    while c <= size - 1:
                        item = types.InlineKeyboardButton(board[r][c], callback_data=str(r) + " " + str(c))
                        row.append(item)
                        c += 1
                    markup.row(*row)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text=f"Ход {current_player}:",
                                      reply_markup=markup)

    except Exception as e:
        print(repr(e))


def check_winner():
    global current_player
    global board

    # строки
    for row in board:
        for col in range(3):
            if all(row[col + i] == current_player for i in range(3)):
                return True

    # колонки
    for col in range(5):
        for row in range(3):
            if all(board[row + i][col] == current_player for i in range(3)):
                return True

    # диагонали
    for row in range(3):
        for col in range(3):
            if all(board[row + i][col + i] == current_player for i in range(3)):
                return True
            if all(board[row + i][col + 2 - i] == current_player for i in range(3)):
                return True

    return False


def is_board_full():
    global board
    return all(all(cell != '⏹️' for cell in row) for row in board)


bot.polling(none_stop=True)
