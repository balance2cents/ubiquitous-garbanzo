#!/usr/bin/env python3
"""Assemble the single-file artifact page: shell + vocab + content + app -> dist/pyatyorka.html"""
import json, pathlib
src = pathlib.Path(__file__).parent / 'src'
vocab = json.loads((src/'vocab.json').read_text())
page = (src/'shell.html').read_text()
page += '\n<script>\nconst VOCAB = ' + json.dumps(vocab, ensure_ascii=False, separators=(',',':')) + ';\n</script>'
page += '\n<script>\n' + (src/'content.js').read_text() + '\n</script>'
page += '\n<script>\n' + (src/'app.js').read_text() + '\n</script>\n'
out = pathlib.Path(__file__).parent / 'dist' / 'pyatyorka.html'
out.parent.mkdir(exist_ok=True)
out.write_text(page)
print(out, len(page.encode()), 'bytes')
