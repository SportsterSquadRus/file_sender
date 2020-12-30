import argparse


def parser()
    url = '127.0.0.1'
    port = 8000
    timer = 1
    parser = argparse.ArgumentParser()
    parser.add_argument('--u')
    parser.add_argument('--p')
    parser.add_argument('--t')

    keys = parser.parse_args()
    parsed_args = vars(keys)

    print(parsed_args)

    if parsed_args['u']:
        url = parsed_args['u']
    if parsed_args['p'] and parsed_args['p'].isdigit():
        port = parsed_args['p']
    if parsed_args['t'] and parsed_args['t'].isdigit():
        timer = int(parsed_args['t'])
    return url, port, timer