import organizer
import argparse

def main():
    parser = argparse.ArgumentParser(description="A CLI that automatically sorts your ~/Downloads directory according to file extensions.")
    parser.add_argument('--watch', action='store_true', help='Watch the downloads directory for new files.')
    args = parser.parse_args()

    if args.watch:
        print('Watching Downloads Folder...\n')
        watch = organizer.OnFileChange()
        watch.run()
    else:
        organizer.sort_files()

if __name__ == "__main__":
    main()
