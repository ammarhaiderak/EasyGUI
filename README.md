# TABLE OF CONTENTS

[INTRODUCTION](#_bbqh0c7e3rik)

[DEFINITIONS](#_vztnx98a5vkb)

[COMMAND FORMAT](#_e0aav57k291w)

[CLIENT SERVER COMMUNICATION](#_gx9cdbrmd7kk)

[COMMANDS](#_a6eh4lhk756x)

[EXAMPLES](#_8ravy3p6bnxc)

[THE GENERATOR](#_373hpcjkdju1)

[WIDGETS](#_nrlw31fizytt)

[BUTTON](#_761zra8nbzol)

[LABEL](#_h8wm4pw60qx3)

[EDIT](#_lymy0uh3k2su)

[MEMO](#_gz7qssgbzyx4)

[LIST](#_4ds3cqov79rt)

[COMBO](#_1b3fl5a1lyvm)

[CHECK](#_3o7sxtcssfx1)

[RADIO](#_56mdf5l5j3hc)

[SHAPE](#_vct2eqi5qrir)

[SLIDER](#_wo064enqjem2)

[IMAGE](#_aixyyijs5tx5)

[WEB](#_fwtqnoe49stj)

[UTILITY COMMANDS:](#_x9ayo549j4sq)

[Delete](#_z4ay3cug7kln)

[Load](#_o7linu5amx87)

[Write](#_37r4wo92lvr4)

[INTERNALS](#_dkn5rd120sw2)

[SETUP](#_zc6ib2a28h5t)

[WINDOWS](#_vj8zy1qazl3t)

[LINUX](#_etjzaj4jwrms)

#


# INTRODUCTION [↑](#_g7yze8loi1xi)

EasyGUI is an easy and simple way to create a Graphical User Interface on an Android device without any Android programming experience.

The system works by sending simple messages via Wi-Fi (using TCP) from any device and any operating system, to a target Android device (Mobile Phone or Tablet). These messages are simple strings that allow the creation of 12 different Widgets and a virtually

The most significant thing about these Widgets are that they are dynamic. Meaning that their size, shape, position, and color can be changed even after they were created, even during run-time.

Basically EasyGUI works as a Client, communicating with a Server on another device. The server may be ANY kind of hardware using ANY Operating System. All the logic resides in the Server which can be written in ANY language, (Python, Basic, C, C++, Pascal, JavaScript, Lua etc.) as long as they can send and receive messages using Sockets. This way most of the effort in creating an App can be concentrated at the &quot;Business End&quot; in the Server.

#


# DEFINITIONS [↑](#_g7yze8loi1xi)

**Client** : An Android device, A Mobile Phone, An Android Tablet or A Laptop running the Android

Operating System

**Server** : Any kind of Computing device, A Desktop, Laptop, Mobile phone, Single Board Computer (SBC) that is capable of Wi-Fi communication using Sockets.

It may be an Apple Phone or Tablet, An IBM compatible desktop, a Linux system, Another Android device of any kind, or an SBC like the ESP32 or Arduino.

**Template** : One or more pages containing EasyGUI widgets.

**Widget** : A Graphical User Interface Item, that allows communication with the user.

#


# COMMAND FORMAT [↑](#_g7yze8loi1xi)

Each Command consists of a Key/Value pair, where the Key is separated from the Value by an Equal (=) sign. Ie. 01=MyButton

Multiple Commands can be strung together where each Command is separated by a Tilde (~).

Ie. "01=MyButton~Left=500~Top=300~Text=Press This"

The first Command in a multiple Command line must be the command that identifies the Type and ID of the Widget.

The ID of a Widget must be unique. Even in a multiple Page Template.

All keywords are Case sensitive. There must NOT be spaces between separators.

In a Multi Page Template, The first page is always &quot;Page0, followed by Page1, Page2.

etc. in that strict sequence. There are no practical limits to the number of pages a Template may contain.

All colors are expressed as 9 digits RGB

#


# CLIENT SERVER COMMUNICATION [↑](#_g7yze8loi1xi)

The Server will be loaded first, and will display it&#39;s IP address and Port Number. waiting for the Client to initiate the conversation.

The first time the App is loaded it will prompt you for the last three digits of the Server&#39;s IP (leading zero fill to 3 digits) and the Port no (leading zero fill to 5 digits).

After that the Client will store this data, and it will only be necessary to re-input it if the Server&#39;s IP address or the Port number has changed.

Example: if your Servers IP address is: 192.168.24.73 and the Port is 4000, type in the following when prompted: 07304000

The Client will send a start message first, containing it&#39;s IP and other identifying information.

After The initial handshaking, ALL TRANSACTIONS MUST BE IN PAIRS. Ie. Each **TRANSMIT (Put)** must be followed by a **RECEIVE (Get)**

The Server will send Commands to the Client to create or change the Widgets. The Client will reply to each message with either: OK (Message 40) or ERROR (Message 96), or in the case of a SYNTAX ERROR 99.

It is the Servers responsibility to check if an error has occurred.

**A typical sequence of events** :

1. Create a Template, either using EasyGen or manually using SimpServer.py
2. Server issues a Wait (40) command to wait for user action
3. The User performs an action (like pressing a Button)
4. The Client replies passing 3 or more pieces of information
  1. The type of the Widget
  2. The ID of the Widget
  3. The action the user performed (like short press/long press)
5. The Server takes the necessary action based upon the Reply from the Client
6. Repeat from Step 2

#


# COMMANDS [↑](#_g7yze8loi1xi)

These Commands are contained in the supplied EasyGUI.py module. These are provided to make the programming of the Server even easier.

**It&#39;s use is not compulsory or necessary in order to use EasyGUI, you can do all the detailed server programming yourself.**

**Open (Port)**- This will open communication on the Port number specified.

**Put (message)**- Sends a message to the Client to create or change a widget. All the Widgets parameters will be updated in the Dictionaries in the config.py module which holds the current parameters of all widgets.

**Get ()** - Receives a message from the Client, and returns the Client&#39;s reply

**Send(message)** - The combination or Put and Get. Returns the Client&#39;s reply

**Find (ID,Key)**- Returns the current value of the Widget&#39;s as per the Key.

if the following message was sent:

"1=MyButton~Left=500~Top=300~Color=255000000"

Find(&#39;MyButton&#39;,&#39;Top&#39;) will return 300

**Wait()**  **-** Sends a message **40** to the Client, and waits until a user action, which will be passed to the Server by the Client.

**GetTemplate(FileName)**  **-** Reads a Template, which is stored on the Client and displays it. It will also update the dictionaries in config.py which holds the current values of all widgets.

#


# EXAMPLES [↑](#_g7yze8loi1xi)

Python example where you can type each command manually, and the widgets will be

created/changed interactively.

# SimpleServer.py (Using EasyGUI - No error checking performed)

EasyGUI import \*

import config from EasyGUI import \*

Open(4000) # Open Socket

while True:

Mess = input(&#39;Send: &#39;) # Type in Command

Put(Mess) # Transmit Command

Print(Get()) # print the received reply

![](RackMultipart20200906-4-l9nmj5_html_7d31fade30f8296b.gif)

This Garage Door Opener Server demonstrates the power of EasyGUI. It uses 2 Image widgets (the Garage and the Door) and 1 button. The Template only contains 4 Commands.

# Garage.py (Using EasyGUI)

import time from EasyGUI import \*

import config

def GoUp(): # Function to make the door go up

for n in range(400,0,-10):

time.sleep(.1)

Send(&#39;11=door~Height=&#39; + str(n))

Send(&#39;01=up~Text=DOWN&#39;)

def GoDown(): # Function to make the door go Down

for n in range(0,480, +10):

time.sleep(.1)

Send(&#39;11=door~Height=&#39; + str(n))

Send(&#39;01=up~Text=UP&#39;)

Open(4000) # Open Socket

Send(&#39;51=Load~Text=Garage.dat&#39;) # Load the template from the Client

time.sleep(.5) # sleep for half second

while True:

Wait() # Wait for button press

GoUp()

Wait() # Wait for button press

GoDown()

![](RackMultipart20200906-4-l9nmj5_html_7d31fade30f8296b.gif)

This is an example of a server using Micropython for Single Board Computers (like 8266 or ESP32).

#MicroPython SimpServer (Without EasyGUI and with Error checking)

import sys

import socket

CRLF = &#39;\r\n&#39;

port = 4000

s = socket;

def Put(mess):

c.send((mess + CRLF).encode()) # Send message

def Get():

return c.recv(1024).decode() # Read reply

def Open(port):

global c

global s

s = socket.socket(socket.AF\_INET, socket.SOCK\_STREAM)

s.setsockopt(socket.SOL\_SOCKET, socket.SO\_REUSEADDR, 1)

s.bind( (&#39;&#39;, port) )

s.listen(10)

print (&#39;Listening on Port &#39; + str(port))

c, a = s.accept()

print (&#39;Client connected&#39;, a)

print(Get())

def Close(): # Close Socket

c.close()

s.close()

def Start():

Open(port) # Open Socket

Put(&#39;51=Load~Text=Sample.dat&#39;) #Load from Client

print(Get())

Start()

while True:

Put(&#39;40&#39;) # wait for Client&#39;s reply

rec = Get()

if (rec == &#39;40=Radio~2&#39;): # Finish, close

Put(&#39;Exit&#39;)

Close()

print(&#39;Socket Closed&#39;)

sys.exit()

if (rec == &#39;&#39;): # Client offline

Close() # Close socket

print(&#39;Reopening&#39;)

Start() # Reopen Socket

print(rec)

![](RackMultipart20200906-4-l9nmj5_html_7d31fade30f8296b.gif)

This an example Server written in JavaScript:

const net = require(&#39;net&#39;);

const server = net.createServer((socket) =\&gt; {

console.log(&#39;Connection from&#39;, socket.remoteAddress, &#39;port&#39;, socket.remotePort);

socket.on(&#39;data&#39;, (buffer) =\&gt; {

//console.log(&#39;Request from&#39;, socket.remoteAddress, &#39;port&#39;, socket.remotePort);

console.log(&#39;Recieved:&#39;,`${buffer.toString(&#39;utf-8&#39;)}\n`);

var msg=require(&#39;prompt&#39;);

msg.start();

msg.get([&#39;command&#39;], function (err, result) {

//

// Log the results.

//

//console.log(&#39;Command-line input received:&#39;);

console.log(&#39; command: &#39; + result.command);

socket.write(`${result.command}\n`);

});

});

socket.on(&#39;Exit&#39;, () =\&gt; {

console.log(&#39;Closed&#39;, socket.remoteAddress, &#39;port&#39;, socket.remotePort);

});

});

//server.maxConnections = 20;

server.listen(4002);

![](RackMultipart20200906-4-l9nmj5_html_7d31fade30f8296b.gif)

An Example for the 8266 using Arduino code:

#include &quot;ESP8266WiFi.h&quot;

const char\* ssid = &quot;yourNetworkName&quot;;

const char\* password = &quot;yourNetworkPass&quot;;

WiFiServer wifiServer(80);

void setup() {

Serial.begin(115200);

delay(1000);

WiFi.begin(ssid, password);

while (WiFi.status() != WL\_CONNECTED) {

delay(1000);

Serial.println(&quot;Connecting..&quot;);

}

Serial.print(&quot;Connected to WiFi. IP:&quot;);

Serial.println(WiFi.localIP());

wifiServer.begin();

}

void loop() {

WiFiClient client = wifiServer.available();

if (client) {

while (client.connected()) {

while (client.available()\&gt;0) {

char c = client.read();

Serial.write(c);

}

delay(10);

}

client.stop();

Serial.println(&quot;Client disconnected&quot;);

}

}

![](RackMultipart20200906-4-l9nmj5_html_7d31fade30f8296b.gif)

# THE GENERATOR [↑](#_g7yze8loi1xi)

In order to make it easier to design Widgets, and place them on the Page, we have developed the EasyGen Generator. This Graphical User Interface Designer will allow the designer to see the end result on the Client device itself as the design is being developed.

![](RackMultipart20200906-4-l9nmj5_html_2296d4ccaf8d4302.jpg)

**How to use EasyGen:**

1 - Start EasyGen (python EasyGen.py)

2 - Load the App on the Client. The EasyGen GUI will be displayed

Select a Widget from the Select Type list by clicking on it

a - Page0 will be the default

b - Type in a unique ID. The Widget will appear immediately on the Client&#39;s screen

in position x=0, y=0, and it will appear in the Widget List

c - If you want to move or resize the Widgets, click on the Move or Size button

and use the 4 arrow keys to move and or resize the Widget. Each press of the arrow keys will move or resize the widget by 10 pixels.

As the arrow keys manipulate the Widget the fields on the Gui will change automatically.

d - Fill in the rest of the fields, as necessary

e - Add more widgets

3 - If you want to edit any of the Widgets, click on it in the Widgets list, and all it&#39;s

parameters will, be displayed so you can edit them

4 - When the Template is Completed, type in the Name of the file that you want to save it to

on the Client and press &#39;Save Template&#39;

5 - If you want to edit an existing Template, Type the name of the file into the FileName

entry and press &#39;Load Template&#39;

Since this Script is provided in Source format, you are welcome to modify it, after which any responsibility for the results will be yours .

# WIDGETS
#
[↑](#_g7yze8loi1xi)

## BUTTON

| **PARAM** | **TYPE** | **DEFAULT** | **COMMENT** |
| --- | --- | --- | --- |
| **Type** | **01** | | **Button** |
| ID | | | AlphaNumeric - Must be unique |
| Left | | 0 | Numeric |
| Top | | 0 | Numeric |
| Width | | 500 | Numeric |
| Height | | 200 | Numeric |
| Text | | | Displayed Text - if blank, ID is used |
| Just | | 1 | Text Justification - Left = 1, Center = 2, Right = 3 |
| Back | | 236236236 | Background Color (RGB) |
| Color | | 000000000 | Foreground Color (RGB) |
| Size | | 14 | Font Size |
| Style | | 0 | Font Style - Normal = 0, Bold = 1, talic = 2, Underline = 4 |
| Min | | | Not used |
| Max | | | Not used |
| Pos | | | Not used |
| **Reply** | | | 40=ID~1 for short press, 2 for long press |

##


## LABEL [↑](#_g7yze8loi1xi)

| **PARAM** | **TYPE** | **DEFAULT** | **COMMENT** |
| --- | --- | --- | --- |
| **Type** | **02** | | **Label** |
| ID | | | AlphaNumeric - Must be unique |
| Left | | 0 | Numeric |
| Top | | 0 | Numeric |
| Width | | 500 | Numeric |
| Height | | 200 | Numeric |
| Text | | | Displayed Text - if blank, ID is used |
| Just | | 1 | Text Justification - Left = 1, Center = 2, Right = 3 |
| Back | | 236236236 | Background Color (RGB) |
| Color | | 000000000 | Foreground Color (RGB) |
| Size | | 14 | Font Size |
| Style | | 0 | Font Style - Normal = 0, Bold = 1, talic = 2, Underline = 4 |
| Min | | | Not used |
| Max | | | Not used |
| Pos | | | Not used |
| **Reply** | | | 40=ID~1 for short press, 2 for long press |

##

##


## EDIT [↑](#_g7yze8loi1xi)

| **PARAM** | **TYPE** | **DEFAULT** | **COMMENT** |
| --- | --- | --- | --- |
| **Type** | **03** | | **Edit** |
| ID | | | AlphaNumeric - Must be unique |
| Left | | 0 | Numeric |
| Top | | 0 | Numeric |
| Width | | 500 | Numeric |
| Height | | 150 | Numeric |
| Text | | | Default Text to display - \* if password |
| Just | | 1 | Text Justification - Left = 1, Center = 2, Right = 3 |
| Back | | 236236236 | Background Color (RGB) |
| Color | | 000000000 | Foreground Color (RGB) |
| Size | | 14 | Font Size |
| Style | | 0 | Font Style - Normal = 0, Bold = 1, talic = 2, Underline = 4 |
| Min | | | Not used |
| Max | | | Not used |
| Pos | | | Not used |
| **Reply** | | | 40=ID~My Name (The entered line) |

##


##


## MEMO [↑](#_g7yze8loi1xi)

| **PARAM** | **TYPE** | **DEFAULT** | **COMMENT** |
| --- | --- | --- | --- |
| **Type** | **04** | | **Memo** |
| ID | | | AlphaNumeric - Must be unique |
| Left | | 0 | Numeric |
| Top | | 0 | Numeric |
| Width | | 500 | Numeric |
| Height | | 500 | Numeric |
| Text | | | Displayed Text |
| Just | | 1 | Text Justification - Left = 1, Center = 2, Right = 3 |
| Back | | 236236236 | Background Color (RGB) |
| Color | | 000000000 | Foreground Color (RGB) |
| Size | | 14 | Font Size |
| Style | | 0 | Font Style - Normal = 0, Bold = 1, talic = 2, Underline = 4 |
| Min | | | Not used |
| Max | | | Not used |
| Pos | | | Not used |
| **Reply** | | | 40=ID~Line1|Line2 (Lines entered separated by &quot;|&quot; |

##


##


## LIST [↑](#_g7yze8loi1xi)

| **PARAM** | **TYPE** | **DEFAULT** | **COMMENT** |
| --- | --- | --- | --- |
| **Type** | **05** | | **List** |
| ID | | | AlphaNumeric - Must be unique |
| Left | | 0 | Numeric |
| Top | | 0 | Numeric |
| Width | | 500 | Numeric |
| Height | | 500 | Numeric |
| Text | | | Displayed Text, Lines separated by &quot;|&quot; |
| Just | | 1 | Text Justification - Left = 1, Center = 2, Right = 3 |
| Back | | 236236236 | Background Color (RGB) |
| Color | | 000000000 | Foreground Color (RGB) |
| Size | | 14 | Font Size |
| Style | | 0 | Font Style - Normal = 0, Bold = 1, talic = 2, Underline = 4 |
| Min | | | Not used |
| Max | | | Not used |
| Pos | | | Not used |
| **Reply** | | | 40=ID~Line2 (the selected line) |

##


##


## COMBO [↑](#_g7yze8loi1xi)

| **PARAM** | **TYPE** | **DEFAULT** | **COMMENT** |
| --- | --- | --- | --- |
| **Type** | **06** | | **Combo** |
| ID | | | AlphaNumeric - Must be unique |
| Left | | 0 | Numeric |
| Top | | 0 | Numeric |
| Width | | 500 | Numeric |
| Height | | 150 | Numeric |
| Text | | | Displayed Text, Lines separated by &quot;|&quot; |
| Just | | 1 | Text Justification - Left = 1, Center = 2, Right = 3 |
| Back | | 236236236 | Background Color (RGB) |
| Color | | 000000000 | Foreground Color (RGB) |
| Size | | 14 | Font Size |
| Style | | 0 | Font Style - Normal = 0, Bold = 1, talic = 2, Underline = 4 |
| Min | | | Not used |
| Max | | | Not used |
| Pos | | | Not used |
| **Reply** | | | 40=ID~Item3 (the selected Item) |

##


##


## CHECK [↑](#_g7yze8loi1xi)

| **PARAM** | **TYPE** | **DEFAULT** | **COMMENT** |
| --- | --- | --- | --- |
| **Type** | **07** | | **Check** |
| ID | | | AlphaNumeric - Must be unique |
| Left | | 0 | Numeric |
| Top | | 0 | Numeric |
| Width | | 150 | Numeric |
| Height | | 150 | Numeric |
| Text | | | Text to display with the Checkbox |
| Just | | 1 | Display Text at Left = 1, Right = 2, Top = 3, Bottom = 4 |
| Back | | 236236236 | Background Color (RGB) |
| Color | | 000000000 | Foreground Color (RGB) |
| Size | | 14 | Font Size |
| Style | | 0 | Font Style - Normal = 0, Bold = 1, talic = 2, Underline = 4 |
| Min | | | Not used |
| Max | | | Not used |
| Pos | | 0 | Unchecked = 0, Checked = 1 |
| **Reply** | | | 40=ID~0 for Unchecked, 1 for Checked |

##


##


## RADIO [↑](#_g7yze8loi1xi)

| **PARAM** | **TYPE** | **DEFAULT** | **COMMENT** |
| --- | --- | --- | --- |
| **Type** | **08** | | **Radio** |
| ID | | | AlphaNumeric - Must be unique |
| Left | | 0 | Numeric |
| Top | | 0 | Numeric |
| Width | | 150 | Numeric |
| Height | | 150 | Numeric |
| Text | | | Each Buttons Text separated by &quot;|&quot; |
| Just | | 1 | Text of Left = 1, Text on Right = 2 |
| Back | | 236236236 | Background Color (RGB) |
| Color | | 000000000 | Foreground Color (RGB) |
| Size | | 14 | Font Size |
| Style | | 0 | Font Style - Normal = 0, Bold = 1, talic = 2, Underline = 4 |
| Min | | 1 | Horizontal = 1, Vertical = 2 |
| Max | | 0 | Indicates which button is ON |
| Pos | | 0 | Off = 0, ON = 1 |
| **Reply** | | | 40=ID~1 (0 = First button,1 = Second Button) ….. |

##


##


## SHAPE [↑](#_g7yze8loi1xi)

| **PARAM** | **TYPE** | **DEFAULT** | **COMMENT** |
| --- | --- | --- | --- |
| **Type** | **09** | | **Shape** |
| ID | | | AlphaNumeric - Must be unique |
| Left | | 0 | Numeric |
| Top | | 0 | Numeric |
| Width | | 150 | Numeric |
| Height | | 150 | Numeric |
| Text | | | Not Used |
| Just | | 1 | Square = 1, Circle = 2 |
| Back | | 236236236 | Background Color (RGB) |
| Color | | 000000000 | Drawing Color (RGB) |
| Size | |
 | Not used |
| Style | |
 | Not used |
| Min | | 1 | Non-Transparent = 1, Transparent = 2 |
| Max | | | Not used |
| Pos | | | Not used |
| **Reply** | | | 40=ID~1 |

##


##


## SLIDER [↑](#_g7yze8loi1xi)

| **PARAM** | **TYPE** | **DEFAULT** | **COMMENT** |
| --- | --- | --- | --- |
| **Type** | **10** | | **Slider** |
| ID | | | AlphaNumeric - Must be unique |
| Left | | 0 | Numeric |
| Top | | 0 | Numeric |
| Width | | 500 | Numeric |
| Height | | 200 | Numeric |
| Text | | | Not Used |
| Just | | 1 | Horizontal = 1, Vertical = 2 |
| Back | | 236236236 | Background Color (RGB) |
| Color | | 000000000 | Foreground Color (RGB) |
| Size | |
 | Not Used |
| Style | |
 | Not Used |
| Min | | 0 | Minimum Value |
| Max | | 100 | Maximum Value |
| Pos | | 50 | Current Value |
| **Reply** | | | 40=ID~Current Position of Slider |

##


##


## IMAGE [↑](#_g7yze8loi1xi)

| **PARAM** | **TYPE** | **DEFAULT** | **COMMENT** |
| --- | --- | --- | --- |
| **Type** | **11** | | **Image** |
| ID | | | AlphaNumeric - Must be unique |
| Left | | 0 | Numeric |
| Top | | 0 | Numeric |
| Width | | 500 | Numeric |
| Height | | 500 | Numeric |
| Text | | | File Name (if file is in Client) or URL |
| Just | |
 | Not used |
| Back | |
 | Not used |
| Color | |
 | Not used |
| Size | |
 | Not used |
| Style | |
 | Not used |
| Min | | | Not used |
| Max | | | Not used |
| Pos | | | Not used |
| **Reply** | | | 40=ID~1 fort short press, 2 for long press |

##


##


## WEB [↑](#_g7yze8loi1xi)

| **PARAM** | **TYPE** | **DEFAULT** | **COMMENT** |
| --- | --- | --- | --- |
| **Type** | **12** | | **Web** |
| ID | | | AlphaNumeric - Must be unique |
| Left | | 0 | Numeric |
| Top | | 0 | Numeric |
| Width | | 500 | Numeric |
| Height | | 200 | Numeric |
| Text | | | URL |
| Just | |
 | Not Used |
| Back | |
 | Not Used |
| Color | |
 | Not Used |
| Size | |
 | Not Used |
| Style | |
 | Not Used |
| Min | | | Not Used |
| Max | | | Not Used |
| Pos | | | Not Used |
| **Reply** | | | 40=ID~URL of the Web address navigated to |

##


# UTILITY COMMANDS: [↑](#_g7yze8loi1xi)

These Commands do NOT create widgets. They are provided for utility purposes

## Delete

| **PARAM** | **TYPE** | **DEFAULT** | **COMMENT** |
| --- | --- | --- | --- |
| **Type** | **50** | | **Delete** |
| ID | | | &#39;Delete&#39; |
| Text | |
 | The ID of the Widget to be deleted from the Page |
| **Reply** | |
 | If OK = 40, If Widget does not exists = 96 |

Example: 50=Delete~Text=MyButton

## Load

| **PARAM** | **TYPE** | **DEFAULT** | **COMMENT** |
| --- | --- | --- | --- |
| **Type** | **51** | | **Load** |
| ID | | | &#39;Load&#39; |
| Text | |
 | TheFileName of the Template stored on the Client |
| Just |
 | 0 | 0 = Clear, 1 =Overlay |
| **Reply** | |
 | If OK = 40, If file does not exists = 96 |

Example: 51=Load~Text=Template1.dat

NOTE: Using this will NOT update config.py

## Write

| **PARAM** | **TYPE** | **DEFAULT** | **COMMENT** |
| --- | --- | --- | --- |
| **Type** | **52** | | **Write** |
| ID | | | &#39;Write&#39;&#39; |
| Text | |
 | The Filename that the Template will be written to |
| **Reply** | |
 | If OK = 40, If FileName already exists = 96 |

Example: 52=Write~Text=NewTemplate.dat

Exit

| **PARAM** | TYPE | DEFAULT | COMMENT |
| --- | --- | --- | --- |
| Type |
 | | **Exit** |

Exit the App

# INTERNALS [↑](#_g7yze8loi1xi)

**config.py** - This module holds the following variables :

LOT This is a List of Dictionaries, where each Dictionary holds a Widget, and each

Key/Value pair contains the Widget&#39;s current properties.

W The Screen width of the current Client

H The Screen Height of the current Client

Port The current Communication Port

IP The IP of the Host

Keys The 4 Arrow-Key keyboard values for the keyboard of the Server (Used

by the Generator)

**EasyGUI.py -**

This module contains the various functions described under [COMMANDS](#_a6eh4lhk756x)

This is an optional Module, and should you want to code the Server by yourself

from scratch, you are free to do so.

Since this module is provided in Source format, you are welcome to modify it, after which any responsibility for the results will be yours

#


# SETUP [↑](#_g7yze8loi1xi)

PREREQUISITES (for python):

python 3.x

Tkinter (pip install Tkinter)

keyboard (pip install keyboard)

messagebox (pip install messagebox)

All the necessary files will be contained in EasyGUI.zip.

1 - Unzip EasyGUI.zip into a Folder created for EasyGUI

2 - The following files will be created:

Setup.py - This script will create config.py

EasyGen.py - The Generator

EasyGUI.py - The Command module

SimpServer.py - The simplest possible Server example

MicroPython SimpServer - A simple Server for MicroPython

JavaScript Server - A simple Server written in JavaScript

3 - Run Setup.py (python Setup.py)

In order to be able to use the arrow keys in EasyGen which seems to be different on some operating systems the keyboard module need to be installed: (pip install keyboard)

Setup.py will prompt you to press each of the arrow keys in turn, the results of which will be stored in config.py


