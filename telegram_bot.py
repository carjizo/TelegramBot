from telegram.ext import Updater, CallbackContext, CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram import Update

updater = Updater(
    token='5237631573:AAEkmCd7i_pcxe1KL8bfVAUeGqphOxIHRuw', 
    use_context=True,
    request_kwargs={'read_timeout': 1000, 'connect_timeout': 1000}
    )

dispatcher = updater.dispatcher


def start(
    update: Update, 
    context: CallbackContext
    ):
    context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="Soy una bot, por favor háblame!"
        )

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def echo(
    update: Update, 
    context: CallbackContext
    ):
    context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=update.message.text)
        

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

def video(
    update: Update, 
    context: CallbackContext
    ):
    context.bot.send_video(
        chat_id=update.effective_chat.id, 
        video=open('./video_capture/output.avi','rb'),
        caption="Hola, te envio este video, miralo!"
        )

video_handler = CommandHandler('video', video)
dispatcher.add_handler(video_handler)





updater.start_polling()



