# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  the game looked like it was ready, finalized
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  1. the hints were telling us to go backwords
  2. instead of getting 8 attempts you actually get 9 attempts becuase the start is at 0
  3. score doesn't reset when you click new game
  4. when new game is clicked, the message: "Game over. Start a new game to try again."
      doesn't go away
  5. when I enter a non-numeric input, it still adds to the "attempts left" and actually passes the number as well
**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| guess of 60  | "too high"(hint) | "too low" (hint) | none
| string  | stays in the same attemps | decreases the attempts still | none
| new game --> clicked | message "Game over. Start a new game to try again." should go away | message stays and no functionality when starting new game| none

---

## 2. How did you use AI as a teammate?

- **Which AI tools did you use on this project?**
  I used Claude Code (agent mode) inside VS Code as my pair-programmer. I drove the
  decisions and scope; the AI explained logic, made edits I reviewed, and ran the tests.

- **A correct AI suggestion (and how I verified it).**
  When I described the backwards hints, the AI traced a concrete example (secret = 10,
  guess = 7) and showed that `check_guess` returned the right *outcome* ("Too Low") but
  the wrong *message* ("Go LOWER") — the hint text was simply swapped. It suggested
  flipping the two messages so the arrow points toward the secret. I verified this two
  ways: I replayed it in the running game (guessing 7 against 10 now says "Go HIGHER"),
  and I added pytest cases that assert on the message text. All passed.

- **An incorrect / misleading AI suggestion (and how I verified it).**
  The starter project already contained AI-generated scaffold tests that imported
  `check_guess` from `logic_utils` and asserted `result == "Win"`. That was misleading on
  two counts: `logic_utils` was still an unimplemented stub, and the function actually
  returns a `(outcome, message)` tuple, not a bare string — so the assertion could never
  be true. I caught this by running the full suite (it raised `NotImplementedError` /
  failed the comparison), then fixed it by implementing `logic_utils`, repointing the
  imports, and unpacking the tuple (`outcome, message = check_guess(...)`). Lesson:
  AI-written tests can look authoritative but encode wrong assumptions — run them.

---

## 3. Debugging and testing your fixes

- **How I decided a bug was really fixed.**
  I treated "fixed" as needing two independent confirmations: the behavior had to change
  in the actual running game, *and* an automated test had to pin it down so it can't
  silently regress. For the hint bug, eyeballing the game wasn't enough because the
  *outcome label* was already correct — only the user-facing message was wrong — so I
  specifically tested the message string.

- **A test I ran and what it showed.**
  I ran `pytest tests/` (9 tests, all passing). The key ones assert that a too-high guess
  contains "LOWER" and a too-low guess contains "HIGHER", plus a parametrized sweep over
  edge cases like 99-vs-1. Writing these showed me that asserting only on the outcome
  ("Too High") would have *passed even with the bug present* — the message-level assertion
  is what actually guards the fix.

- **Did AI help me design or understand the tests?**
  Yes. The AI pointed out that the bug lived in the message text, not the outcome, so it
  recommended asserting on the hint string and parametrizing several guess/secret pairs
  instead of writing one example. It also flagged that importing from `app.py` drags in
  Streamlit, which is why we moved the logic into `logic_utils.py` so tests stay fast and
  import-clean.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  - Streamlit reruns: Everytime you interact with the page, the whole script runs from top to bottom. In contrast to other apps, they are kept running and only update "one thing" but in this game, everytime the user hits "Submit Guess" app.py runs from the top.
  - Session State: This acts a little memory box that survives those reruns. So important components such as secret number, attempts, score, etc. are kept during that users session.
  - I would say that streamlit is a tool for building web apps in Python and reruns is what reruns the entire script and session state is what keeps those values between reruns.
  

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
