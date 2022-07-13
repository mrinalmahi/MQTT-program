# MQTT-program
1. Connect to the broker. 
2. Send a message containing your student ID to the topic ”login”. Example-> Topic: ”login”,
Message: ”12345”.
3. Once you sent the message to ”login”, you will receive a message on the topic ”<STUDENT ID>/UUID”.
The message will contain a UNIQUE ID. Example-> Topic: ”12345/UUID”, Message: ”1234-
fdsfs-12441-qa241”. 
4. After 3 secods from the publishing of the UNIQUE ID, you will receive multiple messages on
the topic ”<UNIQUE ID>” with different commands. Example-> Topic: ”1234-fdsfs-12441-
qa241”, Message: ”CMD1”.
5. For each command you will have to send a specific reply (check the commands and the replies
below) to the followind topic: ”<UNIQUE ID>/<CMD>”. Example-> Topic: ”1234-fdsfs12441-qa241/CMD1”, Message: ”Apple”. (30 points)
6. Once all the commands are handled and replies are sent, you will receive the following message:
”Well done my IoT!” on the topic ”<UNIQUE ID>”. Example-> Topic: ”1234-fdsfs-12441-
qa241”, Message: ”Well done my IoT!”.
7. Once you receive this message, the communcation is over and you can disconnect from the
broker. 
Possible commands that can be received and the reply that you have to send for each command:
• ”CMD1” -> ”Apple”
• ”CMD2” -> ”Cat”
Page 1 of 2
• ”CMD3” -> ”Dog”
• ”CMD4” -> ”Rat”
• ”CMD5” -> ”Boy”
• ”CMD6” -> ”Girl”
• ”CMD7” -> ”Toy”
