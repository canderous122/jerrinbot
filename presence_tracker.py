import time

last_marvel_message_time = 0

def is_playing_marvel_rivals(member):
    #check if member is playing marvel rivals
    if member.activities:
        for activity in member.activities:
            if hasattr(activity, 'name') and 'marvel rivals' in activity.name.lower():
                return True
    return False

async def check_marvel_rivals(bot, before, after, channel_id):
    #check if someone started playing and send message if cooldown passed
    global last_marvel_message_time

    #check if they just started playing
    if is_playing_marvel_rivals(after) and not is_playing_marvel_rivals(before):
        #check if an hour has passed
        if time.time() - last_marvel_message_time > 3600:
            channel = bot.get_channel(channel_id)
            if channel:
                await channel.send(f"{after.mention} is gooning, time to pop off!")
                last_marvel_message_time = time.time()