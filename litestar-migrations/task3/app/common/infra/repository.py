class RDBRepository:
    @staticmethod
    def add(session, instance):
        return session.add(instance)

    @staticmethod
    def commit(session):
        return session.commit()
