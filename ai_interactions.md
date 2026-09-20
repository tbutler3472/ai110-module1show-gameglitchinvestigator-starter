# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

I asked the AI agent to add a Guess History feature to the game so it could keep track of the guesses the user made. I also wanted the history to reset when a new game started or when the difficulty was changed.

**What did the agent do?**

The agent changed the app.py file and added the Guess History to the sidebar. It makes it so only valid number guesses were added to the history and then when the a input is  invalid it won't be added. It also made the guess history reset when I started a new game or changed the difficulty.

**What did you have to verify or fix manually?**

I manually ran the game to make sure the Guess History actually worked. I entered multiple number guesses and made sure they showed up in the history. And saw on the side after every new guess the previous guess would show up with a number beside it with the guess number as well. I also made sure entering something that wasn't a number like a word wouldn't count as a guess. 

Files modified: The agent modified app.py to add the Guess History feature. No changes were needed to logic_utils.py or tests/test_game_logic.py.

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.
 Prompt Used:

Identify three potential edge cases for my number guessing game and create pytest tests for them. Make sure the tests verify that the game handles the edge cases correctly.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|------------|-------------|-------------------|--------------|----------------|
| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|------------|-------------|-------------------|--------------|----------------|
| Boundary exact match | Identify three edge cases for my game and make pytest tests for them. | Test the lowest and highest numbers in the range. | Yes | I chose this to make sure the game still works correctly at the lowest and highest numbers. |
| Extreme comparison hints | Identify three edge cases for my game and make pytest tests for them. | Test guesses that are really far from the secret number. | Yes | I chose this to make sure the higher and lower hints still work when the guess is far away from the secret number. |
| Near-boundary guesses | Identify three edge cases for my game and make pytest tests for them. | Test guesses that are one number away from the secret number. | Yes | I chose this to make sure the game still gives the right hint when the guess is really close to the secret number. ||

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
