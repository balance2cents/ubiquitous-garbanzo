# Пятёрка: Russian A1 tutoring platform

Study platform for a Russian course taught in German with *Jasno! neu A1–A2* (Klett), Lektion 1–9.
Written A1 exam: **Wed 16 Dec 2026**.

Live page: https://claude.ai/artifact/Buahkex6k1cogR8s8s2CvD

- `src/vocab.json`: the Kursbuch's Lernwortschatz (bold words) for L1–9, with stress marks, English and the book's German gloss
- `src/content.js`: grammar in English, workbook self-tests ("Что правильно?") with answer keys, drills, readings, writing tasks, week plan
- `src/app.js`: flashcards (spaced repetition), quizzes, mock exam, mistake log, tutor desk, db sync
- `python3 build.py` → `dist/pyatyorka.html` (the published single-file page)

Data lives in the artifact's db: `p5/student` (her progress) and `p5/tutor` (scope, plan, notes, feedback).
The artifact owner sees the tutor desk; everyone else sees the student view.
