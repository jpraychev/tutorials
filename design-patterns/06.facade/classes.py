class Computer:

    def start(self):
        """ Start a computer using facade pattern """
        self.__bios()
        self.__post()
        self.__mbr()
        self.__kernel()
        self.__os()

    def __bios(self):
        print('BIOS sequence initiated...')

    def __post(self):
        print('Power on self test in progress...')

    def __mbr(self):
        print('Locating master boot record...')

    def __kernel(self):
        print('Loading kernel...')
        
    def __os(self):
        print('Operating system loaded.')