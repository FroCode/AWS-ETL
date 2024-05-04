CREATE SCHEMA oltp;

-- Companies Table
CREATE TABLE oltp.companies (
    company_id INT PRIMARY KEY,
    name VARCHAR(255),
    valuation DECIMAL(12, 2),
    date_joined DATE,
    year DATE,
    country VARCHAR(100),
    city_id INT,
    industry_id INT,
    type VARCHAR(255),
    description TEXT,
    website VARCHAR(255),
    FOREIGN KEY (city_id) REFERENCES oltp.cities(city_id),
    FOREIGN KEY (industry_id) REFERENCES oltp.industries(industry_id)
);

-- Cities Table
CREATE TABLE oltp.cities (
    city_id INT PRIMARY KEY,
    name VARCHAR(255)
);

-- Industries Table
CREATE TABLE oltp.industries (
    industry_id INT PRIMARY KEY,
    name VARCHAR(255)
);

-- Investors Table
CREATE TABLE oltp.investors (
    investor_id INT PRIMARY KEY,
    name VARCHAR(255)
);

-- Company Investors Junction Table
CREATE TABLE oltp.company_investors (
    company_id INT,
    investor_id INT,
    FOREIGN KEY (company_id) REFERENCES oltp.companies(company_id),
    FOREIGN KEY (investor_id) REFERENCES oltp.investors(investor_id),
    PRIMARY KEY (company_id, investor_id)
);
SELECT * FROM oltp.cities