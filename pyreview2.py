ddef create_youtube_video(title,description):
  

  new_youtube_video={ "title": title,
    "description": description,
    "likes":0,
    "dislikes":0,
    "comments":{}
    }

  return new_youtube_video

def like(video):
  if "likes" in video:
    video["likes"] += 1
  return video 
def dislike(video):
  if "dislikes" in video:
    video["dislikes"] += 1
    return video

def add_comment(youtube_video, username, comment_text):
  youtube_video['comments'][username] = comment_text
  return youtube_video


new_video = create_youtube_video(input("Enter the title of the video "), input("Enter the description of the video"))
print("New YouTube Video:", new_video)
updated_video = like(new_video)
print("Updated YouTube Video:", updated_video)

video = like(video)
video = dislike(video)
video = add_comment(video, "user123", "Great tutorial!")

for _ in range(495):
    video = like(video)


print(video)