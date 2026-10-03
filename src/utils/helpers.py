from dotenv import load_dotenv
import os

class selectEnv:
    def __init__(self, envName=None):
        self.envName = envName.lower() if envName else None
    
    def load(self):
        if self.envName == "custom":
            load_dotenv(os.path.join(os.path.dirname(__file__), "../../.custom.env"))
        else:
            load_dotenv(os.path.join(os.path.dirname(__file__), "../../.env"))