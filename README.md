<h1 align="center">Whatsapp</h1>

The program reads the file with the exported Whatsapp messages and counts the number of messages in the file.

```python
# Example in console
Alex: 5672
Jane: 6673
Total messages: 12345
```

## How it Works

1. Get the parent directory.

```python
os.path.dirname(os.path.abspath(__file__)
```

2. Using os.walk() we can traverse recursively through all the subdirectories of the parent directory. By using a for loop to loop over all the files in each directory, we can calculate the statistics for each file.

```python
def openRoot(root):
    for path, _, files in os.walk(root):
        for file in files:
            if file.endswith(".txt"):
                print("---STATISTICS---")
                countFiles(os.path.join(path, file))
                print("\n\n")
```

3. Using the regex, we can check if the line is a start of a message.

```python
# Regex: '00/00/0000, 00:00 - '
regex = "\d{2}\/\d{2}\/\d{4},{1} {1}\d{2}:{1}\d{2} {1}-{1} {1}"

with open(path, encoding="utf8") as textfile:
    for line in textfile:
        position = re.search(regex, line)
```

4. If the line is a message, get the username and increment it by 1 in the 'messages' dictionary object.

```python
        if position is not None and line.count(':') >= 2:
            totalMessages += 1
            username = ":".join(line.split(':', 2)[:2])[position.end():]
            if username in messages:
                messages[username] += 1
            else:
                messages[username] = 1
```

## Credits

Everything is coded by Alex lo Storto

Licensed under the MIT License.
