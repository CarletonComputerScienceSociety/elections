from elections.main import db

from sys import argv

def main():
    if len(argv) < 2:
        print 'Please provide a subcommand.'
    elif argv[1] == 'create':
        db.create_all()
    else:
        print 'Invalid subcommand {}.'.format(argv[1])

if __name__ == '__main__':
    main()
