from user import User
from post import Post

app_user_info = User("rmc@rmc.com", "Rodrigo", "123456",  "DevOps")
app_user_info.get_username()
app_user_info.change_job_title("Cloud Engineer")
app_user_info.get_username()

new_post = Post("on a secret mission today", app_user_info.name)
new_post.get_post_info()
