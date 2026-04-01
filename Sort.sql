-- Table for friends and their subjects and scores
CREATE TABLE friends_scores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    friend_name VARCHAR(100) NOT NULL,
    subject VARCHAR(100) NOT NULL,
    score INT NOT NULL
);

-- Insert sample data
INSERT INTO friends_scores (friend_name, subject, score) VALUES
('Alice', 'Math', 95),
('Alice', 'Science', 88),
('Bob', 'Math', 92),
('Bob', 'English', 85),
('Charlie', 'History', 90);

-- View all scores
SELECT * FROM friends_scores ORDER BY friend_name, subject;

-- Example: Get average score per friend
SELECT friend_name, AVG(score) AS average_score
FROM friends_scores
GROUP BY friend_name
ORDER BY average_score DESC;