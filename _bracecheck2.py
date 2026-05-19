path = r'c:\Users\mkaouari\Documents\training-platform\portfolio islam\portfolio.html'
with open(path, encoding='utf-8') as f:
    content = f.read()

start = content.index('<script>') + len('<script>')
end = content.rindex('</script>')
js = content[start:end]

depth = 0
in_string = None
prev = ''
stack = []  # track (lineno, depth) when depth increases

lines = js.split('\n')
for lineno, line in enumerate(lines, 1):
    i = 0
    while i < len(line):
        c = line[i]
        if in_string:
            if c == '\\':
                i += 2
                continue
            if c == in_string:
                in_string = None
        else:
            if c in ('"', "'", '`'):
                in_string = c
            elif c == '{':
                depth += 1
                stack.append((lineno, depth, line.strip()[:80]))
            elif c == '}':
                depth -= 1
                if stack:
                    stack.pop()
        prev = c
        i += 1

print(f"Final brace depth: {depth}")
print(f"Unclosed open braces ({len(stack)}):")
for lineno, d, text in stack[-5:]:
    print(f"  Line {lineno} (depth {d}): {text}")
