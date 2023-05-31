from FacebookPostsScraper import FacebookPostsScraper as Fps
from pprint import pprint as pp

# Enter your Facebook email and password
email = 'YOUR_EMAIL'
password = 'YOUR_PASWORD'

# Instantiate an object
fps = Fps(email, password, post_url_text='Full Story')

# Example with single profile
single_profile = 'https://www.facebook.com/BillGates'
data = fps.get_posts_from_profile(single_profile)
pp(data)

fps.posts_to_csv('my_posts')  # You can export the posts as CSV document
# fps.posts_to_excel('my_posts')  # You can export the posts as Excel document
# fps.posts_to_json('my_posts')  # You can export the posts as JSON document