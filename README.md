# BUMP: Smart Location-Based Conversation Starter
Bump up your connection with BUMP! Bump enables opportune friendships that were never possible before. Connect with people around you who share similar interests.

## What is BUMP?
Every minute of every day, we pass by countless individuals with very interesting lives, perspectives and experiences -- people you would've loved to connect with. Yet so many of these connections never have the chance of happening. 

Even when you actively seek out these connections it is sometimes hard to find someone who shares a similar interest in the person. Thus, we created an app that allows you to overcome this challenge.

BUMP is a smart location-based conversation starter that connects users with similar interests.
When the user inputs their interest in the app, BUMP will locate other nearby users and utilize the NLP algorithm to match you up with someone with similar interests. Once the user receives the notification, they will have the option to accept the invitation to start a conversation, reply later by sharing contact information, or decline. During the conversation, both users can use each other's list of interests as a guideline to facilitate a smooth conversation. At the end of the conversation, the user will be given the opportunity to rate or report the conversation.


## How we built it

Backend - We developed the backend using Flask and PostgreSQL. The backend interacted with the frontend through a set of API calls (Spec: https://docs.google.com/document/d/1e2iQhsyTeqddxOafKg6qoAgDFuydDjqwuYIvAT4Z5YY/edit?usp=sharing). The backend took care of processing and storing user data, running the algorithm to compute matches, and handling authentication with Firebase. The backend is deployed on Google Cloud's App Engine.

Frontend - We designed the UX/UI on AdobeXD, creating a rough mockup of our idea. The frontend was implemented in React Native for both IOS and Android.
Algorithm - Utilized SpaCy, an advanced Natural Language Processing (NLP) Library, to create a matching algorithm that connected users together based on their indicated interests.

## What's next for Bump
- Improve NLP model
- Improve mobile application
