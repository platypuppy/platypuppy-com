import os
import re

allChapters = []

inDir  = "_in/"
outDir = "Chapters/"

def makeChapter(filename):
    if (not(re.match(r'.*(_out.txt).*', filename))):
        inFilepath = inDir + filename
        m = re.match(r'^(.*)\..*$', filename)
        outFilepath = outDir + m.group(1) + ".html"
        print("Writing " + inFilepath + " to " + outFilepath)
        chapter = open(inFilepath, "r")
        HTMLChapter = open(outFilepath, "w")
        
        HTMLChapter.write(
"\
<html>\n\
  <head>\n\
    <title>platypuppy.com</title>\n\
    <link rel='stylesheet' href='../../style.css'>\n\
    <link rel='icon' href='../../icon.jpg'>\n\
  </head>\n\
  <body>\n\
    <div class='header'>\n\
      <a href='../../index.html'\n\
         class='silent'>\n\
        <h1>platypuppy.com</h1>\n\
      </a>\n\
    </div>\n\
    <div class='body'>\n\
      <div class='files'>\n\
        <div class='filesContent'>\n\
          <a href='Chapters.html'\n\
             class='silent'>\n\
            <p class='clean'>Chapters</p>\n\
          </a>\n\
          <div class=indent>\n\
"
        )

        for chap in allChapters:
            m1 = re.match(r'^(.*)\..*$', chap)
            m2 = re.match(r'^\D*(\d+).*$', chap)
            HTMLChapter.write(
"\
            <a href='" + m1.group(1) + ".html'\n\
               class='silent'>\n\
              <p class='clean'>Chapter #" + m2.group(1) + "</p>\n\
            </a>\n\
"
            )

        HTMLChapter.write(
"\
          </div>\n\
          <a href='../CharacterSheets/characterSheets.html'\n\
             class='silent'>\n\
            <p class=clean>Character Sheets</p>\n\
          </a>\n\
        </div>\n\
      </div>\n\
      <div class='content'>\n\
        <div class='text'>\n\
"
        )

        newLine = True
        extraDivs = 0
        for line in chapter.readlines():
            m1 = re.match(r'^# (.*)$', line)
            m2 = re.match(r'^\s*(.+)\s*$', line)
            m3 = re.match(r'^\\$', line)
            if (re.match(r'^.*---.*$', line)):
                if not(newLine):
                    HTMLChapter.write(
"\
            </p>\n\
"
                    )
                    newLine = True
                HTMLChapter.write(
"\
            <div class=indent>\n\
              <hr/>\n\
            </div>\n\
"
                )
            elif (m1):
                if not(newLine):
                    HTMLChapter.write(
"\
            </p>\n\
"
                    )
                    newLine = True
                HTMLChapter.write(
"\
          <h2>" + m1.group(1) + "</h2>\n\
          <hr/>\n\
          <p class=listHeader></p>\n\
          <div class=indent>\n\
"
                )
                extraDivs += 1
            elif (m3):
              HTMLChapter.write(
"\
            </p>\n\
"
              )
              HTMLChapter.write(
"\
            <p class=list>\n\
"
              )
            elif (m2):
                if newLine:
                    HTMLChapter.write(
"\
            <p class=list>\n\
"
                    )
                HTMLChapter.write(
"              " + m2.group(1) + "\n"
                )
                newLine = False
              
            else:
                if not(newLine):
                    HTMLChapter.write(
"\
            </p>\n\
"
                    )
                newLine = True

        if not(newLine):
            HTMLChapter.write(
"\
            </p>\n\
"
            )
            
        for i in range(extraDivs):
            HTMLChapter.write(
"\
          </div>\n\
"
            )
        HTMLChapter.write(
"\
        </div>\n\
      </div>\n\
    </div>\n\
  </body>\n\
</html>\n\
"
        )
        chapter.close()
        HTMLChapter.close()
    else:
        print("file was out.txt")

def makeChapters():
    chaptersIndex = open(outDir + "Chapters.html", "w")

    chaptersIndex.write(
    "\
<html>\n\
  <head>\n\
    <title>platypuppy.com</title>\n\
    <link rel='stylesheet' href='../../style.css'>\n\
    <link rel='icon' href='../../icon.jpg'>\n\
  </head>\n\
  <body>\n\
    <div class='header'>\n\
      <a href='../../index.html'\n\
         class='silent'>\n\
        <h1>platypuppy.com</h1>\n\
      </a>\n\
    </div>\n\
    <div class='body'>\n\
      <div class='files'>\n\
        <div class='filesContent'>\n\
          <a href='Chapters.html'\n\
             class='silent\n\
            <p class='clean'>Chapters</p>\n\
          </a>\n\
          <div class=indent>\n\
"
    )

    for chap in allChapters:
        m1 = re.match(r'^(.*)\..*$', chap)
        m2 = re.match(r'^\D*(\d+).*$', chap)
        chaptersIndex.write(
"\
            <a href='" + m1.group(1) + ".html'\n\
               class='silent'>\n\
              <p class='clean'>Chapter #" + m2.group(1) + "</p>\n\
            </a>\n\
"
        )
    chaptersIndex.write(
"\
          </div>\n\
          <a href='../CharacterSheets/characterSheets.html'\n\
             class='silent'>\n\
            <p class=clean>Character Sheets</p>\n\
          </a>\n\
        </div>\n\
      </div>\n\
      <div class='content'>\n\
        <div class='text'>\n\
          <h2>Adventures of Sakata Kiwa: Chapters</h2>\n\
          <hr/>\n\
          <p class=listHeader>Chapters:</p>\n\
          <div class=indent>\n\
"
    )

    for chap in allChapters:
        m1 = re.match(r'^(.*)\..*$', chap)
        m2 = re.match(r'^\D*(\d+).*$', chap)
        chaptersIndex.write(
"\
            <a href='" + m1.group(1) + ".html'\n\
               class='silent'>\n\
              <p>Chapter #" + m2.group(1) + "</p>\n\
            </a>\n\
"
        )
    
    chaptersIndex.write(
"\
          </div>\n\
        </div>\n\
      </div>\n\
    </div>\n\
  </body>\n\
</html>\n\
"
    )
    
    chaptersIndex.close()
        
os.system("tree " + inDir + " > " + inDir + "_out.txt")

chapters = open(inDir + "_out.txt", "r")

for line in chapters.readlines():

    m = re.match(r'^\W*(\w*.txt)$', line)
    if m:
      if (not(re.match(r'.*(_out.txt).*', m.group(1)))):
        allChapters.append(m.group(1))

chapters.close()

print("\nChapters found: ")
for chap in allChapters:
    print(" - " + chap)

print("\n")

makeChapters()

chapters = open(inDir + "_out.txt", "r")

for line in chapters.readlines():

    m = re.match(r'^\W*(\w*.txt)$', line)
    if m:
        makeChapter(m.group(1))
