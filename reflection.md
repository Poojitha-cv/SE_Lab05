# Reflection – Lab 5: Static Code Analysis

---

### 1. Which issues were the easiest to fix, and which were the hardest? Why?

The easiest problems to fix were mostly style-related, like adding missing docstrings, removing extra spaces, and cleaning up blank lines. Those didn’t affect how the program worked — they were just about making the code cleaner and following PEP 8 rules.

The harder issues were the ones that involved logic and security. For example, changing the mutable default argument (`logs=[]`) to `None` took some thought because it could affect how data was shared between calls. Replacing the unsafe `eval()` function with `ast.literal_eval()` was also tricky since I had to make sure the new version still worked correctly but safely.

---

### 2. Did the static analysis tools report any false positives? If so, describe one example.

Yes, Pylint flagged the use of a global variable (`stock_data`) as a bad practice. Technically, that’s true for large projects, but in this small program, the global variable made sense because it’s used to store shared inventory data. So, this warning didn’t really indicate an actual problem — it was more of a false positive in this case.

---

### 3. How would you integrate static analysis tools into your actual software development workflow?

If I were working on a real project, I’d use these tools regularly — not just at the end.  
- I’d run Pylint, Flake8, and Bandit locally before every commit to catch issues early.  
- Then, I’d add them to a CI pipeline (like GitHub Actions) so every push and pull request is automatically checked.  
- I’d also set a minimum score for Pylint and treat Bandit’s output as part of the security review before deployment.  

This setup would make sure that bad code or security risks never make it into the main branch.

---

### 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

After fixing all the issues, the code definitely looked and worked better.  
- It’s easier to read now because of consistent naming and proper docstrings.  
- It’s more secure since `eval()` was replaced with a safer option.  
- The program is more reliable — removing mutable default arguments and adding input validation stopped some subtle bugs.  
- Overall, the code feels cleaner, safer, and more professional.  

Using static analysis made a big difference — it forced me to pay attention to details I might have missed otherwise.
