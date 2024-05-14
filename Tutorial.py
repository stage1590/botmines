import time
import random
from datetime import datetime
import bd

import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

api_key = '6998203922:AAE004UkzJmLyWpldDVmximlfYR6TG1A_kE'
chat_id = '-1002003028428'

bot = telebot.TeleBot(token=api_key)

def ALERT_GALE1():
    current_time = datetime.now()
    formatted_time = current_time.strftime('%H:%M:%S')
    message_id = bot.send_message(chat_id=chat_id, text=f'''
🔍 Possivel Entrada Detectada''').message_id
    bd.message_ids1 = message_id
    time.sleep(15)
    bd.message_delete1 = True

def DELETE_GALE1():
    if bd.message_delete1:
        bot.delete_message(chat_id=chat_id, message_id=bd.message_ids1)
        bd.message_delete1 = False

def gerar_minas(quantidade):
    minas = ['💣'] * quantidade + ['💎'] * (25 - quantidade)
    random.shuffle(minas)
    return minas

def button_link():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton(text="📲 Cadastre-se Agora", url="https://cool-bet.com/yj5p5c4gb"))
    return markup

while True:
    current_time = datetime.now()
    formatted_time = current_time.strftime('%H:%M:%S')
    print(formatted_time)

    minas_configuracoes = [3, 4]
    for minas in minas_configuracoes:
       cores = ['⭐', '🟦', '🟦', '🟦', '🟦', '⭐', '🟦', '🟦', '🟦', '🟦', '⭐', '🟦', '🟦', '🟦', '🟦', '⭐', '🟦', '🟦', '🟦', '🟦', '⭐', '🟦', '🟦', '⭐', '🟦']

    ALERT_GALE1()  

    DELETE_GALE1()  

    sample = random.sample(cores, k=25)
    message_text = f'''
🕛 Válido até: {formatted_time}
✅ Apostar 3% da sua BANCA                                                    
💣 Minas: {minas}
⏰ Valido Durante: 4 minutos
🔁 Nº de entradas: 3

{' '.join(sample[:5])}
{' '.join(sample[5:10])}
{' '.join(sample[10:15])}
{' '.join(sample[15:20])}
{' '.join(sample[20:])}
'''

    dados = bot.send_message(chat_id=chat_id, text=message_text, reply_markup=button_link())

    time.sleep(240)

    bot.edit_message_text(f'''
✅Sinal finalizado às: {formatted_time}✅
Bateu a meta? Volte AMANHÃ!
    ''', dados.chat.id, dados.message_id)
