from .utils.parser import *
from .utils.Instagram import *
from .objects.objects import *
class InstagramPy:
    def __init__(self, data: str = None):
        if data != None:
            parser = Parser(data)
            data = parser.create()

        self.cookies = parser.cookies
        self.headers = parser.headers
        self.username = parser.username

        self.instagram = Instagram(self.cookies, headers=self.headers)
        pass


    def profile(self, username: str = None):
        if username != None:
            return Profile(self.instagram.get(f"/v1/users/web_profile_info/?username={username}"))
        else:
            return Profile(self.instagram.get(f"/v1/users/web_profile_info/?username={self.username}"))
        
    def get_followers(self, userId: int, count: int = 12):
        return self.instagram.get(f"/v1/friendships/{userId}/followers/?count={count}&search_surface=follow_list_page")
    
    def show_many(self, listIds: list):
        ids = ""
        for id in listIds:
            ids = ids + f"{id},"
        ids = ids[:-1]

        return self.instagram.post("/v1/friendships/show_many/", body={"user_ids": ids})
    

    def get_followersV2(self, userId, count: int = 12):
        followers = self.get_followers(userId, count)
        ids = []
        for user in followers["users"]:
            ids.append(user["id"])
            

        
        show_many = self.show_many(ids)
        
        users = []
        for user in followers:

            o = {
                "username": user["username"],
                "id": user["id"],
                "is_private": user["is_private"],
                "status": show_many[user["id"]]
            }
        
            users.append(o)

        return users
    

    def follower(self, userId: int):
        return StatusFollower(self.instagram.post(f"/v1/friendships/create/{userId}/", body={"container_module": "profile", "nav_chain": "PolarisFeedRoot:feedPage:4:topnav-link,PolarisStoriesV3Root:StoriesPage:10:unexpected,PolarisFeedRoot:feedPage:11:unexpected,PolarisProfilePostsTabRoot:profilePage:12:unexpected,PolarisProfilePostsTabRoot:profilePage:13:unexpected", "user_id": userId}))
        pass

    def unfollower(self, userId: int):
        return StatusFollower(self.instagram.post(f"/v1/friendships/destroy/{userId}/", body={"container_module": "profile", "nav_chain": "PolarisFeedRoot:feedPage:4:topnav-link,PolarisStoriesV3Root:StoriesPage:10:unexpected,PolarisFeedRoot:feedPage:11:unexpected,PolarisProfilePostsTabRoot:profilePage:12:unexpected,PolarisProfilePostsTabRoot:profilePage:13:unexpected", "user_id": userId}))
        pass
