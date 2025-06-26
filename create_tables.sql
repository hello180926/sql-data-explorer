-- 创建一个简单的用户信息表
CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    email VARCHAR(100)
);

-- 插入一些示例数据
INSERT INTO users (id, name, age, email) VALUES
(1, 'Alice', 23, 'alice@example.com'),
(2, 'Bob', 30, 'bob@example.com'),
(3, 'Charlie', 28, 'charlie@example.com');
