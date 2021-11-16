CREATE TABLE IF NOT EXISTS marklar.T1(
    F1 nvarchar(32) PRIMARY KEY, 
    F2 nvarchar(32) PRIMARY KEY, 
    F3 binary(max)
    );

CREATE TABLE IF NOT EXISTS marklar.T2(
    F1 int PRIMARY KEY,
    F2 bit,
    F3 float,
    F4 decimal(64),    

CONSTRAINT FK_Bar FOREIGN KEY (BarId)
    REFERENCES marklar.T1(F1, F2)
);
