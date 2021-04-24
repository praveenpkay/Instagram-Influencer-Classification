from instaloader import Instaloader, Profile


def get_data(target_profile):
    loader = Instaloader()
    loader.login("xxxxxxxx", "xxxxxxxxx")
    profile = Profile.from_username(loader.context, target_profile)
    num_followers = profile.followers
    total_num_likes = 0
    total_num_comments = 0
    total_num_posts = 0

    for post in profile.get_posts():
        total_num_likes += post.likes
        total_num_comments += post.comments
        total_num_posts += 1

    engagement = float(total_num_likes + total_num_comments) / (num_followers * total_num_posts)
    return {"handle": target_profile, "followers": num_followers,
            "post_count": total_num_posts, "avg_likes_per_post": total_num_likes/total_num_posts,
            "avg_comments_per_post": total_num_comments/total_num_posts,
            "Engagement": engagement}

