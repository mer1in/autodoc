# Autodoc

Welcome to the magical realm of autodoc! This project endeavors to simplify the often mythical task of documenting Flask APIs. Think of it as embarking on a quest to capture elusive creatures—be it the hidden unicorns lurking in the dusty corners of Jira or the dragons concealed within the code forests.

## Overview

In this whimsical journey, we hold dear the motto: "done is better than perfect." Perfect unicorns or flawlessly scaled dragons may seem enchanting, but opting for "done" means corralling lively creatures, akin to maybe an unshaved yak—quirky yet undeniably present in your Flask API documentation. Despite imperfections, they're alive, usable, and immensely valuable!

## Usage

### Annotating Paths for Documentation

To harness the magic of autodoc, annotate your paths within your Flask application with the following format:

```python
from autodoc import route

@route('/path/<param>', {"GET": ["array", "of", "roles"]})
def your_function_name(param):
    """
    Add your function's docstring here.
    """
    # Your function code goes here
```

By adding this annotation and including a docstring within your function, autodoc will perform its sorcery, automatically generating descriptions for your endpoints, along with the **app.route** setup and permissions checks.

In this whimsical journey, we hold dear the motto: "done is better than perfect." Perfect unicorns or flawlessly scaled dragons may seem enchanting, but opting for "done" means corralling lively creatures, akin to maybe an unshaved yak—quirky yet undeniably present in your Flask API documentation. Despite imperfections, they're alive, usable, and immensely valuable!

### Running the Server and Examples

To witness the magic firsthand, follow these steps:

1. Clone the repository.
2. Navigate to the project directory.
3. Run the `runme.sh` script by executing the following command in your terminal:

    ```bash
    ./runme.sh
    ```

This script spins up the server with examples and executes various requests, showcasing the functionality and wonders of autodoc.

## Contribution

Join our quest to enhance this documentation adventure! We welcome contributors who can add their own unique creatures (or code improvements) to our magical menagerie.

In this realm where perfection remains elusive, autodoc seeks to provide functional documentation—a treasure trove of creatures, each adding its own unique charm to your coding adventure!

Happy documenting, and may you capture the quirkiest of creatures in your Flask API journey!
