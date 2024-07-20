class Profile:
    def __init__(self, data):
        self.json = data["data"]["user"]
        self.username = self.json["username"]
        self.full_name = self.json["full_name"]
        self.id = self.json["id"]
        self.bio = self.json["biography"]
        self.following = self.json["edge_follow"]["count"]
        self.followers = self.json["edge_followed_by"]["count"]
        self.is_verified = self.json["is_verified"]
        self.is_private = self.json["is_private"]
        self.picture = self.json["profile_pic_url_hd"]
        self.fbid = self.json["fbid"]


    def __repr__(self):
        return f'Profile(username="{self.username}", full_name="{self.full_name}", id={self.id}, fbid={self.fbid}, following={self.following}, followers={self.followers}, bio="{self.bio}", is_verified={self.is_verified}, is_private={self.is_private}, picture="{self.picture}", json)'
    

class Follower:
    def __init__(self, data):
        self.json = data
        pass

class StatusFollower:
    def __init__(self, data):
        self.json = data["friendship_status"]

        self.following = self.json["following"]
        self.followed_by = self.json["followed_by"]
        self.blocking = self.json["blocking"]
        self.is_private = self.json["is_private"]
        self.incoming_request = self.json["incoming_request"]
        self.outgoing_request = self.json["outgoing_request"]
        self.is_restricted = self.json["is_restricted"]


    def __repr__(self):
        return f'StatusFollwer(following={self.following}, followed_by={self.followed_by}, blocking={self.blocking}, is_private={self.is_private}, incoming_request={self.incoming_request}, outgoing_request={self.incoming_request}, is_restricted={self.is_restricted})'
        pass