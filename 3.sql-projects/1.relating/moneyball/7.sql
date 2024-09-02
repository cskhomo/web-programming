SELECT first_name, last_name
FROM players
JOIN salaries on players.id = player_id
WHERE salary = (
    SELECT MAX(salary)
    FROM salaries
);