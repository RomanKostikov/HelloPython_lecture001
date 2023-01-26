"""Doc."""
from telegram.ext import ApplicationBuilder, CommandHandler
from bot_commands import hi_command, time_command, help_command, sum_command

app = ApplicationBuilder().token(
    "5899506735:AAGtU9VzrtuLLHgLpGaf3kgTEfF-ePqLTXY").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))

print('server start')
app.run_polling()
