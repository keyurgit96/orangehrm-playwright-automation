from dotenv import load_dotenv
from datetime import datetime
import os


class selectEnv:
    def __init__(self, envName=None):
        self.envName = envName.lower() if envName else None

    def load(self):
        if self.envName == "custom":
            load_dotenv(os.path.join(os.path.dirname(__file__), "../../.custom.env"))
        else:
            load_dotenv(os.path.join(os.path.dirname(__file__), "../../.env"))


class logger:
    def __init__(self,page,screenshot=True,snapshot=True,source=True):
        self.page=page
        self.screenshot=screenshot
        self.snapshot=snapshot
        self.source=source

    def startLogging(self):
        self.page.context.tracing.start(screenshots=self.screenshot, snapshots=self.snapshot, sources=self.source)

    def stopLogging(self, fileName=None):
        if fileName:
            os.makedirs('./logs', exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            path='./logs/'+timestamp+'_'+fileName+'.zip'
            self.page.context.tracing.stop(path=path)
        else:
            raise AttributeError(
                "Please provide name while stopping logger.(logger().stopLogging(FILENAME))"
            )
