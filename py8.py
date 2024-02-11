import requests
import logging
from telegram.ext import *
from telegram.ext import Updater, CommandHandler
import responses
from bs4 import BeautifulSoup


def send_message_to_telegram_bot(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, params=params)
    updates_data = response.json()
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print("Failed to send message.")
bot_token = "6923769393:AAE4JNy4bTkBvchtDE5AJAZjTpd4O1F5JmA"
chat_id = "5158199727"
channel_username = "https://t.me/Ethio_shopping_channel"
# Replace with your scraped data
url = 'https://addismercato.com/'
url2 = 'https://addismercato.com/%E1%8B%A8%E1%88%B4%E1%89%B6%E1%89%BD-women-s/'
url3 = 'https://addismercato.com/men-s-%E1%8B%A8%E1%8B%88%E1%8A%95%E1%8B%B6%E1%89%BD/'
url4 = 'https://addismercato.com/automotive/'





response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, 'html.parser')

category = soup.find_all('h5', class_="product-name")
catli = [h5.text for h5 in category[:10]]  # Limit to the first 5 elements


price = soup.find_all('span', class_="product-price")
pricloop = [span.text for span in price[:10]]  # Limit to the first 5 elements

photo = soup.find_all('img', class_='photo')
img = [img['src'] for img in photo[:10]]




response2 = requests.get(url2)
content2 = response2.content

soup2 = BeautifulSoup(content2, 'html.parser')

ul_tag = soup2.find('ul', class_='products-grid grid-list')

category2 = ul_tag.find_all('h5', class_="product-name")
catli2 = [h5.text for h5 in category2[:5]]  # Limit to the first 5 elements

price2 = ul_tag.find_all('span', class_="product-price")
pricloop2 = [span.text for span in price2[:5]]  # Limit to the first 5 elements

photo2 = ul_tag.find_all('img', class_='photo')
img2 = [img['src'] for img in photo2[:5]]






response3 = requests.get(url3)
content3 = response3.content

soup3 = BeautifulSoup(content3, 'html.parser')

ul_tag3 = soup3.find('ul', class_='products-grid grid-list')

category3 = ul_tag3.find_all('h5', class_="product-name")
catli3 = [h5.text for h5 in category3[:5]]  # Limit to the first 5 elements

price3 = ul_tag3.find_all('span', class_="product-price")
pricloop3 = [span.text for span in price3[:5]]  # Limit to the first 5 elements

photo3 = ul_tag3.find_all('img', class_='photo')
img3 = [img['src'] for img in photo3[:5]]






response4 = requests.get(url4)
content4 = response4.content

soup4 = BeautifulSoup(content4, 'html.parser')

ul_tag4 = soup4.find('ul', class_='products-grid grid-list')

category4 = ul_tag4.find_all('h5', class_="product-name")
catli4 = [h5.text for h5 in category4[:5]]  # Limit to the first 5 elements

price4 = ul_tag4.find_all('span', class_="product-price")
pricloop4 = [span.text for span in price4[:5]]  # Limit to the first 5 elements

photo4 = ul_tag4.find_all('img', class_='photo')
img4 = [img['src'] for img in photo4[:5]]



def send_message_to_telegram_channel(bot_token, channel_username, message):
    channel_url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id=@Ethio_shopping_channel"
    channel_params = {
        "chat_id": "@" + channel_username,
        "text": message
    }
    response_channel = requests.post(channel_url, params=channel_params)
    if response_channel.status_code == 200:
        print("Message sent to channel successfully!")
    else: 
        print("Failed to send message to channel.")





logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('starting bot...')
# Send the concatenated data as one message to the Telegram bot

def command1(update, context):
 
 for product_name, product_price, img_link in zip(catli, pricloop, img):
    messages = []
    message = f"Product: {product_name}\nPrice: {product_price}\n{img_link}\n\n"
    messages.append(message)  # Add the message to the list    
    
    send_message_to_telegram_bot(bot_token, chat_id, message.strip())

def command2(update, context):
 
 for product_name2, product_price2, img_link2 in zip(catli2, pricloop2, img2):
    messages2 = []
    message2 = f"Product: {product_name2}\nPrice: {product_price2}\n{img_link2}\n\n"
    messages2.append(message2)  # Add the message to the list    
    
    send_message_to_telegram_bot(bot_token, chat_id, message2.strip())


def command3(update, context):
 
 for product_name3, product_price3, img_link3 in zip(catli3, pricloop3, img3):
    messages3 = []
    message3 = f"Product: {product_name3}\nPrice: {product_price3}\n{img_link3}\n\n"
    messages3.append(message3)  # Add the message to the list    
    
    send_message_to_telegram_bot(bot_token, chat_id, message3.strip())


def command4(update, context):
 
 for product_name4, product_price4, img_link4 in zip(catli4, pricloop4, img4):
    messages4 = []
    message4 = f"Product: {product_name4}\nPrice: {product_price4}\n{img_link4}\n\n"
    messages4.append(message4)  # Add the message to the list    
    
    send_message_to_telegram_bot(bot_token, chat_id, message4.strip())

def command5(update, context):
   for product_name, product_price, img_link in zip(catli, pricloop, img):
    messages = []
    message = f"Product: {product_name}\nPrice: {product_price}\n{img_link}\n\n"
    messages.append(message)
    send_message_to_telegram_channel(bot_token, channel_username, message.strip())
   for product_name3, product_price3, img_link3 in zip(catli3, pricloop3, img3):
    messages3 = []
    message3 = f"Product: {product_name3}\nPrice: {product_price3}\n{img_link3}\n\n"
    messages3.append(message3)  # Add the message to the list    
    send_message_to_telegram_channel(bot_token, channel_username, message3.strip())
   for product_name2, product_price2, img_link2 in zip(catli2, pricloop2, img2):
    messages2 = []
    message2 = f"Product: {product_name2}\nPrice: {product_price2}\n{img_link2}\n\n"
    messages2.append(message2)
    send_message_to_telegram_channel(bot_token, channel_username, message2.strip())


def mess_handl(update, context):
   text = str(update.message.text).lower()
   logging.info(f'user ({update.message.chat.id}) sayes: {text}')

   update.message.reply_text(text)


def error(update, context):
   logging.error(f'update {update} cused error {context.error}')



if __name__ == '__main__':
    updater = Updater(bot_token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('command1', command1))
    dp.add_handler(CommandHandler('command2', command2))
    dp.add_handler(CommandHandler('command3', command3))
    dp.add_handler(CommandHandler('command4', command4))
    dp.add_handler(CommandHandler('command5', command5))

    dp.add_handler(MessageHandler(Filters.text, mess_handl))
    dp.add_error_handler(error)

    updater.start_polling(1.0)
    updater.idel()



