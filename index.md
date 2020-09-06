# Code Talkers
**Inspiration**

The name and idea for this project comes from the Navajo CodeTalkers of World War 2, American soldiers who sent secret military messages over the air in their native Navajo tongue. We noticed that many movies regarding spies tend not to show aspects of disability, or difference from the all perfect James Bond superhero, so we decided to try to make a fun spy themed project for the hearing impaired. Here, we use sign language to communicate secret messages, much like the Navajo soldiers of the past. 

## Sign Language Recognition

Our sign language interpreter used Loic Marie's sign-language-alphabet-recognizer, which utilizes python, opencv and tensorflow to train InceptionV3 models. Here, the sign language interpreter takes in any symbol used to represent a letter in American Sign Language and with a degree of accuracy returns the char equivalent to that letter. This required training the interpreter with datasets to be able to accurately recognize the symbol.

## Cryptography

For driving the cryptography aspect of this project, we use hashes to create our own password system. We encrypt our secret message with SHA-256 encryption. Our system of managing a password and an encrypted message is both simple and relatively secure. While we wished to delve further into encryption and create our own method of securing both the password and the encrypted message, time simply did not allow us to do so.

## UI

For our UI we kept it relatively simple, as a spy only needs basic and unassuming tools. To do this, we utilized tkinter in python to create a relatively unassuming UI, with a plain looking windows default aesthetic. Our UI looks like a basic login to a simple windows tool, but is so much more! We also utilized OpenCV to take in video feeds, which goes to drive our sign language interpreter. 

## Dev Log

-1200: Started idea drafting and coming together with basic roles and duties to be done
-1600: Spend four hours doing datasets and getting machine learning ready
-1800: Start working on encryption and UI interfaces
-2200: Machine Learning training is finally finished
-2300: Spend more time getting OpenCV and a video processor working
-0100: Debate various encryption methods and salted vs plain hashes
-1000: Cry softly and continue trying to get UI to mesh with driver
-1100: make this index page
