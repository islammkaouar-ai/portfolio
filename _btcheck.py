path = r'c:\Users\mkaouari\Documents\training-platform\portfolio islam\portfolio.html'
with open(path, encoding='utf-8') as f:
    content = f.read()

start = content.index('<script>') + len('<script>')
end = content.rindex('</script>')
js = content[start:end]

bt = js.count('`')
print(f'Backtick count: {bt} ({"even - OK" if bt % 2 == 0 else "ODD - SYNTAX ERROR"})')
print(f'Total script lines: {len(js.splitlines())}')

# Find the positions of each backtick to check for odd-indexed ones
positions = [i for i, c in enumerate(js) if c == '`']
if bt % 2 != 0:
    print(f"Unmatched backtick near char {positions[-1]}")
    snippet_start = max(0, positions[-1] - 100)
    print(repr(js[snippet_start:positions[-1]+50]))
