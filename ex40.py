class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics
	
    def sing(self):
        for line in self.lyrics:
            print line

happy = Song(["Happy Bday to you", 
"Happy bday dear xyz", "happy bday to you"])	

bulls = Song(["Hello world", "How you guys doing"])

happy.sing()
bulls.sing()		