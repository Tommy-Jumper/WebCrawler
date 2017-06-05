import os, re

class Song:
    """Constructor of class Song, it is used to show describe song
    Args:
        title (string): title/name of the song
		artist (sring): artist of the song
		file_url (string): url to show the mp3 files of the song
		lyric_url (string): url to show lyric files of the song 
    """
    def __init__(self, title=None, artist=None, file_url=None, lyric_url=None):
		self.title = title
		self.artist = artist
		self.file_url = file_url
		self.lyric_url = lyric_url

    def __str__(self):
        if(self.title is not None and self.artist is not None and self.file_url is not None and
           self.lyric_url is not None):
    		return self.title + " | "+ self.artist + " | "+self.file_url + " | "+self.lyric_url
        else:
            return self.title

class Node:
    """Constructor of class Node to represent binary tree
    Args:
        left_node (Node): left childreen of current node
		right_node (Node): right childreen of current node
		value (string): value/key index of the tree, would be name of song/name of artist/ lyrics word
		item (List of Song): contains list of song related to the value content in the Node
    """
    def __init__(self, value, item=None):
		self.left_node = None
		self.right_node = None
		self.value = value
		self.item = item

class Tree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def add(self, value, item=None):
        if(self.root == None):
            self.root = Node(value, item)
        else:
            self._add(value, self.root, item)

    def _add(self, value, node, item):
        if(value < node.value):
            if(node.left_node != None):
                self._add(value, node.left_node,item)
            else:
                node.left_node = Node(value,item)
        else:
            if(node.right_node != None):
                self._add(value, node.right_node,item)
            else:
                node.right_node = Node(value, item)

    def find(self, value):
        if(self.root != None):
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, node):
        if(value == node.value):
            return node
        elif(value < node.value and node.left_node != None):
            self._find(value, node.left_node)
        elif(value > node.value and node.right_node != None):
            self._find(value, node.right_node)

    def deleteTree(self):
        self.root = None

    def printTree(self):
        if(self.root != None):
            self._printTree(self.root)

    def _printTree(self, node):
        if(node != None):
            self._printTree(node.left_node)
            print "VALUE: "+str(node.value)
            for index, itm in enumerate(node.item):
			    print('item: '+str(itm))
            self._printTree(node.right_node)


class Index:
    def __init__(self):
        self.index = None

    def parse_songs_artists_tree(self):
        ''' returns the title, artist and lyrics'''
        path = '../1000a-iartist/750 a-i artist'
        artists, songs, lyrics = [], [], []
        artists_tree = Tree()
        songs_tree = Tree()
        songs = []
        artist_songs=[]
        current_artist=None
        for root, dirs, files in os.walk(path):
            # get Artist
            for file in files:
                # get Songs Title
                if file.endswith('.mp3'):
                    song= Song()
                    artist_name = re.sub(r'(.*?)\\', '', root.__str__()).replace("_TopSongs", "")
                    song.artist=artist_name
                    if (current_artist is None):
                        current_artist=artist_name
                    artists.append(artist_name)
                    print file
                    song.file_url=str(file)
                    song_title=re.search('_(.+?).mp3', file.__str__()).group(1)
                    song.title=song_title
                    # get Songs Lyric
                    file_path = os.path.join(root, file).replace(".mp3", ".lrc")
                    try:
                        lyric = ""
                        f = open(file_path, "r")
                        for line in f:
                            lyric = (lyric + re.sub(r'\[(.*?)\]', '', line))
                        lyrics.append(lyric)
                        f.close()
                        song.lyric_url=file_path
                    except IOError:
                        print file_path, "error"
                        print ("I/O error({0}): {1}".format(IOError.errno, IOError.strerror)), IOError
                        lyrics.append("")
                        song.lyric_url =""
                    except:
                        print file_path, "error"
                        lyrics.append("")
                        song.lyric_url =""
                        raise
                    songs.append(song)
                    songs_tree.add(song.title,songs)
                    songs=[]
                    if(current_artist!=artist_name):
                        artists_tree.add(current_artist,artist_songs)
                        artist_songs=[]
                        artist_songs.append(song)
                    else:
                        artist_songs.append(song)
                        print song.title

                    current_artist=artist_name
                    # print artists, songs, lyrics
        return artists_tree, songs_tree

    def parse_collection(self):
        ''' returns the title, artist and lyrics'''
        path = '../1000a-iartist/750 a-i artist'
        artists, songs, lyrics = [], [], []

        artists_tree = Tree()
        songs_tree = Tree()

        for root, dirs, files in os.walk(path):
            # get Artist
            for file in files:
                # get Songs Title
                if file.endswith('.mp3'):
                    artists.append(re.sub(r'(.*?)\\', '', root.__str__()).replace("_TopSongs", ""))
                    print file
                    songs.append(re.search('_(.+?).mp3', file.__str__()).group(1))
                    # get Songs Lyric
                    file_path = os.path.join(root, file).replace(".mp3", ".lrc")
                    try:
                        lyric = ""
                        f = open(file_path, "r")
                        for line in f:
                            lyric = (lyric + re.sub(r'\[(.*?)\]', '', line))
                        lyrics.append(lyric)
                        f.close()
                    except IOError:
                        print file_path, "error"
                        print ("I/O error({0}): {1}".format(IOError.errno, IOError.strerror)), IOError
                        lyrics.append("")
                    except:
                        print file_path, "error"
                        lyrics.append("")
                        raise
                        # print artists, songs, lyrics
        return artists, songs, lyrics


def main():
    path= '../1000a-iartist/750 a-i artist'
    #Read Arib's file
    #artists, songs, lyrics = Index.parse_collection()
    artists_tree,songs_tree = Index().parse_songs_artists_tree()
    artists_tree.printTree()
    songs_tree.printTree()
#    for index, song in enumerate(artists):
#        print song
		
main()