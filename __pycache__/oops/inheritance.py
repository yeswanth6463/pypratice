class device:
    def __init__(self):
        print("u can access video")
        print("u can access audio")

class audio(device):
    def __init__(self):
        super().__init__()
        print("u access audio by using this device")
    def format(self):
        print("audio format is mp3")
    def frequency(self):
        print("audio all type bandwidth ")

class video(device):
    def __init__(self):
        super().__init__()
        print("u access video by using this device")
    def formatvideo(self):
        print("u can use mp4 format")
    def resolution(self):
        print("devices support upto 4k resolution")
        

class speaker(audio):
    def __init__(self):
        super().__init__()
        print("speaker supports this format")
    
    def volume(self):
        print("speaker volume is 100%")

class mic(speaker):
    def __init__(self):
        super().__init__()
        print("mic is used for recording")
    def mic(self):
        print("mic is connect to the speaker")
    
c1=mic()
c1.volume()
c1.mic()
c1.format()
c1.frequency()

c2=video()
c2.formatvideo()
c2.resolution()

c3=device()

