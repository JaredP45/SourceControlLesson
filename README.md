# SourceControlLesson
Example source control lesson for class on Jan 25.

Order of Steps:

$ git clone https://github.com/JaredP45/SourceControlLesson

-- Add python file, make it print "Hello world"

$ git status

$ git add . 

$ git status

$ git commit -m "Added python file"

-- Get repository key 

$ git push origin main

$ git status

-- Go to python file on GitHub, change "Hello world" to "Hello nether" (simulates another user pushing up changes to same file)

$ git pull origin master

$ git status
