CREATE DATABASE IF NOT EXISTS salon_db;
USE salon_db;
CREATE TABLE IF NOT EXISTS appointments (
  id INT AUTO_INCREMENT PRIMARY KEY,
  customer_name VARCHAR(100) NOT NULL,
  phone CHAR(10) NOT NULL,
  gender ENUM('Female','Male','Other') NOT NULL,
  service VARCHAR(50) NOT NULL,
  stylist VARCHAR(100) NOT NULL,
  appointment_date DATE NOT NULL,
  time_slot VARCHAR(20) NOT NULL
);
INSERT INTO appointments (customer_name, phone, gender, service, stylist, appointment_date, time_slot) VALUES
('Meena','9876543210','Female','Hair Spa','Anu','2026-10-20','10:00'),
('Arun','9876543211','Male','Haircut','Ravi','2026-10-20','11:00'),
('Zara','9876543212','Other','Facial','Kavi','2026-10-21','12:00');
-- READ
SELECT * FROM appointments ORDER BY customer_name;
-- UPDATE (change id to an existing record)
UPDATE appointments SET stylist='Kavi' WHERE id=1;
-- DELETE (change id to an existing record)
DELETE FROM appointments WHERE id=3;
