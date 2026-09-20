# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

 The game's purpose is to guess a randomly generated secret number while using higher and lower hints to find the correct answer.

 The bugs I found were reversed higher/lower hints, the secret number not matching the selected difficulty range, and the game not resetting correctly when changing difficulty.

I fixed the hint logic, made the secret number follow the selected difficulty range, and fixed the game so it properly updates when the difficulty changes.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

## Demo Walkthrough

1. User selects a difficulty level for the game.
2. The game generates a secret number based on the selected difficulty range.
3. User enters a guess that is lower than the secret number.
4. The game returns "Too Low" and tells the user to go higher.
5. User enters a guess that is higher than the secret number.
6. The game returns "Too High" and tells the user to go lower.
7. The user continues guessing until they enter the correct secret number.
8. The game tells the user that their guess is correct and shows their final result.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
