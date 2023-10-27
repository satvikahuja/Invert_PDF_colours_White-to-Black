# Invert PDF Colors

If you, like me, are getting eye strain due to the bright colors in PDFs (especially those given for college study material), this tool might be for you. 

## Why this tool?

I tried searching Google for a similar tool but found many of them had page restrictions. This program will convert your PDF to an inverted color PDF. 

## Benefits

- Converts white pages to black.
- Helps in reducing eye strain.

## How to Use

1. Make sure you have `poppler` installed on your system. Follow the instructions provided [here](#installing-poppler) to install and set it up.
2. After installing `poppler`, run the Python script provided to convert your PDFs.

## Installing Poppler

### For macOS:
Use Homebrew:

```bash
brew install poppler
```
### For Linux (Debian/Ubuntu):

\`\`\`bash
sudo apt-get install poppler-utils
\`\`\`

### For Windows:

- Download the `poppler` binaries from [here](http://blog.alivate.com.au/poppler-windows/).
- Extract the files.
- Add the path to the `bin` directory in the extracted folder to your system's `PATH` environment variable.

After setting up `poppler`, run the Python script to invert the colors of your PDFs and enjoy a more comfortable reading experience.
