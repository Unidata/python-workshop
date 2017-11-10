Testing
=======

What is Software Testing?
-------------------------
- Testing is a way to make sure that software keeps working like you expect
- You write code that runs other code and validates the results

Types of Tests
--------------
- Unit tests
  - Tests of individual units of code (functions, classes).
  - Test wide array of inputs and cases try to exhaustively capture cases
- Regression tests
  - Test that nothing has broken after making changes
- Integration tests
  - Test that different pieces of code work together properly
- Acceptance tests
  - Test that code meets certain sets of external requirements

- None of that matters to us as scientists

Testing Strategies
------------------
- The right kind of test for your code: the kind you're willing to write
- Requirements:
  - Automated: computer can evaluate whether the test passes
  - Consistent: no spurious failures
  - Self-contained: no external resources, the test completely controls everything
- At the very least, when you write code, you run it and verify the results
  - Why not turn this into an automated test
  - Doesn't prove correct
  - Verifies that results you thought were sufficient haven't changed
- For some code, can use e.g. values from source reference
- In an ideal world, you write several tests spanning:
  - input types (e.g. arrays, scalars)
  - input domains
  - edge cases

Interactive:
  - Add tests for `temperature.py` to `tests/test_temperature.py`
    - values
    - round trip
  - How do we run tests: `pytest

Exercise:
  - Add calculations for mean and median to `stats.py`
  - Add tests to make sure everything is working fine
  - Make sure it works for both even- and odd-sized arrays

Exercise:
  - Use tests to find the bugs in the `moving_average` function
