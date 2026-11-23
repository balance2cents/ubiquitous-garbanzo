# The Commonplace

Personal study hub for The Great Courses, published as a claude.ai artifact:
https://claude.ai/artifact/QLQ1tnHQbotSfiupicEFSx

- `index.html` is the page (categories, course pages, lecture view, quiz, cases with AI feedback, tutor, highlighter, spaced review).
- `content/*.py` holds course content written with the small `L()` DSL in `content/_dsl.py`.
- `python3 build.py` turns content into `courses/<id>.json`, which the page fetches.

To add a course: write its content modules, add an entry to `COURSES` in `build.py` and in `index.html`, run the build, and republish with the new JSON file in `files`.
