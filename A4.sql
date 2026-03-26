CREATE TABLE IF NOT EXISTS PRODUCT(
    PRO_ID TEXT PRIMARY KEY,
    PRO_NAME TEXT,
    PRO_PRICE TEXT,
    PRO_COM TEXT
);

INSERT INTO PRODUCT(PRO_ID,PRO_NAME,PRO_PRICE,PRO_COM)
VALUES
    ("101","MOTHER BOARD","3200","15"),
    ("102","KEY BOARD","450","16"),
    ("103","ZIP DRIVE","250","14"),
    ("104","SPEAKER","550","16"),
    ("105","MONITOR","5000","11"),
    ("106","DVD DRIVE","900","12"),
    ("107","CD DRIVE","800","12"),
    ("108","PRINTER","2600","13"),
    ("109","REFILL CARTRIDGE","350","13"),
    ("110","MOUSE","250","12");
SELECT pro_name, pro_price
    FROM PRODUCT
    WHERE pro_price =
    (SELECT MIN(pro_price) FROM PRODUCT);
SELECT pro_name, pro_price
    FROM PRODUCT
    WHERE pro_price =
    (SELECT MAX(pro_price) FROM PRODUCT);