from .wrapper import GitlabWrapper
import os


def get_parser(subparsers):
    parser = subparsers.add_parser(
        "projects", help='List projects')
    parser.add_argument('-c', '--cache',
                        default=os.path.join(
                            os.environ['HOME'], '.config', 'gitlablistpy', 'projects.db'),
                        help='Cache file')
    parser.add_argument('-r', '--refresh', action="store_true",
                        default=False, help='Refresh cache')
    parser.set_defaults(func=main)
    return parser


def main(args):
    if os.path.isfile(args.cache) and not args.refresh:
        with open(args.cache) as f:
            print(f.read())
    else:
        if not os.path.isdir(os.path.dirname(args.cache)):
            os.mkdir(os.path.dirname(args.cache))
        projects = GitlabWrapper.get().projects.list(iterator=True)
        with open(args.cache, 'w+') as f:
            f.writelines((i.path_with_namespace+'\n' for i in projects))
