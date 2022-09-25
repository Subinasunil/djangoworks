import json
with open("blogs.json",encoding="utf-8") as f:
    data=json.load(f)
    print(data)
print(len(data))

#number of post by userid=1
user_post=[post for post in data if post['userId']==1]
print(len(user_post))

#total number of likes for postId 6
total_num_of_likes=[len(post["liked_by"]) for post in data if post["postId"]==6]
print(total_num_of_likes)

#number of post liked by user=2

num_of_post=len([post for post in data if 2 in post["liked_by"]])
print(num_of_post)




