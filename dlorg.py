from organizer.organizer import main
import argparse

def main():
    parser = argparse.ArgumentParser(description="A CLI that automatically sorts your ~/Downloads directory according to file extensions.")
    args = parser.parse_args()
    organizer.sort_files()

if __name__ == "__main__":
    main()
