import pynder
facebook_auth_token = "______"
session = pynder.Session(facebook_auth_token)
friends = session.get_fb_friends()

for friend in friends:
    print(friend.name)
    print(friend.facebook_link)
