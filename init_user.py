from app import db, app, User

with app.app_context():
    # db.drop_all()
    db.create_all()

    user1 = User("test_user1@test.com", "Test User1", "111")
    user2 = User("test_user2@test.com", "Test User2", "222")

    db.session.add_all([user1, user2])

    db.session.commit()

    print(user1.id)
    print(user2.id)
