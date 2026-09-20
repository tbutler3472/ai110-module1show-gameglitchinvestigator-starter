# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?
When I first ran it the game looked like a regular guessing number game and how it looked like it was suppose to from the video example. But, I realized there were serious problems affter playing it 3 times and it wasn't running properly. One of the problems is that it would keep telling me to guess lower even when the number was higher than my guess. Not only that but, it gave a secret number on each difficulty outside of the range of numbers it was suppose to be and gave a negative score for my guess.
- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
Easy mode inputed 1 as my guess| It would tell me to go higher or my guess was right because 1 was the lowest in the 1-20 range| Hint showed the number was 72 outside the range|none 
Hard mode guessed 4 when the secret number was 90| Expected the game would told me to go higher since i was way off| Game told me to go lower instead|none 
Selected Hard Mode| That the hard mode would have the biggest range| Normal had the biggest range from 1-100 and hard had 1-50 when hard suppose to be most challenging mode|none

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used chat gpt outside of vs code to help with instructions and organization and then used co pilot in vs code to make the changes to the actual code and sugestions. 
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
One example of a correct suggestion AI gave me was that the higher and lower hint messages were reversed and it correctly suggested to move the check guess logic into logic utilis. To verify this was correct I ran the py test after all the changes were implemented and all 4 test passed. I also checked the game and the logic was fixed and it now told me to go higher when my guess was to low instead of saying go lower. 
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
One suggestion that was misleading was that it said I needed to change the test before I ran them. So when it suggested it and i ran the py test it failed 3 of 4 of the test so in order to fix it I had the AI update the old test so that it would match the check guess function that was already returned and I ran the py test after the changes and then all 4 of the test passed. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided the bug was really fixed by running the game and testing to see if the original bug was what it shoul've been after the changes or if it was the same, worse or just not fixed like it was suppose to be. 
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

I ran a pytest to help fix when it would tell you higher and lower wiht your guesses. The test helped check that when the guess was lower than the secret number it would tell the player to guess higher and when the guess was higher then the secret number it would tell the player to guess lower. The test passed which showed me that my codes hint logic was now working correctly because before 3 of the 4 test failed. 

Did AI help you design or understand any tests? How?
Yes, AI helped me design the test for the higher lower bug. I was struggling to figure out how to check that the fixes were acually work. So I used AI to help me make a test that helped check what the game should return when the guess was higher or lower than the secret number. Which helped understand how the pytest can automatically check if the game logic is actually working. 

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

I would explain as simple as I could say Streamlit is what runs and displays the dahsboard for the game. When the user interacts dashboard though thats when streamlit re runs the code in order to update the app. While the session state saves information like for example the secret number, score and the attempts so when the code re runs the information is not lost. 
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
One habit I want to reuse in future labs and projects is instead of assuming the code I get from AI automatically works making sure i test it and make sure it's actually doing what I want it to do instead of assuming it does. Another thing would also be giving more specific details when I prompt the AI as well.  
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
I think one thing i would differently would be not only reviewing the changes but also instead of relying on one AI for everything like Chat GPT branch out more and look at different outputs that be generated from like Claude, Co Pilot, and Google Gemni. 
- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project changed the way I think about AI code because it made me more aware of the mistakes AI can do with code or even not fully give what you ask for originally. It also made me realize how important learning how to ask and prompt is and the language and directions you give to the AI. 