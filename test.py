from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.functions.channels import GetChannelsRequest
from telethon.tl.types import ChannelParticipantsRecent
from telethon.tl.functions.users import GetUsersRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.utils import get_input_peer
from telethon.tl.types.channels import ChannelParticipants
from telethon.tl.functions.messages import SendMessageRequest
import sys
import urllib 
import time
api_id = ******  # 
api_hash = '*******'
phone_number = '****8'

client = TelegramClient('%sweessionname%', api_id, api_hash)  
client.connect() # logining and connecting to Telegram servers

if not client.is_user_authorized():  # authorization (if there is no .session file created before)
    client.send_code_request(phone_number)
    client.sign_in(phone_number, input('Enter the code: '))

result = client(ResolveUsernameRequest('___NODEVIEWCOPY___33___NODEVIEWCOPY___'))
found_chats = result.chats
found_users = result.users

r = client(GetParticipantsRequest(result.chats[0],
filter=ChannelParticipantsRecent(),
                           # List of filters https://lonamiwebs.github.io/Telethon/types/channel_participants_filter.html
                           offset=___NODEVIEWCOPY___34___NODEVIEWCOPY___,  # getting info from 0th user
                           limit=5000)  # limiting number of users in a request
						   )

fusers=r.users