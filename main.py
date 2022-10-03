#from existing import MP3player
#from adapter import NewMP3Player

#if __name__ == "__main__":
 #   oPlayer = MP3player()
  #  player = NewMP3Player(oPlayer)
   # player.add_file("a.mp3")
    #player.add_file("b.mp3")
    #player.add_file("c.mp3")
    #player.play()


from adapter import NewMP3Player2
if __name__ == "__main__":
     # oPlayer = MP3player()
     player = NewMP3Player2()
     player.add_file("a.mp3")
     player.add_file("b.mp3")
     player.add_file("c.mp3")
     player.play()




