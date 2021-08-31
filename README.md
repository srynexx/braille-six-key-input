# braille-six-key-input
A repository for Braille six key input or Perkins braille concept using QWERTY keyboard in Python

Braille six key input or Perkins Braille uses 6 set of keys, one for each dot in a braille cell.
To type in braille, use SDFJKL keys only from keyboard (best if keyboard has N-key rollover feature).
Different combinations of SDFJKL keys gives different braille code.
Each key combinations must be pressed and released together at once.

F = dot-1, D = dot-2, S = dot-3, J = dot-4, K = dot-5, L = dot-6.

![Corresponding key for its dot](https://user-images.githubusercontent.com/89833078/131568421-d1a54187-5b05-4d83-931d-2cb33469c1e1.png)

Hit *Return* key on keyboard to display typed braille code with its corresponding translation, or click the green button.
Based on grade 1 braille.
For extra, *backspace* key is included to delete each braille code like deleting normal letter.
For extra, *spacebar* key is included to add gap between each word like normal text does.
Make sure GUI window is in focus for key binding to work (best if the small textbox is tapped 1st b4 start typing)

The braille typing algorithm is achieved using key bindings provided in Python Tkinter GUI library.
It is by no means all perfect but as far as i concern, it is working and gets the job done :sweat_smile:.
Feel free to use it as you see fit.
If there is any correction or additions that can be made, be my guest and make them happen :wink:.
Below is the sample figure of the working GUI.

![Sample of working GUI](https://user-images.githubusercontent.com/89833078/131570856-aaef42cc-679b-415a-aecf-554da0d43e6b.PNG)
