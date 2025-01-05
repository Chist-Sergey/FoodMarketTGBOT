import os
import dotenv
import logging
import telegram as tl
import telegram.ext

dotenv.load_dotenv()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


def start(update: telegram.ext.Update, context: telegram.ext.CallbackContext):
    update.message.reply_text("Hello World!")


if __name__ == "__main__":
    bot = tl.ApplicationBuilder().token(os.getenv("TOKEN")).build()

    bot.add_handler(tl.CommandHandler("start", start))

    bot.run_polling(poll_interval=1.0)
