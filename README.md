## IMPORTANT
Get the repository key in the class discussions (Courses/Discussions).
I suppose you could create a basic python script and then just push it up with the key. Once pushed, go back to the repository on GitHub (here) and then click "Create Pull Request" and submit that. Once I see the changes I'll merge it with the repository.


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
