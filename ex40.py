# exercise 40: introducing OOP

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics
        self.lineCount = len(lyrics)

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

nirvana_lyrics = ["Come as you are",
                  "as you were",
                  "as I want you to be"]

come_as_you_are = Song(nirvana_lyrics)

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
come_as_you_are.sing_me_a_song()
print(come_as_you_are.lineCount)
