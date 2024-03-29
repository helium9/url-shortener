### Future
I plan to integrate the backend into a website which users can directly use to shorten URLs. Thus, the CLI will no longer be required. The website will be responsive and will generate a shareable QR code compatible with popular social media apps. The use of QR codes will make the usage more practical as users don't derive semantic information from QR codes but they do that from normal URLs. The shorter is the URL, the better will be the QR code due to low information density. Also, much later I can make a PWA out of it as well.<br>
# url-shortener
A python CLI project for Programming Club Induction participation 2023.
## Usage
Download and run the executable `CLI(web).exe`. <br>NOTE: An active internet connection is required for the program to work. 
An error `Connection Failed.` will be shown otherwise.
<br>The file is provided in the root directory.
<br><br>
## Working idea of the program
An app which shortens a given URL.
The CLI app works in a similar manner as any URL shortening services out there (like- https://bitly.com, https://cutt.ly, etc.). 
A redirection request is processed when the user enters a shortened link.
The shortened link and original link relations are stored in a json file located in the server. The backend server is created using Flask.
When the user enters a link to be shortened, at first the json file is checked for any pre-existing relations, if not then the program creates one and updates the json file.
A new shortened link and long link relation is created using an algorithm which simply supplies a number as a key for the key-value pair.
The number (key) is added by one everytime a new url relation is added.
All keys are represented in 62 base number system to be able to store more information in less characters. It uses all the lower/upper alphabets and numbers.
<br>So, a valid shortened link may be `ak10.pythonanywhere.com/5` where `5` is the key. Sometimes, the provided link may not be that short and that is due to the limitaion of the domain name. The URL, `ak10.pythonanywhere.com/` is itself pretty big and that is due to the hosting website. A custom domain which is shorter would have resolved the issue.
<br>
## Files
The files provided are exactly as they were in the development working directory.
<br>Python files, `CLI.py` and `server.py` were used earlier to host the system locally. 
<br> **NOTE:** Their final version (hosted on https://www.pythonanywhere.com/) are designated with a `(web)` suffix, i.e. the actual file used for making `CLI(web).exe` is `CLI(web).py` and the server file is `server(web).py`, but on the server this is still named `server.py`.
<br>Here, the `Files/` directory contains `maps.json` which is used to store redirection relations. It is only representative.
<br>
## Screenshots
<img src="https://user-images.githubusercontent.com/26248161/219958899-0be3a3b9-7fc3-4fda-bc53-2fbb5aca0ffa.png" width=70% height=70%>
<img src="https://user-images.githubusercontent.com/26248161/219958924-8bf4887c-b267-481f-8f91-9d8b5cecdafb.png" width=70% height=70%>

