#from existing import MP3player
#class NewMP3Player:
# def __init__(self, mplayer:MP3player):
#     self.player = mplayer
#      self.file_list = []

#  def add_file(self, file:str):
#      if file.endswith(".mp3"):
#          self.file_list.append(file)
  #      else:
#         raise Exception("file not supported")

#  def play(self):
#      for f in self.file_list:
#        self.player.play(f)
#




from existing import MP3player
class NewMP3Player2(MP3player):
    def __init__(self):
       super().__init__()
         self.file_list = []

     def add_file(self, file:str):
         if file.endswith(".mp3"):
             self.file_list.append(file)
         else:
             raise Exception("file not supported")

     def play(self):
         for f in self.file_list:
             super().play(f)

