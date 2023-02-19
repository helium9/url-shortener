# url-shortener
A python CLI project for Programming Club Induction participation 2023.
## Installation
Run the executable `CLI(web).exe`. <br>NOTE: An active internet connection is required for the program to work.
<br><br>
## Working idea of the program
The CLI app works in a similar manner as any URL shortening services out there (like- https://bitly.com, https://cutt.ly, etc.). 
The working is simply a redirection request that is processed when the user enters a shortened link.
The shortened link and original link relations are stored in a json file located in the server.
When the user enters a link to be shortened, at first the json file is checked for any pre-existing relations, if not then the program creates one and updates the json file.
A new shortened link and long link relation is created using an algorithm which simply supplies a number as a key for the key-value pair.
The number (key) is added by one everytime a new url relation is added.
All keys are represented in 62 base number system to be able to store more information in less characters. It uses all the lower/upper alphabets and numbers.
<br>So, a valid shortened link may be `C/5` where `5` is the key. Sometimes, the provided link may not be that short and that is due to the limitaion of the domain name. The URL, `ak10.pythonanywhere.com/` is itself pretty big and that is due to the hosting website. A custom domain which is shorter would have resolved the issue.
<br>
## Files
The files provided are exactly as they were in the working directory.
<br>Python files, `CLI.py` and `server.py` were used earlier to host the system locally. Their final version (hosted on https://www.pythonanywhere.com/) are designated with a `(web)` suffix.
<br>The `Files/` directory contains `maps.json` which is used to store redirection relations. It is only representative.

