import telepot
token = '554680415:AAHWqnbApEfGVpdA9AB1Xey9qzRy-TOcUPM'
TelegramBot = telepot.Bot(token)
print TelegramBot.getMe()