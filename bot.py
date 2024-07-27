from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from asyncio import sleep
from random import choice
import logging
from pyrogram.errors import FloodWait

logging.basicConfig(level=logging.INFO)

from motor.motor_asyncio import AsyncIOMotorClient


URI = "mongodb+srv://Chetancode:ankit090@cluster0.bjqkhqd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Establish a connection to the MongoDB server
client = AsyncIOMotorClient(URI)

# Select the database
db = client['usernames_db']

# Select the collection
collection = db['usernames']

admin_id = [6639559853,5871038439]

channel_dictionary = {
    '-1001997981310' : "https://t.me/ChetuP18",
    '-1002058092597' : "https://t.me/TirangaAsliChetan",
    '-1001990308626' : "https://t.me/AsliChetan_Prediction",
    '-1002029214229' : "https://t.me/BDGASLI_PREDICTION"
}

api_id = '22368708'  # Your api_id
api_hash = 'ec241c37a122cda302d68cb1415d2bff'  # Your api_hash
bot_token = '7398623122:AAHCC8bbGutcy4CuNrDhiCw1vvxoR6DrCLU'#'7032384318:AAFgxr2YFvDwp_WAiGQSkWodKfFJFs0Fk-0'  # Your bot's token

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

image_join = "https://telegra.ph/file/7d36a15ebfb442b3b43ab.jpg"

code_img = "https://telegra.ph/file/12475f925e0f1f3cfa8de.jpg"

image_success = "https://telegra.ph/file/ac64992d7bc2b068bece7.jpg"
recharging = {}
predicting = {}

game0 = "55 CLUB"
game1 = "TIRANGA GAMES"
game2 = "BDG"

game_codes = {
    game0:"####0",
    game1:"####1",
    game2:"####2"
}


game0_link = "https://55club08.in/#/register?invitationCode=42613173458"
game1_link = "https://tirangaclub.net/#/register?invitationCode=15152485405"
game2_link = "https://bdg2222.com/#/register?invitationCode=u8BOw1609901"


image_game = {"https://telegra.ph/file/31bccfcf79ce935f26acb.jpg":game0_link,
              "https://telegra.ph/file/8f140f16dbd65f3e1c560.jpg":game1_link,
              "https://telegra.ph/file/c661b7fded340c7705738.jpg":game2_link}

image_photos = list(image_game.keys())

uid_text = '''🌟 Hey User!

Create your new account with our special link to get free recharge.

Special Link: {}

After create the new account with above special link submit your game UID

📥 Enter Your Game UID '''

success_text = "✅ Your recharge of {} has been successful"

results = ['Big','Small']

prediction_link = {'55 𝘾𝙇𝙐𝘽' : "https://55club08.in/#/register?invitationCode=42613173458",
                   '𝙏𝙞𝙧𝙖𝙣𝙜𝙖 𝙂𝙖𝙢𝙚𝙨' : "https://tirangaclub.net/#/register?invitationCode=15152485405",
                   'ʙᴅɢ' : "https://bdg2222.com/#/register?invitationCode=u8BOw1609901"}

games = list(prediction_link.keys())

result_text = '''✅Prediction Result:
👨‍💻Period No: {}
⚡Result: {}

 Powered by 😈 : 𝘾𝙝𝙚𝙩𝙖𝙣 𝙋18'''

bot_username = "Matrix_ModBot"


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

    join_buttons = [
        join_buttons = [
        [InlineKeyboardButton("Join Channel", url=link)]
        for i, (channel_id, link) in enumerate(channel_dictionary.items())]
    
    # Add the verify button
    join_buttons.append([InlineKeyboardButton("Verify", callback_data="verify")])
    keyb = InlineKeyboardMarkup(join_buttons)

    await message.reply_photo(image_join,caption="You need to be a member of all the channels to use this bot.", reply_markup=keyb)

@app.on_message(filters.private & filters.command("gamelist") & filters.user(admin_id))
async def gamelist(client, message):
    await message.reply(f"list of games as follows : {list(game_codes.keys())}")

@app.on_message(filters.private & filters.command("code") & filters.user(admin_id))
async def code(client, message):

    if len(message.command) > 1:
        query = message.command[1:]
    else:
        await message.reply("provide arguments accordingly using this format : /code gamename$givencode")
        return
    query = ' '.join(query)

    query = query.split('$')
    print(query)
    if len(query) < 2:
        await message.reply("Invalid command Use this format : /code gamename$givencode")
        return
    
    game = query[0]
    code = query[1]

    print(f"{game} ----- {code}")

    if game in game_codes.keys():

        if game == game0:
            # game_codes[game0] = code
            game_codes.update({game0 : code})
            await message.reply(f"Code updated for {game0} with new code : {game_codes.get(game0)}")

        elif game == game1:
            # game_codes[game1] = code
            game_codes.update({game1 : code})
            await message.reply(f"Code updated for {game1} with new code : {game_codes.get(game1)}")

        elif game == game2:
            # game_codes[game2] = code
            game_codes.update({game2 : code})
            await message.reply(f"Code updated for {game2} with new code : {game_codes.get(game2)}")
            
    else:
        await message.reply("Game name is invalid or not in library")

async def ask_for_task(client,message):
    message = message.message
    keyboard1 = InlineKeyboardMarkup([
        [InlineKeyboardButton("Free Recharge", callback_data="free_recharge"),
        InlineKeyboardButton("ɢᴇᴛ ᴘʀᴇᴅɪᴄᴛɪᴏɴ", callback_data="prediction")],
        [InlineKeyboardButton("ɢɪꜰᴛ ᴄᴏᴅᴇ 🎁", callback_data="daily")]
    ])
    await message.reply_text('''Hey 👋,
    
    I am MΛƬЯIX MӨD BӨƬ 🤖
    
    If you register with my link I can give
    you free recharge and 80-90% accurate prediction.
    
    What Can I Do For You ? ''',reply_markup=keyboard1)

async def chk_if_member(client,callback_query,function_to_run,first:bool):
    user_id = callback_query.from_user.id
    user_name = callback_query.from_user.username
    not_joined_channels = []
    
    # Check if the user has joined all channels
    for channel_id in channel_dictionary.keys():
        print(channel_id)

        try:
            member = await app.get_chat_member(channel_id, user_id)
            # print(member)
            if member.status not in ["left", "kicked"]:
                print("channel member true")
            else:
                raise UserNotParticipant
        except UserNotParticipant:
            not_joined_channels.append(channel_id)
        
        except Exception as e:
            print(f"$#problem during channel {channel_id} : {e}")
    
    if not not_joined_channels:
        # User has joined all channels
        # await callback_query.message.edit_text("Welcome! You have joined all the channels.")
        if first:
            await callback_query.message.edit_text("Verification successful! You are now a member of the channel.")

        # await ask_for_task(client, callback_query.message)

        await function_to_run(client,callback_query)

    else:
        print(not_joined_channels)
        # User has not joined all channels
        try:
            await callback_query.message.edit_text(
                "You need to join all the channels to proceed.",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton(f"Join Channel {i+1}", url=channel_dictionary[channel_id])]
                    for i, channel_id in enumerate(not_joined_channels)
                ] + [[InlineKeyboardButton("Verify", callback_data="verify")]])
            )
        except:
            print("already edited")
        await callback_query.answer("You are not yet a member. Please join the channel and click verify again.", show_alert=True)

@app.on_callback_query(filters.regex('daily'))
async def daily(client, callback_query):
    # for i,game in enumerate(games):
    #     print(f"daily_{i}")
    kobe = [[InlineKeyboardButton(game,callback_data=f"code_{i}")] for i,game in enumerate(games)]

    kobe.append([InlineKeyboardButton("back",callback_data="back")])

    kob = InlineKeyboardMarkup(kobe)

    await callback_query.message.reply(f"Which games's code would you like to know",reply_markup=kob)

@app.on_callback_query(filters.regex(r"^code_"))
async def see_daily(client,callback_query):

    async def fuc(client,callback_query):
        game_index = int(callback_query.data.split('_')[1])
        game_codes_names = list(game_codes.keys())
        game_codes_vals = list(game_codes.values())

        game_name = game_codes_names[game_index]
        code_to_show = game_codes_vals[game_index]

        await callback_query.message.reply_photo(code_img,caption = f'''✅️ Your Code For {game_name} Is Generated Successfully ✅

🤩 Code: {code_to_show}



📝 ɴᴏᴛᴇ: ɪꜰ ᴛʜᴇ ᴄᴏᴅᴇ ᴅᴏᴇꜱɴ'ᴛ ᴡᴏʀᴋ ᴛʜᴇɴ ᴋɪɴᴅʟʏ ᴀꜰᴛᴇʀ ꜱᴏᴍᴇ ᴛɪᴍᴇ ɴᴇᴡ ᴄᴏᴅᴇ ᴡɪʟʟ ʙᴇ ᴜᴘᴅᴀᴛᴇᴅ ꜱᴏᴏɴ''')
    
    await chk_if_member(client,callback_query,fuc,first=False)

@app.on_callback_query(filters.regex("verify"))
async def verify(client, callback_query):
    await chk_if_member(client, callback_query,ask_for_task,first=True)
    

@app.on_callback_query(filters.regex("free_recharge"))
async def free_recharge(client,callback_query):
    
    async def fuc(client,callback_query):
        keyboard0 = InlineKeyboardMarkup([
                [InlineKeyboardButton(game0, callback_data=f"game_0"),
                InlineKeyboardButton(game1,callback_data=f"game_1")],

                [InlineKeyboardButton(game2, callback_data=f"game_2")]
            ])
        await callback_query.message.reply_text("In Which Game Do You Want Free Recharge ? .",reply_markup=keyboard0)

    await chk_if_member(client,callback_query,fuc,False)

@app.on_callback_query(filters.regex('prediction'))
async def prediction(client, callback_query):
    
    async def fuc(client,callback_query):
        keyboard3 = InlineKeyboardMarkup([
            [InlineKeyboardButton(games[0], callback_data="predict_0"),
            InlineKeyboardButton(games[1],callback_data="predict_1")],
            
            [InlineKeyboardButton(games[2], callback_data="predict_2")]
            
            [ InlineKeyboardButton("Back",callback_data="back")]
        ])
    
        await callback_query.message.reply_text("ᴡʜɪᴄʜ ɢᴀᴍᴇ ᴘʀᴇᴅɪᴄᴛɪᴏɴ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ?",reply_markup=keyboard3)

    await chk_if_member(client,callback_query,fuc,False)


@app.on_callback_query(filters.regex(r"^predict_"))
async def predict_for_game(client, callback_query):

    async def fuc(client,callback_query):
        
        game_name = games[int(callback_query.data.split('_')[1])]

        link = prediction_link[game_name]

        registered_or_not = InlineKeyboardMarkup([[InlineKeyboardButton("𝙔𝙀𝙎❤️‍🔥",callback_data="yes"),InlineKeyboardButton("𝙉𝙤🥺",callback_data="no")]])
        await callback_query.message.reply_text(f'''💡 This Prediction Bot will only work when you have Register with bellow links.

        {game_name}:
        {link}


        📑 If you follow with above links, there will be upto 99% chance of right prediction.''')
        await callback_query.message.reply_text(f"𝙃𝙖𝙫𝙚 𝙔𝙤𝙪 𝘾𝙤𝙢𝙥𝙡𝙚𝙩𝙚𝙙 𝙏𝙝𝙚 𝙍𝙚𝙜𝙞𝙨𝙩𝙧𝙖𝙩𝙞𝙤𝙣?",reply_markup=registered_or_not)

    await chk_if_member(client,callback_query,fuc,False)


@app.on_callback_query(filters.regex('no'))
async def no(client,callback_query):
    await callback_query.answer("Register kar bsdk😑",show_alert=True)

@app.on_callback_query(filters.regex('yes'))
async def yes(client,callback_query):

    async def fuc(client,callback_query):
        user_id = callback_query.message.chat.id
        await callback_query.message.reply_text(f"🎮 Enter Period last 3 digits. :")
        predicting[user_id] = True

    await chk_if_member(client,callback_query,fuc,False)


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
                [InlineKeyboardButton("𝙉𝙚𝙭𝙩 𝙋𝙧𝙚𝙙𝙞𝙘𝙩𝙞𝙤𝙣", callback_data="yes"),
                InlineKeyboardButton("𝘽𝘼𝘾𝙆",callback_data="prediction")]
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
    await ask_for_task(client, callback_query)


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
