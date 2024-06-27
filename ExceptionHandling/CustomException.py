class CitizenshipError(Exception):

    def __init__(self,citizenship, message="Be Indian. Buy Indian"):
        self.citizenship = citizenship
        self.message = message
        super().__init__(self.message)


a = input("Enter your citizenship")
if a != "India":
    raise CitizenshipError(a)


    raise CitizenshipError