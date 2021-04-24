import pandas as pd
from csv import DictWriter
from check_engagement_rate import get_data
field_names = ["handle", "followers", "post_count",
               "avg_likes_per_post", "avg_comments_per_post",
               "Engagement"]

df = pd.read_csv("instagram.csv")
handles = list(df['handle'])
for i in handles:
    print("Getting details of: " + i)
    with open("insta_data.csv", "a", newline="") as f:
        dictwriter_object = DictWriter(f, fieldnames=field_names)
        dictwriter_object.writerow(get_data(i))
