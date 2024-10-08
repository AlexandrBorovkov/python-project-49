#!/usr/bin/env python3.12


from brain_games.games.service_brain_gcd import start_game, answer_processing


def main():
    username = start_game()
    answer_processing(username)


if __name__ == '__main__':
    main()
