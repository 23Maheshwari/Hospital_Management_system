-- Create Database
CREATE DATABASE IF NOT EXISTS hospital_db;
USE hospital_db;
-- drop database hospital_db;

-- Patient Table
CREATE TABLE IF NOT EXISTS Patient (
    patient_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    date_of_birth DATE,
    gender VARCHAR(10),
    contact_number VARCHAR(15),
    address TEXT
);

-- Doctor Table
CREATE TABLE IF NOT EXISTS Doctor (
    doctor_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    specialization VARCHAR(100),
    contact_number VARCHAR(15)
);

-- Appointment Table
CREATE TABLE IF NOT EXISTS Appointment (
    appointment_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT,
    doctor_id INT,
    appointment_date DATE,
    description TEXT,
    FOREIGN KEY (patient_id) REFERENCES Patient(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES Doctor(doctor_id)
);

-- Insert into Patient table
INSERT INTO Patient (first_name, last_name, date_of_birth, gender, contact_number, address) VALUES
('Ananya', 'Sharma', '1990-04-15', 'Female', '9876543210', 'Chennai'),
('Rahul', 'Verma', '1985-07-21', 'Male', '9123456780', 'Delhi'),
('Sneha', 'Patel', '1993-11-10', 'Female', '9988776655', 'Mumbai'),
('Arjun', 'Nair', '1988-09-05', 'Male', '9012345678', 'Bangalore'),
('Meena', 'Rao', '1996-02-28', 'Female', '9345678901', 'Hyderabad'),
('Ravi', 'Kumar', '1982-12-12', 'Male', '9000001111', 'Pune'),
('Priya', 'Singh', '1995-06-18', 'Female', '9123456789', 'Kolkata'),
('Vikram', 'Joshi', '1980-03-23', 'Male', '9988998899', 'Coimbatore'),
('Divya', 'Iyer', '1991-08-14', 'Female', '9876501234', 'Madurai'),
('Karthik', 'Reddy', '1987-01-30', 'Male', '9123498765', 'Trichy');

-- Insert into Doctor table
INSERT INTO Doctor (first_name, last_name, specialization, contact_number) VALUES
('Dr. Amit', 'Desai', 'Cardiology', '9898989898'),
('Dr. Neha', 'Kapoor', 'Neurology', '9797979797'),
('Dr. Raj', 'Mehta', 'Orthopedics', '9696969696'),
('Dr. Sita', 'Bansal', 'Dermatology', '9595959595'),
('Dr. Arvind', 'Swamy', 'Pediatrics', '9494949494'),
('Dr. Kavya', 'Sen', 'Gynecology', '9393939393'),
('Dr. Manish', 'Gupta', 'Oncology', '9292929292'),
('Dr. Lakshmi', 'Menon', 'Psychiatry', '9191919191'),
('Dr. Ramesh', 'Shah', 'Urology', '9090909090'),
('Dr. Divya', 'Krishnan', 'ENT', '8989898989');

-- Insert into Appointment table with appointment_id
INSERT INTO Appointment (appointment_id, patient_id, doctor_id, appointment_date, description) VALUES
(101, 1, 1, '2025-04-01', 'Heart checkup'),
(102, 2, 2, '2025-04-02', 'Migraine issues'),
(103, 3, 3, '2025-04-03', 'Knee pain'),
(104, 4, 4, '2025-04-04', 'Skin rash'),
(105, 5, 5, '2025-04-05', 'Child vaccination'),
(106, 6, 6, '2025-04-06', 'Pregnancy consultation'),
(107, 7, 7, '2025-04-07', 'Cancer screening'),
(108, 8, 8, '2025-04-08', 'Mental health evaluation'),
(109, 9, 9, '2025-04-09', 'Urine infection'),
(110, 10, 10, '2025-04-10', 'Hearing loss treatment');
