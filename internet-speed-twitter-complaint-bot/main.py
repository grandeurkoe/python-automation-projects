from twitter_bot import InternetSpeedTwitterBot

PROMISED_DOWM = 20
PROMISED_UP = 20

my_bot = InternetSpeedTwitterBot()
my_bot.get_internet_speed()

# Compare Current Internet Speed and Promised Internet Speed.
if float(my_bot.up) <= float(PROMISED_UP) or float(my_bot.down) <= float(PROMISED_DOWM):
    my_bot.tweet_at_provider(PROMISED_UP, PROMISED_DOWM)
