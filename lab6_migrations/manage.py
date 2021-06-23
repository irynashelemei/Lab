from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager


if __name__ == "__main__":
    from lab6_migrations.portfolio import app, db
    from lab6_migrations.portfolio import models

    migrate = Migrate(app, db, render_as_batch=True)
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)

    manager.run()
