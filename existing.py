
class MP3player:
    def play(self, filename:str):
        if filename.endswith(".mp3"):
            print("Playing {0}".format(filename))
        else:
            raise Exception("{0} not supported".format(filename))

#assume that we already have a class for playing the MP3 files in this class MP3 player.
#This class provides an interface or function to play that given MP3 file. So in this class we have a method play, OK, and it accepts the filename
# and it checks whether the filename is ending with an MP3 if it is the case, then it simply plays.
#In our case. I have simply put the a print statement just to denote that this particular MP3 file is being
#played. This is a dummy implementation of this play method just for the simplicity sake.

#So this way we have this MP three player class providing one method to play the MP3 file that given an MP3 file.
#OK, now what we want in our application is. We want a class which is able to play a list of MP3 files, not a single MP three file, rather,
#given a list of MP three files, the class should be able to play all these files one by one. This is our required functionality.
# Now, in order to make use of this poetry class, what we do is we write an adapter.