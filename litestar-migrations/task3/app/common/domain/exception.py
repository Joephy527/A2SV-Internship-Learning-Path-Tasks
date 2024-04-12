class BaseMsgException(Exception):
    message: str

    def __str__(self):
        return self.message
