
import argparse
import helper




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Process PDF files from a directory.")
    parser.add_argument(
        '-d', '--directory',
        type=str,
        default="./pdfs",
        help="Directory containing PDF files"
    )

    args = parser.parse_args()
    helper.ingest_pdfs(args.directory)
