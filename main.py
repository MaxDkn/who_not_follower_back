import re
from pathlib import Path
from typing import Iterable, Set

HREF_REGEX = re.compile(r'href="/([^/]+?)/"')


def extract_usernames_from_file(path: Path) -> Set[str]:
    usernames: set[str] = set()

    with path.open("r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            for match in HREF_REGEX.finditer(line):
                usernames.add(match.group(1))

    return usernames


def usernames_to_string(usernames: Iterable[str]) -> str:
    return "\n".join(sorted(usernames))


def save_usernames(usernames: Iterable[str], output: Path) -> None:
    output.write_text(usernames_to_string(usernames), encoding="utf-8")


def main() -> None:
    followers_path = Path("data/followers")
    following_path = Path("data/following")

    followers = extract_usernames_from_file(followers_path)
    following = extract_usernames_from_file(following_path)

    save_usernames(followers, Path("followers.txt"))
    save_usernames(following, Path("following.txt"))

    not_follow_back = following - followers

    save_usernames(not_follow_back, Path("who_not_follow_back.txt"))

    print(f"Followers: {len(followers)}")
    print(f"Following: {len(following)}")
    print(f"Not following back: {len(not_follow_back)}")


if __name__ == "__main__":
    main()