class Task:
    #Dunder means private attribute
    #On Python every attribute is public, thats why use Dunder ("__")
    def __init__(self,title,description,expiration_date,priority,user):
        self.__title = title
        self.__description = description
        self.__expiration_date = expiration_date
        self.__priority = priority
        self.__user = user

    def info(self):
        print(self.title)
        print(self.description)
        print(self.expiration_date)
        print(self.priority)

    #Getters and Setters
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self,title):
        self.__title= title
    
    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self,description):
        self.__description = description

    @property
    def expiration_date(self):
        return self.__expiration_date
    @expiration_date.setter
    def expiration_date(self,expiration_date):
        self.__expiration_date = expiration_date

    @property
    def priority(self):
        return self.__priority
    @priority.setter
    def priority(self,priority):
        self.__priority = priority

    @property
    def user(self):
        return self.__user
    @user.setter
    def user(self,user):
        self.__user = user