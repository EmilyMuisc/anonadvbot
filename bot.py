from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from asyncio import sleep
from random import choice
import logging
from pyrogram.errors import FloodWait

logging.basicConfig(level=logging.INFO)

from motor.motor_asyncio import AsyncIOMotorClient


URI = "mongodb+srv://pandatdb:ankit090@pamdatdb.akvof4j.mongodb.net/?retryWrites=true&w=majority&appName=pamdatdb"
# Establish a connection to the MongoDB server
client = AsyncIOMotorClient(URI)

# Select the database
db = client['usernames_db']

# Select the collection
collection = db['usernames']

admin_id = ['5871038439']

channel_id = 'shrexgawd'  # Replace with your channel's id
channel_link = f'https://t.me/{channel_id}'
api_id = '22368708'  # Your api_id
api_hash = 'ec241c37a122cda302d68cb1415d2bff'  # Your api_hash
bot_token = '7107349240:AAF3Yce6Q6Jd7Ytu4IxTTfz1_n3iGZ4hXUs'#'7032384318:AAFgxr2YFvDwp_WAiGQSkWodKfFJFs0Fk-0'  # Your bot's token

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

image_join = "https://telegra.ph/file/65debb2541f63213510b5.jpg"

image_success = "https://telegra.ph/file/ac64992d7bc2b068bece7.jpg"
recharging = {}
predicting = {}

game0 = "Tirangagames"
game1 = "Big Mumbai"
game0_link = "https://tirangalottery.in/#/register?invitationCode=15152485405"
game1_link = "https://big-mumbai.club/#/register?invitationCode=18222435694"
image_game = {"https://telegra.ph/file/209005ce9f1d0c0f73188.jpg":game0_link,
              "https://telegra.ph/file/fcf0481ad4de9ee356dcb.png":game1_link}

image_photos = list(image_game.keys())

uid_text = '''🌟 Hey User!

Create your new account with our special link to get free recharge.

Special Link: {}

After create the new account with above special link submit your game UID

📥 Enter Your Game UID '''
success_text = "✅ Your recharge of {} has been successful"

results = ['Big','Small']

prediction_link = {'game1' : "link1", 
                   'game2' : "link2"}

games = list(prediction_link.keys())

result_text = '''test period:{} result:{}'''

bot_username = "dalal_90_bot"

def get_random_result():

    return choice(results)

@app.on_message(filters.private & filters.command("start"))
async def start(client, message):
    user_id = message.from_user.id
    username = message.from_user.username or "unknown"

    if await collection.count_documents({'user_id': user_id}) == 0 and username != bot_username:
        await collection.insert_one({'user_id': user_id, 'username': username})
        print(f"Hello {username}, your ID has been added to the database!")
    else:
        print(f"Hello {username}, you are already registered.")

    print("started_sending")
    keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("Join Channel", url=channel_link)],
            [InlineKeyboardButton("Verify Membership", callback_data="verify")]
        ])
    await message.reply_photo(image_join,caption="You need to be a member of the channel to use this bot.", reply_markup=keyboard)

    # member = await client.get_chat_member(channel_id, message.from_user.id)
    # if member.status not in ["left", "kicked"]:

        

    # else:
    #     await message.reply_text("You are not a member yet, pls join meow")
    #     await start(client, message)

async def ask_for_task(client,message):
    keyboard1 = InlineKeyboardMarkup([
        [InlineKeyboardButton("Free Recharge", callback_data="free_recharge"),
        InlineKeyboardButton("Prediction", callback_data="prediction")]
    ])
    await message.reply_text("Select Task",reply_markup=keyboard1)

@app.on_callback_query(filters.regex("verify"))
async def verify(client, callback_query):
    try:
        member = await client.get_chat_member(channel_id, callback_query.from_user.id)
        if member.status not in ["left", "kicked"]:
            await callback_query.message.edit_text("Verification successful! You are now a member of the channel.")
            # await start(client, callback_query.message)
            await ask_for_task(client, callback_query.message)
            
        else:
            raise UserNotParticipant
    except UserNotParticipant:
        await callback_query.answer("You are not yet a member. Please join the channel and click verify again.", show_alert=True)

@app.on_callback_query(filters.regex("free_recharge"))
async def free_recharge(client,callback_query):
    try:
        member = await client.get_chat_member(channel_id, callback_query.from_user.id)
        if member.status not in ["left", "kicked"]:
            keyboard0 = InlineKeyboardMarkup([
                [InlineKeyboardButton(game0, callback_data=f"game_0"),
                InlineKeyboardButton(game1,callback_data=f"game_1")]
            ])
        
            await callback_query.message.reply_text("what game would you like to recharge?.",reply_markup=keyboard0)
        else:
            raise UserNotParticipant
    except UserNotParticipant:
        await callback_query.answer("You are not yet a member. Please join the channel and click verify again.", show_alert=True)

@app.on_callback_query(filters.regex('prediction'))
async def prediction(client, callback_query):
    try:
        global predicting
        user_id = callback_query.message.chat.id
        predicting[user_id] = False
        member = await client.get_chat_member(channel_id, callback_query.from_user.id)
        if member.status not in ["left", "kicked"]:
            keyboard3 = InlineKeyboardMarkup([
                [InlineKeyboardButton(games[0], callback_data="predict_0"),
                InlineKeyboardButton(games[1],callback_data="predict_1"),
                InlineKeyboardButton("back",callback_data="back")]
            ])
        
            await callback_query.message.reply_text("what game would you like to play for prediction",reply_markup=keyboard3)
        else:
            raise UserNotParticipant
    except UserNotParticipant:
        await callback_query.answer("You are not yet a member. Please join the channel and click verify again.", show_alert=True)


@app.on_callback_query(filters.regex(r"^predict_"))
async def predict_for_game(client, callback_query):
    try:
        # user_id = callback_query.message.chat.id
        
        game_name = games[int(callback_query.data.split('_')[1])]
        link = prediction_link[game_name]
        member = await client.get_chat_member(channel_id, callback_query.from_user.id)
        if member.status not in ["left", "kicked"]:
            
            # await callback_query.message.reply_text(f"enter period number for {game_name}")
            # predicting[user_id] = True
            registered_or_not = InlineKeyboardMarkup([[InlineKeyboardButton("yes",callback_data="yes"),InlineKeyboardButton("no",callback_data="no")]])
            await callback_query.message.reply_text(f"to play {game_name} you have to register at {link}")
            await callback_query.message.reply_text(f"have you registered?",reply_markup=registered_or_not)
        else:
            raise UserNotParticipant
    except UserNotParticipant:
        await callback_query.answer("You are not yet a member. Please join the channel and click verify again.", show_alert=True)

@app.on_callback_query(filters.regex('no'))
async def no(client,callback_query):
    await callback_query.answer("register kar bsdk",show_alert=True)

@app.on_callback_query(filters.regex('yes'))
async def yes(client,callback_query):
    try:

        user_id = callback_query.message.chat.id
        member = await client.get_chat_member(channel_id, callback_query.from_user.id)
        if member.status not in ["left", "kicked"]:
            
            await callback_query.message.reply_text(f"enter period number :")
            predicting[user_id] = True
           
        else:
            raise UserNotParticipant
    except UserNotParticipant:
        await callback_query.answer("You are not yet a member. Please join the channel and click verify again.", show_alert=True)

@app.on_callback_query(filters.regex(r"^game_"))
async def verify(client, callback_query):
    global recharging
    try:
        user_id = callback_query.message.chat.id
        recharging[user_id] = True
        image_id = image_photos[int(callback_query.data.split("_")[1])]
        link = image_game[image_id]

        await callback_query.message.reply_photo(image_id,caption=uid_text.format(link))
        print(recharging)
    except UserNotParticipant:
        await callback_query.answer("You are not yet a member. Please join the channel and click verify again.", show_alert=True)

@app.on_message(filters.private & filters.regex(r'^\d+$'))
async def number_handler(client, message):
    # print(recharging)
    # print(recharging[message.chat.id])
    try:
        if recharging[message.chat.id]:
            number = message.text
            keyboard_options = InlineKeyboardMarkup([
                [InlineKeyboardButton("100", callback_data="recharged_100"),
                InlineKeyboardButton("200", callback_data="recharged_200"),
                InlineKeyboardButton("500", callback_data="recharged_500")],

                [InlineKeyboardButton("1000", callback_data="recharged_1000"),
                InlineKeyboardButton("5000", callback_data="recharged_5000"),
                InlineKeyboardButton("10000", callback_data="recharged_10000")]
                
            ])
            await message.reply_text(f"💰Select amount for recharge for Game UID: {number}",reply_markup=keyboard_options)

        else:
            print(recharging)
    except Exception as e:
        print(e)

    try:
        if predicting[message.chat.id]:
        
            number = message.text
            keyboard= InlineKeyboardMarkup([
                [InlineKeyboardButton("Next_prediction", callback_data="yes"),
                InlineKeyboardButton("Back",callback_data="prediction")]
            ])
            keyboard1 = InlineKeyboardMarkup([
                [InlineKeyboardButton("Back",callback_data="prediction")]
            ])
            result = get_random_result()
            if len(number) == 3:
                await message.reply_text(result_text.format(number,result),reply_markup=keyboard)
            else :
                await message.reply_text("unrecognised value",reply_markup=keyboard1)

        else:
            print(predicting)

    except Exception as e:
        print(e)

@app.on_callback_query(filters.regex('back'))
async def back(client,callback_query):
    global predicting
    user_id = callback_query.message.chat.id
    predicting[user_id] = False
    recharging[user_id] = False
    # await verify(client,callback_query)
    await ask_for_task(client, callback_query.message)

# @app.on_callback_query(filters.regex('next'))
# async def back(client,callback_query):
#     global predicting
#     user_id = callback_query.message.chat.id
#     predicting[user_id] = True
#     await predict_for_game(client,callback_query,)

@app.on_callback_query(filters.regex(r"^recharged_"))
async def rechared(client, callback_query):
    global recharging
    try:
        user_id = callback_query.message.chat.id
        recharging[user_id] = False
        amount = callback_query.data.split("_")[1]
        msg = await callback_query.message.reply_text(f"Recharging")
        i = 1
        while i<=5:
            await msg.edit_text(f"Recharging{'.'*i}")
            await sleep(0.8)
            i += 1
        await msg.delete()
        keylu = InlineKeyboardMarkup([[InlineKeyboardButton("back",callback_data='back')]])
        await callback_query.message.reply_photo(image_success,caption=success_text.format(amount),reply_markup=keylu)
    except UserNotParticipant:
        await callback_query.answer("You are not yet a member. Please join the channel and click verify again.", show_alert=True)


@app.on_message(filters.command("bcast") & filters.user(admin_id))
async def broadcast(client, message):
    text = message.text.split(None, 1)[1]
    users = await collection.find({}, {'_id': 0, 'user_id': 1}).to_list(None)
    for user in users:
        try:
            await client.send_message(user['user_id'], text)
        except FloodWait as e:
            print(f"Rate limit exceeded. Sleeping for {e.x} seconds.")
            await sleep(e.x)
            await client.send_message(user['user_id'], text)
        except Exception as e:
            print(e)

@app.on_message(filters.command("fcast") & filters.user(admin_id) & filters.reply)
async def forward_broadcast(client, message):
    if not message.reply_to_message:
        await message.reply_text("Please reply to a message you want to forward.")
        return
    users = await collection.find({}, {'_id': 0, 'user_id': 1}).to_list(None)
    for user in users:
        try:
            await client.forward_messages(chat_id=user['user_id'], from_chat_id=message.chat.id, message_ids=message.reply_to_message.message_id)
        except FloodWait as e:
            print(f"Rate limit exceeded. Sleeping for {e.x} seconds.")
            await sleep(e.x)
            await client.forward_messages(chat_id=user['user_id'], from_chat_id=message.chat.id, message_ids=message.reply_to_message.message_id)
        except Exception as e:
            print(e)



app.run()
