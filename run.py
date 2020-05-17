from app import create_app, db
from app.auth.models import User
from sqlalchemy import exc


if __name__ == '__main__':
    flask_app = create_app('dev')
    with flask_app.app_context():
        db.create_all()
        flask_app.run()
a=1

"""
flask_app = create_app('dev')
with flask_app.app_context():
    db.create_all()
    flask_app.run ( debug=True )


    except exc.IntegrityError:
        flask_app.run(debug=True)
"""

