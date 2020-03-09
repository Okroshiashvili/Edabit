


def get_extension(lst):
    return [i.split(".")[1] for i in lst]




# Test case

print(get_extension(["code.html", "code.css"])) # ["html", "css"]

print(get_extension(["project1.jpg", "project1.pdf", "project1.mp3"])) # ["jpg", "pdf", "mp3"]

print(get_extension(["ruby.rb", "cplusplus.cpp", "python.py", "javascript.js"])) # ["rb", "cpp", "py", "js"]



