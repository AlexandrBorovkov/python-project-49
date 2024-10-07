#!/usr/bin/env python3.12


from brain_games.service_brain_even import start_game, answer_processing


def main():
    username = start_game()
    answer_processing(username)


if __name__ == '__main__':
    main()
