import time
import random
import json
import telebot
from datetime import datetime, timedelta
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
import bd

api_key = '6998203922:AAE004UkzJmLyWpldDVmximlfYR6TG1A_kE'
chat_id = '-1002003028428'

bot = telebot.TeleBot(token=api_key)

def ALERT_GALE1():
    message_id = bot.send_message(chat_id=chat_id, text='🔍 Possível Entrada Detectada').message_id
    bd.message_ids1 = message_id
    time.sleep(15)
    bd.message_delete1 = True

def DELETE_GALE1():
    if bd.message_delete1 == True:
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
    current_time = datetime.now().strftime('%H:%M')
    print(current_time)

    minas_configuracoes = [3, 4]
    cores = ['💎', '⬛️', '⬛️', '⬛️', '⬛️', '💎', '⬛️', '⬛️', '⬛️', '⬛️', '💎', '⬛️', '⬛️', '⬛️', '⬛️', '💎', '⬛️', '⬛️', '⬛️', '⬛️', '💎', '⬛️', '⬛️', '💎', '⬛️']

    for minas in minas_configuracoes:
        ALERT_GALE1()
        current_time_dt = datetime.now()
        future_time_dt = current_time_dt + timedelta(minutes=4)
        future_time_str = future_time_dt.strftime('%H:%M')
        sample = random.sample(cores, k=25)
        message_text = f'''
❗️ SINAIS REI_DO_LUCRO777 ❗️
🕛 Válido até: {future_time_str}
✅ Apostar 3% da sua BANCA                                                    
💣 Minas: {minas}
⏰ Válido durante: 4 minutos
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
✅ Green ✅ Sinal finalizado às: {future_time_str}
Bateu a meta? Volte AMANHÃ!
''', dados.chat.id, dados.message_id)
        DELETE_GALE1()

    time.sleep(90)
