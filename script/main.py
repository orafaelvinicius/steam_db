
from procedures.screaping import Steamdb
from procedures.send_to_big_query import data_to_bigQuery
from procedures.send_to_sheets import data_to_sheets


def main():
    print('\\\\\\\\\\ Executando a raspagem //////////')

    Steamdb().run()

    data_to_sheets()

    data_to_bigQuery()

    print('\\\\\\\\\\ Raspagem concluída, dados no sheets e no BQ //////////')


if __name__ == '__main__':
    main()