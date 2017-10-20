import requests
import urllib

BASE_URL = 'https://api.instagram.com/v1/'
APP_ACCESS_TOKEN ="5701860028.67656b6.f52a12b27d4244768e570138a5b75604"


#get info self account
def self_info():
  request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
  print 'GET request url : %s' % (request_url)
  user_info = requests.get(request_url).json()

  if user_info['meta']['code'] == 200:
    if len(user_info['data']):
      print 'Username: %s' % (user_info['data']['username'])
      print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
      print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
      print 'No. of posts: %s' % (user_info['data']['counts']['media'])
    else:
      print 'User does not exist!'
  else:
    print 'Status code other than 200 received!'
#getting user id
def get_user_id(insta_username):
    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            return user_info['data'][0]['id']
        else:
            return None
    else:
        print 'Status code other than 200 received!'
        exit()
# getting info of other user
def get_user_info(insta_username):
  user_id = get_user_id(insta_username)
  if user_id == None:
    print 'User does not exist!'
    exit()
  request_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
  print 'GET request url : %s' % (request_url)
  user_info = requests.get(request_url).json()

  if user_info['meta']['code'] == 200:
    if len(user_info['data']):
      print 'Username: %s' % (user_info['data']['username'])
      print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
      print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
      print 'No. of posts: %s' % (user_info['data']['counts']['media'])
    else:
      print 'There is no data for this user!'
  else:
    print 'Status code other than 200 received!'
#getting media of own post
def get_own_post():
  request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (APP_ACCESS_TOKEN)
  print 'GET request url : %s' % (request_url)
  own_media = requests.get(request_url).json()

  if own_media['meta']['code'] == 200:
    if len(own_media['data']):
      image_name = own_media['data'][0]['id'] + '.jpeg'
      image_url = own_media['data'][0]['images']['standard_resolution']['url']
      urllib.urlretrieve(image_url, image_name)
      print 'Your image has been downloaded!'
      return own_media['data'][0]['id']
    else:
      print 'Post does not exist!'
  else:
    print 'Status code other than 200 received!'
# getting media of user post
def get_user_post(insta_username):
  user_id = get_user_id(insta_username)
  if user_id == None:
    print 'User does not exist!'
    exit()
  request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
  print 'GET request url : %s' % (request_url)
  user_media = requests.get(request_url).json()

  if user_media['meta']['code'] == 200:
    if len(user_media['data']):
      image_name = user_media['data'][0]['id'] + '.jpeg'
      image_url = user_media['data'][0]['images']['standard_resolution']['url']
      urllib.urlretrieve(image_url, image_name)
      print 'Your image has been downloaded!'
      return user_media['data'][0]['id']
    else:
      print 'Post does not exist!'
  else:
    print 'Status code other than 200 received!'
# like own post
def like_own_post():


  media_id = get_own_post()
  request_url = (BASE_URL + 'media/%s/likes') % (media_id)
  payload = {"access_token": APP_ACCESS_TOKEN}
  print 'POST request url : %s' % (request_url)
  post_a_like = requests.post(request_url, payload).json()
  if post_a_like['meta']['code'] == 200:
    print 'Like was successful!'
  else:
    print 'Your like was unsuccessful. Try again!'

# like user post
def like_a_post(insta_username):
  media_id = get_user_post(insta_username)
  request_url = (BASE_URL + 'media/%s/likes') % (media_id)
  payload = {"access_token": APP_ACCESS_TOKEN}
  print 'POST request url : %s' % (request_url)
  post_a_like = requests.post(request_url, payload).json()
  if post_a_like['meta']['code'] == 200:
      print 'Like was successful!'
  else:
      print 'Your like was unsuccessful. Try again!'
# comment on own post
def own_post_comment():
  media_id = get_own_post()
  comment_text = raw_input("Your comment: ")
  payload = {"access_token": APP_ACCESS_TOKEN, "text": comment_text}
  request_url = (BASE_URL + 'media/%s/comments') % (media_id)
  print 'POST request url : %s' % (request_url)

  make_comment = requests.post(request_url, payload).json()
  if make_comment['meta']['code'] == 200:
    print "Successfully added a new comment!"
  else:
    print "Unable to add comment. Try again!"

# comment on users post
def post_a_comment(insta_username):
  media_id = get_user_post(insta_username)
  comment_text = raw_input("Your comment: ")
  payload = {"access_token": APP_ACCESS_TOKEN, "text" : comment_text}
  request_url = (BASE_URL + 'media/%s/comments') % (media_id)
  print 'POST request url : %s' % (request_url)

  make_comment = requests.post(request_url, payload).json()
  if make_comment['meta']['code'] == 200:
      print "Successfully added a new comment!"
  else:
      print "Unable to add comment. Try again!"
def start_choice():
  print "what do you want to do"
  print "1.to get self info/n 2.to get user info/n 3.get own post/n 4.get user post/n 5.like own post/n 6.like user post/n 7.comment on own post/n 8. comment on users post/n"
  choice= raw_input("enter your choice")
  if choice==1:
    self_info()
  elif choice==2:
    print "choose user reccommended user/n 1.darkmagician_10/n 2.1s211998"
    user_choice=raw_input("enter your choice")
    if user_choice==1:
      get_user_info("darkmagician_10")
    elif user_choice==2:
      get_user_info("ls211998")
  elif choice==3:
    get_own_post()
  elif choice==4:
    print "choose user reccommended user/n 1.darkmagician_10/n 2.1s211998"
    user_choice = raw_input("enter your choice")
    if user_choice == 1:
      get_user_post("darkmagician_10")
    elif user_choice == 2:
      get_user_post("ls211998")
  elif choice==5:
    like_own_post()
  elif choice==6:
    print "choose user reccommended user/n 1.darkmagician_10/n 2.1s211998"
    user_choice = raw_input("enter your choice")
    if user_choice == 1:
      like_a_post("darkmagician_10")
    elif user_choice == 2:
      like_a_post("ls211998")
  elif choice==7:
    own_post_comment()
  elif choice ==8:
    print "choose user reccommended user/n 1.darkmagician_10/n 2.1s211998"
    user_choice = raw_input("enter your choice")
    if user_choice == 1:
      post_a_comment("darkmagician_10")
    elif user_choice == 2:
      post_a_comment("ls211998")


