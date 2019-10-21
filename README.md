# BUMP: Smart Location-Based Conversation Starter
Bump up your connection with BUMP! Bump enables opportune friendships that were never possible before. Connect with people around you who share similar interests.

<img width="428" alt="Screen Shot 2019-10-20 at 3 38 42 AM" src="https://user-images.githubusercontent.com/45777902/67168697-b7633980-f374-11e9-986e-1ee9da72f82f.png">


## What is BUMP?
Every minute of every day, we pass by countless individuals with very interesting lives, perspectives and experiences -- people you would've loved to connect with. Yet so many of these connections never have the chance of happening. 

Even when you actively seek out these connections it is sometimes hard to find someone who shares a similar interest in the person. Thus, we created an app that allows you to overcome this challenge.

BUMP is a smart location-based conversation starter that connects users with similar interests.
When the user inputs their interest in the app, BUMP will locate other nearby users and utilize the NLP algorithm to match you up with someone with similar interests. Once the user receives the notification, they will have the option to accept the invitation to start a conversation, reply later by sharing contact information, or decline. During the conversation, both users can use each other's list of interests as a guideline to facilitate a smooth conversation. At the end of the conversation, the user will be given the opportunity to rate or report the conversation.


## How we built it

Backend - We developed the backend using Flask and PostgreSQL. The backend interacted with the frontend through a set of API calls (Spec: https://docs.google.com/document/d/1e2iQhsyTeqddxOafKg6qoAgDFuydDjqwuYIvAT4Z5YY/edit?usp=sharing). The backend took care of processing and storing user data, running the algorithm to compute matches, and handling authentication with Firebase. The backend is deployed on Google Cloud's App Engine.

Frontend - We designed the UX/UI on AdobeXD, creating a rough mockup of our idea. The frontend was implemented in React Native for both IOS and Android.

Algorithm - Utilized SpaCy, an advanced Natural Language Processing (NLP) Library, to create a matching algorithm that connected users together based on their indicated interests.


## App Layout

### Login Page
<img width="345" alt="Screen Shot 2019-10-20 at 8 05 46 PM 1" src="https://user-images.githubusercontent.com/45777902/67168737-05783d00-f375-11e9-9f8b-46b3e0d1ffaf.png">

### Interest Log
<img width="344" alt="Screen Shot 2019-10-20 at 2 50 25 AM" src="https://user-images.githubusercontent.com/45777902/67168723-e11c6080-f374-11e9-8077-67f8cbcb1d08.png">

The user can input the topic of interest they want to talk about with the others around them.

### Notification
<img width="347" alt="Screen Shot 2019-10-20 at 2 50 48 AM" src="https://user-images.githubusercontent.com/45777902/67168750-28a2ec80-f375-11e9-814e-79914ddf630f.png">

<img width="347" alt="Screen Shot 2019-10-20 at 2 50 57 AM" src="https://user-images.githubusercontent.com/45777902/67168768-5b4ce500-f375-11e9-8835-32c822f83564.png">

The user will get a "bump" / notification if you want to get a match. They will be able to view the other user's profile and decide if they want to accept to talk now, send them your contact to talk later, or decline.

### Rate Conversation
<img width="343" alt="Screen Shot 2019-10-20 at 2 51 42 AM" src="https://user-images.githubusercontent.com/45777902/67168796-92bb9180-f375-11e9-933c-e6df2f07cf0b.png">

The user will be able to rate the conversation after meeting the other user.


## What's next for Bump
- Improve NLP model
- Improve mobile application
