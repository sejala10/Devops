-- Table 1: Employees
CREATE TABLE Employees (
  EmployeeID INT,
  FirstName VARCHAR(50),
  LastName VARCHAR(50),
  Department VARCHAR(50),
  Salary DECIMAL(10, 2)
);

-- Table 2: Customers
CREATE TABLE Customers (
  CustomerID INT,
  FirstName VARCHAR(50),
  LastName VARCHAR(50),
  Email VARCHAR(100),
  Phone VARCHAR(20)
);

-- Table 3: Orders
CREATE TABLE Orders (
  OrderID INT,
  CustomerID INT,
  OrderDate DATE,
  TotalAmount DECIMAL(12, 2),
  Status VARCHAR(20)
);
