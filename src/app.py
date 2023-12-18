'''The module of the bot'''
import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import bot

load_dotenv()

# bot setup
Token = os.getenv('TELEGRAM_BOT_API')
app = ApplicationBuilder().token(Token).build()

# Init app handles
app.add_handler(CommandHandler('start', bot.start))
app.add_handler(CommandHandler('content', bot.content))
app.add_handler(CommandHandler('info', bot.info))
app.add_handler(CommandHandler('Python', bot.Python))
app.add_handler(CommandHandler('SQL', bot.SQL))
app.add_handler(CommandHandler('subgraph', bot.sub_graph_testing))

app.run_polling()
