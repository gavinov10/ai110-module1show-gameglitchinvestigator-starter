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

- [ ] Describe the game's purpose.
   - the games purpose is to guess the right number that was randomized with a limited number of guesses. 
- [ ] Detail which bugs you found.
   1. I found that clicking new game had a bug and didn't really start a new game.
   2. the hints were hinting back the wrong hints. for eg. if the number was higher than the secret number then it would say to keep going higher and vise versa with if the guess with lower.
   3. if a user entered a non-numeric input, the attempts would still change even though it shouldn't affect the attempts
- [ ] Explain what fixes you applied.
   1. I applied the hinting bug, and so now it correctly tells the user whether they are too high or too low from the secret number
   2. Secondly, I fixed the new game button. Now when a user clicks new game a new game starts and there is no bugs.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a guess
2. Hints return either "Too low" or "Too High"
3. Number of guesses decreses until 0 or game ends if correct number
4. Click new game
5. A new game is initialized and are able to go again

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
platform darwin -- Python 3.12.0, pytest-9.0.3, pluggy-1.6.0 -- /Users/gv/Library/Mobile Documents/com~apple~CloudDocs/Builds/CodePath/AI Engineering/ai110-module1show-gameglitchinvestigator-starter/.venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/gv/Library/Mobile Documents/com~apple~CloudDocs/Builds/CodePath/AI Engineering/ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collected 9 items                                                                                                                                              

tests/test_game_logic.py::test_hint_says_go_lower_when_guess_too_high PASSED                                                                             [ 11%]
tests/test_game_logic.py::test_hint_says_go_higher_when_guess_too_low PASSED                                                                             [ 22%]
tests/test_game_logic.py::test_hint_direction_matches_outcome[60-50-Too High-LOWER] PASSED                                                               [ 33%]
tests/test_game_logic.py::test_hint_direction_matches_outcome[40-50-Too Low-HIGHER] PASSED                                                               [ 44%]
tests/test_game_logic.py::test_hint_direction_matches_outcome[99-1-Too High-LOWER] PASSED                                                                [ 55%]
tests/test_game_logic.py::test_hint_direction_matches_outcome[1-99-Too Low-HIGHER] PASSED                                                                [ 66%]
tests/test_game_logic.py::test_winning_guess PASSED                                                                                                      [ 77%]
tests/test_game_logic.py::test_guess_too_high PASSED                                                                                                     [ 88%]
tests/test_game_logic.py::test_guess_too_low PASSED                                                                                                      [100%]
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
