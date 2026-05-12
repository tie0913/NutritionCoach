CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,

    name VARCHAR(100) NOT NULL,

    password VARCHAR(255) NOT NULL,

    email VARCHAR(255) NOT NULL UNIQUE,

    birth_date DATE NOT NULL,

    create_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

    update_time DATETIME NOT NULL
        DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE profiles (
    id INT PRIMARY KEY AUTO_INCREMENT,

    user_id INT NOT NULL UNIQUE,

    weight FLOAT,

    height FLOAT,

    bmr INT,

    chronic JSON,

    allergies JSON,

    goals JSON,

    CONSTRAINT fk_profile_user
        FOREIGN KEY (user_id)
        REFERENCES users(id)
        ON DELETE CASCADE
);

CREATE TABLE food_logs (
    id INT PRIMARY KEY AUTO_INCREMENT,

    user_id INT NOT NULL,

    name VARCHAR(255) NOT NULL,

    quantity FLOAT NOT NULL,

    calories INT NOT NULL,

    carbs INT NOT NULL,

    protein INT NOT NULL,

    fats INT NOT NULL,

    create_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_foodlog_user
        FOREIGN KEY (user_id)
        REFERENCES users(id)
        ON DELETE CASCADE
);

CREATE TABLE plans (
    id INT PRIMARY KEY AUTO_INCREMENT,

    user_id INT NOT NULL,

    breakfast JSON,

    lunch JSON,

    snack JSON,

    dinner JSON,

    create_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_plan_user
        FOREIGN KEY (user_id)
        REFERENCES users(id)
        ON DELETE CASCADE
);