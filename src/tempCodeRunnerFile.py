    # Drop all tables
    db.drop_all()

    # Recreate all tables based on the models
    db.create_all()