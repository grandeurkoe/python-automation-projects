from instafollower import InstaFollower

SIMILAR_ACCOUNTS = 'chefsteps'

my_insta = InstaFollower()
my_insta.login(SIMILAR_ACCOUNTS)
follower_list = my_insta.find_followers()
my_insta.follow(follower_list)
