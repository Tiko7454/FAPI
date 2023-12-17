from sqlalchemy.orm import Session


def commit_before_return(func):
    def wrapper(db: Session, *args, **kwargs):
        res = func(db, *args, **kwargs)
        db.commit()
        return res

    return wrapper
