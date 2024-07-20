class Parser:
    def __init__(self, fileDir):
        self.data = open(fileDir, "r").read()
        self.cookies = {}
        self.headers = {}
        
        self.username = None
        pass


    def create(self):
        data = self.data.split("\n")
        for i in data:
            a = i.split(": ")

            key = a[0]
            value = a[1]

            check = key.upper() in ["ACCEPT-LANGUAGE", "X-CSRF-TOKEN", "X-CSRFTOKEN", "X-IG-APP-ID", "USER-AGENT", "X-ASBD-ID", "ACCEPT", "SEC-FETCH-SITE", "SEC-FETCH-MODE", "SEC-FETCH-DEST", "COOKIE", "REFERER"]

            if check == True:
                if key.upper() == "COOKIE":
                    cookies = value.split("; ")
                    for ii in cookies:
                        a = ii.split("=")

                        key = a[0]
                        value = a[1]


                        self.cookies[key] = value 

                elif key.upper() == "ACCEPT":
                    self.headers[key] = "Application/json"
                
                elif key.upper() == "REFERER":
                    self.username = value.replace("https://www.instagram.com/", "").replace("/", "").strip()
                else:
                    self.headers[key] = value

