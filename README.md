# who_not_follow_back

Small script to find which Instagram accounts you follow that **do not follow you back**.

The script parses Instagram HTML and extracts usernames from profile links.

## How it works

The script looks for links like:

```

href="/username/"

```

This is more reliable than parsing CSS classes, since Instagram changes them often.

---

# Usage

## 1. Open Instagram

Go to:

- your **Followers**
- your **Following**

Example:

```

[https://www.instagram.com/your_username/followers/](https://www.instagram.com/your_username/followers/)
[https://www.instagram.com/your_username/following/](https://www.instagram.com/your_username/following/)

```

---

## 2. Copy the page content

1. Scroll **all the way down** until all accounts are loaded.
2. Right click anywhere on the page
3. Click **Inspect**
4. Find the container that contains the list of users
5. Right click it → **Copy → Copy element**

---

## 3. Paste the HTML

Paste the copied HTML into these files:

```

data/followers
data/following

```

Example project structure:

```

project/
│
├── main.py
├── README.md
│
├── data/
│   ├── followers
│   └── following

```

---

## 4. Run the script

```

python main.py

```

---

# Output files

The script will generate:

```

followers.txt
following.txt
who_not_follow_back.txt

```

### followers.txt
List of people that follow you.

### following.txt
List of people you follow.

### who_not_follow_back.txt
People **you follow but who don't follow you back**.

---

# Example

```

Followers: 320
Following: 450
Not following back: 130

```

---

# Requirements

Python 3.9+

No external dependencies.