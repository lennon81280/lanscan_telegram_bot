from telegram.ext import Updater, CommandHandler
import logging
import nmap

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s ' )

def start(bot, update):
    update.message.reply_text('Hello World!')

def scan(bot, update):

	nm = nmap.PortScanner()
	machines = nm.scan(hosts='192.168.1.0/24', arguments='-sP')
	for k,v in machines['scan'].iteritems(): 
		if str(v['status']['state']) == 'up':
			try:
				update.message.reply_text(str(v['addresses']['ipv4'])+"-"+str(v['addresses']['mac'])+ "-"+str(v['vendor']))
			except: 
				update.message.reply_text(str(v['addresses']['ipv4'])+"-No MAC detected.")
				
updater = Updater('YourTokenHERE')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('scan', scan))

updater.start_polling()
updater.idle()
