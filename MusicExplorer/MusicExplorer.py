import os

# Globals
src = "F:\\Music"
html = input("Welcome to the Music Explorer, html (y/n)? ")
outfilepath = "C:\\Users\\jediKnight\\Desktop\\musiclibrary.htm"
results = ""


# Gets all the files and folders in the source directory
# ==============================================
def writefolders(artist):
    global results

    # Skip a couple
    if artist == "Amazon Music":
        return
    if artist == "Playlists":
        return
    if artist == "GuitarTracks":
        return

    # Path to this "artist"
    loc = os.path.join(src, artist)

    # Only Folders
    if os.path.isfile(loc):
        return
    
    # Start this artist
    if html == "y":
        results += "&#149;&nbsp;<a href=\"javascript:void(0);\" onclick=\"toggledisplay('" + artist + "');\">" + artist + "</a></br>\n" 
        results += "<div id=\"" + artist + "\" style=\"display:none;\">\n"
    else:
        results += artist + "\n"
       
    
    things = os.listdir(loc)
    for thing in things:
        # no files
        if os.path.isdir(os.path.join(loc, thing)):
            if html == "y":
                results += "--- <a target=\"_blank\" href=\"https://www.google.com/search?q=" + artist + "+" + thing + "\">" + thing + "</a><br/>\n"
            else:
                results += "--- " + thing + "\n"

    if html == "y":
        results += "</div>\r"
         
# ==============================================
# Program
# ==============================================
artists = os.listdir(src)
for artist in artists:
    writefolders(artist.strip())

outfile = open(outfilepath, "w")
print(results, file = outfile)

