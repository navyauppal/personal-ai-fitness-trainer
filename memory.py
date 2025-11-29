class InMemorySessionService:
    def __init__(self):
        self.session_data={}

    def start_session(self,profile:dict):
        self.session_data=profile

    def get_session_profile(self):
        return self.session_data    
        