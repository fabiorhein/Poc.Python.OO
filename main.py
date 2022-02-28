from user import User
from post import Post

app_user_one = User("fabiorhein@gmail.com", "Fabio", "123", "Software Engineer")
app_user_one.get_user_info()
app_user_one.change_job_title("DevOps Engineer")
app_user_one.get_user_info()

app_user_two = User("nathielle@gmail.com", "Nathielle", "456", "Administrator Manager")
app_user_two.get_user_info()

app_post = Post("on a secret mission today", app_user_two.name)
app_post.get_post_info()

