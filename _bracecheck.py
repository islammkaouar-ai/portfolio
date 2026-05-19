path = r'c:\Users\mkaouari\Documents\training-platform\portfolio islam\portfolio.html'
with open(path, encoding='utf-8') as f:
    content = f.read()

start = content.index('<script>') + len('<script>')
end = content.rindex('</script>')
js = content[start:end]

# Simple brace balance check (ignoring strings and comments)
depth = 0
in_string = None
prev = ''
errors = []

lines = js.split('\n')
for lineno, line in enumerate(lines, 1):
    i = 0
    while i < len(line):
        c = line[i]
        if in_string:
            if c == '\\' and prev != '\\':
                i += 2
                continue
            if c == in_string:
                in_string = None
        else:
            if c in ('"', "'", '`'):
                in_string = c
            elif c == '{':
                depth += 1
            elif c == '}':
                depth -= 1
                if depth < 0:
                    errors.append(f"Line {lineno}: extra closing brace, depth went to {depth}")
                    depth = 0
        prev = c
        i += 1

print(f"Final brace depth: {depth} ({'balanced' if depth == 0 else 'UNBALANCED'})")
if errors:
    for e in errors[:10]:
        print(e)
print("Done.")
