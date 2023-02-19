# url-shortener
<br><br>
## Working of the program.
### A python CLI project for Programming Club Induction participation 2023.
The CLI app works in a similar manner as any URL shortening services out there (like- https://bitly.com, https://cutt.ly, etc.). 
The working is simply a redirection request that is processed when the user enters a shortened link.
The shortened link and original link relations are stored in a json file located in the server.
When the user enters a link to be shortened, at first the json file is checked for any pre-existing relations, if not then the program creates one and updates the json file.
A new shortened link and long link relation is created using an algorithm which simply supplies a number as a key for the key-value pair.
The number (key) is added by one everytime a new url relation is added.
All keys are represented in 62 base number system to be able to store more information in less characters. It uses all the lower/upper alphabets and numbers.

